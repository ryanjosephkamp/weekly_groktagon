# Scrape Bundle Artifact Addendum

**Date:** 2026-05-22  
**Status:** Approved plan modification  
**Related documents:** `planning/gpt-5.5-setup-plan.md`, `planning/implementation-plan.md`

## Purpose

This addendum modifies the data handling behavior of the daily scraping workflow. The goal is to improve convenience for the user and GPT-5.5 while maintaining the existing privacy and non-commitment rules for raw data.

## Approved Changes

### 1. Continue generating individual JSON files
- The GitHub Action must continue to generate all six individual JSON files (e.g. `01-xai-home.json`, `02-xai-blog.json`, etc.) plus `manifest.json`.
- These files will remain part of the workflow artifact.

### 2. Generate a single consolidated Markdown bundle
- In addition to the individual JSON files, the Action must generate **one Markdown file** that contains:
  - A clear header with instructions for GPT-5.5
  - The full `manifest.json` content
  - All six source JSON files embedded in clearly labeled code blocks

### 3. Filename convention
- Use the detailed naming pattern:  
  `scrape-bundle-YYYY-WXX-YYYYMMDD-HHMMSS.md`  
  Example: `scrape-bundle-2026-W21-20260522-201424.md`

### 4. Artifact packaging
- The Markdown bundle file must be included in the **same GitHub Actions artifact** as the individual JSON files and manifest.
- This allows the user to download a single artifact zip that contains everything needed for report generation.

### 5. Implementation location
- The logic to generate the Markdown bundle should be added inside `scripts/daily_grok_scrape.py`.
- A new helper function should be created (e.g. `generate_scrape_bundle_markdown(...)`) that is called at the end of a successful scrape run.
- The function should accept the list of results and the manifest, then write the formatted Markdown file to the artifact staging directory.

## Markdown Bundle File Format

The generated Markdown file must follow this general structure (exact formatting and header instructions to be finalized):

```markdown
# Weekly Grok Scrape Results — 2026-W21

**Run started:** [timestamp]  
**Source count:** [number]  
**Status:** All sources successful

## Instructions for GPT-5.5

[Placeholder for instructions — e.g. “You are to use ONLY the content in this file to generate Report 1…”]

---

## manifest.json

```json
{ ... manifest content ... }
```

---

## 01-xai-home.json

```json
{ ... full JSON ... }
```

## 02-xai-blog.json

```json
{ ... full JSON ... }
```

[Additional sources follow the same pattern...]

---

**End of scrape bundle**
```

> **Note:** The user will insert the final detailed format (including exact header text and any additional instructions for GPT-5.5) into this section before the addendum is considered complete.

## Key Requirements for the Markdown Bundle

- Must start with a clear header containing week identifier, run timestamp, number of sources, and instructions for GPT-5.5.
- Each JSON must appear in its own clearly labeled section.
- The full raw JSON must be embedded inside fenced code blocks.
- The file must remain self-contained so it can be downloaded and fed directly to GPT-5.5.

## Impact on Existing Behavior

- No change to `.gitignore` or commit behavior — raw data is still never committed to the repository.
- No change to the workflow triggers, schedule (`03:00 UTC`), or dry-run capability.
- The Markdown bundle is generated **in addition to** (not instead of) the existing individual JSON + manifest files.

## Next Steps (User Plan)

1. Upload this addendum to `planning/docs/`.
2. Instruct GPT-5.5 to update the repository to implement this change (modify `daily_grok_scrape.py` and ensure the workflow artifact includes the new Markdown file).
3. Re-run the manual GitHub Action to verify correct artifact generation.
4. Use the generated Markdown bundle for Report 1 creation.
5. Later evaluate whether additional sources should be added to `scripts/sources.json`.

## Notes

This change improves usability for both the human user and the GPT-5.5 agent while preserving the core privacy and non-pollution principles of the original plan.
```

---