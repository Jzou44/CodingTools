# Unified Input Component Design

**Date:** 2026-04-29
**Scope:** ~21 single-line input converter tools

## Problem

The converter tools that use `<input type="text">` each define their own card container and input field CSS in inline `<style>` blocks, with 12+ different class names (`nc-input-field`, `roman-input-card`, `dec-input-field`, `hex-rgb-input-card`, etc.). The CSS properties are nearly identical across all of them, resulting in significant duplication.

**Out of scope:**
- ~30 textarea-based tools already use a consistent `editor-area` pattern
- 4 CodeMirror-based tools (`ascii-to-hex`, `hex-to-ascii`, `binary-to-text`, `text-to-binary`) use `.pane-card` with CodeMirror — different visual pattern, already consistent among themselves

## Design

### Shared CSS Classes (in `src/css/tool.css`)

Six new classes replace all tool-specific variants:

**`.tool-input-card`** — card container:
```css
.tool-input-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 28px;
  box-shadow: var(--shadow-sm);
  position: relative;
  overflow: hidden;
}

.tool-input-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--tool-accent, var(--secondary));
}
```

**`.tool-input-field`** — single-line input:
```css
.tool-input-field {
  width: 100%;
  font-family: var(--tool-font, 'IBM Plex Mono', monospace);
  font-size: var(--tool-font-size, 32px);
  font-weight: 500;
  color: var(--text-primary);
  background: transparent;
  border: none;
  outline: none;
  padding: 8px 0;
  letter-spacing: 0.02em;
  caret-color: var(--tool-accent, var(--secondary));
}

.tool-input-field::placeholder {
  color: var(--text-muted);
  font-size: 20px;
  font-weight: 400;
}
```

**`.tool-label`** — section label (input/output):
```css
.tool-label {
  font-family: 'DM Sans', sans-serif;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--text-muted);
  margin-bottom: 12px;
}
```

**`.tool-hint`** — hint text below input:
```css
.tool-hint {
  font-size: 13px;
  color: var(--text-muted);
  margin-top: 8px;
  font-family: 'DM Sans', sans-serif;
}

.tool-hint code {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 12px;
  background: var(--code-bg);
  padding: 2px 6px;
  border-radius: 4px;
  color: var(--text-secondary);
}
```

**`.tool-output-card`** — output card container:
```css
.tool-output-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 28px;
  box-shadow: var(--shadow-sm);
  position: relative;
  min-height: 120px;
  display: flex;
  flex-direction: column;
  transition: border-color 0.3s;
}

.tool-output-card.has-result {
  border-color: var(--tool-accent, var(--secondary));
}
```

**`.tool-output-value`** — output value display:
```css
.tool-output-value {
  font-family: var(--tool-font, 'IBM Plex Mono', monospace);
  font-size: var(--tool-output-font-size, 42px);
  font-weight: 500;
  color: var(--text-primary);
  letter-spacing: 0.02em;
  line-height: 1.2;
  min-height: 50px;
  word-break: break-all;
  transition: color 0.3s;
}

.tool-output-value.empty {
  color: var(--text-muted);
  font-size: 18px;
  font-weight: 400;
  font-style: italic;
  letter-spacing: 0;
}

.tool-output-value.error {
  color: var(--error);
  font-size: 15px;
  font-weight: 500;
  font-style: normal;
  letter-spacing: 0;
  font-family: 'DM Sans', sans-serif;
}
```

**Responsive** (shared across all above):
```css
@media (max-width: 600px) {
  .tool-input-field { font-size: var(--tool-font-size-mobile, 24px); }
  .tool-output-value { font-size: var(--tool-output-font-size-mobile, 32px); }
  .tool-input-card, .tool-output-card { padding: 20px; }
}
```

### CSS Custom Properties for Per-Tool Customization

Tools customize via CSS variables set on the card element:

| Variable | Default | Purpose |
|----------|---------|---------|
| `--tool-accent` | `var(--secondary)` | Accent bar color, caret color, output border color |
| `--tool-font` | `'IBM Plex Mono', monospace` | Input and output font family |
| `--tool-font-size` | `32px` | Input font size |
| `--tool-font-size-mobile` | `24px` | Input font size on mobile |
| `--tool-output-font-size` | `42px` | Output value font size |
| `--tool-output-font-size-mobile` | `32px` | Output value font size on mobile |

For gradient accent bars (e.g., rgb-to-hex), the tool overrides the `::before` background in its own inline `<style>` block.

### Per-Tool Inline Style Blocks

After migration, each tool's `<style>` block retains only:
1. CSS variable declarations on the card element (via `style` attribute or scoped CSS)
2. Tool-specific layout CSS (field groups, visual elements)
3. Gradient `::before` overrides (if needed)
4. Output field styling (if different from input)

All card-structure and input-base CSS is removed.

## Migration Plan

### Single-Input Tools (~18 tools)

These tools have one `<input type="text">` inside a card:

- Number base: `binary-to-decimal`, `decimal-to-binary`, `decimal-to-octal`, `decimal-to-hex`, `hex-to-decimal`, `octal-to-decimal`
- Roman numerals: `numbers-to-roman-numerals`, `roman-numerals-to-numbers`
- Decimal converters: `decimal-to-fraction`, `decimal-to-percent`
- Percent converters: `percent-to-decimal`, `percent-to-fraction`
- Hex color: `hex-to-rgb`, `hex-to-rgba`
- Text/hex: `binary-to-hex`, `hex-to-binary`
- Number: `number-to-words`
- Other: `fraction-to-percent` (single fraction input variant)

**Migration per tool:**
1. Replace tool-specific card class (e.g., `nc-input-card`) with `tool-input-card`
2. Replace tool-specific input class (e.g., `nc-input-field`) with `tool-input-field`
3. Add CSS variables on the card element for accent color, font, etc.
4. Remove duplicated CSS from inline `<style>` block
5. Keep tool-specific layout and output CSS

### Multi-Input Tools (~5 tools)

These tools have multiple inputs inside one card:

- `rgb-to-hex` — 3 number inputs (R, G, B)
- `rgba-to-hex` — 4 number inputs (R, G, B, A)
- `fraction-to-decimal` — 3 text inputs (integer, numerator, denominator)
- `fraction-to-percent` — 3 text inputs

**Migration per tool:**
1. Replace tool-specific card class with `tool-input-card`
2. For number inputs: keep tool-specific field classes (layout-dependent), or add `tool-input-field` alongside
3. Add CSS variables on the card element

### Tools NOT Migrated

- ~30 textarea-based tools using `editor-area` pattern (already consistent)
- 4 CodeMirror-based tools: `ascii-to-hex`, `hex-to-ascii`, `binary-to-text`, `text-to-binary` (use `.pane-card` with CodeMirror, different pattern)

## File Changes

| File | Change |
|------|--------|
| `src/css/tool.css` | Add `.tool-input-card` and `.tool-input-field` classes |
| `src/tools/*.njk` (~21 files) | Replace tool-specific classes with shared classes, remove duplicated CSS |

## Expected Outcome

- 12+ tool-specific class names replaced by 2 shared classes
- ~300-400 lines of duplicated CSS removed from inline `<style>` blocks across ~21 tools
- All converter tools visually consistent with the decimal-to-hex / roman-numerals reference style
- Per-tool customization via CSS variables (accent color, font)
- No visual regressions — all tools look identical before and after
