# GPT-5.5 Setup Plan for The Weekly Groktagon

**Status:** Updated setup plan for review. Do not execute until explicitly approved.

## References

- `planning/PROJECT.md` — master project context, locked folder structure, branding requirements, automation responsibilities, public-content rules, success criteria.
- `planning/implementation-plan.md` — locked v1.5 implementation plan, phase sequence, daily scrape technical specification, logo requirements.
- `planning/constitutions/gpt-5.5-constitution.md` — role definition, allowed and forbidden file boundaries, citation discipline, verification requirements.
- `assets/README.md` — current asset usage guidance for `assets/groktagon-logo.png`.
- User clarification responses supplied on 2026-05-22 — approved scrape artifact handling, source list, workflow schedule, first pilot week folder, author links, Markdown-only publishing, logo path, logo placement, artifact retention, logo width, and recommended additions.

## 1. Setup Scope and Boundaries

This plan covers the scaffolding and preparation work needed to support the 4-week pilot described in the locked project documents. The setup work must create the repository structure, automation, reusable prompts, documentation, helper scripts, README expansion, and final blog post template needed for weekly publishing while preserving the required public/private separation and citation discipline.

The setup work must stay inside the allowed scaffolding role:

- Create new files and folders needed for the project setup.
- Expand `README.md`.
- Modify only files created during the approved setup work, except for the allowed README expansion and this user-approved update to `planning/gpt-5.5-setup-plan.md`.
- Do not modify or delete `Report-*.md`, `planning/PROJECT.md`, `planning/implementation-plan.md`, `planning/constitutions/gpt-5.5-constitution.md`, `.gitignore`, or any existing file not explicitly allowed.
- Do not generate final public blog prose that lacks source traceability.
- Do not commit raw scraped data, sanitized summaries, scrape manifests, or other scrape outputs.
- Do not begin implementation until the user explicitly approves execution after this plan-alignment phase is complete.

## 2. Confirmed User Decisions

The following decisions are now approved and should be treated as locked for setup unless the user changes them later:

1. Raw scrape outputs must be stored only as GitHub Actions workflow artifacts and must never be committed to the repository.
2. No sanitized summaries or manifests should be committed outside `raw/`.
3. Initial official source list should be maintained in `scripts/sources.json` and include:
   - `https://x.ai/`
   - `https://x.ai/blog`
   - `https://x.ai/news`
   - `https://grok.x.ai/`
   - `https://docs.x.ai/`
   - `https://docs.x.ai/developers/release-notes`
4. Daily workflow schedule should be `03:00 UTC`.
5. Create the first real pilot week folder: `weekly/2026-W21/`.
6. In `weekly/2026-W21/`, include:
   - `reports/`
   - a placeholder `final-blog-post.md` copied from the approved final blog post template structure.
7. Do not commit `weekly/2026-W21/raw/` or any raw scrape data.
8. Author links for README and templates:
   - GitHub: `https://github.com/ryanjosephkamp`
   - Personal website / portfolio: `https://ryanjosephkamp.github.io/`
   - X: `https://x.com/ryanjosephkamp`
   - LinkedIn: `https://www.linkedin.com/in/rjk1999/`
   - YouTube: `https://www.youtube.com/@RyanJosephKamp`
   - Hugging Face: `https://huggingface.co/ryanjosephkamp`
9. Use plain Markdown rendering for now.
10. Do not add Jekyll, `_config.yml`, or additional GitHub Pages configuration at this stage.
11. Use the root-relative logo path `/assets/groktagon-logo.png` in README and all templates.
12. Use a centered logo at the top of README and final blog post templates.
13. Add a scraper dry-run mode before enabling normal execution.
14. Keep source URLs in a small editable config file.
15. Add a publication checklist.
16. Treat the first week as an end-to-end pilot rehearsal before relying on automation for publication.
17. Use the GitHub default artifact retention period for workflow artifacts.
18. Use an approximate logo display width of `220`.
19. Manually review the first workflow artifact after the first run before relying on the workflow for the full pilot.
20. Keep the official source list intentionally small during Week 1 and expand only after the pilot workflow is stable.

## 3. Pre-Execution Verification

Before any setup implementation begins:

1. Confirm the current repository still contains:
   - `planning/PROJECT.md`
   - `planning/implementation-plan.md`
   - `planning/constitutions/gpt-5.5-constitution.md`
   - `planning/gpt-5.5-setup-plan.md`
   - `assets/groktagon-logo.png`
   - `assets/README.md`
   - `.gitignore`
   - `README.md`
2. Re-read the locked planning documents and confirm no setup requirement has changed.
3. Verify that `assets/groktagon-logo.png` exists before adding README or template references to it.
4. Inspect `.gitignore` only to confirm `weekly/*/raw/` remains private; do not edit it unless the user explicitly approves.
5. Identify any existing generated setup files to avoid overwriting user-authored work.
6. Confirm this updated plan has no unresolved required clarification questions before execution.

## 4. Target Folder and File Scaffolding

Create the missing project folders required for the pilot:

1. `.github/workflows/`
   - Holds the daily scraping workflow.
2. `scripts/`
   - Holds project automation scripts and source configuration.
3. `planning/prompts/`
   - Holds reusable report and synthesis prompt templates.
4. `planning/docs/`
   - Holds operational documentation for the pilot.
5. `weekly/`
   - Holds weekly issue folders.
6. `weekly/2026-W21/`
   - First real pilot week folder.
7. `weekly/2026-W21/reports/`
   - Holds committed weekly report drafts when the user adds them.
8. `weekly/2026-W21/final-blog-post.md`
   - Placeholder final blog post file copied from the approved template structure.

If placeholder directories would otherwise be empty, add minimal `.gitkeep` files only in newly created non-raw folders that must be committed. Do not add `.gitkeep` inside any `raw/` folder.

## 5. README Expansion Plan

Expand `README.md` into a clear public project landing page that introduces the blog and pilot without exposing unnecessary internal workflow details.

The README should include:

1. Centered logo at the top:
   - Image path: `/assets/groktagon-logo.png`
   - Alt text: `The Weekly Groktagon`
   - Display width approximately `220`.
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
7. Links section:
   - Repository link.
   - Author GitHub profile: `https://github.com/ryanjosephkamp`
   - Personal website / portfolio: `https://ryanjosephkamp.github.io/`
   - X: `https://x.com/ryanjosephkamp`
   - LinkedIn: `https://www.linkedin.com/in/rjk1999/`
   - YouTube: `https://www.youtube.com/@RyanJosephKamp`
   - Hugging Face: `https://huggingface.co/ryanjosephkamp`
8. References section citing the planning sources used for README content.

Avoid mentioning internal model assistance or process labels in public-facing README language.

## 6. Daily Scraping Automation Plan

Create `.github/workflows/daily-grok-scrape.yml` with:

1. Workflow name matching the project specification.
2. Triggers:
   - daily scheduled run at `03:00 UTC`
   - manual `workflow_dispatch`
3. Permissions:
   - minimum permissions needed to read repository contents and upload workflow artifacts.
   - no repository write permission for scrape outputs because no scrape outputs should be committed.
4. Runtime:
   - Python setup step
   - dependency installation step
   - scraper execution step
   - workflow artifact upload step for raw scrape outputs
5. Safety rules:
   - no raw data committed
   - no sanitized summaries or manifests committed
   - polite request timing
   - clear nonzero failure on script errors
   - no secrets printed
6. Debugging support:
   - workflow summary showing scrape date, target week folder, source count, dry-run status, and artifact name.
   - artifact upload for raw scrape outputs only.

The workflow must not run any commit step for scrape outputs. Do not set a custom artifact retention period during setup; use the GitHub default unless the user later approves a different retention policy.

## 7. Scraper Script Plan

Create `scripts/daily_grok_scrape.py` to support the workflow.

The script should:

1. Determine the ISO week folder name in `YYYY-WXX` format by default.
2. Allow an optional output directory argument so GitHub Actions can write raw outputs to a temporary artifact staging directory instead of the repository working tree.
3. Include a dry-run mode that validates configuration, resolves the target week, lists sources, and exits without fetching or writing scrape data.
4. Use `scripts/sources.json` as the editable reviewed source list.
5. Start with these source URLs:
   - `https://x.ai/`
   - `https://x.ai/blog`
   - `https://x.ai/news`
   - `https://grok.x.ai/`
   - `https://docs.x.ai/`
   - `https://docs.x.ai/developers/release-notes`
6. Use `requests` and `trafilatura` if dependency approval and advisory review pass.
7. Apply polite scraping practices:
   - descriptive user agent
   - request timeout
   - retry limits
   - delay between requests
8. Save structured raw output per source in the artifact staging directory with:
   - title, if extractable
   - URL
   - retrieval timestamp
   - extracted text or extraction error
   - metadata needed for traceability
9. Maintain a machine-readable scrape manifest inside the artifact only, not in the repository.
10. Avoid copying raw text into committed public files.
11. Exit successfully when no source changes are detected and fail clearly on configuration or network errors that block the run.

## 8. Dependency and Security Plan

Before adding or pinning dependencies:

1. Confirm exact package names and versions.
2. Check supported ecosystems for advisories before adding dependencies.
3. Prefer minimal dependencies:
   - `requests`
   - `trafilatura`, using a current reviewed version if advisory checks pass.
4. Add dependency declarations only if useful for repeatable automation, such as:
   - `requirements.txt`
5. Avoid broad dependency updates unrelated to the scraper.
6. Ensure scripts do not log secrets, tokens, or private raw content unnecessarily.
7. If advisory checks identify a blocking issue, stop and ask the user before choosing an alternate extraction library.

## 9. Prompt Template Plan

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

## 10. Final Blog Post Template Plan

Create a reusable final blog post template in `planning/prompts/final-blog-post-template.md` or `planning/docs/final-blog-post-template.md`.

The template should include:

1. Centered logo at the top:
   - Image path: `/assets/groktagon-logo.png`
   - Alt text: `The Weekly Groktagon`
   - Display width approximately `220`.
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
8. Links placeholder for:
   - repository
   - author GitHub profile: `https://github.com/ryanjosephkamp`
   - personal website / portfolio: `https://ryanjosephkamp.github.io/`
   - X: `https://x.com/ryanjosephkamp`
   - LinkedIn: `https://www.linkedin.com/in/rjk1999/`
   - YouTube: `https://www.youtube.com/@RyanJosephKamp`
   - Hugging Face: `https://huggingface.co/ryanjosephkamp`
9. `## References` placeholder.
10. Pre-publication checklist requiring citation coverage and public/private separation verification.

The template should not contain invented factual content. It should use placeholders where weekly facts will later be inserted from cited reports.

Copy this same template structure into `weekly/2026-W21/final-blog-post.md` as empty placeholder content during execution.

## 11. Pilot Operations Documentation Plan

Create operational docs in `planning/docs/`:

1. `planning/docs/weekly-workflow.md`
   - Describes the weekly cycle from daily scraping through final post publication.
2. `planning/docs/source-and-citation-guidelines.md`
   - Explains traceability, original wording, and reference expectations.
3. `planning/docs/debugging-github-action.md`
   - Explains how to manually dispatch the workflow, inspect logs, retrieve workflow artifacts, and diagnose scrape failures.
4. `planning/docs/publication-checklist.md`
   - Provides a repeatable checklist for each weekly final post.

Each doc with factual project requirements should cite the locked planning files in a References section.

## 12. Weekly Folder Preparation Plan

Prepare `weekly/2026-W21/` as the first real pilot week folder.

During execution:

1. Create `weekly/2026-W21/reports/`.
2. Add a `.gitkeep` file inside `weekly/2026-W21/reports/` if needed to commit the folder before report files exist.
3. Create `weekly/2026-W21/final-blog-post.md` from the final blog post template structure.
4. Do not create committed raw data.
5. Do not create `weekly/2026-W21/raw/` unless the runtime scraper needs it locally; if created by a run, it must remain uncommitted due to `.gitignore`.
6. Do not overwrite existing weekly folders or reports.

Also create a reusable script such as `scripts/create_week_folder.py` or document a manual process for future weeks. The script should not overwrite existing files.

## 13. Debugging and Validation Plan

After setup implementation, validate in this order:

1. Repository safety check:
   - Confirm forbidden files were not modified.
   - Confirm no existing files were deleted.
   - Confirm no scrape outputs were staged.
   - Confirm no `weekly/*/raw/` data was staged.
2. Markdown review:
   - Confirm created docs include References sections where factual claims appear.
   - Confirm public-facing files avoid internal model attribution.
3. Script validation:
   - Run Python syntax checks for new scripts.
   - Run scraper dry-run mode.
   - Confirm normal scraper output goes to an artifact staging directory, not a committed repo path.
4. Workflow validation:
   - Check workflow YAML syntax where available.
   - Confirm scheduled and manual triggers exist.
   - Confirm schedule is `03:00 UTC`.
   - Confirm artifact upload exists.
   - Confirm workflow artifact retention uses the GitHub default.
   - Confirm no commit step exists for scrape outputs.
5. Git status review:
   - Verify only intended files changed.
6. Final security validation:
   - Confirm no secrets, tokens, or private raw content are present.
   - Run available repository validation tools before finalizing.

## 14. Suggested Execution Sequence After Final Approval

1. Re-read locked planning files and verify current repo state.
2. Create missing scaffold folders.
3. Expand `README.md` with centered logo and public project overview.
4. Create final blog post template with centered logo.
5. Create `weekly/2026-W21/reports/`.
6. Create `weekly/2026-W21/final-blog-post.md` placeholder from the final blog post template.
7. Create prompt templates for all 8 reports and final synthesis.
8. Create pilot operations docs.
9. Add scraper dependency declaration after advisory review.
10. Create `scripts/sources.json`.
11. Create scraper script with dry-run support and artifact-staging output support.
12. Create GitHub Actions workflow with daily `03:00 UTC` schedule and artifact upload.
13. Run validation checks.
14. Review changed files against forbidden-file boundaries.
15. After the first workflow run, manually review the first artifact before relying on the workflow for the full pilot.
16. Report completion with any unresolved issues.

## 15. Remaining Clarification Questions Before Execution

No required clarification questions remain before execution.

No optional clarification questions remain before execution.

## 16. Remaining Recommendations

No blocking or non-blocking recommendations remain before execution. The previously listed non-blocking recommendations have been approved and incorporated into the setup plan.

## 17. Plan Alignment Status

This plan is fully aligned for execution. If the user explicitly approves execution, setup can begin without additional clarification questions or recommendations.
