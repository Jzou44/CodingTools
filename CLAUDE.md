# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Coding.Tools — a free, multilingual (14 languages) developer toolbox website with 60+ browser-based tools. Live at `coding.tools`.

## Running the Project

```bash
# Local dev (Flask dev server)
pip install -r requirements.txt
python app.py                    # Flask dev server on 0.0.0.0:8080

# Production (Waitress)
python main.py                   # Waitress on 0.0.0.0:8080

# New UI preview (standalone static files)
node new_ui/server.js            # Serves new_ui/ on localhost:5500
```

Docker:
```bash
docker build -t codingtools:v20230410 .
docker run --rm -it -v /app:/app -v /tmp:/tmp -p 8080:8080 codingtools:v20230410 bash
```

## Architecture

### Backend (Flask)

- **`app.py`** — Creates Flask app, registers all blueprints, defines 404 handler
- **`main.py`** — Production entry: `waitress.serve(app)`
- **`Logic/`** — Business logic modules (config, image processing, IP geolocation, network tools)
- **`Blueprints/`** — ~75 blueprint files, one per tool category per language

Each tool route builds a `model` dict (SEO metadata, CDN versions, lang) and returns `render_template()`.

### i18n Pattern

No Flask-Babel. Each language has **duplicated blueprint files and templates** with language-prefixed URLs:
- English (default): `/md5`, `/json-formatter`
- Chinese: `/cn/md5`, `/cn/json-formatter`
- Japanese: `/jp/md5`, `/jp/json-formatter`
- 13 languages total: en, cn, tw, jp, kr, es, de, fr, it, pt, ru, id, ar

### Templates (Old UI)

```
templates/
├── Common/          # Shared partials (nav, footer, ads, SEO tags, CSS/JS includes)
├── DevTool/         # Homepage templates (one per language)
├── HexToDecimal/    # Number conversion tools (per-language subdirs)
├── JsonFormatter/   # JSON/XML/HTML/CSS/JS/SQL formatters
├── PasswordsGenerator/  # Hash generators, Base64, password tools
├── MyIpAddress/     # Network tools (IP, ping, DNS, traceroute, whois)
├── ImageUtilities/  # Image compression, EXIF tools
├── StringUtilities/ # Text tools (regex, word count, case converter)
└── Blog/            # Blog articles
```

Template inheritance: `base_layout.html` → tool templates via `{% extends %}` + `{% block content %}`.

### New UI (`new_ui/`) — Eleventy + Nunjucks

Standalone Eleventy-based redesign, not yet integrated into Flask. Uses Nunjucks templates with i18n support for 9 languages.

#### Running the New UI

```bash
# Build (Eleventy generates dist/ from src/)
cd new_ui && npx @11ty/eleventy

# Start dev server (serves dist/ on localhost:5500)
node new_ui/server.js

# After changing src/ files, rebuild then restart:
cd new_ui && npx @11ty/eleventy
# Kill old process: taskkill //F //PID <pid>  (Windows) or pkill -f "node.*server.js"
node new_ui/server.js
```

**Important**: The server serves from `dist/`, not `src/`. Always rebuild with Eleventy after template/data changes. The server handles directory URLs (e.g., `/cn` → `/cn/index.html`).

#### Directory Structure

```
new_ui/
├── server.js                    # Static file server (port 5500, serves dist/)
├── .eleventy.js                 # Eleventy config
├── package.json                 # Scripts: build, dev, debug
├── css/style.css                # Design system (DM Sans, category colors)
├── js/
│   ├── main.js                  # Scroll animations (IntersectionObserver), search filter, toast
│   └── tool-common.js           # Shared tool page utilities (copy, download, line numbers)
├── src/
│   ├── index.njk                # English homepage
│   ├── localized-index.njk      # Generates /cn/, /tw/, ... /pt/ index pages via pagination
│   ├── _includes/
│   │   ├── base.njk             # Base HTML layout (head, body, scripts blocks)
│   │   ├── navbar.njk           # Top nav (lang-aware home link)
│   │   ├── sidebar.njk          # Tool sidebar (lang-aware links + translated titles)
│   │   ├── footer.njk           # Footer with language switcher
│   │   └── tool-layout.njk      # Shared tool page layout (extends base.njk)
│   ├── _data/
│   │   ├── tools.json           # Tool metadata (title, slug, category, icon SVG)
│   │   ├── categories.json      # Category metadata (id, name, count, icon SVG)
│   │   ├── t.json               # UI string translations (buttons, labels) per language
│   │   ├── toolData.json        # Per-tool content translations (descriptions, steps, etc.)
│   │   └── homepage.json        # Homepage translations (hero text, category names, tool titles)
│   └── tools/                   # Tool page templates
│       ├── *.njk                # English tool pages (8 tools)
│       ├── cn/cn.11tydata.js    # Chinese data resolver + cn/*.njk tool pages
│       ├── tw/tw.11tydata.js    # Traditional Chinese
│       ├── jp/jp.11tydata.js    # Japanese
│       ├── kr/kr.11tydata.js    # Korean
│       ├── fr/fr.11tydata.js    # French
│       ├── de/de.11tydata.js    # German
│       ├── es/es.11tydata.js    # Spanish
│       └── pt/pt.11tydata.js    # Portuguese
└── dist/                        # Generated output (served by server.js)
```

#### i18n Pattern (New UI)

Each language has a `<lang>.11tydata.js` that loads translations from `t.json` and `toolData.json`, exposing computed data (`toolTitle`, `toolDescription`, `categoryName`, etc.) and `sidebarToolTitles` for the sidebar.

Localized tool pages set `lang` and `toolId` in frontmatter; content is rendered via `{{ t.ui.* }}` and `{{ toolData.* }}` (with `| safe` for HTML-containing fields like steps and descriptions).

Localized index pages are generated from `localized-index.njk` using Eleventy pagination over the language list.

Key Nunjucks patterns:
- `{{ toolData.steps[i] | safe }}` — renders HTML (e.g., `<strong>`) in translated content
- `{{ homepage[lang].title }}` — localized homepage text
- `{% if lang and lang != 'en' %}/{{ lang }}/{% else %}/{% endif %}` — language-aware links

Current tools (8): base64-encode, base64-decode, md5-generator, sha1-generator, sha256-generator, sha384-generator, sha512-generator, password-generator

### Key Patterns

- **Model dict**: Every route passes a `model` dict to templates with SEO fields (`headerTitle`, `description`, `keywords`, `image`), CDN versions, and `lang`
- **Production detection**: `FLAG_IS_PRODUCTION_ENV = not (os.name == 'nt')` — controls analytics, ads, IP detection
- **Caching**: Flask-Caching (simple, in-memory) for IP geolocation (30-day TTL) and whois lookups
- **Network tools**: Delegate to system commands via `os.popen()` (ping, nslookup, traceroute, whois)
- **Image tools**: Pillow for compression, exifread for EXIF, files stored at `/tmp/codingtool/{session}/`

### Infrastructure

- **Nginx** (`config/codingtools.conf`) → reverse proxy to Flask on port 8080
- **Docker**: Ubuntu 22.04 base with networking tools pre-installed
- **IP2Location**: SQLite DB at `/app/IP2Location/ip_4_20210626.db`, auto-generated from CSV
