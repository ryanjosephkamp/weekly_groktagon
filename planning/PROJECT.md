# The Weekly Groktagon — PROJECT.md (v1.5)

**Locked Version**: v1.5  
**Repo**: github.com/ryanjosephkamp/weekly_groktagon  
**Status**: 4-week pilot (full 8 reports every week from Week 1)  
**Public launch**: After successful completion of the 4-week pilot

## 1. Project Overview
The Weekly Groktagon is a professional weekly blog focused exclusively on Grok and xAI developments. It is hosted on GitHub Pages and published every week.

Each edition is built from exactly **8 distinct component reports**. These reports are collected, analyzed, and synthesized into a single polished Markdown blog post with exactly 8 main sections (one per report).

**All public-facing content must strictly follow these rules**:
- Zero hallucinations — every factual claim must be traceable to a cited source.
- Original wording only — never copy source text verbatim unless placed in quotation marks with a clear inline citation.
- No AI attribution — never mention Grok, GPT-5.5, Claude, Copilot, or any AI assistance in the final blog post or any public file.
- Full citation discipline — every report and the final blog post must include a `## References` section.
- Privacy — raw scraped data stays private (`raw/` folder is gitignored).

## 2. The 8 Component Reports
Each Sunday the user provides Grok with the current week’s folder contents. Grok generates the reports one by one.

1. **Report 1: Official xAI Sources Summary**  
   Comprehensive synthesis of everything xAI officially published or updated about Grok during the week. Data comes only from the raw files collected by daily GitHub Actions.

2. **Report 2: Additional Web Deep Dive (Non-X, Non-Research Databases)**  
   New practical/technical information about Grok (features, benchmarks, novel use cases) from the open web, excluding X and research databases.

3. **Report 3: X Platform Deep Dive**  
   Additional new, relevant information from X only. Extremely careful filtering to avoid irrelevant content.

4. **Report 4: Research Platforms & Academic Deep Dive**  
   New research papers, pre-prints, or academic discussions that either directly reference Grok or contain findings with meaningful implications for Grok (e.g., new LLM architectures, reasoning techniques).

5. **Report 5: Community & Ecosystem Insights**  
   Real-world user adoption, creative applications, tips, integrations, and sentiment from developer communities outside of X (Reddit, Hacker News, Stack Overflow, GitHub discussions, etc.).

6. **Report 6: Competitor & Industry Context**  
   Balanced context on how developments in the broader AI/LLM landscape relate to or contrast with Grok during the week.

7. **Report 7: Practical Tutorials & Vibe-Coding Spotlight**  
   Curate and synthesize 1–3 of the most interesting, reproducible practical examples or workflows using Grok that emerged during the week.

8. **Report 8: Forward-Looking Signals & Roadmap Synthesis**  
   Credible hints, indirect signals, or strategic statements from xAI or reliable secondary sources about potential future developments (strictly grounded in cited sources only).

## 3. Locked Folder Structure
```
weekly_groktagon/
├── .github/workflows/               # Daily scraping Action (created by GPT-5.5)
├── assets/                          # Static assets (logo, images, etc.)
├── planning/
│   ├── PROJECT.md                   # ← This file (complete project context)
│   ├── implementation-plan.md
│   ├── constitutions/
│   │   └── gpt-5.5-constitution.md
│   ├── prompts/                     # Reusable prompt templates
│   └── docs/
├── weekly/
│   └── YYYY-WXX/
│       ├── raw/                     # Gitignored – raw scraped data
│       ├── reports/                 # Committed – Report-1.md … Report-8.md
│       └── final-blog-post.md       # Committed
├── .gitignore
└── README.md                        # Minimal at first (GPT-5.5 will expand)
```

## 3.5 Branding & Assets
- **Logo**: `assets/groktagon-logo.png` (white geometric icon on black background)
- The logo must appear at the top of:
  - The main `README.md`
  - Every final `final-blog-post.md` (as header image or top-left branding)
- GitHub Pages will serve the logo via the relative path `/assets/groktagon-logo.png`
- No other branding assets are required at this time.

## 4. GPT-5.5 Responsibilities (Scaffolding & Automation Agent)
You (GPT-5.5) are responsible for:
- Creating the GitHub Action workflow(s) according to the Technical Spec below.
- Setting up the correct folder structure.
- Creating any helper scripts or prompt templates needed.
- Expanding the `README.md` into a clear, professional project README.

**Strict Boundaries** (see full constitution in `planning/constitutions/gpt-5.5-constitution.md`):
- **Allowed**: Create new files/folders, modify files you created, expand README.md.
- **Strictly Forbidden**: Modify or delete any `Report-*.md`, `PROJECT.md`, `implementation-plan.md`, or the constitution file (unless explicitly instructed later).

## 5. GitHub Action Technical Spec (Daily Scrape)
- **Name**: `daily-grok-scrape.yml`
- **Trigger**: Daily at a fixed time + manual dispatch
- **Purpose**: Scrape official xAI/Grok sources and save clean structured data to `weekly/YYYY-WXX/raw/`
- **Tech**: Python + requests + trafilatura (preferred)
- **Rules**: Polite scraping, error handling, only commit if new content, never commit the `raw/` folder
- **Output**: JSON or Markdown files with title, URL, date, extracted text, metadata

## 6. Final Blog Post Requirements
The GPT-5.5 agent must produce one `final-blog-post.md` with:
- Clickable Table of Contents
- Short introduction
- Exactly 8 main sections (one per report)
- Conclusion
- Full `## References` section
- Links to the repo, author’s GitHub, personal site, and social profiles
- Professional, readable Markdown suitable for GitHub Pages

## 7. Success Criteria (End of 4-Week Pilot)
- 4 complete public blog posts published
- 100% citation coverage and zero hallucinations
- Zero AI attribution in any public content
- Clean public/private separation working
- Workflow feels sustainable for the user

---
