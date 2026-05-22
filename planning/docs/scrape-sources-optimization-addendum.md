# Scrape Sources Optimization & Bundle Addendum

**Date:** 2026-05-22  
**Status:** Approved plan modification  
**Related documents:** 
- `planning/gpt-5.5-setup-plan.md`
- `planning/docs/scrape-bundle-artifact-addendum.md`
- `scripts/sources.json`

## Purpose

This addendum refines the daily scraping configuration to reduce duplication, increase signal quality, and provide GPT-5.5 with higher-value official xAI content for Report 1 (Official xAI Sources Summary) while preserving all previous privacy and artifact rules.

## Approved Changes

### 1. Source List Optimization (Remove Duplicates)
Remove the following low-value / duplicate sources:
- `https://x.ai/news` (nearly identical to blog)
- `https://grok.x.ai/` (nearly identical to x.ai home)

### 2. Add High-Value Sources
Add the following stable, high-signal official xAI pages to `scripts/sources.json`:

- `https://x.ai/api` (API landing page)
- `https://console.x.ai/` (console overview — if publicly accessible)
- Any additional stable changelog or “What’s New” pages discovered during testing

The final recommended minimal high-value list is:
- `https://x.ai/`
- `https://x.ai/blog`
- `https://docs.x.ai/`
- `https://docs.x.ai/developers/release-notes` (highest value source)
- `https://x.ai/api`

### 3. Continue Existing Behavior
- Continue generating all individual JSON files + `manifest.json`.
- Continue generating the consolidated `scrape-bundle-YYYY-WXX-YYYYMMDD-HHMMSS.md` Markdown artifact (exact format already implemented in the previous addendum).
- All raw data and artifacts remain non-committed and private.

### 4. Optional Enhancement (Recommended)
Optionally add a short `summary-snippets.md` file inside the same artifact containing just the title + first 2–3 sentences of each source. This provides GPT-5.5 a quick overview without loading the full JSONs immediately.

## Impact on Existing Behavior

- No change to `.gitignore`, commit behavior, or artifact privacy rules.
- No change to the Markdown bundle generation logic or filename convention.
- The scraper will now produce cleaner, higher-signal data for Report 1.

## Implementation Instructions for GPT-5.5

When implementing this addendum:
1. Update `scripts/sources.json` with the optimized list above.
2. Modify `scripts/daily_grok_scrape.py` if needed to support any new sources gracefully.
3. Ensure the Markdown bundle continues to be generated correctly.
4. (Optional) Add logic for `summary-snippets.md` if you consider it valuable.
5. You may update your own constitution (`planning/constitutions/gpt-5.5-constitution.md`) if it improves maintainability of the scraper.

Do **not** modify:
- `planning/PROJECT.md`
- `planning/implementation-plan.md`
- `planning/gpt-5.5-setup-plan.md`
- `planning/docs/scrape-bundle-artifact-addendum.md`

---