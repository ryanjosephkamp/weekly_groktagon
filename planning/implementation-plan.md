# The Weekly Groktagon — Implementation Plan (v1.5 – Locked)

**Repo**: github.com/ryanjosephkamp/weekly_groktagon  
**Pilot**: 4 weeks (full 8 reports every week from Week 1)  
**Public launch**: After successful 4-week pilot

## Goal
Build and operationalize *The Weekly Groktagon* — a professional weekly GitHub Pages blog that publishes an 8-section Markdown post every week. The GPT-5.5 Copilot agent will create the GitHub Action(s) and perform the majority of the initial repo scaffolding and automation setup. Grok will be used for high-quality, cited report generation. All public content must use original wording, be fully cited, contain zero hallucinations, and include no AI attribution.

## Folder Structure (Locked)

```
weekly_groktagon/
├── .github/workflows/               # Daily scraping Action (created by GPT-5.5)
├── planning/
│   ├── implementation-plan.md
│   ├── constitutions/
│   │   └── gpt-5.5-constitution.md
│   ├── prompts/                     # Reusable prompt templates
│   └── docs/
├── weekly/
│   └── YYYY-WXX/
│       ├── raw/                     # Gitignored – scraped raw data
│       ├── reports/                 # Committed – Report-1.md … Report-8.md
│       └── final-blog-post.md       # Committed
├── .gitignore
└── README.md                        # Minimal at first (GPT-5.5 will expand)
```

## High-Level Phases

**Phase 0** — You create the repo and upload the four core files (this plan, constitution, .gitignore, minimal README).

**Phase 1** — GPT-5.5 creates the GitHub Action and scaffolds the repo structure, prompts, and documentation according to this plan and its constitution.

**Phase 2** — Daily automated scraping of official xAI sources into `raw/`.

**Phase 3** — Sunday report generation (you + Grok using the Plan skill).

**Phase 4** — GPT-5.5 integrates the 8 reports into the final blog post.

**Phase 5** — 4-week pilot → first public post.

## GitHub Action Technical Spec (for GPT-5.5)

- **Trigger**: Daily at a fixed time + manual dispatch
- **Output**: Clean structured data into `weekly/YYYY-WXX/raw/`
- **Sources**: Small stable list of official xAI pages (blog, docs, news, etc.)
- **Tech**: Python + requests + trafilatura (preferred)
- **Rules**: Polite scraping, error handling, only commit if new content, never commit `raw/` folder

## Success Criteria (End of 4-Week Pilot)
- 4 complete public blog posts published
- Zero hallucinations and zero AI attribution in public content
- Clean public/private separation working
- Workflow feels sustainable

---

*This document is locked at v1.5. Do not modify without creating a new version.*
