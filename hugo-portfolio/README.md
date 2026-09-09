# Hugo portfolio staging area

This folder is a theme-agnostic Hugo scaffold for Christian González Pérez's portfolio.

## Purpose

- Keep the current Publii/GitHub Pages site untouched while the portfolio is designed.
- Test Hugo themes such as Hugo Profile or Adritian without changing `main`.
- Build the portfolio as an expandable résumé plus selected case studies.

## Current structure

- `hugo.yaml` — basic site configuration.
- `content/` — future résumé, experience, education, project and case-study content.
- `layouts/` — temporary placeholder layout until a theme is selected.
- `.github/workflows/hugo-portfolio-build.yml` — build validation only; it does **not** deploy or replace the live Glezper site.

## Deployment plan

1. Select the final Hugo theme.
2. Add/configure the theme and migrate the 2025 portfolio content into structured sections.
3. Build and review on a temporary/staging URL.
4. Only after approval, decide whether the portfolio should live at `glezper.com/portafolio` or a subdomain.

The live Publii deployment on `main` should remain untouched until the portfolio is approved.
