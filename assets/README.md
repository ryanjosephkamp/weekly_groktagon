# assets/

This folder contains all static assets (logos, images, icons, banners, etc.) used by **The Weekly Groktagon** blog and GitHub Pages site.

## Current Assets

- **`groktagon-logo.png`** — The official project logo (white geometric Groktagon icon on black background).

**Used in:**
- Main `README.md`
- Every weekly `final-blog-post.md` (as header/branding image)

## How to Reference Assets

In any Markdown file (README.md or final blog posts), use the relative path:

```markdown
![The Weekly Groktagon](/assets/groktagon-logo.png)
```

For a centered logo with custom sizing:

```markdown
<p align="center">
  <img src="/assets/groktagon-logo.png" alt="The Weekly Groktagon" width="220">
</p>
```

## Guidelines

- Use clear, descriptive, kebab-case filenames (e.g. `weekly-cover-2026-w22.png`)
- Prefer PNG (with transparency when appropriate) or SVG for logos/icons
- Optimize all images for web performance
- When adding new assets, briefly document them in this file

---

*Part of The Weekly Groktagon project*
