<div align="center">

# Coding.Tools

### The Developer Toolbox

**63 free, browser-based developer tools that respect your privacy.**

No sign-up. No tracking. Website tools run in your browser. A small optional A2A runtime exposes a server-side subset of deterministic tools for agent-to-agent calls.

[![Live Site](https://img.shields.io/badge/Live-coding.tools-blue?style=for-the-badge)](https://coding.tools)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#license)
[![Languages](https://img.shields.io/badge/Languages-9-orange?style=for-the-badge)](#internationalization)

<br/>

**English** | [中文](README_CN.md)

</div>

---

## Why Coding.Tools?

- **Privacy first**: tools run locally in the browser.
- **Static-first design**: the production website is plain HTML, CSS, JavaScript, and static assets.
- **A2A runtime**: `/a2a/*` exposes supported deterministic tools for agent clients.
- **Multilingual**: English plus 8 localized language trees.
- **No framework runtime**: Eleventy generates the site; tools use vanilla JavaScript.
- **Checked translations**: `npm run check` validates page coverage, translation shape, category counts, and common localized-template regressions.

---

## Tools at a Glance

| Category | Tools | What You Can Do |
|----------|------:|-----------------|
| Hash & Cryptography | 8 | Base64, MD5, SHA-1/256/384/512, password generation |
| Number Conversion | 26 | Hex, decimal, binary, octal, ASCII, Roman numerals, RGB/RGBA, fractions, percentages |
| String & Text Utilities | 8 | Text editing, regex testing/replacement, word and character counts, case conversion |
| Formatter & Minifier | 14 | JSON, XML, HTML, CSS, JavaScript, SQL formatting and minification, JSON/XML conversion |
| Image Utilities | 7 | PNG/JPEG compression, progressive JPEG, Photo2Pixel, image Base64, EXIF viewing/removal |

**63 tools** across **5 categories**, available in **9 languages**.

---

## Quick Start

```bash
npm install
npm run dev
```

The Eleventy dev server runs at [http://localhost:5500](http://localhost:5500).

## Commands

```bash
npm run check          # Validate structure, i18n coverage, categories, and localized templates
npm run build          # Run check, then build the static site into dist/
npm run dev            # Eleventy dev server on localhost:5500
npm run debug          # Eleventy dev server with debug logging
npm run a2a            # A2A runtime on localhost:5510
npm run a2a:test       # Validate the A2A runtime endpoints
npm run mcp            # MCP stdio server for local MCP clients
npm run mcp:test       # Validate MCP HTTP and stdio interfaces
npm run skills:generate # Generate English Codex skills for every MCP tool
npm run skills:check   # Validate generated Codex skills and installer metadata
npm run docker:build   # Build the nginx-based Docker image
npm run docker:run     # Run the Docker image on localhost:8080
npm run docker:smoke   # Verify the running Docker container
npm run docker:stop    # Stop and remove the local Docker test container
npm run docker:test    # Build, run, and verify the Docker image
```

The website is served from the generated `dist/` directory. The A2A/MCP runtime is a separate Node process proxied by nginx under `/a2a/*` and `/mcp`.
Set `SITE_BASE_URL` when building for a non-production host, for example `docker build --build-arg SITE_BASE_URL=http://localhost:8080 -t coding-tools .`.

## MCP

The MCP runtime exposes every entry in `src/_data/tools.json` through `tools/list`. Deterministic server-side tools execute directly through `tools/call`; browser-only image tools return a typed MCP tool error with a link to the web UI.

For HTTP clients, send JSON-RPC requests to `/mcp` with `Content-Type: application/json`, `Accept: application/json, text/event-stream`, and `MCP-Protocol-Version: 2025-06-18`. For MCP clients that hide JSON-RPC details, configure the endpoint and pass only the `params.arguments` object shown in each skill's Example Arguments section.

HTTP endpoint:

```bash
curl http://localhost:5510/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -H 'MCP-Protocol-Version: 2025-06-18' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"sha256-generator","arguments":{"input":"abc"}}}'
```

Local stdio server command for MCP clients:

```bash
node server/mcp-stdio.js
```

## Codex Skills

This repository includes English Codex skills for every Coding.Tools MCP tool. Each skill contains the MCP tool name, input schema, output schema, example arguments, parsing guidance, and a production endpoint.

The bundled examples use synthetic, non-sensitive values. Tools that need no input, or browser-only image tools that only return a web UI link through MCP, intentionally use `{}` as their example arguments.

Install all bundled skills from a GitHub checkout with:

```bash
npx github:<owner>/<repo>
```

For a fork or a private checkout, replace `<owner>/<repo>` with the GitHub repository path. The installer copies skills to `$CODEX_HOME/skills` when `CODEX_HOME` is set, otherwise to `~/.codex/skills`.

Useful installer options:

```bash
npx github:<owner>/<repo> -- --list
npx github:<owner>/<repo> -- --dry-run
npx github:<owner>/<repo> -- --force
npx github:<owner>/<repo> -- --target ./my-skills
```

Regenerate and validate the skill bundle after MCP schema changes:

```bash
npm run skills:generate
npm run skills:check
```

---

## Architecture

```text
coding-tools/
├── .eleventy.js                 # Eleventy configuration
├── Dockerfile                   # Static nginx container for dist/
├── package.json                 # npm scripts and dependencies
├── scripts/
│   └── check-structure.js       # Structure and i18n validation
├── src/
│   ├── index.njk                # English homepage
│   ├── localized-index.njk      # Localized homepage generator
│   ├── sitemap.xml.njk          # Sitemap for all languages and tools
│   ├── robots.txt.njk
│   ├── _includes/               # Layouts, partials, and macros
│   ├── _data/
│   │   ├── site.js              # Site metadata and language list
│   │   ├── tools.json           # Tool metadata
│   │   ├── categoryDefinitions.json
│   │   ├── categories.js
│   │   ├── homepage.json        # Homepage translations
│   │   ├── t/                   # Per-language UI translations
│   │   ├── t.js                 # Loads t/*.json
│   │   ├── toolData/            # Per-tool translated content
│   │   └── toolData.js          # Loads toolData/*.json
│   ├── css/
│   │   ├── style.css
│   │   └── tool.css
│   ├── js/                      # Shared client-side utilities and bundled libraries
│   ├── assets/                  # Favicons, images, and Photo2Pixel ONNX model
│   └── tools/
│       ├── *.njk                # English tool pages
│       ├── cn/ tw/ jp/ kr/      # CJK localized tool pages
│       └── fr/ de/ es/ pt/      # European localized tool pages
└── dist/                        # Generated output, gitignored
```

**Tech stack:** Eleventy v3, Nunjucks, custom CSS, vanilla JavaScript.

---

## Internationalization

Supported languages:

| Language | Code | HTML lang |
|----------|------|-----------|
| English | `en` | `en` |
| Chinese Simplified | `cn` | `zh-CN` |
| Chinese Traditional | `tw` | `zh-TW` |
| Japanese | `jp` | `ja` |
| Korean | `kr` | `ko` |
| French | `fr` | `fr` |
| German | `de` | `de` |
| Spanish | `es` | `es` |
| Portuguese | `pt` | `pt` |

Localized tool pages set `lang` and `toolId` in frontmatter, then render translated content through `{{ t.ui.* }}` and `{{ toolData.* }}`. Metadata such as title, description, tool title, and category name is computed from `toolData` by `src/_data/makeToolLangData.js`.

Do not add localized frontmatter fields like `title`, `description`, `toolTitle`, `toolDescription`, or `categoryName`; they override translated data and are rejected by `npm run check`.

---

## Validation

`npm run check` verifies:

- every language listed in `site.js` exists in homepage and UI translation data
- every tool in `tools.json` has one `src/_data/toolData/<slug>.json`
- every toolData file has all 9 languages with matching keys and array lengths
- localized non-empty English baseline fields are not empty
- category counts match actual tools
- every English and localized tool template exists
- localized templates have correct `lang`, `toolId`, and permalink data
- localized templates do not use metadata frontmatter overrides or known hard-coded English UI strings

`npm run build` runs this validation first through `prebuild`.

---

## Adding or Updating a Tool

1. Add or update metadata in `src/_data/tools.json`.
2. Add or update translated content in `src/_data/toolData/<slug>.json`.
3. Add any shared UI strings to `src/_data/t/<lang>.json` for every language.
4. Create or update the English template in `src/tools/<slug>.njk`.
5. Create or update localized templates in each language directory.
6. Run `npm run check` and `npm run build`.

---

## License

MIT License.

---

<div align="center">

[Visit coding.tools](https://coding.tools)

</div>
