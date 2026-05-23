<p align="center">
  <img src="/assets/groktagon-logo.png" alt="The Weekly Groktagon" width="220">
</p>

# The Weekly Groktagon

The Weekly Groktagon is a weekly GitHub Pages publication for tracking xAI-related developments during a 4-week pilot phase. The repository is structured so each weekly edition can be assembled from eight component reports into one final Markdown post, matching the locked project structure in `planning/PROJECT.md` and `planning/implementation-plan.md`.

## Pilot Status

The project is in active setup for a 4-week pilot. Public launch is planned after the pilot is completed successfully, as defined in the locked project context.

## Publishing Model

- Each weekly edition is prepared as plain Markdown.
- Each final post is organized around exactly eight component report sections.
- Weekly content lives under `weekly/YYYY-WXX/`.
- Source collection output is kept out of public commits and handled through private workflow artifacts.

## Daily Source Collection

The daily source collection workflow now uses the optimized official xAI source list configured in `scripts/sources.json`:

- xAI home: <https://x.ai/>
- xAI blog: <https://x.ai/blog>
- xAI docs: <https://docs.x.ai/>
- xAI developer release notes: <https://docs.x.ai/developers/release-notes>
- xAI API: <https://x.ai/api>
- xAI Cloud Console: <https://console.x.ai/>
- xAI developer models: <https://docs.x.ai/developers/models>
- xAI developer pricing: <https://docs.x.ai/developers/pricing>

Each workflow artifact includes the individual source JSON files, `manifest.json`, a consolidated Markdown bundle named with the `scrape-bundle-YYYY-WXX-YYYYMMDD-HHMMSS.md` pattern, and `summary-snippets.md` for quick review. Raw scrape outputs and scrape-derived artifacts remain private workflow artifacts and must not be committed.

## Public Content Standards

Every public post should follow these standards:

- factual claims must be supported by cited sources;
- wording must be original unless text is clearly quoted and cited;
- each report and final post must include a `## References` section;
- raw scrape output must not be committed to the repository.

## Repository Structure

```text
weekly_groktagon/
├── .github/workflows/          # Daily source collection workflow
├── assets/                     # Static project assets
├── planning/                   # Project plans, prompts, and operating docs
├── scripts/                    # Automation scripts and source configuration
├── weekly/                     # Weekly Markdown publication folders
├── .gitignore
└── README.md
```

## Links

- Repository: <https://github.com/ryanjosephkamp/weekly_groktagon>
- GitHub: <https://github.com/ryanjosephkamp>
- Personal site: <https://ryanjosephkamp.github.io/>
- X: <https://x.com/ryanjosephkamp>
- LinkedIn: <https://www.linkedin.com/in/rjk1999/>
- YouTube: <https://www.youtube.com/@RyanJosephKamp>
- Hugging Face: <https://huggingface.co/ryanjosephkamp>

## References

- `planning/PROJECT.md`
- `planning/implementation-plan.md`
- `planning/gpt-5.5-setup-plan.md`
- `planning/docs/scrape-bundle-artifact-addendum.md`
- `planning/docs/scrape-sources-optimization-addendum.md`
- `planning/docs/scrape-sources-enhancement-addendum.md`
- `scripts/sources.json`
- `assets/README.md`
