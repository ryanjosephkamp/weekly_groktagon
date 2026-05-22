# GPT-5.5 Setup Plan for The Weekly Groktagon

**Status:** Draft setup plan for review. Do not execute until explicitly approved.

## References

- `planning/PROJECT.md` — master project context, locked folder structure, branding requirements, automation responsibilities, public-content rules, success criteria.
- `planning/implementation-plan.md` — locked v1.5 implementation plan, phase sequence, daily scrape technical specification, logo requirements.
- `planning/constitutions/gpt-5.5-constitution.md` — role definition, allowed and forbidden file boundaries, citation discipline, verification requirements.
- `assets/README.md` — current asset usage guidance for `assets/groktagon-logo.png`.

## 1. Setup Scope and Boundaries

This plan covers the scaffolding and preparation work needed to support the 4-week pilot described in the locked project documents. The setup work must create the repository structure, automation, reusable prompts, documentation, helper scripts, README expansion, and final blog post template needed for weekly publishing while preserving the required public/private separation and citation discipline.

The setup work must stay inside the allowed scaffolding role:

- Create new files and folders needed for the project setup.
- Expand `README.md`.
- Modify only files created during the approved setup work, except for the allowed README expansion.
- Do not modify or delete `Report-*.md`, `planning/PROJECT.md`, `planning/implementation-plan.md`, `planning/constitutions/gpt-5.5-constitution.md`, `.gitignore`, or any existing file not explicitly allowed.
- Do not generate final public blog prose that lacks source traceability.
- Do not commit raw scraped data.

## 2. Pre-Execution Verification

Before any setup implementation begins:

1. Confirm the current repository still contains:
   - `planning/PROJECT.md`
   - `planning/implementation-plan.md`
   - `planning/constitutions/gpt-5.5-constitution.md`
   - `assets/groktagon-logo.png`
   - `assets/README.md`
   - `.gitignore`
   - `README.md`
2. Re-read the locked planning documents and confirm no setup requirement has changed.
3. Verify that `assets/groktagon-logo.png` exists before adding README or template references to it.
4. Inspect `.gitignore` only to confirm `weekly/*/raw/` remains private; do not edit it unless the user explicitly approves.
5. Identify any existing generated setup files to avoid overwriting user-authored work.

## 3. Target Folder and File Scaffolding

Create the missing project folders required for the pilot:

1. `.github/workflows/`
   - Holds the daily scraping workflow.
2. `scripts/`
   - Holds project automation scripts.
3. `planning/prompts/`
   - Holds reusable report and synthesis prompt templates.
4. `planning/docs/`
   - Holds operational documentation for the pilot.
5. `weekly/`
   - Holds weekly issue folders.
6. `weekly/YYYY-WXX/` example structure, if approved as a placeholder:
   - `reports/`
   - `final-blog-post.md` template or example file only if the user wants an initial dated week folder.
   - Do not create or commit `raw/` contents.

If placeholder directories would otherwise be empty, add minimal `.gitkeep` files only in newly created non-raw folders that must be committed. Do not add `.gitkeep` inside `raw/` unless the user explicitly approves changing the private-data workflow.

## 4. README Expansion Plan

Expand `README.md` into a clear public project landing page that introduces the blog and pilot without exposing internal workflow details beyond what is appropriate for readers.

The README should include:

1. Logo at the top:
   - Use `assets/groktagon-logo.png`.
   - Prefer centered HTML for consistent GitHub rendering:
     - image source for root README rendering: `assets/groktagon-logo.png`
     - GitHub Pages root path to verify during setup: `/assets/groktagon-logo.png`
     - alt text: `The Weekly Groktagon`
     - width near `220` unless the user requests a different size.
2. Project title and short description.
3. Pilot status.
4. Publishing model:
   - Weekly GitHub Pages blog.
   - Each final post is synthesized from 8 component reports.
5. Public content standards:
   - cited claims only
   - original wording
   - references section
   - no raw scraped data in public commits
6. Repository structure summary.
7. Links section placeholders for:
   - repository
   - author GitHub profile
   - personal site
   - social profiles
8. References section citing the planning sources used for README content if factual project claims are included.

Avoid mentioning internal model assistance or process labels in public-facing README language.

## 5. Daily Scraping Automation Plan

Create `.github/workflows/daily-grok-scrape.yml` with:

1. Workflow name matching the project specification.
2. Triggers:
   - daily scheduled run at a fixed UTC time
   - manual `workflow_dispatch`
3. Permissions:
   - minimum required permission to write repository contents if committing generated scrape artifacts is approved.
4. Runtime:
   - Python setup step
   - dependency installation step
   - scraper execution step
   - conditional commit step only when generated output changes
5. Safety rules:
   - no raw data committed if `weekly/*/raw/` remains gitignored
   - polite request timing
   - clear nonzero failure on script errors
   - no secrets printed
6. Debugging support:
   - workflow summary showing scrape date, target week folder, source count, and whether changes were detected
   - artifact upload only if the user approves retaining raw scrape outputs outside git

Because the locked documents say raw scraped data belongs in `weekly/YYYY-WXX/raw/` but also must not be committed, implementation should clarify whether GitHub Actions should persist raw outputs as workflow artifacts, commit sanitized metadata elsewhere, or only run as a collection aid. This is a required clarification before final automation execution.

## 6. Scraper Script Plan

Create `scripts/daily_grok_scrape.py` to support the workflow.

The script should:

1. Determine the ISO week folder name in `YYYY-WXX` format.
2. Create `weekly/YYYY-WXX/raw/` locally at runtime.
3. Fetch a small stable list of official xAI/Grok pages maintained in a separate reviewed config file, such as `scripts/sources.json`, with each entry containing at minimum a source name and URL.
4. Use `requests` and `trafilatura` if dependency approval and advisory review pass.
5. Apply polite scraping practices:
   - descriptive user agent
   - request timeout
   - retry limits
   - delay between requests
6. Save structured output per source with:
   - title, if extractable
   - URL
   - retrieval timestamp
   - extracted text or extraction error
   - metadata needed for traceability
7. Maintain a machine-readable scrape manifest for debugging.
8. Avoid copying large raw text into committed public files.
9. Exit successfully when no source changes are detected and fail clearly on configuration or network errors that block the run.

## 7. Dependency and Security Plan

Before adding or pinning dependencies:

1. Confirm exact package names and versions.
2. Check supported ecosystems for advisories before adding dependencies.
3. Prefer minimal dependencies:
   - `requests`
   - `trafilatura`, if still preferred after advisory review
4. Add dependency declarations only if useful for repeatable automation, such as:
   - `requirements.txt`
5. Avoid broad dependency updates unrelated to the scraper.
6. Ensure scripts do not log secrets, tokens, or private raw content unnecessarily.

## 8. Prompt Template Plan

Create reusable internal prompt templates under `planning/prompts/`.

Recommended templates:

1. `planning/prompts/report-1-official-xai-sources.md`
   - Guides creation of the official xAI sources report from collected weekly raw files.
2. `planning/prompts/report-2-web-deep-dive.md`
   - Guides non-X, non-research open web synthesis.
3. `planning/prompts/report-3-x-platform-deep-dive.md`
   - Guides X-only review with strict relevance filtering.
4. `planning/prompts/report-4-research-platforms.md`
   - Guides research and academic synthesis.
5. `planning/prompts/report-5-community-ecosystem.md`
   - Guides community and ecosystem synthesis.
6. `planning/prompts/report-6-competitor-industry-context.md`
   - Guides competitor and broader industry context synthesis.
7. `planning/prompts/report-7-practical-tutorials.md`
   - Guides tutorial and reproducible workflow spotlight curation.
8. `planning/prompts/report-8-forward-looking-signals.md`
   - Guides grounded roadmap and signals synthesis.
9. `planning/prompts/final-blog-post-synthesis.md`
   - Guides integration of the 8 reports into a final weekly post.

Every prompt template should require:

- original wording
- clear citations
- `## References`
- no unsupported claims
- no raw data publication
- exactly the intended report scope

## 9. Final Blog Post Template Plan

Create a reusable final blog post template in `planning/prompts/final-blog-post-template.md` or `planning/docs/final-blog-post-template.md`.

The template should include:

1. Logo at the top:
   - Use `/assets/groktagon-logo.png` in the final blog post template because the primary rendering target is GitHub Pages.
   - Use repository-relative paths such as `../../assets/groktagon-logo.png` only for optional local or direct GitHub repository previews, not as the default publication path.
   - Include descriptive alt text.
   - Keep it as a header image or top-left branding, matching the project requirement.
2. Title placeholder:
   - `# The Weekly Groktagon — YYYY-WXX`
3. Publication date placeholder.
4. Short introduction placeholder.
5. Clickable table of contents with exactly 8 report sections.
6. Exactly 8 main section placeholders:
   - Official xAI Sources Summary
   - Additional Web Deep Dive
   - X Platform Deep Dive
   - Research Platforms & Academic Deep Dive
   - Community & Ecosystem Insights
   - Competitor & Industry Context
   - Practical Tutorials & Vibe-Coding Spotlight
   - Forward-Looking Signals & Roadmap Synthesis
7. Conclusion placeholder.
8. Links placeholder for repository, author GitHub, personal site, and social profiles.
9. `## References` placeholder.
10. Pre-publication checklist requiring citation coverage and public/private separation verification.

The template should not contain invented factual content. It should use placeholders where weekly facts will later be inserted from cited reports.

## 10. Pilot Operations Documentation Plan

Create operational docs in `planning/docs/`:

1. `planning/docs/weekly-workflow.md`
   - Describes the weekly cycle from daily scraping through final post publication.
2. `planning/docs/source-and-citation-guidelines.md`
   - Explains traceability, original wording, and reference expectations.
3. `planning/docs/debugging-github-action.md`
   - Explains how to manually dispatch the workflow, inspect logs, and diagnose scrape failures.
4. `planning/docs/publication-checklist.md`
   - Provides a repeatable checklist for each weekly final post.

Each doc with factual project requirements should cite the locked planning files in a References section.

## 11. Weekly Folder Preparation Plan

For the 4-week pilot, prepare repeatable folder creation rather than manually hard-coding every future date unless the user approves fixed pilot week folders.

Recommended approach:

1. Add a script such as `scripts/create_week_folder.py` or document a manual process.
2. The script should create:
   - `weekly/YYYY-WXX/reports/`
   - placeholder report filenames only if approved
   - a final blog post template copy only if approved
3. Do not create committed raw data.
4. Do not overwrite existing weekly folders or reports.
5. Print clear next steps after folder creation.

## 12. Debugging and Validation Plan

After setup implementation, validate in this order:

1. Repository safety check:
   - Confirm forbidden files were not modified.
   - Confirm no existing files were deleted.
   - Confirm no `weekly/*/raw/` data was staged.
2. Markdown review:
   - Confirm created docs include References sections where factual claims appear.
   - Confirm public-facing files avoid internal model attribution.
3. Script validation:
   - Run Python syntax checks for new scripts.
   - Run scraper in a safe dry-run mode if implemented.
4. Workflow validation:
   - Check workflow YAML syntax where available.
   - Confirm scheduled and manual triggers exist.
5. Git status review:
   - Verify only intended files changed.
6. Final security validation:
   - Confirm no secrets, tokens, or private raw content are present.
   - Run available repository validation tools before finalizing.

## 13. Suggested Execution Sequence After Approval

1. Re-read locked planning files and verify current repo state.
2. Create missing scaffold folders.
3. Expand `README.md` with logo and public project overview.
4. Create final blog post template with logo placeholder.
5. Create prompt templates for all 8 reports and final synthesis.
6. Create pilot operations docs.
7. Add scraper dependency declaration after advisory review.
8. Create scraper script with dry-run support.
9. Create GitHub Actions workflow.
10. Run validation checks.
11. Review changed files against forbidden-file boundaries.
12. Report completion with any unresolved questions.

## 14. Open Clarifications Before Execution

1. Should daily scrape outputs be stored only as workflow artifacts, or should sanitized summaries/manifests be committed somewhere outside `raw/`?
2. Which official xAI/Grok source URLs should be included in the initial stable source list?
3. What fixed UTC time should the daily workflow use?
4. Should the setup create a first real `weekly/YYYY-WXX/` folder for the current week, or only reusable templates and scripts?
5. What author links should appear in README and final blog post templates?
6. Should GitHub Pages use plain Markdown rendering only, or should the setup add a Pages/Jekyll configuration later?
7. Should the final blog post logo be centered at the top or placed as compact top-left branding?

## 15. Recommended Additions

1. Add a dry-run mode to the scraper before enabling any commit behavior.
2. Keep source lists in a small editable config file so updates do not require changing scraper logic.
3. Add a publication checklist that must be completed before each public final post.
4. Use workflow artifacts for raw scrape output unless the user approves another private retention strategy.
5. Treat the first week as an end-to-end pilot rehearsal before relying on automation for publication.
