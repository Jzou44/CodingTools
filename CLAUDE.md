# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Coding.Tools — a free, multilingual (9 languages) developer toolbox website with 62+ browser-based tools. Live at `coding.tools`.

## Running the Project

```bash
# Install dependencies
npm install

# Development (Eleventy dev server with hot reload)
npm run dev              # Serves on localhost:5500

# Build static site
npm run build            # Generates dist/ from src/
```

## Architecture

### Tech Stack

- **Static Site Generator**: Eleventy (11ty) v3 with Nunjucks templates
- **Styling**: Custom CSS (DM Sans font, category color system)
- **JavaScript**: Vanilla JS (no frameworks)
- **Output**: Pure static HTML/CSS/JS — no server-side processing

### Directory Structure

```
coding-tools/
├── .eleventy.js              # Eleventy configuration
├── package.json              # Project manifest and scripts
├── .gitignore                # Ignores node_modules/ and dist/
│
├── src/                      # Source files (Eleventy input)
│   ├── index.njk             # English homepage
│   ├── localized-index.njk   # Localized homepage generator
│   │
│   ├── _includes/            # Nunjucks layouts and partials
│   │   ├── base.njk          #   Base HTML structure
│   │   ├── navbar.njk        #   Top navigation bar
│   │   ├── sidebar.njk       #   Tool sidebar
│   │   ├── footer.njk        #   Footer with language switcher
│   │   └── tool-layout.njk   #   Shared tool page layout
│   │
│   ├── _data/                # Data files (tool metadata & translations)
│   │   ├── tools.json        #   Tool definitions (title, slug, category, icon)
│   │   ├── categories.json   #   Category definitions
│   │   ├── t.json            #   UI string translations
│   │   ├── toolData.json     #   Tool content translations
│   │   └── homepage.json     #   Homepage translations
│   │
│   ├── css/                  # Stylesheets
│   │   ├── style.css         #   Main stylesheet (design system)
│   │   └── tool.css          #   Tool page styles
│   │
│   ├── js/                   # Client-side JavaScript
│   │   ├── main.js           #   Homepage interactions
│   │   ├── tool-common.js    #   Shared tool utilities
│   │   ├── sqlformatter.js   #   SQL formatter library
│   │   ├── vkbeautify.js     #   Code beautifier library
│   │   └── numberToWords.min.js  # Number conversion library
│   │
│   └── tools/                # Tool page templates
│       ├── *.njk             #   English tools (62 files)
│       ├── cn/               #   Chinese Simplified
│       ├── tw/               #   Chinese Traditional
│       ├── jp/               #   Japanese
│       ├── kr/               #   Korean
│       ├── fr/               #   French
│       ├── de/               #   German
│       ├── es/               #   Spanish
│       └── pt/               #   Portuguese
│
└── dist/                     # Generated output (gitignored)
```

### i18n Pattern

Each language has a `<lang>.11tydata.js` file that loads translations from `_data/t.json` and `_data/toolData.json`, exposing computed data for templates.

Localized tool pages set `lang` and `toolId` in frontmatter; content renders via `{{ t.ui.* }}` and `{{ toolData.* }}` (with `| safe` for HTML).

Localized index pages generated from `localized-index.njk` using Eleventy pagination over the language list.

Key Nunjucks patterns:
- `{{ toolData.steps[i] | safe }}` — renders HTML in translated content
- `{{ homepage[lang].title }}` — localized homepage text
- `{% if lang and lang != 'en' %}/{{ lang }}/{% else %}/{% endif %}` — language-aware links

### Languages Supported

English (en), Chinese Simplified (cn), Chinese Traditional (tw), Japanese (jp), Korean (kr), French (fr), German (de), Spanish (es), Portuguese (pt)

## Key Patterns

- **Tool pages**: Each tool is a `.njk` file in `src/tools/` with localized versions in language subdirectories
- **Shared layouts**: Tool pages extend `tool-layout.njk` which extends `base.njk`
- **Data-driven**: Tool metadata, translations, and categories are all in `_data/` JSON files
- **Static output**: Eleventy generates pure static HTML/CSS/JS — no server-side processing at runtime
- **Client-side tools**: All tools run entirely in the browser (hash generators, formatters, converters, etc.)

## Development Notes

- After changing `src/` files, run `npm run build` to regenerate `dist/`
- The dev server (`npm run dev`) auto-rebuilds on file changes
- Tool pages use vanilla JavaScript for interactivity
- CSS uses a design system with category-specific color variables
