<div align="center">

# Coding.Tools

### The Developer Toolbox

**62+ free, browser-based developer tools that respect your privacy.**

No sign-up. No tracking. No data sent to servers. Everything runs in your browser.

[![Live Site](https://img.shields.io/badge/Live-coding.tools-blue?style=for-the-badge)](https://coding.tools)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#license)
[![Languages](https://img.shields.io/badge/Languages-9-orange?style=for-the-badge)](#-internationalization)

<br/>

**English** | [中文](README_CN.md)

</div>

---

## Why Coding.Tools?

Most online developer tools are cluttered with ads, require sign-ups, or send your data to remote servers. Coding.Tools is different:

- **Privacy First** — All tools run 100% in your browser. Your code, passwords, and data never leave your device.
- **Zero Friction** — No registration, no API keys, no waiting. Just open and use.
- **Beautiful Design** — Clean interface with thoughtful color coding for each tool category.
- **Truly Multilingual** — Full support for 9 languages, not just translated labels.
- **Free Forever** — Open source, no premium tiers, no hidden costs.

---

## Tools at a Glance

| Category | Tools | What You Can Do |
|----------|------:|-----------------|
| Hash & Cryptography | 8 | Base64, MD5, SHA-1/256/384/512, Password Generator |
| Number Conversion | 26 | Hex, Decimal, Binary, Octal, ASCII, Roman, RGB, Fractions |
| String & Text | 8 | Regex Tester, Word Counter, Case Converter, Text Editor |
| Formatter & Minifier | 14 | JSON, XML, HTML, CSS, JavaScript, SQL formatting & minification |
| Image Utilities | 6 | Compress PNG/JPEG, EXIF viewer/remover, Image to Base64 |

**62 tools** across **5 categories**, available in **9 languages**.

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/your-username/coding-tools.git
cd coding-tools

# Install dependencies
npm install

# Start development server
npm run dev
```

Open [http://localhost:5500](http://localhost:5500) in your browser.

### Other Commands

```bash
npm run build          # Build static site to dist/
node server.js         # Production server (serves dist/ on port 5500)
```

---

## Architecture

```
coding.tools
├── .eleventy.js           # Eleventy configuration
├── server.js              # Production static file server
├── src/
│   ├── index.njk          # Homepage template
│   ├── _includes/         # Layouts and partials
│   │   ├── base.njk       # Base HTML structure
│   │   ├── navbar.njk     # Navigation bar
│   │   ├── sidebar.njk    # Tool sidebar
│   │   └── tool-layout.njk # Tool page layout
│   ├── _data/             # Tool data and translations
│   │   ├── tools.json     # Tool definitions
│   │   ├── t.json         # UI translations
│   │   └── toolData.json  # Tool content translations
│   └── tools/             # Tool page templates
│       ├── *.njk          # English tools
│       ├── cn/            # Chinese (Simplified)
│       ├── jp/            # Japanese
│       ├── kr/            # Korean
│       └── ...            # 5 more languages
├── css/                   # Stylesheets
├── js/                    # Client-side JavaScript
└── dist/                  # Generated output
```

**Tech Stack:** Eleventy v3 + Nunjucks + Vanilla JS — no frameworks, no bloat.

---

## Internationalization

Coding.Tools speaks your language:

| | Language | Code | | Language | Code |
|---|----------|------|---|----------|------|
| 🇺🇸 | English | `en` | 🇫🇷 | French | `fr` |
| 🇨🇳 | Chinese (Simplified) | `cn` | 🇩🇪 | German | `de` |
| 🇹🇼 | Chinese (Traditional) | `tw` | 🇪🇸 | Spanish | `es` |
| 🇯🇵 | Japanese | `jp` | 🇧🇷 | Portuguese | `pt` |
| 🇰🇷 | Korean | `kr` | | | |

Each language has fully translated tool descriptions, step-by-step guides, and UI elements — not just labels.

---

## Tool Details

### Hash & Cryptography

Generate hashes, encode data, and create secure passwords — all offline.

`Base64 Encode` `Base64 Decode` `MD5 Generator` `SHA1 Generator` `SHA256 Generator` `SHA384 Generator` `SHA512 Generator` `Password Generator`

### Number Conversion

Convert between number systems with instant, real-time results.

`Hex ↔ Decimal` `Octal ↔ Decimal` `Binary ↔ Decimal` `Binary ↔ Hex` `ASCII Table` `Hex ↔ ASCII` `Binary ↔ Text` `Fraction ↔ Decimal` `Percent ↔ Decimal` `Hex ↔ RGB` `Roman Numerals`

### String & Text Utilities

Powerful text manipulation tools for developers and writers.

`Text Editor` `Regex Tester` `Regex Replace` `Word Counter` `Character Count` `Case Converter` `Reverse Text` `Number to Words`

### Formatter & Minifier

Beautify or compress your code with one click.

`JSON` `XML` `HTML` `CSS` `JavaScript` `SQL` — each with format and minify options, plus `JSON ↔ XML` conversion.

### Image Utilities

Process images directly in your browser. No uploads required.

`Compress PNG` `Compress JPEG` `Progressive JPEG` `Image to Base64` `EXIF Viewer` `EXIF Remover`

---

## Contributing

Contributions are welcome! Whether it's adding a new tool, fixing a bug, or improving translations.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-tool`)
3. Commit your changes (`git commit -m 'Add amazing tool'`)
4. Push to the branch (`git push origin feature/amazing-tool`)
5. Open a Pull Request

### Adding a New Tool

1. Add tool metadata to `src/_data/tools.json`
2. Create the tool template in `src/tools/your-tool.njk`
3. Add translations to `src/_data/t.json` and `src/_data/toolData.json`
4. Create localized versions in language subdirectories

---

## License

MIT License — use it however you want.

---

<div align="center">

**Built with care for developers who value privacy and simplicity.**

[Visit coding.tools](https://coding.tools)

</div>
