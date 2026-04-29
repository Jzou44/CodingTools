# Unified Input Components Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace 12+ tool-specific CSS class names with shared classes across ~21 converter tools, eliminating ~300-400 lines of duplicated inline CSS.

**Architecture:** Add shared CSS classes to `src/css/tool.css` for card containers, input fields, output cards, and common UI elements (labels, hints, values). Each tool's inline `<style>` block is trimmed to only tool-specific overrides. CSS custom properties (`--tool-accent`, `--tool-font`, etc.) handle per-tool customization.

**Tech Stack:** Eleventy (Nunjucks templates), CSS custom properties, vanilla CSS

---

## File Structure

| File | Change |
|------|--------|
| `src/css/tool.css` | Add shared classes: `.tool-input-card`, `.tool-input-field`, `.tool-output-card`, `.tool-label`, `.tool-hint`, `.tool-output-value` |
| `src/tools/decimal-to-hex.njk` | Migrate `nc-` prefix classes to shared classes |
| `src/tools/binary-to-decimal.njk` | Migrate `nc-` prefix classes to shared classes |
| `src/tools/decimal-to-binary.njk` | Migrate `nc-` prefix classes to shared classes |
| `src/tools/decimal-to-octal.njk` | Migrate `nc-` prefix classes to shared classes |
| `src/tools/hex-to-decimal.njk` | Migrate `nc-` prefix classes to shared classes |
| `src/tools/octal-to-decimal.njk` | Migrate `nc-` prefix classes to shared classes |
| `src/tools/roman-numerals-to-numbers.njk` | Migrate `roman-` prefix classes to shared classes |
| `src/tools/numbers-to-roman-numerals.njk` | Migrate `roman-` prefix classes to shared classes |
| `src/tools/hex-to-rgb.njk` | Migrate `hex-rgb-` prefix classes to shared classes |
| `src/tools/hex-to-rgba.njk` | Migrate `hex-rgba-` prefix classes to shared classes |
| `src/tools/rgb-to-hex.njk` | Migrate `rgb-hex-` prefix card/label/hint to shared classes |
| `src/tools/rgba-to-hex.njk` | Migrate `rgba-hex-` prefix card/label/hint to shared classes |
| `src/tools/decimal-to-fraction.njk` | Migrate `dec-` prefix classes to shared classes |
| `src/tools/decimal-to-percent.njk` | Migrate `dec-pct-` prefix classes to shared classes |
| `src/tools/percent-to-decimal.njk` | Migrate `pct-dec-` prefix classes to shared classes |
| `src/tools/percent-to-fraction.njk` | Migrate `pct-frac-` prefix classes to shared classes |
| `src/tools/fraction-to-decimal.njk` | Migrate `frac-` prefix card/label/hint to shared classes |
| `src/tools/fraction-to-percent.njk` | Migrate `frac-pct-` prefix classes to shared classes |
| `src/tools/binary-to-hex.njk` | Already uses shared classes — no changes |
| `src/tools/hex-to-binary.njk` | Check if needs migration |
| `src/tools/number-to-words.njk` | Already uses shared classes — no changes |

---

## Task 1: Add Shared CSS Classes to `src/css/tool.css`

**Files:**
- Modify: `src/css/tool.css:600` (append after existing content)

- [ ] **Step 1: Read the current end of `src/css/tool.css` to find the insertion point**

Read `src/css/tool.css` lines 590-603. The new classes go after the last existing rule.

- [ ] **Step 2: Append shared input card and field classes**

Append to `src/css/tool.css`:

```css
/* ============================================================
   Shared Converter Components
   Replaces tool-specific prefixes (nc-, roman-, dec-, etc.)
   with unified classes. Customize via CSS custom properties.
   ============================================================ */

/* --- Input Card --- */
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

/* --- Input Field --- */
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

/* --- Label --- */
.tool-label {
  font-family: 'DM Sans', sans-serif;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--text-muted);
  margin-bottom: 12px;
}

/* --- Hint --- */
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

/* --- Output Card --- */
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

/* --- Output Label --- */
.tool-output-label {
  font-family: 'DM Sans', sans-serif;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--text-muted);
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

/* --- Output Value --- */
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

/* --- Responsive --- */
@media (max-width: 600px) {
  .tool-input-field {
    font-size: var(--tool-font-size-mobile, 24px);
  }
  .tool-output-value {
    font-size: var(--tool-output-font-size-mobile, 32px);
  }
  .tool-input-card,
  .tool-output-card {
    padding: 20px;
  }
}
```

- [ ] **Step 3: Run the dev server to verify CSS loads without errors**

Run: `npm run dev`
Expected: Server starts on localhost:5500 without CSS errors

- [ ] **Step 4: Verify decimal-to-hex still looks correct (no migration yet)**

Open `http://localhost:5500/tools/decimal-to-hex/` in browser. The tool should look identical to before — the new shared classes are not yet used by any tool.

- [ ] **Step 5: Commit**

```bash
git add src/css/tool.css
git commit -m "feat: add shared converter component CSS classes"
```

---

## Task 2: Migrate `decimal-to-hex.njk` (Reference Tool)

**Files:**
- Modify: `src/tools/decimal-to-hex.njk`

This is the reference tool with `nc-` prefix. Migration sets the pattern for all other tools.

- [ ] **Step 1: Read the full file to understand current structure**

Read `src/tools/decimal-to-hex.njk`. Note the `<style>` block and HTML structure.

- [ ] **Step 2: Update HTML classes**

In the HTML, replace:
- `class="nc-input-card"` → `class="tool-input-card" style="--tool-accent: var(--secondary)"`
- `class="nc-input-label"` → `class="tool-label"`
- `class="nc-input-field"` → `class="tool-input-field"`
- `class="nc-input-hint"` → `class="tool-hint"`
- `class="nc-output-card"` → `class="tool-output-card"`
- `class="nc-output-label"` → `class="tool-output-label"`
- `class="nc-output-value"` → `class="tool-output-value"`
- `class="nc-output-value empty"` → `class="tool-output-value empty"`
- `class="nc-output-value error"` → `class="tool-output-value error"`

- [ ] **Step 3: Remove migrated CSS from inline `<style>` block**

Remove these rules from the `<style>` block (they are now in `tool.css`):
- `.nc-input-card` (full rule)
- `.nc-input-card::before` (full rule)
- `.nc-input-label` (full rule)
- `.nc-input-field` (full rule)
- `.nc-input-field::placeholder` (full rule)
- `.nc-input-hint` (full rule)
- `.nc-input-hint code` (full rule)
- `.nc-output-card` (full rule)
- `.nc-output-card.has-result` (full rule)
- `.nc-output-label` (full rule)
- `.nc-output-value` (full rule)
- `.nc-output-value.empty` (full rule)
- `.nc-output-value.error` (full rule)
- Mobile `@media` rules for `.nc-input-field`, `.nc-output-value`, `.nc-input-card`, `.nc-output-card`

**Keep these tool-specific rules:**
- `.nc-converter` (layout)
- `.nc-arrow`, `.nc-arrow::before`, `.nc-arrow-icon`, `.nc-arrow-icon:hover`
- `.nc-secondary-grid`, `.nc-secondary-card`, `.nc-secondary-card.has-result`, `.nc-secondary-label`, `.nc-secondary-value`, `.nc-secondary-value.empty`
- `.nc-toolbar`, `.nc-toolbar-left`, `.nc-toolbar-right`
- `.nc-ref`, `.nc-ref-title`, `.nc-ref-grid`, `.nc-ref-item`, `.nc-ref-item .dec`, `.nc-ref-item .arrow`, `.nc-ref-item .hex`
- Mobile rules for `.nc-secondary-grid`

- [ ] **Step 4: Verify in browser**

Open `http://localhost:5500/tools/decimal-to-hex/`. Compare visually with the pre-migration state. The tool should look identical:
- Input card has green accent bar (`--secondary`)
- Input field is 32px monospace
- Output card has green border when result is shown
- All tool-specific elements (arrow, secondary grid, ref table) unchanged

- [ ] **Step 5: Commit**

```bash
git add src/tools/decimal-to-hex.njk
git commit -m "refactor(decimal-to-hex): migrate to shared CSS classes"
```

---

## Task 3: Migrate Number Base Converters (5 tools)

**Files:**
- Modify: `src/tools/binary-to-decimal.njk`
- Modify: `src/tools/decimal-to-binary.njk`
- Modify: `src/tools/decimal-to-octal.njk`
- Modify: `src/tools/hex-to-decimal.njk`
- Modify: `src/tools/octal-to-decimal.njk`

These 5 tools use the same `nc-` prefix pattern as decimal-to-hex. They differ only in accent color (`--accent` instead of `--secondary`) and ref-item class names.

- [ ] **Step 1: Migrate `binary-to-decimal.njk`**

Same HTML class replacements as Task 2, but with:
- `style="--tool-accent: var(--accent)"` on the input card (uses accent, not secondary)
- Output card also gets `style="--tool-accent: var(--accent)"`

Remove the same CSS rules from the inline `<style>` block. Keep tool-specific rules (arrow, secondary grid, toolbar, ref).

The `.nc-input-field` in this tool has `caret-color: var(--accent)` — this is handled by `--tool-accent` CSS variable on the card, which cascades to the input field's `caret-color: var(--tool-accent, var(--secondary))`.

- [ ] **Step 2: Verify `binary-to-decimal.njk` in browser**

Open `http://localhost:5500/tools/binary-to-decimal/`. Verify:
- Orange accent bar (uses `--accent`)
- Orange caret in input field
- Orange border on output card when result shown

- [ ] **Step 3: Migrate `decimal-to-binary.njk`**

Same pattern as binary-to-decimal. Read the file first to confirm it uses `nc-` prefix with `--accent` color.

- [ ] **Step 4: Migrate `decimal-to-octal.njk`**

Same pattern.

- [ ] **Step 5: Migrate `hex-to-decimal.njk`**

Same pattern.

- [ ] **Step 6: Migrate `octal-to-decimal.njk`**

Same pattern.

- [ ] **Step 7: Verify all 5 tools in browser**

Open each tool and verify visual consistency:
- `http://localhost:5500/tools/decimal-to-binary/`
- `http://localhost:5500/tools/decimal-to-octal/`
- `http://localhost:5500/tools/hex-to-decimal/`
- `http://localhost:5500/tools/octal-to-decimal/`

- [ ] **Step 8: Commit**

```bash
git add src/tools/binary-to-decimal.njk src/tools/decimal-to-binary.njk src/tools/decimal-to-octal.njk src/tools/hex-to-decimal.njk src/tools/octal-to-decimal.njk
git commit -m "refactor: migrate 5 number base converters to shared CSS classes"
```

---

## Task 4: Migrate Roman Numeral Tools (2 tools)

**Files:**
- Modify: `src/tools/roman-numerals-to-numbers.njk`
- Modify: `src/tools/numbers-to-roman-numerals.njk`

These tools use `roman-` prefix. Key differences from the default:
- Accent bar: `linear-gradient(90deg, var(--secondary), var(--accent))`
- Input font: `'Fraunces', serif` (not IBM Plex Mono)
- Input font-size: `36px` (not 32px)
- Input font-weight: `700` (not 500)
- Input letter-spacing: `0.08em` (not 0.02em)
- Input text-transform: `uppercase`
- Placeholder: `font-size: 18px`, `font-style: italic`, `letter-spacing: 0`
- Output font-size: `48px`
- Mobile input font-size: `28px`, output: `36px`

- [ ] **Step 1: Add CSS variable overrides for gradient accent bar**

Since `--tool-accent` only supports solid colors (via `background: var(--tool-accent)`), gradient accent bars need a `::before` override. Add to the tool's inline `<style>`:

```css
.tool-input-card::before {
  background: linear-gradient(90deg, var(--secondary), var(--accent));
}
```

- [ ] **Step 2: Update HTML classes in `roman-numerals-to-numbers.njk`**

Replace:
- `class="roman-input-card"` → `class="tool-input-card"` (with `::before` override in `<style>`)
- `class="roman-input-label"` → `class="tool-label"`
- `class="roman-input-field"` → `class="tool-input-field" style="--tool-font: 'Fraunces', serif; --tool-font-size: 36px; --tool-font-size-mobile: 28px; --tool-accent: var(--accent)"`
- Additional inline styles on the input: `font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase;`
- `class="roman-input-hint"` → `class="tool-hint"`
- `class="roman-output-card"` → `class="tool-output-card" style="--tool-accent: var(--secondary)"`
- `class="roman-output-label"` → `class="tool-output-label"`
- `class="roman-output-value"` → `class="tool-output-value" style="--tool-output-font-size: 48px; --tool-output-font-size-mobile: 36px"`
- `class="roman-output-value empty"` → `class="tool-output-value empty"`
- `class="roman-output-value error"` → `class="tool-output-value error"`

- [ ] **Step 3: Remove migrated CSS from inline `<style>` block**

Remove: `.roman-input-card`, `::before`, `.roman-input-label`, `.roman-input-field`, `::placeholder`, `.roman-input-hint`, `.roman-input-hint code`, `.roman-output-card`, `.has-result`, `.roman-output-label`, `.roman-output-value`, `.empty`, `.error`, mobile rules for these.

Keep: `.roman-converter`, arrow, toolbar, ref, and ref-item rules.

- [ ] **Step 4: Migrate `numbers-to-roman-numerals.njk`**

Same pattern — this is the reverse direction tool.

- [ ] **Step 5: Verify both tools in browser**

- `http://localhost:5500/tools/roman-numerals-to-numbers/`
- `http://localhost:5500/tools/numbers-to-roman-numerals/`

Verify: Fraunces serif font, uppercase, gradient accent bar, 48px output.

- [ ] **Step 6: Commit**

```bash
git add src/tools/roman-numerals-to-numbers.njk src/tools/numbers-to-roman-numerals.njk
git commit -m "refactor: migrate roman numeral tools to shared CSS classes"
```

---

## Task 5: Migrate Hex Color Tools (2 tools)

**Files:**
- Modify: `src/tools/hex-to-rgb.njk`
- Modify: `src/tools/hex-to-rgba.njk`

These tools have unique gradient accent bars and tool-specific features (color swatch, RGB channels).

- [ ] **Step 1: Migrate `hex-to-rgb.njk`**

HTML class replacements:
- `class="hex-rgb-input-card"` → `class="tool-input-card"`
- `class="hex-rgb-label"` → `class="tool-label"`
- `class="hex-rgb-input-field"` → `class="tool-input-field" style="--tool-accent: var(--accent)"`
- `class="hex-rgb-input-hint"` → `class="tool-hint"`
- `class="hex-rgb-output-card"` → `class="tool-output-card" style="--tool-accent: var(--accent)"`
- `class="hex-rgb-output-label"` → `class="tool-output-label"`
- `class="hex-rgb-output-value"` → `class="tool-output-value" style="--tool-output-font-size: 28px; --tool-output-font-size-mobile: 22px"`
- `class="hex-rgb-output-value empty"` → `class="tool-output-value empty"`
- `class="hex-rgb-output-value error"` → `class="tool-output-value error"`

Add to inline `<style>` for gradient accent bar:
```css
.tool-input-card::before {
  background: linear-gradient(90deg, #e74c3c, #f39c12, #2ecc71, #3498db, #9b59b6);
}
```

Remove migrated CSS. Keep: `.hex-rgb-converter`, `.hex-rgb-actions`, arrow, toolbar, all swatch rules, all channel rules.

- [ ] **Step 2: Migrate `hex-to-rgba.njk`**

Same pattern as hex-to-rgb. Read the file to confirm structure.

- [ ] **Step 3: Verify both tools in browser**

- `http://localhost:5500/tools/hex-to-rgb/`
- `http://localhost:5500/tools/hex-to-rgba/`

Verify: Rainbow gradient accent bar, color swatch, RGB channel display.

- [ ] **Step 4: Commit**

```bash
git add src/tools/hex-to-rgb.njk src/tools/hex-to-rgba.njk
git commit -m "refactor: migrate hex color tools to shared CSS classes"
```

---

## Task 6: Migrate RGB/RGBA Input Tools (2 tools)

**Files:**
- Modify: `src/tools/rgb-to-hex.njk`
- Modify: `src/tools/rgba-to-hex.njk`

These are multi-input tools. The card, label, and hint can use shared classes. The multi-input field layout and per-channel focus colors stay tool-specific.

- [ ] **Step 1: Migrate `rgb-to-hex.njk`**

HTML class replacements:
- `class="rgb-hex-input-card"` → `class="tool-input-card"`
- `class="rgb-hex-label"` → `class="tool-label"`
- `class="rgb-hex-input-hint"` → `class="tool-hint"`
- `class="rgb-hex-output-card"` → `class="tool-output-card" style="--tool-accent: var(--accent)"`
- `class="rgb-hex-output-label"` → `class="tool-output-label"`
- `class="rgb-hex-output-value"` → `class="tool-output-value" style="--tool-output-font-size: 32px; --tool-accent: var(--accent)"`
- `class="rgb-hex-output-value empty"` → `class="tool-output-value empty"`
- `class="rgb-hex-output-value error"` → `class="tool-output-value error"`

Add to inline `<style>` for gradient accent bar:
```css
.tool-input-card::before {
  background: linear-gradient(90deg, #e74c3c, #2ecc71, #3498db);
}
```

**Keep tool-specific:** `.rgb-hex-converter`, `.rgb-hex-input-fields`, `.rgb-hex-field-group`, `.rgb-hex-field-label`, `.rgb-hex-field-input` (completely different styling — has border, background, border-radius, text-align: center), `.r-field/.g-field/.b-field` focus colors, `.rgb-hex-actions`, arrow, toolbar, swatch rules.

- [ ] **Step 2: Migrate `rgba-to-hex.njk`**

Same pattern. Has an additional alpha channel field.

- [ ] **Step 3: Verify both tools in browser**

- `http://localhost:5500/tools/rgb-to-hex/`
- `http://localhost:5500/tools/rgba-to-hex/`

Verify: RGB gradient accent bar, 3-field input layout, per-channel focus colors.

- [ ] **Step 4: Commit**

```bash
git add src/tools/rgb-to-hex.njk src/tools/rgba-to-hex.njk
git commit -m "refactor: migrate RGB/RGBA input tools to shared CSS classes"
```

---

## Task 7: Migrate Decimal/Percent/Fraction Converters (5 tools)

**Files:**
- Modify: `src/tools/decimal-to-fraction.njk`
- Modify: `src/tools/decimal-to-percent.njk`
- Modify: `src/tools/percent-to-decimal.njk`
- Modify: `src/tools/percent-to-fraction.njk`
- Modify: `src/tools/fraction-to-percent.njk`

These tools use various prefixes (`dec-`, `dec-pct-`, `pct-dec-`, `pct-frac-`, `frac-pct-`) but follow the same card/field/output pattern.

- [ ] **Step 1: Migrate `decimal-to-fraction.njk`**

HTML class replacements:
- `class="dec-input-card"` → `class="tool-input-card" style="--tool-accent: var(--secondary)"`
- `class="dec-input-label"` → `class="tool-label"`
- `class="dec-input-field"` → `class="tool-input-field" style="--tool-accent: var(--secondary)"`
- `class="dec-input-hint"` → `class="tool-hint"`
- `class="dec-output-card"` → `class="tool-output-card" style="--tool-accent: var(--secondary)"`
- `class="dec-output-label"` → `class="tool-output-label"`

Add gradient accent bar override in `<style>`:
```css
.tool-input-card::before {
  background: linear-gradient(90deg, var(--secondary), #3d8b6a);
}
```

**Keep tool-specific:** `.dec-converter`, arrow, toolbar, ref, and the entire fraction result visual system (`.dec-result-visual`, `.dec-res-integer`, `.dec-res-dot`, `.dec-res-stack`, `.dec-res-num-row`, `.dec-res-den-row`).

Note: This tool has a custom output display (fraction visual), not a standard `.tool-output-value`. The output card gets the shared class, but the inner content stays tool-specific.

- [ ] **Step 2: Migrate `decimal-to-percent.njk`**

Read the file to confirm structure. Likely uses `dec-pct-` prefix. Same migration pattern.

- [ ] **Step 3: Migrate `percent-to-decimal.njk`**

HTML class replacements:
- `class="pct-dec-input-card"` → `class="tool-input-card"`
- `class="pct-dec-label"` → `class="tool-label"`
- `class="pct-dec-input-field"` → `class="tool-input-field" style="--tool-accent: var(--accent)"`
- `class="pct-dec-input-hint"` → `class="tool-hint"`
- `class="pct-dec-output-card"` → `class="tool-output-card" style="--tool-accent: var(--accent)"`
- `class="pct-dec-output-label"` → `class="tool-output-label"`
- `class="pct-dec-output-value"` → `class="tool-output-value" style="--tool-output-font-size: 36px; --tool-accent: var(--accent)"`

Add gradient accent bar override:
```css
.tool-input-card::before {
  background: linear-gradient(90deg, var(--accent), #d4725a);
}
```

**Keep tool-specific:** `.pct-dec-converter`, `.pct-dec-input-wrap`, `.pct-dec-suffix`, arrow, toolbar, ref.

- [ ] **Step 4: Migrate `percent-to-fraction.njk`**

Read the file to confirm structure. Same pattern.

- [ ] **Step 5: Migrate `fraction-to-percent.njk`**

Read the file to confirm structure. Same pattern.

- [ ] **Step 6: Verify all 5 tools in browser**

- `http://localhost:5500/tools/decimal-to-fraction/`
- `http://localhost:5500/tools/decimal-to-percent/`
- `http://localhost:5500/tools/percent-to-decimal/`
- `http://localhost:5500/tools/percent-to-fraction/`
- `http://localhost:5500/tools/fraction-to-percent/`

- [ ] **Step 7: Commit**

```bash
git add src/tools/decimal-to-fraction.njk src/tools/decimal-to-percent.njk src/tools/percent-to-decimal.njk src/tools/percent-to-fraction.njk src/tools/fraction-to-percent.njk
git commit -m "refactor: migrate decimal/percent/fraction converters to shared CSS classes"
```

---

## Task 8: Migrate Fraction Input Tool

**Files:**
- Modify: `src/tools/fraction-to-decimal.njk`

This tool has a unique fraction visual input (integer + numerator/denominator stack). The card and label use shared classes, but the input fields are completely custom.

- [ ] **Step 1: Migrate `fraction-to-decimal.njk`**

HTML class replacements:
- `class="frac-input-card"` → `class="tool-input-card"`
- `class="frac-input-label"` → `class="tool-label"`
- `class="frac-input-hint"` → `class="tool-hint"`
- `class="frac-output-card"` → `class="tool-output-card" style="--tool-accent: var(--accent)"`
- `class="frac-output-label"` → `class="tool-output-label"`
- `class="frac-output-value"` → `class="tool-output-value" style="--tool-output-font-size: 42px; --tool-accent: var(--accent)"`
- `class="frac-output-value empty"` → `class="tool-output-value empty"`
- `class="frac-output-value error"` → `class="tool-output-value error"`

Add gradient accent bar override:
```css
.tool-input-card::before {
  background: linear-gradient(90deg, var(--accent), #d4725a);
}
```

Remove migrated CSS. **Keep tool-specific:** `.frac-converter`, entire fraction visual system (`.frac-visual`, `.frac-integer-field`, `.frac-separator-dot`, `.frac-stack`, `.frac-num-row`, `.frac-den-row`, focus-within), arrow, toolbar, ref.

- [ ] **Step 2: Verify in browser**

Open `http://localhost:5500/tools/fraction-to-decimal/`. Verify:
- Card has gradient accent bar
- Fraction visual input (integer + numerator/denominator) works correctly
- Output card shows result

- [ ] **Step 3: Commit**

```bash
git add src/tools/fraction-to-decimal.njk
git commit -m "refactor(fraction-to-decimal): migrate to shared CSS classes"
```

---

## Task 9: Migrate Remaining Tools

**Files:**
- Modify: `src/tools/binary-to-hex.njk` (check if needs migration)
- Modify: `src/tools/hex-to-binary.njk` (check if needs migration)
- Any other tools not yet migrated

- [ ] **Step 1: Check `binary-to-hex.njk`**

This tool reportedly has NO inline `<style>` block and uses shared classes (`text-input`, `output-field`). Verify this is still correct — no migration needed.

- [ ] **Step 2: Check `hex-to-binary.njk`**

Read the file. If it has inline styles with tool-specific prefixes, migrate it.

- [ ] **Step 3: Scan for any remaining tools with tool-specific input card/field classes**

Run: `grep -l "input-card\|input-field" src/tools/*.njk` to find any tools not yet migrated.

- [ ] **Step 4: Commit any remaining migrations**

```bash
git add -A
git commit -m "refactor: migrate remaining converter tools to shared CSS classes"
```

---

## Task 10: Final Verification

- [ ] **Step 1: Build the site**

Run: `npm run build`
Expected: Build succeeds without errors.

- [ ] **Step 2: Spot-check 5 random tools in the built output**

Open files from `dist/tools/` and verify the HTML references the shared `tool-input-card`, `tool-input-field` classes.

- [ ] **Step 3: Verify no visual regressions**

Open these tools in the browser and compare with pre-migration screenshots (if available):
- `http://localhost:5500/tools/decimal-to-hex/` (reference)
- `http://localhost:5500/tools/roman-numerals-to-numbers/` (custom font)
- `http://localhost:5500/tools/hex-to-rgb/` (gradient + swatch)
- `http://localhost:5500/tools/rgb-to-hex/` (multi-input)
- `http://localhost:5500/tools/fraction-to-decimal/` (fraction visual)

- [ ] **Step 4: Count removed CSS lines**

Run: `git diff --stat` to see total lines changed across all files.

- [ ] **Step 5: Final commit (if any cleanup needed)**

```bash
git add -A
git commit -m "chore: final cleanup for unified input components"
```
