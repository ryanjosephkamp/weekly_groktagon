# Scrape Sources Enhancement Addendum

**Date:** 2026-05-22  
**Status:** Approved plan modification  
**Related documents:** 
- `planning/gpt-5.5-setup-plan.md`
- `planning/docs/scrape-bundle-artifact-addendum.md`
- `scripts/sources.json`

## Purpose

This addendum further refines the daily scraping configuration to:
- Add three high-value official xAI sources
- Generate a short `summary-snippets.md` file inside the same artifact for quick scanning by GPT-5.5
- Keep the existing optimized source list, Markdown bundle, and privacy rules intact

## Approved Changes

### 1. Updated Source List (Final Recommended Set)
Update `scripts/sources.json` to the following stable, high-signal official sources:

- `https://x.ai/`
- `https://x.ai/blog`
- `https://docs.x.ai/`
- `https://docs.x.ai/developers/release-notes` (highest value)
- `https://x.ai/api`
- `https://console.x.ai/` (Cloud Console)
- `https://docs.x.ai/developers/models`
- `https://docs.x.ai/developers/pricing`

This brings the total to 8 focused sources while eliminating previous duplicates.

### 2. New Summary Snippets File
In addition to the individual JSON files, `manifest.json`, and the full `scrape-bundle-*.md`, the scraper must also generate a short file named **`summary-snippets.md`** inside the same artifact.

**Format for `summary-snippets.md`** (example structure):

``````markdown
# Scrape Summary Snippets — 2026-W21

**Run started:** [timestamp]
**Source count:** 8

## 01-xai-home.json
Title: xAI
First sentences: [first 2–3 sentences of extracted_text]

## 02-xai-blog.json
Title: News: Research, Product & Company Updates | xAI
First sentences: [first 2–3 sentences of extracted_text]

[Repeat for every source...]
``````

This file provides GPT-5.5 with a quick, scannable overview of all sources without loading the full JSONs.

### 3. No Other Behavioral Changes
- Continue generating all individual JSON files + `manifest.json` + the consolidated Markdown bundle.
- All raw data remains in the artifact only — never committed.
- No changes to `.gitignore`, triggers, schedule, or dry-run mode.

## Implementation Instructions for GPT-5.5

When implementing this addendum:
1. Update `scripts/sources.json` with the exact list above.
2. Modify `scripts/daily_grok_scrape.py` to:
   - Generate `summary-snippets.md` in the artifact staging directory
   - Include it in the same artifact as the other files
3. Ensure the Markdown bundle generation continues unchanged.
4. You may update your own constitution (`planning/constitutions/gpt-5.5-constitution.md`) if needed for better maintainability.

**Do NOT modify:**
- `planning/PROJECT.md`
- `planning/implementation-plan.md`
- `planning/gpt-5.5-setup-plan.md`
- `planning/docs/scrape-bundle-artifact-addendum.md`

---
