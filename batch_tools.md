# Batch Tool Plan

This document records tools that are strong candidates for batch processing.

## S-Level Batch Tools

These tools have clear repeatable input/output behavior and high user value when
processing multiple values or files at once.

### Base64

- `base64-encode`
- `base64-decode`

### Hash Generators

- `md5-generator`
- `sha1-generator`
- `sha256-generator`
- `sha384-generator`
- `sha512-generator`

### URL Encoding

- `url-encode`
- `url-decode`

### Formatter and Minifier

- `json-formatter`
- `json-minifier`
- `xml-formatter`
- `xml-minifier`
- `json-to-xml`
- `xml-to-json`
- `html-beautifier`
- `html-minifier`
- `javascript-beautifier`
- `javascript-minifier`
- `css-beautifier`
- `css-minifier`
- `sql-formatter`
- `sql-minifier`

### Number and Encoding Conversion

- `hex-to-decimal`
- `decimal-to-hex`
- `octal-to-decimal`
- `decimal-to-octal`
- `binary-to-decimal`
- `decimal-to-binary`
- `binary-to-hex`
- `hex-to-binary`
- `hex-to-ascii`
- `ascii-to-hex`
- `binary-to-text`
- `text-to-binary`
- `roman-numerals-to-numbers`
- `numbers-to-roman-numerals`

### Fraction, Decimal, and Percent Conversion

- `fraction-to-decimal`
- `decimal-to-fraction`
- `percent-to-decimal`
- `decimal-to-percent`
- `percent-to-fraction`
- `fraction-to-percent`

### Text Transformation

- `regex-replace`
- `case-converter`
- `reverse-text`
- `number-to-words`

### Image Utilities

- `image-resize`
- `compress-png`
- `compress-jpeg`
- `progressive-jpeg`
- `image-to-base64`
- `exif-remover`

## First Implementation Batch

The first batch should be implemented as a `Single` / `Batch` tab on each page.

- Base64: `base64-encode`, `base64-decode`
- Hash: `md5-generator`, `sha1-generator`, `sha256-generator`, `sha384-generator`, `sha512-generator`
- Formatter/minifier: `json-formatter`, `json-minifier`, `xml-formatter`, `xml-minifier`, `html-beautifier`, `html-minifier`, `javascript-beautifier`, `javascript-minifier`, `css-beautifier`, `css-minifier`, `sql-formatter`, `sql-minifier`
- Image tools: `image-resize`, `image-to-base64`

## Second Implementation Batch

The second batch uses the same `Single` / `Batch` tab model and keeps output
mapped by `Source`, so line input and file input results are easy to trace.

- URL: `url-encode`, `url-decode`
- Text transformation: `case-converter`, `reverse-text`, `regex-replace`, `number-to-words`
- Number/base conversion: `hex-to-decimal`, `decimal-to-hex`, `octal-to-decimal`, `decimal-to-octal`, `binary-to-decimal`, `decimal-to-binary`, `binary-to-hex`, `hex-to-binary`
- Text/byte encoding conversion: `hex-to-ascii`, `ascii-to-hex`, `binary-to-text`, `text-to-binary`
- Roman numerals: `roman-numerals-to-numbers`, `numbers-to-roman-numerals`
- Fraction/percent conversion: `fraction-to-decimal`, `decimal-to-fraction`, `percent-to-decimal`, `decimal-to-percent`, `percent-to-fraction`, `fraction-to-percent`

Deferred image UI unification:

- `compress-png`, `compress-jpeg`, `progressive-jpeg`, and `exif-remover`
  already behave like batch-first pages. They should be redesigned in a separate
  pass instead of being wrapped in another `Single` / `Batch` shell.

## Batch UX Rules

- Keep the existing page as the default `Single` tab.
- Add `Batch` as an optional tab, not a replacement for the current workflow.
- Text tools should support line-based batch input and optional multiple-file input when useful.
- Formatter/minifier tools should prefer file-based batch input for structured code, because line-based JSON/XML/HTML splitting is usually unsafe.
- Batch output should show per-item success or error status.
- Single result downloads should download the file directly; multiple file results should use a ZIP when binary files are produced.
- Every skipped or failed item should be visible with a reason.
- New UI labels should use shared data/i18n patterns when localized copy is added later.
