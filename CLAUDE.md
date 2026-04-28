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

### New UI (`new_ui/`) — In Progress

Standalone static HTML redesign, not yet integrated into Flask. Silicon Valley aesthetic.

```
new_ui/
├── index.html          # Homepage with search + 71 tool cards
├── tool.html           # JSON Formatter (template for tool pages)
├── base64-encode.html  # Working Base64 encode/decode tool
├── server.js           # Dev server (port 5500, resolves .html extensions)
├── css/style.css       # Design system (Plus Jakarta Sans, category colors)
└── js/main.js          # Scroll animations, search filter, toast system
```

Design system: CSS custom properties in `style.css`. Category-specific accent colors (purple/blue/cyan/amber/emerald/pink). All icons are inline SVGs (no Font Awesome). All tool logic runs client-side.

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
