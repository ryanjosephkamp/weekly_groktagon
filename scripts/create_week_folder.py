#!/usr/bin/env python3
"""Create a weekly folder from the reusable final post template without overwriting files."""

from __future__ import annotations

import argparse
from datetime import UTC, date, datetime
from pathlib import Path


def current_week() -> str:
    today = datetime.now(UTC).date()
    iso_year, iso_week, _ = today.isocalendar()
    return f"{iso_year}-W{iso_week:02d}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a weekly publication folder.")
    parser.add_argument("--week", default=current_week(), help="Week folder name in YYYY-WXX format.")
    parser.add_argument("--template", default="planning/prompts/final-blog-post-template.md")
    parser.add_argument("--weekly-root", default="weekly")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    template = Path(args.template)
    weekly_root = Path(args.weekly_root)
    target = weekly_root / args.week
    reports = target / "reports"
    final_post = target / "final-blog-post.md"

    if not template.is_file():
        raise SystemExit(f"Template not found: {template}")
    if final_post.exists():
        raise SystemExit(f"Refusing to overwrite existing final post: {final_post}")

    reports.mkdir(parents=True, exist_ok=True)
    gitkeep = reports / ".gitkeep"
    if not gitkeep.exists():
        gitkeep.write_text("", encoding="utf-8")
    final_post.write_text(template.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Created {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
