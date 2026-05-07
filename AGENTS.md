# AGENTS.md

This file provides guidance to Codex and other coding agents when working in this repository.

## Project Overview

Coding.Tools is a free multilingual developer toolbox website at `coding.tools`.

- 63 browser-based tools
- 9 languages: `en`, `cn`, `tw`, `jp`, `kr`, `fr`, `de`, `es`, `pt`
- 5 categories: image utilities, formatter/minifier, hash/cryptography, number conversion, string/text utilities
- Static output only: generated HTML/CSS/JS and assets in `dist/`

## Running the Project

```bash
npm install

npm run check          # validate structure and i18n coverage
npm run build          # run check, then generate dist/
npm run dev            # Eleventy dev server on localhost:5500
npm run debug          # Eleventy dev server with debug logging

npm run docker:build   # build nginx static-site image
npm run docker:run     # run container on localhost:8080
npm run docker:stop    # stop and remove local test container
npm run docker:test    # build and run container
```

There is no Node production server in this repo. Production/deployment serves `dist/` as static files.

## Architecture

### Tech Stack

- Static site generator: Eleventy v3 with Nunjucks templates
- Styling: custom CSS in `src/css/`
- JavaScript: vanilla browser JavaScript in `src/js/` and page templates
- Output: static HTML/CSS/JS/assets in `dist/`
- Docker: nginx image that serves the generated static files

### Directory Structure

```text
coding-tools/
├── .eleventy.js
├── Dockerfile
├── package.json
├── scripts/
│   └── check-structure.js
├── src/
│   ├── index.njk
│   ├── localized-index.njk
│   ├── sitemap.xml.njk
│   ├── robots.txt.njk
│   ├── _includes/
│   │   ├── base.njk
│   │   ├── navbar.njk
│   │   ├── sidebar.njk
│   │   ├── footer.njk
│   │   ├── tool-layout.njk
│   │   ├── homepage-content.njk
│   │   ├── homepage-footer.njk
│   │   ├── photo2pixel-page.njk
│   │   └── macros/
│   ├── _data/
│   │   ├── site.js
│   │   ├── tools.json
│   │   ├── categoryDefinitions.json
│   │   ├── categories.js
│   │   ├── homepage.json
│   │   ├── t/
│   │   │   ├── en.json
│   │   │   └── <lang>.json
│   │   ├── t.js
│   │   ├── toolData/
│   │   │   ├── base64-encode.json
│   │   │   └── <tool-slug>.json
│   │   ├── toolData.js
│   │   ├── makeToolLangData.js
│   │   └── loadJsonDirectory.js
│   ├── css/
│   ├── js/
│   ├── assets/
│   └── tools/
│       ├── *.njk
│       ├── cn/
│       ├── tw/
│       ├── jp/
│       ├── kr/
│       ├── fr/
│       ├── de/
│       ├── es/
│       └── pt/
└── dist/
```

## i18n Pattern

- Languages are defined in `src/_data/site.js`.
- UI strings live in `src/_data/t/<lang>.json` and are loaded by `src/_data/t.js`.
- Tool content lives in `src/_data/toolData/<slug>.json`; each file contains all 9 language objects.
- `src/_data/toolData.js` merges per-tool JSON files into a language-keyed lookup.
- `src/_data/makeToolLangData.js` exposes `lang`, `t`, `toolData`, `toolDataLookup`, computed metadata, and sidebar titles to tool templates.
- Localized tool pages should set `lang`, `toolId`, `category`, `activeTool`, and `permalink`.
- Localized tool pages should render translated content through `{{ t.ui.* }}` and `{{ toolData.* }}`.

Do not add localized frontmatter fields for:

- `title`
- `description`
- `toolTitle`
- `toolDescription`
- `categoryName`

Those values are computed from `toolData`; adding them to localized templates overrides translations and fails `npm run check`.

## Validation Rules

`scripts/check-structure.js` is the source of truth for structural checks. It verifies:

- language sets in `homepage`, `t`, and `site`
- homepage and UI translation shape against English
- one `toolData/<slug>.json` per `tools.json` slug
- every toolData file has all languages
- localized toolData keys and array lengths match the English baseline
- localized fields are not empty when the English baseline is non-empty
- homepage tool titles and category translations cover all tools/categories
- category counts match actual tools
- English and localized tool templates exist
- localized `toolId` and permalink match expected values
- localized templates do not use metadata frontmatter overrides
- localized templates do not contain known hard-coded English UI regressions

`npm run build` runs `npm run check` first via `prebuild`.

## Key Patterns

- Tool pages extend `src/_includes/tool-layout.njk`, which extends `base.njk`.
- Homepage content is data-driven through `src/_data/homepage.json`.
- Localized index pages are generated from `src/localized-index.njk` via Eleventy pagination.
- The sitemap iterates every language and every tool slug.
- Client-side tools must run entirely in the browser.
- Shared tool helpers belong in `src/js/tool-common.js` when they are reusable.
- Generated `dist/` and `node_modules/` are gitignored.

## Adding or Updating Tools

1. Add or update the tool in `src/_data/tools.json`.
2. Add or update `src/_data/toolData/<slug>.json` with all 9 language objects.
3. Add shared UI strings to every `src/_data/t/<lang>.json` if needed.
4. Add or update `src/tools/<slug>.njk`.
5. Add or update every localized template under `src/tools/<lang>/<slug>.njk`.
6. Run `npm run check`.
7. Run `npm run build`.

## Development Notes

- Prefer existing Nunjucks/data patterns over hard-coded localized strings.
- Use `{{ value | safe }}` only for translation fields that intentionally contain HTML.
- Keep tool behavior client-side; do not introduce server-side runtime dependencies.
- If translations or localized templates change, run `npm run check` before building.
- If rendered output matters, run `npm run build` and inspect `dist/`.
