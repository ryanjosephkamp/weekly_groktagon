#!/usr/bin/env python3
"""Collect configured official source pages into an artifact staging directory."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import tempfile
import time
from dataclasses import dataclass
from datetime import UTC, date, datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import requests
import trafilatura

DEFAULT_USER_AGENT = "weekly-groktagon-scraper/1.0 (+https://github.com/ryanjosephkamp/weekly_groktagon)"
DEFAULT_TIMEOUT = 30
DEFAULT_RETRIES = 2
DEFAULT_DELAY_SECONDS = 2.0


@dataclass(frozen=True)
class Source:
    """Validated source configuration entry."""

    name: str
    url: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect configured weekly source pages.")
    parser.add_argument(
        "--sources",
        default="scripts/sources.json",
        help="Path to the JSON source configuration file.",
    )
    parser.add_argument(
        "--output-dir",
        help="Artifact staging directory for raw collection output. Defaults to a temporary directory.",
    )
    parser.add_argument(
        "--summary-file",
        help="Optional path for a non-raw JSON run summary.",
    )
    parser.add_argument(
        "--date",
        help="UTC date to use for ISO week resolution, in YYYY-MM-DD format. Defaults to today.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate configuration and show the target week without fetching or writing raw output.",
    )
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help="Request timeout in seconds.")
    parser.add_argument("--retries", type=int, default=DEFAULT_RETRIES, help="Retries per source after the first attempt.")
    parser.add_argument(
        "--delay",
        type=float,
        default=DEFAULT_DELAY_SECONDS,
        help="Delay between source requests in seconds.",
    )
    return parser.parse_args()


def resolve_run_date(value: str | None) -> date:
    if not value:
        return datetime.now(UTC).date()
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError("--date must use YYYY-MM-DD format") from exc


def iso_week_folder(run_date: date) -> str:
    iso_year, iso_week, _ = run_date.isocalendar()
    return f"{iso_year}-W{iso_week:02d}"


def load_sources(path: Path) -> list[Source]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"Source configuration not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Source configuration is invalid JSON: {path}") from exc

    raw_sources = data.get("sources") if isinstance(data, dict) else data
    if not isinstance(raw_sources, list) or not raw_sources:
        raise ValueError("Source configuration must contain a non-empty 'sources' list")

    sources: list[Source] = []
    seen_urls: set[str] = set()
    for index, raw_source in enumerate(raw_sources, start=1):
        if not isinstance(raw_source, dict):
            raise ValueError(f"Source #{index} must be an object")
        name = str(raw_source.get("name", "")).strip()
        url = str(raw_source.get("url", "")).strip()
        parsed = urlparse(url)
        if not name:
            raise ValueError(f"Source #{index} is missing a name")
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError(f"Source #{index} has an invalid URL: {url}")
        if url in seen_urls:
            raise ValueError(f"Duplicate source URL configured: {url}")
        seen_urls.add(url)
        sources.append(Source(name=name, url=url))
    return sources


def safe_slug(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return slug or "source"


def extract_title(html: str) -> str | None:
    match = re.search(r"<title[^>]*>(.*?)</title>", html, flags=re.IGNORECASE | re.DOTALL)
    if not match:
        return None
    title = re.sub(r"\s+", " ", match.group(1)).strip()
    return title or None


def fetch_source(session: requests.Session, source: Source, timeout: int, retries: int) -> dict[str, Any]:
    retrieved_at = datetime.now(UTC).isoformat()
    last_error: str | None = None
    response: requests.Response | None = None

    for attempt in range(1, retries + 2):
        try:
            response = session.get(source.url, timeout=timeout)
            if response.status_code >= 500 and attempt <= retries + 1:
                last_error = f"HTTP {response.status_code}"
                time.sleep(min(2 * attempt, 10))
                continue
            break
        except requests.RequestException as exc:
            last_error = f"{type(exc).__name__}: {exc}"
            if attempt <= retries:
                time.sleep(min(2 * attempt, 10))
                continue
            response = None
            break

    if response is None:
        return {
            "name": source.name,
            "url": source.url,
            "retrieved_at": retrieved_at,
            "status": "error",
            "error": last_error or "request failed",
        }

    extracted_text: str | None = None
    extraction_error: str | None = None
    if response.ok:
        try:
            extracted_text = trafilatura.extract(
                response.text,
                url=response.url,
                include_comments=False,
                include_tables=True,
            )
        except Exception as exc:  # noqa: BLE001 - preserve extraction failure in raw artifact metadata.
            extraction_error = f"{type(exc).__name__}: {exc}"
    else:
        extraction_error = f"HTTP {response.status_code}"

    return {
        "name": source.name,
        "url": source.url,
        "final_url": response.url,
        "retrieved_at": retrieved_at,
        "status": "ok" if response.ok else "error",
        "status_code": response.status_code,
        "content_type": response.headers.get("content-type"),
        "title": extract_title(response.text),
        "content_sha256": hashlib.sha256(response.content).hexdigest(),
        "extracted_text": extracted_text,
        "extraction_error": extraction_error,
    }


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def bundle_timestamp(run_started_at: str) -> str:
    try:
        return datetime.strptime(run_started_at, "%Y%m%dT%H%M%SZ").strftime("%Y%m%d-%H%M%S")
    except ValueError as exc:
        raise ValueError("run_started_at must use YYYYMMDDTHHMMSSZ format") from exc


def generate_scrape_bundle_markdown(
    *,
    output_dir: Path,
    target_week: str,
    run_started_at: str,
    manifest: dict[str, Any],
    source_results: list[tuple[str, dict[str, Any]]],
    blocking_failures: int,
) -> str:
    bundle_filename = f"scrape-bundle-{target_week}-{bundle_timestamp(run_started_at)}.md"
    status = "All sources successful" if blocking_failures == 0 else f"{blocking_failures} source(s) reported errors"
    lines = [
        f"# Weekly Grok Scrape Results — {target_week}",
        "",
        f"**Run started:** {run_started_at}  ",
        f"**Source count:** {manifest['source_count']}  ",
        f"**Status:** {status}",
        "",
        "## Instructions for GPT-5.5",
        "",
        "Use only the content in this scrape bundle and its embedded source metadata when drafting Report 1 "
        "(Official xAI Sources Summary), as defined in planning/PROJECT.md and "
        "planning/prompts/report-1-official-xai-sources.md. "
        "Treat the embedded JSON as raw source material, preserve citation traceability to the listed source URLs "
        "and files, use original wording, and do not publish raw scrape text wholesale.",
        "",
        "---",
        "",
        "## manifest.json",
        "",
        "```json",
        json.dumps(manifest, indent=2, sort_keys=True),
        "```",
        "",
        "---",
        "",
    ]

    for filename, result in source_results:
        lines.extend(
            [
                f"## {filename}",
                "",
                "```json",
                json.dumps(result, indent=2, sort_keys=True),
                "```",
                "",
            ]
        )

    lines.extend(["---", "", "**End of scrape bundle**", ""])
    (output_dir / bundle_filename).write_text("\n".join(lines), encoding="utf-8")
    return bundle_filename


def build_summary(
    *,
    run_started_at: str,
    target_week: str,
    source_count: int,
    output_dir: str | None,
    dry_run: bool,
    artifact_file_count: int,
    bundle_file: str | None = None,
) -> dict[str, Any]:
    summary = {
        "run_started_at": run_started_at,
        "target_week": target_week,
        "source_count": source_count,
        "output_dir": output_dir,
        "dry_run": dry_run,
        "artifact_file_count": artifact_file_count,
    }
    if bundle_file:
        summary["bundle_file"] = bundle_file
    return summary


def main() -> int:
    args = parse_args()
    try:
        run_date = resolve_run_date(args.date)
        target_week = iso_week_folder(run_date)
        sources = load_sources(Path(args.sources))
    except ValueError as exc:
        print(f"Configuration error: {exc}", file=sys.stderr)
        return 2

    run_started_at = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")

    if args.dry_run:
        summary = build_summary(
            run_started_at=run_started_at,
            target_week=target_week,
            source_count=len(sources),
            output_dir=None,
            dry_run=True,
            artifact_file_count=0,
        )
        print(json.dumps({**summary, "sources": [source.__dict__ for source in sources]}, indent=2))
        if args.summary_file:
            write_json(Path(args.summary_file), summary)
        return 0

    output_dir = Path(args.output_dir) if args.output_dir else Path(tempfile.mkdtemp(prefix="weekly-groktagon-raw-"))
    output_dir.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers.update({"User-Agent": DEFAULT_USER_AGENT})

    manifest_entries: list[dict[str, Any]] = []
    source_results: list[tuple[str, dict[str, Any]]] = []
    blocking_failures = 0
    for index, source in enumerate(sources, start=1):
        result = fetch_source(session, source, args.timeout, args.retries)
        filename = f"{index:02d}-{safe_slug(source.name)}.json"
        write_json(output_dir / filename, result)
        source_results.append((filename, result))
        manifest_entries.append(
            {
                "name": source.name,
                "url": source.url,
                "file": filename,
                "status": result.get("status"),
                "status_code": result.get("status_code"),
                "retrieved_at": result.get("retrieved_at"),
            }
        )
        if result.get("status") != "ok":
            blocking_failures += 1
        if index < len(sources):
            time.sleep(max(args.delay, 0))

    manifest = {
        "run_started_at": run_started_at,
        "target_week": target_week,
        "source_count": len(sources),
        "sources": manifest_entries,
    }
    write_json(output_dir / "manifest.json", manifest)
    bundle_file = generate_scrape_bundle_markdown(
        output_dir=output_dir,
        target_week=target_week,
        run_started_at=run_started_at,
        manifest=manifest,
        source_results=source_results,
        blocking_failures=blocking_failures,
    )

    summary = build_summary(
        run_started_at=run_started_at,
        target_week=target_week,
        source_count=len(sources),
        output_dir=str(output_dir),
        dry_run=False,
        artifact_file_count=len(manifest_entries) + 2,
        bundle_file=bundle_file,
    )
    if args.summary_file:
        write_json(Path(args.summary_file), summary)
    print(json.dumps(summary, indent=2))

    if blocking_failures == len(sources):
        print("All configured sources failed; treating run as blocked.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
