# Semantic-Safe Minifiers and Lossless JSON/XML Structure

## Context

The browser tools, batch tools, and MCP runtime currently implement text minification and JSON/XML conversion independently. Several paths use regular expressions over the entire input, so comment markers or repeated whitespace inside literals are treated as syntax. The JSON/XML paths also disagree about wrapping and drop information such as XML attributes and element-name case.

This change fixes high-priority review items 3 and 4 without adding a browser bundling pipeline or server runtime dependency.

## Goals

- Preserve JavaScript, CSS, SQL, HTML, and XML semantics while minifying.
- Produce exactly one well-formed XML document for every supported JSON input.
- Preserve XML element-name case, attributes, text, and repeated sibling elements when converting to JSON.
- Give the single-page tools, batch processing, and MCP runtime the same behavior.
- Reject unsupported or malformed input explicitly instead of silently truncating or renaming data.
- Add direct regression coverage for every reported corruption or data-loss case.

## Non-goals

- Competing with optimizing compilers such as Terser or Clean-CSS.
- Supporting DTD expansion, custom XML entities, or a fully validating XML parser.
- Guaranteeing an exact JSON type round trip through arbitrary XML. XML scalar values continue to become JSON strings.
- Changing translations or the visual design of any tool page.

## Chosen approach

Add a dependency-free shared transformer module that can be loaded as a browser script and required by Node. Existing compatibility globals remain available, but delegate to the shared implementation. Browser tool templates, batch processing, and `server/mcp-tools.js` call the same public functions.

This approach is preferred over adding multiple parser/minifier dependencies because Coding.Tools currently has no client bundling pipeline. It is preferred over local regex patches because duplicated fixes would keep the three execution paths inconsistent.

## Components and interfaces

### Shared transformer module

`src/js/text-transformers.js` exposes a UMD-style API:

- `minifyJavaScript(source)`
- `minifyCss(source)`
- `minifySql(source)`
- `minifyHtml(source)`
- `minifyXml(source)`
- `jsonToXml(sourceOrValue, options)`
- `xmlToJson(source, options)`

All functions are deterministic and side-effect free. They throw descriptive `SyntaxError` or `TypeError` values for invalid input.

### Compatibility adapter

`src/js/html-minifier-compat.js` keeps the existing `window.htmlminifier` and `window.JXON` entry points needed by current templates. The adapter contains no independent transformation logic; it translates legacy calls to the shared API.

### Consumers

- Individual tool templates call the shared API directly where practical.
- `src/js/batch-tools.js` delegates supported transformations to the shared API.
- `server/mcp-tools.js` requires the same module and applies existing MCP option handling around it.

## Minifier behavior

### JavaScript

A stateful lexical scan distinguishes code, quoted strings, template literals, regular-expression literals, line comments, and block comments. Comment-looking text inside a literal is copied exactly. Removed comments leave a separator when adjacent tokens would otherwise merge. Line terminators that can affect automatic semicolon insertion are preserved. Outside literals, runs of horizontal whitespace may become one space, but punctuation-adjacent whitespace is removed only when token boundaries remain unambiguous.

The implementation is deliberately conservative: smaller output never takes priority over executable equivalence.

### CSS

The scanner protects quoted strings, escapes, and function contents. Comments are removed only in normal CSS syntax. Whitespace is normalized conservatively, preserving descendant combinators and required spaces in constructs such as `calc()`. String values such as `content: "/*keep*/"` remain byte-for-byte intact.

### SQL

The scanner protects single-quoted strings, double-quoted identifiers, backtick identifiers, bracket identifiers, and PostgreSQL dollar-quoted strings. `--` and block comments are recognized only outside protected regions. Remaining whitespace is collapsed to a single separator. Comment removal cannot concatenate neighboring SQL tokens.

### HTML and XML

Markup scanning distinguishes tags, attributes, comments, declarations, processing instructions, CDATA, raw-text elements, and ordinary text nodes. Ordinary text, `<pre>` content, CDATA, and raw `script`/`style` content are never globally whitespace-collapsed. Safe whitespace inside tags is normalized, and removable comments are discarded without joining surrounding text.

HTML and XML use separate entry points. XML handling is stricter and reports malformed nesting. Neither path removes inter-element whitespace text merely because it appears between tags, since that text can be significant.

## JSON to XML mapping

The converter always emits exactly one document element:

- A top-level object with exactly one valid XML-name key uses that key as the document element. This preserves existing examples such as `{ "person": ... }` becoming `<person>...</person>`.
- Every other top-level object uses `<root>` and serializes its keys as children.
- A top-level array uses `<root>` and serializes every entry as `<item>`.
- A top-level scalar uses `<root>` containing the escaped scalar text.
- Nested arrays repeat their property element. Arrays directly contained by an array use `<item>`.
- `null` and empty strings produce empty elements; booleans and numbers use their JSON textual representation.

Object keys used as element names must be valid XML names. Invalid names cause a descriptive error instead of being silently changed. Text and attribute values are escaped once.

The optional MCP `rootName` forces that name to be the single outer document element. For arrays, its entries are children named `item`; the root itself is never repeated.

## XML to JSON mapping

The parser preserves qualified element and attribute names exactly, including case and namespace prefixes. It rejects malformed nesting, unterminated constructs, unsupported doctypes, and unknown entities.

Each document returns an object keyed by the exact root element name. Element values follow these rules:

- A text-only element becomes a string.
- Attributes are stored under `@attributes` as a name-to-string object.
- Text in an element that also has attributes or child elements is stored under `#text`.
- Child elements use their exact names as keys.
- Repeated same-name children become arrays in source order.
- Empty elements become an empty string unless attributes require an object.

Mixed text/element content is preserved in source order under `#content`. Each text entry is a string and each element entry is a single-key object. When `#content` is present, children are not duplicated into grouped keys. `jsonToXml` accepts this representation so mixed content can be converted back without reordering.

Formatting-only whitespace between child elements is ignored for compatibility with current XML-to-JSON output. Non-whitespace text is always retained. This change does not add a whitespace-preservation option.

## Error handling

- Minifiers throw for unterminated strings, comments, template literals, CDATA, or malformed XML structures where continuing would risk corruption.
- JSON parsing errors retain the native parser message with tool-level context.
- XML parsing errors include an approximate input offset and the construct that failed.
- Existing browser and batch error presentation remains responsible for translating thrown errors into user-visible messages.
- MCP tools return their existing structured error response with the new validation message.

No transformation returns a partially converted result after detecting malformed input.

## Testing strategy

Add a Node regression suite that imports the real shared module. Tests are written first and observed failing before production changes.

Required minifier cases include:

- JavaScript strings containing repeated spaces, `//`, `/* */`, and `</script>`.
- JavaScript ASI-sensitive line breaks and regex/template literals.
- CSS `content` values containing comment markers and required `calc()` spacing.
- SQL strings and quoted identifiers containing `--` or block-comment markers, including bracket and dollar quoting.
- HTML `<pre>` content, inline-element separator text, and raw script/style content.
- XML text whitespace, CDATA, attributes, and comments adjacent to text.

Required conversion cases include:

- Multi-key top-level JSON objects produce one `<root>`.
- Top-level arrays retain every entry under one `<root>`.
- MCP `rootName` also retains all array entries.
- XML attributes and element-name case survive XML-to-JSON.
- Repeated siblings become arrays.
- Escaped entities decode once and re-encode once.
- Mixed content retains ordering through `#content`.
- Malformed JSON/XML and invalid XML names fail explicitly.

Parity tests run the same fixtures through the shared browser-facing API, batch dispatcher, and MCP tool handler where those layers are directly importable. Existing `npm run mcp:test`, structure checks, and build remain required gates.

## Acceptance criteria

- None of the reported literal or text-node examples are modified semantically.
- Browser single-tool, browser batch, and MCP outputs match for shared transformations.
- JSON-to-XML never returns multiple root elements or truncates a top-level array.
- XML-to-JSON retains attributes and exact element-name case.
- All new regression tests, `npm run mcp:test`, `npm run check`, and `npm run build` pass.
- Generated pages load the shared script before every consumer and expose no browser console errors during representative tool runs.
