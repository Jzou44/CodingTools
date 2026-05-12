const tools = require("../src/_data/tools.json");
const site = require("../src/_data/site");
const dns = require("dns").promises;
const net = require("net");
const { Worker } = require("worker_threads");
const { executeTool, ToolInputError } = require("./a2a-tools");
const { isRuntimeTool } = require("../src/_data/a2aRuntimeTools");
const mcpExamples = require("../src/_data/mcpExamples");

class McpToolError extends Error {
  constructor(message) {
    super(message);
    this.name = "McpToolError";
  }
}

const toolIds = Object.keys(tools);
const MAX_IMAGE_BYTES = 5 * 1024 * 1024;
const MAX_TEXT_CHARS = 200000;
const MAX_REGEX_TEXT_CHARS = 20000;
const MAX_REGEX_PATTERN_CHARS = 500;
const MAX_REGEX_MATCHES = 1000;
const REGEX_TIMEOUT_MS = 300;
const MAX_JSON_TO_XML_DEPTH = 100;
const browserOnlyToolIds = new Set([
  "photo2pixel",
  "compress-png",
  "compress-jpeg",
  "progressive-jpeg",
  "exif-viewer",
  "exif-remover"
]);

const noArgumentToolIds = new Set(["ascii-table", "roman-numerals-chart"]);

const textInputDescriptions = {
  "base64-encode": "Plain text to encode as Base64.",
  "base64-decode": "Base64 text to decode.",
  "md5-generator": "Text to hash with MD5.",
  "sha1-generator": "Text to hash with SHA-1.",
  "sha256-generator": "Text to hash with SHA-256.",
  "sha384-generator": "Text to hash with SHA-384.",
  "sha512-generator": "Text to hash with SHA-512.",
  "hex-to-decimal": "Hexadecimal integer, with or without a 0x prefix.",
  "decimal-to-hex": "Decimal integer.",
  "octal-to-decimal": "Octal integer.",
  "decimal-to-octal": "Decimal integer.",
  "binary-to-decimal": "Binary integer containing only 0 and 1.",
  "decimal-to-binary": "Decimal integer.",
  "binary-to-hex": "Binary integer containing only 0 and 1.",
  "hex-to-binary": "Hexadecimal integer, with or without a 0x prefix.",
  "ascii-to-hex": "Text to convert to hexadecimal byte pairs.",
  "hex-to-ascii": "Hexadecimal byte pairs to convert to text.",
  "binary-to-text": "8-bit binary bytes separated by whitespace.",
  "text-to-binary": "Text to convert to 8-bit binary bytes.",
  "fraction-to-decimal": "Fraction such as 7/8.",
  "decimal-to-fraction": "Decimal number such as 0.125.",
  "percent-to-decimal": "Percentage such as 18.5%.",
  "decimal-to-percent": "Decimal number such as 0.185.",
  "percent-to-fraction": "Percentage such as 12.5%.",
  "fraction-to-percent": "Fraction such as 1/8.",
  "hex-to-rgb": "Hex color such as #3366CC.",
  "hex-to-rgba": "Hex color such as #3366CC or #3366CCAA.",
  "roman-numerals-to-numbers": "Roman numeral in standard form, from I to MMMCMXCIX.",
  "numbers-to-roman-numerals": "Integer from 1 to 3999.",
  "text-editor": "Text to echo back with line and character counts.",
  "regex-tester": "Text to test against options.pattern.",
  "regex-replace": "Text to search and replace using options.pattern.",
  "url-encode": "Text, URL component, path, query value, or full URL to percent-encode.",
  "url-decode": "Percent-encoded URL, path, query value, or query string to decode.",
  "text-compare": "Original text. Pass the changed text in options.compareTo.",
  "word-counter": "Text to count words, characters, lines, sentences, and paragraphs.",
  "character-count": "Text to count characters, UTF-8 bytes, words, and lines.",
  "case-converter": "Text whose case should be converted.",
  "reverse-text": "Text to reverse.",
  "number-to-words": "Integer from 0 to 999,999,999,999.",
  "json-formatter": "JSON string to format.",
  "json-diff": "Original JSON string. Pass the changed JSON string in options.compareTo.",
  "json-minifier": "JSON string to minify.",
  "xml-formatter": "XML string to format.",
  "xml-minifier": "XML string to minify.",
  "json-to-xml": "JSON string or JSON object to convert to XML.",
  "xml-to-json": "XML string with one root element.",
  "html-beautifier": "HTML string to format.",
  "html-minifier": "HTML string to minify.",
  "javascript-beautifier": "JavaScript string to format.",
  "javascript-minifier": "JavaScript string to minify.",
  "css-beautifier": "CSS string to format.",
  "css-minifier": "CSS string to minify.",
  "sql-formatter": "SQL query to format.",
  "sql-minifier": "SQL query to minify."
};

const rgbInputSchema = {
  oneOf: [
    {
      type: "string",
      description: "CSS rgb(...) or rgba(...) color string."
    },
    {
      type: "object",
      description: "RGB color object.",
      properties: {
        r: { type: "integer", minimum: 0, maximum: 255, description: "Red channel." },
        g: { type: "integer", minimum: 0, maximum: 255, description: "Green channel." },
        b: { type: "integer", minimum: 0, maximum: 255, description: "Blue channel." }
      },
      required: ["r", "g", "b"],
      additionalProperties: false
    }
  ]
};

const rgbaInputSchema = {
  oneOf: [
    {
      type: "string",
      description: "CSS rgba(...) color string."
    },
    {
      type: "object",
      description: "RGBA color object.",
      properties: {
        r: { type: "integer", minimum: 0, maximum: 255, description: "Red channel." },
        g: { type: "integer", minimum: 0, maximum: 255, description: "Green channel." },
        b: { type: "integer", minimum: 0, maximum: 255, description: "Blue channel." },
        a: { type: "number", minimum: 0, maximum: 1, description: "Alpha channel." }
      },
      required: ["r", "g", "b"],
      additionalProperties: false
    }
  ]
};

const optionSchemas = {
  "password-generator": {
    type: "object",
    description: "Password generation settings.",
    properties: {
      length: { type: "integer", minimum: 8, maximum: 128, default: 16, description: "Password length." },
      uppercase: { type: "boolean", default: true, description: "Include uppercase letters A-Z." },
      lowercase: { type: "boolean", default: true, description: "Include lowercase letters a-z." },
      numbers: { type: "boolean", default: true, description: "Include digits 0-9." },
      symbols: { type: "boolean", default: true, description: "Include punctuation symbols." }
    },
    additionalProperties: false
  },
  "hex-to-rgba": {
    type: "object",
    properties: {
      alpha: { type: "number", minimum: 0, maximum: 1, description: "Alpha value to use when the hex input does not include one." }
    },
    additionalProperties: false
  },
  "case-converter": {
    type: "object",
    properties: {
      mode: {
        type: "string",
        enum: ["all", "uppercase", "lowercase", "title", "sentence", "inverted"],
        default: "all",
        description: "Case conversion mode."
      }
    },
    additionalProperties: false
  },
  "number-to-words": {
    type: "object",
    properties: {
      mode: {
        type: "string",
        enum: ["cardinal", "ordinal", "ordinal-number"],
        default: "cardinal",
        description: "Output style."
      }
    },
    additionalProperties: false
  },
  "json-formatter": {
    type: "object",
    properties: {
      spaces: { type: "integer", minimum: 0, maximum: 8, default: 2, description: "Indentation spaces." }
    },
    additionalProperties: false
  },
  "json-to-xml": {
    type: "object",
    properties: {
      rootName: { type: "string", default: "root", description: "XML root element name." }
    },
    additionalProperties: false
  },
  "regex-tester": {
    type: "object",
    properties: {
      pattern: { type: "string", description: "Regular expression pattern without slash delimiters." },
      flags: { type: "string", default: "g", description: "JavaScript regex flags, for example g, i, m, s, u, y." }
    },
    required: ["pattern"],
    additionalProperties: false
  },
  "regex-replace": {
    type: "object",
    properties: {
      pattern: { type: "string", description: "Regular expression pattern without slash delimiters." },
      replacement: { type: "string", default: "", description: "Replacement text. JavaScript backreferences such as $1 are supported." },
      flags: { type: "string", default: "g", description: "JavaScript regex flags, for example g, i, m, s, u, y." }
    },
    required: ["pattern"],
    additionalProperties: false
  },
  "url-encode": {
    type: "object",
    properties: {
      mode: {
        type: "string",
        enum: ["component", "uri"],
        default: "component",
        description: "Use component for query values; use uri to preserve full URL separators."
      },
      spaceAsPlus: {
        type: "boolean",
        default: false,
        description: "Convert encoded spaces from %20 to + for form-style query strings."
      },
      lineByLine: {
        type: "boolean",
        default: false,
        description: "Encode each input line independently."
      }
    },
    additionalProperties: false
  },
  "url-decode": {
    type: "object",
    properties: {
      plusAsSpace: {
        type: "boolean",
        default: true,
        description: "Treat + characters as spaces before decoding."
      },
      parseQuery: {
        type: "boolean",
        default: true,
        description: "Append parsed query-string parameters to the result."
      }
    },
    additionalProperties: false
  },
  "json-diff": {
    type: "object",
    properties: {
      compareTo: {
        type: "string",
        description: "Changed JSON string to compare against the input JSON."
      },
      includeUnchanged: {
        type: "boolean",
        default: false,
        description: "Include unchanged paths in the diff output."
      }
    },
    required: ["compareTo"],
    additionalProperties: false
  },
  "text-compare": {
    type: "object",
    properties: {
      compareTo: {
        type: "string",
        description: "Changed text to compare against the input text."
      },
      ignoreWhitespace: {
        type: "boolean",
        default: false,
        description: "Normalize whitespace before matching lines."
      },
      ignoreCase: {
        type: "boolean",
        default: false,
        description: "Match lines case-insensitively."
      },
      showUnchanged: {
        type: "boolean",
        default: false,
        description: "Include unchanged lines in the diff output."
      }
    },
    required: ["compareTo"],
    additionalProperties: false
  },
  "image-to-base64": {
    type: "object",
    properties: {
      mimeType: {
        type: "string",
        description: "MIME type to use when input is raw Base64 bytes, for example image/png."
      }
    },
    additionalProperties: false
  }
};

const resultDescriptions = {
  "base64-encode": "Base64 encoded text.",
  "base64-decode": "Decoded UTF-8 text.",
  "md5-generator": "MD5 hash as lowercase hexadecimal.",
  "sha1-generator": "SHA-1 hash as lowercase hexadecimal.",
  "sha256-generator": "SHA-256 hash as lowercase hexadecimal.",
  "sha384-generator": "SHA-384 hash as lowercase hexadecimal.",
  "sha512-generator": "SHA-512 hash as lowercase hexadecimal.",
  "hex-to-decimal": "Decimal integer string.",
  "decimal-to-hex": "Uppercase hexadecimal integer string.",
  "octal-to-decimal": "Decimal integer string.",
  "decimal-to-octal": "Octal integer string.",
  "binary-to-decimal": "Decimal integer string.",
  "decimal-to-binary": "Binary integer string.",
  "binary-to-hex": "Uppercase hexadecimal integer string.",
  "hex-to-binary": "Binary integer string.",
  "ascii-to-hex": "Hexadecimal byte pairs separated by spaces.",
  "hex-to-ascii": "Decoded UTF-8 text.",
  "binary-to-text": "Decoded UTF-8 text.",
  "text-to-binary": "8-bit binary bytes separated by spaces.",
  "fraction-to-decimal": "Decimal number string.",
  "decimal-to-fraction": "Reduced fraction string.",
  "percent-to-decimal": "Decimal number string.",
  "decimal-to-percent": "Percentage string.",
  "percent-to-fraction": "Reduced fraction string.",
  "fraction-to-percent": "Percentage string.",
  "rgb-to-hex": "Hex color string in #RRGGBB format.",
  "rgba-to-hex": "Hex color string in #RRGGBBAA format.",
  "roman-numerals-to-numbers": "Decimal integer string.",
  "numbers-to-roman-numerals": "Roman numeral string.",
  "reverse-text": "Reversed text.",
  "number-to-words": "Number rendered as English words or ordinals.",
  "json-formatter": "Formatted JSON string.",
  "json-minifier": "Minified JSON string.",
  "xml-formatter": "Formatted XML string.",
  "xml-minifier": "Minified XML string.",
  "json-to-xml": "XML string.",
  "html-beautifier": "Formatted HTML string.",
  "html-minifier": "Minified HTML string.",
  "javascript-beautifier": "Formatted JavaScript string.",
  "javascript-minifier": "Minified JavaScript string.",
  "css-beautifier": "Formatted CSS string.",
  "css-minifier": "Minified CSS string.",
  "sql-formatter": "Formatted SQL string.",
  "sql-minifier": "Minified SQL string.",
  "url-encode": "Percent-encoded URL text.",
  "url-decode": "Decoded URL text and optional query parameter listing.",
  "json-diff": "Path-by-path JSON diff summary.",
  "text-compare": "Line-by-line text diff summary.",
  "image-to-base64": "Image data URI string."
};

function simpleResultOutputSchema(toolId) {
  return {
    type: "object",
    description: "Machine-readable result. The same value is also available as content[0].text for human-readable MCP clients.",
    properties: {
      result: {
        type: "string",
        description: resultDescriptions[toolId] || `Result from ${tools[toolId].title}.`
      }
    },
    required: ["result"],
    additionalProperties: false
  };
}

const outputSchemas = {
  "password-generator": {
    type: "object",
    description: "Generated password result.",
    properties: {
      password: { type: "string", description: "Generated password." },
      generated: { type: "boolean", description: "True when generation succeeded." }
    },
    required: ["password", "generated"],
    additionalProperties: false
  },
  "ascii-table": {
    type: "array",
    description: "ASCII reference rows.",
    items: {
      type: "object",
      properties: {
        code: { type: "integer", minimum: 0, maximum: 127 },
        hex: { type: "string" },
        binary: { type: "string" },
        character: { type: "string" }
      },
      required: ["code", "hex", "binary", "character"],
      additionalProperties: false
    }
  },
  "roman-numerals-chart": {
    type: "array",
    description: "Roman numeral reference rows.",
    items: {
      type: "object",
      properties: {
        value: { type: "integer" },
        numeral: { type: "string" }
      },
      required: ["value", "numeral"],
      additionalProperties: false
    }
  },
  "hex-to-rgb": {
    type: "object",
    description: "RGB channel object. The CSS rgb(...) string is also available in content[0].text.",
    properties: {
      r: { type: "integer", minimum: 0, maximum: 255 },
      g: { type: "integer", minimum: 0, maximum: 255 },
      b: { type: "integer", minimum: 0, maximum: 255 }
    },
    required: ["r", "g", "b"],
    additionalProperties: false
  },
  "hex-to-rgba": {
    type: "object",
    description: "RGBA channel object. The CSS rgba(...) string is also available in content[0].text.",
    properties: {
      r: { type: "integer", minimum: 0, maximum: 255 },
      g: { type: "integer", minimum: 0, maximum: 255 },
      b: { type: "integer", minimum: 0, maximum: 255 },
      a: { type: "number", minimum: 0, maximum: 1 }
    },
    required: ["r", "g", "b", "a"],
    additionalProperties: false
  },
  "text-editor": {
    type: "object",
    description: "Text echo plus simple text metrics.",
    properties: {
      text: { type: "string" },
      characters: { type: "integer" },
      lines: { type: "integer" }
    },
    required: ["text", "characters", "lines"],
    additionalProperties: false
  },
  "regex-tester": {
    type: "object",
    description: "Regex match list and count.",
    properties: {
      matches: {
        type: "array",
        items: {
          type: "object",
          properties: {
            match: { type: "string" },
            index: { type: "integer" },
            groups: { type: "array", items: { type: "string" } }
          },
          required: ["match", "index", "groups"],
          additionalProperties: false
        }
      },
      count: { type: "integer" }
    },
    required: ["matches", "count"],
    additionalProperties: false
  },
  "case-converter": {
    oneOf: [
      {
        type: "object",
        description: "All case conversions when options.mode is all.",
        properties: {
          uppercase: { type: "string" },
          lowercase: { type: "string" },
          title: { type: "string" },
          sentence: { type: "string" },
          inverted: { type: "string" }
        },
        required: ["uppercase", "lowercase", "title", "sentence", "inverted"],
        additionalProperties: false
      },
      {
        type: "object",
        description: "Single case conversion when options.mode selects one mode.",
        properties: {
          mode: { type: "string" },
          result: { type: "string" }
        },
        required: ["mode", "result"],
        additionalProperties: false
      }
    ]
  },
  "word-counter": {
    type: "object",
    description: "Word and text statistics.",
    properties: {
      words: { type: "integer" },
      characters: { type: "integer" },
      charactersNoSpaces: { type: "integer" },
      lines: { type: "integer" },
      sentences: { type: "integer" },
      paragraphs: { type: "integer" }
    },
    required: ["words", "characters", "charactersNoSpaces", "lines", "sentences", "paragraphs"],
    additionalProperties: false
  },
  "character-count": {
    type: "object",
    description: "Character, byte, word, and line counts.",
    properties: {
      characters: { type: "integer" },
      charactersNoSpaces: { type: "integer" },
      bytesUtf8: { type: "integer" },
      words: { type: "integer" },
      lines: { type: "integer" }
    },
    required: ["characters", "charactersNoSpaces", "bytesUtf8", "words", "lines"],
    additionalProperties: false
  },
  "xml-to-json": {
    type: "object",
    description: "JSON object parsed from the XML root element. The exact root key comes from the XML input."
  }
};

function requireText(input) {
  if (input === undefined || input === null) return "";
  const text = typeof input === "string" ? input : JSON.stringify(input);
  if (text.length > MAX_TEXT_CHARS) {
    throw new McpToolError(`Input is too large. Maximum text input is ${MAX_TEXT_CHARS} characters.`);
  }
  return text;
}

function toolUrl(toolId) {
  return site.absoluteUrl(site.pathFor("en", toolId));
}

function makeInputSchema(toolId) {
  const schema = {
    type: "object",
    description: `Arguments for ${tools[toolId].title}.`,
    properties: {
      input: {
        type: "string",
        description: textInputDescriptions[toolId] || `Input for ${tools[toolId].title}.`
      },
      options: {
        type: "object",
        description: "Optional per-tool settings.",
        additionalProperties: true
      }
    },
    additionalProperties: false,
    examples: mcpExamples.arguments[toolId] ? [mcpExamples.arguments[toolId]] : []
  };

  if (browserOnlyToolIds.has(toolId)) {
    return {
      type: "object",
      description: `${tools[toolId].title} needs browser image APIs. tools/call does not process image bytes server-side; it returns a web UI resource link.`,
      properties: {},
      additionalProperties: false,
      examples: [{}]
    };
  }

  if (noArgumentToolIds.has(toolId)) {
    return {
      type: "object",
      description: `${tools[toolId].title} does not require arguments.`,
      properties: {},
      additionalProperties: false,
      examples: [{}]
    };
  }

  if (toolId === "password-generator") {
    delete schema.properties.input;
  }

  if (toolId === "rgb-to-hex") schema.properties.input = rgbInputSchema;
  if (toolId === "rgba-to-hex") schema.properties.input = rgbaInputSchema;
  if (toolId === "json-to-xml") {
    schema.properties.input = {
      oneOf: [
        { type: "string", description: textInputDescriptions[toolId] },
        { type: "object", description: "JSON object to convert to XML." },
        { type: "array", description: "JSON array to convert to XML." }
      ]
    };
  }

  if (optionSchemas[toolId]) {
    schema.properties.options = optionSchemas[toolId];
  }

  if (toolId === "image-to-base64") {
    schema.properties.input = {
      oneOf: [
        { type: "string", description: "Public image URL, data URI, or raw Base64 image bytes." },
        {
          type: "object",
          description: "Image input object.",
          properties: {
            url: { type: "string", description: "Public http/https image URL." },
            imageUrl: { type: "string", description: "Alias for url." },
            base64: { type: "string", description: "Raw Base64 image bytes." },
            data: { type: "string", description: "Raw Base64 image bytes or data URI." },
            mimeType: { type: "string", description: "MIME type for raw Base64 image bytes." }
          },
          additionalProperties: false
        }
      ]
    };
  }

  return schema;
}

function makeOutputSchema(toolId) {
  if (browserOnlyToolIds.has(toolId)) {
    return {
      type: "object",
      description: `${tools[toolId].title} returns isError=true with a resource_link to the browser UI because server-side image processing is not available.`
    };
  }
  return outputSchemas[toolId] || simpleResultOutputSchema(toolId);
}

function listMcpTools() {
  return toolIds.map((toolId) => ({
    name: toolId,
    title: tools[toolId].title,
    description: `${tools[toolId].description} Web UI: ${toolUrl(toolId)}`,
    inputSchema: makeInputSchema(toolId),
    outputSchema: makeOutputSchema(toolId),
    annotations: {
      readOnlyHint: true,
      destructiveHint: false,
      idempotentHint: toolId !== "password-generator",
      openWorldHint: false
    }
  }));
}

function asciiTable() {
  const rows = [];
  for (let code = 0; code <= 127; code += 1) {
    const hex = code.toString(16).toUpperCase().padStart(2, "0");
    const binary = code.toString(2).padStart(8, "0");
    const character = code < 32 || code === 127 ? controlName(code) : String.fromCharCode(code);
    rows.push({ code, hex, binary, character });
  }
  return rows;
}

function controlName(code) {
  const names = {
    0: "NUL",
    1: "SOH",
    2: "STX",
    3: "ETX",
    4: "EOT",
    5: "ENQ",
    6: "ACK",
    7: "BEL",
    8: "BS",
    9: "TAB",
    10: "LF",
    11: "VT",
    12: "FF",
    13: "CR",
    14: "SO",
    15: "SI",
    16: "DLE",
    17: "DC1",
    18: "DC2",
    19: "DC3",
    20: "DC4",
    21: "NAK",
    22: "SYN",
    23: "ETB",
    24: "CAN",
    25: "EM",
    26: "SUB",
    27: "ESC",
    28: "FS",
    29: "GS",
    30: "RS",
    31: "US",
    127: "DEL"
  };
  return names[code] || "";
}

function romanChart() {
  const rows = [];
  for (let value = 1; value <= 1000; value += 1) {
    rows.push({ value, numeral: numberToRomanNumeral(value) });
  }
  return rows;
}

function numberToRomanNumeral(input) {
  let number = Number(input);
  if (!Number.isInteger(number) || number < 1 || number > 3999) {
    throw new McpToolError("Input must be an integer from 1 to 3999.");
  }
  const values = [
    [1000, "M"],
    [900, "CM"],
    [500, "D"],
    [400, "CD"],
    [100, "C"],
    [90, "XC"],
    [50, "L"],
    [40, "XL"],
    [10, "X"],
    [9, "IX"],
    [5, "V"],
    [4, "IV"],
    [1, "I"]
  ];
  let result = "";
  values.forEach(([value, numeral]) => {
    while (number >= value) {
      result += numeral;
      number -= value;
    }
  });
  return result;
}

function regexFlags(options) {
  return String(options.flags || "g").replace(/[^dgimsuvy]/g, "") || "g";
}

function regexInput(input, options) {
  const text = typeof input === "object" && input ? requireText(input.text) : requireText(input);
  const pattern = options.pattern || (input && typeof input === "object" ? input.pattern : "");
  if (!pattern) throw new McpToolError("A regex pattern is required in options.pattern.");
  const patternText = String(pattern);
  if (text.length > MAX_REGEX_TEXT_CHARS) {
    throw new McpToolError(`Regex tools accept at most ${MAX_REGEX_TEXT_CHARS} input characters.`);
  }
  if (patternText.length > MAX_REGEX_PATTERN_CHARS) {
    throw new McpToolError(`Regex patterns accept at most ${MAX_REGEX_PATTERN_CHARS} characters.`);
  }
  return { text, pattern: patternText, flags: regexFlags(options) };
}

function runRegexWorker(payload) {
  const workerCode = `
    const { parentPort, workerData } = require("worker_threads");
    (() => {
      const { mode, text, pattern, flags, replacement, maxMatches } = workerData;
      try {
        const regex = new RegExp(pattern, flags);
        if (mode === "replace") {
          parentPort.postMessage({ ok: true, text: text.replace(regex, replacement) });
        } else {
          const matches = [];
          let match;
          while ((match = regex.exec(text)) !== null) {
            matches.push({ match: match[0], index: match.index, groups: match.slice(1) });
            if (matches.length > maxMatches) {
              parentPort.postMessage({ ok: false, message: "Regex produced too many matches." });
              return;
            }
            if (!regex.global) break;
            if (match[0] === "") regex.lastIndex += 1;
          }
          parentPort.postMessage({ ok: true, matches });
        }
      } catch (error) {
        parentPort.postMessage({ ok: false, message: error.message });
      }
    })();
  `;

  return new Promise((resolve, reject) => {
    const worker = new Worker(workerCode, { eval: true, workerData: payload });
    const timeout = setTimeout(() => {
      worker.terminate().finally(() => {
        reject(new McpToolError("Regex execution timed out."));
      });
    }, REGEX_TIMEOUT_MS);

    worker.once("message", (message) => {
      clearTimeout(timeout);
      worker.terminate().finally(() => {
        if (message.ok) {
          resolve(message);
        } else {
          reject(new McpToolError(message.message || "Regex execution failed."));
        }
      });
    });
    worker.once("error", (error) => {
      clearTimeout(timeout);
      worker.terminate().finally(() => reject(error));
    });
  });
}

async function regexTester(input, options) {
  const { text, pattern, flags } = regexInput(input, options);
  const result = await runRegexWorker({
    mode: "test",
    text,
    pattern,
    flags,
    maxMatches: MAX_REGEX_MATCHES
  });
  const matches = result.matches;
  return { text: JSON.stringify(matches, null, 2), data: { matches, count: matches.length } };
}

async function regexReplace(input, options) {
  const { text, pattern, flags } = regexInput(input, options);
  const replacement = options.replacement !== undefined
    ? String(options.replacement)
    : input && typeof input === "object" && input.replacement !== undefined
      ? String(input.replacement)
      : "";
  const result = await runRegexWorker({
    mode: "replace",
    text,
    pattern,
    flags,
    replacement,
    maxMatches: MAX_REGEX_MATCHES
  });
  return { text: result.text };
}

function urlEncode(input, options) {
  const text = requireText(input);
  const mode = options.mode === "uri" ? "uri" : "component";
  const encode = mode === "uri" ? encodeURI : encodeURIComponent;
  const output = options.lineByLine
    ? text.split(/\r?\n/).map((line) => encode(line)).join("\n")
    : encode(text);
  return { text: options.spaceAsPlus ? output.replace(/%20/g, "+") : output };
}

function decodeUrlPart(value, plusAsSpace) {
  const text = plusAsSpace ? String(value).replace(/\+/g, " ") : String(value);
  return decodeURIComponent(text);
}

function extractQuery(value) {
  const hashless = String(value).trim().split("#")[0];
  const question = hashless.indexOf("?");
  if (question >= 0) return hashless.slice(question + 1);
  return hashless.charAt(0) === "?" ? hashless.slice(1) : hashless;
}

function parseQueryString(value, plusAsSpace) {
  const source = extractQuery(value);
  if (!source || !/[=&]/.test(source)) return [];
  return source.split("&").filter(Boolean).map((pair, index) => {
    const eq = pair.indexOf("=");
    const rawKey = eq >= 0 ? pair.slice(0, eq) : pair;
    const rawValue = eq >= 0 ? pair.slice(eq + 1) : "";
    return {
      index: index + 1,
      key: decodeUrlPart(rawKey, plusAsSpace),
      value: decodeUrlPart(rawValue, plusAsSpace)
    };
  });
}

function decodeUrlText(value, plusAsSpace) {
  const text = requireText(value);
  if (!text.includes("://")) {
    return decodeUrlPart(text, plusAsSpace);
  }

  const parsed = new URL(text);
  const path = parsed.pathname
    .split("/")
    .map((segment) => decodeUrlPart(segment, false))
    .join("/");
  const queryRows = parseQueryString(text, plusAsSpace);
  const query = queryRows.length
    ? `?${queryRows.map((row) => `${row.key}=${row.value}`).join("&")}`
    : "";
  const hash = parsed.hash ? `#${decodeUrlPart(parsed.hash.slice(1), plusAsSpace)}` : "";
  return `${parsed.origin}${path}${query}${hash}`;
}

function urlDecode(input, options) {
  const text = requireText(input);
  const plusAsSpace = options.plusAsSpace !== false;
  const decoded = decodeUrlText(text, plusAsSpace);
  const rows = options.parseQuery === false ? [] : parseQueryString(text, plusAsSpace);
  const lines = [decoded];
  if (rows.length) {
    lines.push("", "Query Parameters");
    rows.forEach((row) => {
      lines.push(`${row.index}. ${row.key} = ${row.value}`);
    });
  }
  return { text: lines.join("\n") };
}

function stableJsonValue(value) {
  if (Array.isArray(value)) return value.map(stableJsonValue);
  if (!value || typeof value !== "object") return value;
  return Object.keys(value).sort().reduce((result, key) => {
    result[key] = stableJsonValue(value[key]);
    return result;
  }, {});
}

function jsonValuesEqual(left, right) {
  return JSON.stringify(stableJsonValue(left)) === JSON.stringify(stableJsonValue(right));
}

function jsonType(value) {
  if (Array.isArray(value)) return "array";
  if (value === null) return "null";
  return typeof value;
}

function pushJsonChange(changes, type, path, left, right) {
  changes.push({ type, path: path || "$", left, right });
}

function collectJsonDiff(left, right, path, changes, includeUnchanged) {
  if (jsonValuesEqual(left, right)) {
    if (includeUnchanged) pushJsonChange(changes, "unchanged", path, left, right);
    return;
  }

  const leftType = jsonType(left);
  const rightType = jsonType(right);
  if (leftType !== rightType) {
    pushJsonChange(changes, "changed", path, left, right);
    return;
  }

  if (leftType === "array") {
    const length = Math.max(left.length, right.length);
    for (let index = 0; index < length; index += 1) {
      const childPath = `${path}[${index}]`;
      if (index >= left.length) pushJsonChange(changes, "added", childPath, undefined, right[index]);
      else if (index >= right.length) pushJsonChange(changes, "removed", childPath, left[index], undefined);
      else collectJsonDiff(left[index], right[index], childPath, changes, includeUnchanged);
    }
    return;
  }

  if (leftType === "object") {
    const keys = Array.from(new Set(Object.keys(left).concat(Object.keys(right)))).sort();
    keys.forEach((key) => {
      const childPath = `${path}.${key}`;
      if (!Object.prototype.hasOwnProperty.call(left, key)) pushJsonChange(changes, "added", childPath, undefined, right[key]);
      else if (!Object.prototype.hasOwnProperty.call(right, key)) pushJsonChange(changes, "removed", childPath, left[key], undefined);
      else collectJsonDiff(left[key], right[key], childPath, changes, includeUnchanged);
    });
    return;
  }

  pushJsonChange(changes, "changed", path, left, right);
}

function summarizeChanges(changes) {
  return changes.reduce((summary, change) => {
    summary[change.type] += 1;
    return summary;
  }, { added: 0, removed: 0, changed: 0, unchanged: 0 });
}

function formatJsonValue(value) {
  return JSON.stringify(value, null, 2);
}

function jsonDiff(input, options) {
  if (typeof options.compareTo !== "string") {
    throw new McpToolError("options.compareTo must contain the changed JSON string.");
  }

  let left;
  let right;
  try {
    left = JSON.parse(requireText(input));
    right = JSON.parse(requireText(options.compareTo));
  } catch (error) {
    throw new McpToolError(`Invalid JSON: ${error.message}`);
  }

  const changes = [];
  collectJsonDiff(left, right, "$", changes, Boolean(options.includeUnchanged));
  const summary = summarizeChanges(changes);
  const lines = [
    "Summary",
    `Added: ${summary.added}`,
    `Removed: ${summary.removed}`,
    `Changed: ${summary.changed}`,
    `Unchanged: ${summary.unchanged}`,
    ""
  ];

  changes.forEach((change) => {
    lines.push(`[${change.type}] ${change.path}`);
    if (change.type === "added") lines.push(`+ ${formatJsonValue(change.right)}`);
    else if (change.type === "removed") lines.push(`- ${formatJsonValue(change.left)}`);
    else if (change.type === "changed") {
      lines.push(`- ${formatJsonValue(change.left)}`);
      lines.push(`+ ${formatJsonValue(change.right)}`);
    } else {
      lines.push(`  ${formatJsonValue(change.left)}`);
    }
    lines.push("");
  });

  return { text: lines.join("\n").trim() };
}

function normalizeCompareLine(value, options) {
  let result = value;
  if (options.ignoreWhitespace) result = result.replace(/\s+/g, " ").trim();
  if (options.ignoreCase) result = result.toLowerCase();
  return result;
}

function combineTextChanges(ops) {
  const result = [];
  let removed = [];
  let added = [];

  function flush() {
    const pairs = Math.min(removed.length, added.length);
    for (let index = 0; index < pairs; index += 1) {
      result.push({
        type: "changed",
        left: removed[index].left,
        right: added[index].right,
        leftLine: removed[index].leftLine,
        rightLine: added[index].rightLine
      });
    }
    result.push(...removed.slice(pairs), ...added.slice(pairs));
    removed = [];
    added = [];
  }

  ops.forEach((op) => {
    if (op.type === "removed") removed.push(op);
    else if (op.type === "added") added.push(op);
    else {
      flush();
      result.push(op);
    }
  });
  flush();
  return result;
}

function diffTextLines(leftLines, rightLines, options) {
  const leftLength = leftLines.length;
  const rightLength = rightLines.length;
  const dp = Array.from({ length: leftLength + 1 }, () => Array(rightLength + 1).fill(0));

  for (let leftIndex = leftLength - 1; leftIndex >= 0; leftIndex -= 1) {
    for (let rightIndex = rightLength - 1; rightIndex >= 0; rightIndex -= 1) {
      dp[leftIndex][rightIndex] = normalizeCompareLine(leftLines[leftIndex], options) === normalizeCompareLine(rightLines[rightIndex], options)
        ? dp[leftIndex + 1][rightIndex + 1] + 1
        : Math.max(dp[leftIndex + 1][rightIndex], dp[leftIndex][rightIndex + 1]);
    }
  }

  const ops = [];
  let leftIndex = 0;
  let rightIndex = 0;
  while (leftIndex < leftLength && rightIndex < rightLength) {
    if (normalizeCompareLine(leftLines[leftIndex], options) === normalizeCompareLine(rightLines[rightIndex], options)) {
      ops.push({ type: "unchanged", left: leftLines[leftIndex], right: rightLines[rightIndex], leftLine: leftIndex + 1, rightLine: rightIndex + 1 });
      leftIndex += 1;
      rightIndex += 1;
    } else if (dp[leftIndex + 1][rightIndex] >= dp[leftIndex][rightIndex + 1]) {
      ops.push({ type: "removed", left: leftLines[leftIndex], leftLine: leftIndex + 1 });
      leftIndex += 1;
    } else {
      ops.push({ type: "added", right: rightLines[rightIndex], rightLine: rightIndex + 1 });
      rightIndex += 1;
    }
  }

  while (leftIndex < leftLength) {
    ops.push({ type: "removed", left: leftLines[leftIndex], leftLine: leftIndex + 1 });
    leftIndex += 1;
  }
  while (rightIndex < rightLength) {
    ops.push({ type: "added", right: rightLines[rightIndex], rightLine: rightIndex + 1 });
    rightIndex += 1;
  }

  return combineTextChanges(ops);
}

function textCompare(input, options) {
  if (typeof options.compareTo !== "string") {
    throw new McpToolError("options.compareTo must contain the changed text.");
  }

  const changes = diffTextLines(requireText(input).split(/\r?\n/), requireText(options.compareTo).split(/\r?\n/), options);
  const summary = summarizeChanges(changes);
  const visible = options.showUnchanged ? changes : changes.filter((change) => change.type !== "unchanged");
  const lines = [
    "Summary",
    `Added: ${summary.added}`,
    `Removed: ${summary.removed}`,
    `Changed: ${summary.changed}`,
    `Unchanged: ${summary.unchanged}`,
    ""
  ];

  visible.forEach((change) => {
    if (change.type === "unchanged") lines.push(`  ${change.left}`);
    else if (change.type === "added") lines.push(`+ [${change.rightLine}] ${change.right}`);
    else if (change.type === "removed") lines.push(`- [${change.leftLine}] ${change.left}`);
    else {
      lines.push(`~ [${change.leftLine} -> ${change.rightLine}]`);
      lines.push(`- ${change.left}`);
      lines.push(`+ ${change.right}`);
    }
  });

  return { text: lines.join("\n").trim() };
}

function formatXml(input) {
  const text = requireText(input).trim();
  if (!text) return "";
  const tokens = text.match(/<!--[\s\S]*?-->|<!\[CDATA\[[\s\S]*?\]\]>|<[^>]+>|[^<]+/g) || [];
  let depth = 0;
  let line = "";
  const lines = [];

  const flush = () => {
    if (line) {
      lines.push(line);
      line = "";
    }
  };

  tokens.forEach((rawToken) => {
    const token = rawToken.trim();
    if (!token) return;

    if (token.startsWith("</")) {
      depth = Math.max(depth - 1, 0);
      if (line) {
        line += token;
        flush();
      } else {
        lines.push(`${"  ".repeat(depth)}${token}`);
      }
      return;
    }

    if (token.startsWith("<")) {
      const isStandalone = /^<!(?:--|\[CDATA\[)/.test(token)
        || /^<\?/.test(token)
        || /^<![A-Z]/i.test(token)
        || /\/>$/.test(token);
      flush();
      if (isStandalone) {
        lines.push(`${"  ".repeat(depth)}${token}`);
      } else {
        line = `${"  ".repeat(depth)}${token}`;
        depth += 1;
      }
      return;
    }

    const normalizedText = token.replace(/\s+/g, " ");
    if (line) {
      line += normalizedText;
    } else {
      lines.push(`${"  ".repeat(depth)}${normalizedText}`);
    }
  });

  flush();
  return lines.join("\n");
}

function minifyMarkup(input) {
  return requireText(input)
    .replace(/<!--[\s\S]*?-->/g, "")
    .replace(/>\s+</g, "><")
    .replace(/\s+/g, " ")
    .trim();
}

function formatCss(input) {
  return requireText(input)
    .replace(/\s*{\s*/g, " {\n  ")
    .replace(/;\s*/g, ";\n  ")
    .replace(/\s*}\s*/g, "\n}\n")
    .replace(/\n\s*\n/g, "\n")
    .trim();
}

function minifyCss(input) {
  return requireText(input)
    .replace(/\/\*[\s\S]*?\*\//g, "")
    .replace(/\s+/g, " ")
    .replace(/\s*([{}:;,>+~])\s*/g, "$1")
    .replace(/;}/g, "}")
    .trim();
}

function formatJavaScript(input) {
  return requireText(input)
    .replace(/\s*{\s*/g, " {\n  ")
    .replace(/;\s*/g, ";\n")
    .replace(/\s*}\s*/g, "\n}\n")
    .replace(/\n\s*\n/g, "\n")
    .trim();
}

function minifyJavaScript(input) {
  return requireText(input)
    .replace(/\/\*[\s\S]*?\*\//g, "")
    .replace(/(^|[^:])\/\/.*$/gm, "$1")
    .replace(/\s+/g, " ")
    .replace(/\s*([{}();,:=+\-*/<>])\s*/g, "$1")
    .trim();
}

function formatSql(input) {
  const text = requireText(input)
    .replace(/--.*$/gm, "")
    .replace(/\s+/g, " ")
    .replace(/\s*,\s*/g, ", ")
    .trim();
  if (!text) return "";

  const clauses = [
    "SELECT",
    "FROM",
    "WHERE",
    "GROUP BY",
    "ORDER BY",
    "HAVING",
    "LIMIT",
    "VALUES",
    "SET",
    "LEFT JOIN",
    "RIGHT JOIN",
    "INNER JOIN",
    "OUTER JOIN",
    "JOIN",
    "AND",
    "OR"
  ];
  const pattern = new RegExp(`\\b(${clauses.join("|")})\\b`, "gi");
  return text
    .replace(pattern, (match, keyword, offset) => {
      const formattedKeyword = keyword.toUpperCase();
      return offset === 0 ? formattedKeyword : `\n${formattedKeyword}`;
    })
    .replace(/\bASC\b/gi, "ASC")
    .replace(/\bDESC\b/gi, "DESC")
    .replace(/\n(AND|OR)\b/g, "\n  $1")
    .replace(/\n+/g, "\n")
    .trim();
}

function minifySql(input) {
  return requireText(input).replace(/--.*$/gm, "").replace(/\s+/g, " ").trim();
}

function jsonToXml(input, options) {
  let value;
  try {
    value = typeof input === "string" ? JSON.parse(input) : input;
  } catch (error) {
    throw new McpToolError(`Invalid JSON: ${error.message}`);
  }
  const rootName = String(options.rootName || "root");
  return xmlNode(rootName, value);
}

function xmlNode(name, value, depth = 0) {
  if (depth > MAX_JSON_TO_XML_DEPTH) {
    throw new McpToolError(`JSON nesting is too deep. Maximum depth is ${MAX_JSON_TO_XML_DEPTH}.`);
  }
  const safeName = String(name).replace(/[^A-Za-z0-9_.-]/g, "_") || "item";
  if (Array.isArray(value)) {
    return value.map((item) => xmlNode(safeName, item, depth + 1)).join("");
  }
  if (value && typeof value === "object") {
    const inner = Object.entries(value).map(([key, child]) => xmlNode(key, child, depth + 1)).join("");
    return `<${safeName}>${inner}</${safeName}>`;
  }
  return `<${safeName}>${escapeXml(value === undefined || value === null ? "" : String(value))}</${safeName}>`;
}

function escapeXml(value) {
  return value
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function xmlToJson(input) {
  const text = requireText(input).trim();
  const match = text.match(/^<([A-Za-z0-9_.:-]+)[^>]*>([\s\S]*)<\/\1>$/);
  if (!match) throw new McpToolError("XML input must have one root element.");
  return { text: JSON.stringify({ [match[1]]: xmlChildren(match[2]) }, null, 2), data: { [match[1]]: xmlChildren(match[2]) } };
}

function xmlChildren(value) {
  const children = {};
  const pattern = /<([A-Za-z0-9_.:-]+)[^>]*>([\s\S]*?)<\/\1>/g;
  let match;
  let found = false;
  while ((match = pattern.exec(value)) !== null) {
    found = true;
    const childValue = xmlChildren(match[2]);
    if (children[match[1]] !== undefined) {
      if (!Array.isArray(children[match[1]])) children[match[1]] = [children[match[1]]];
      children[match[1]].push(childValue);
    } else {
      children[match[1]] = childValue;
    }
  }
  return found ? children : value.replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&quot;/g, "\"").replace(/&amp;/g, "&");
}

function numberToWords(input, options) {
  const number = Number(requireText(input).trim());
  if (!Number.isSafeInteger(number) || number < 0 || number > 999999999999) {
    throw new McpToolError("Input must be a safe integer from 0 to 999,999,999,999.");
  }
  const words = integerToWords(number);
  if (options.mode === "ordinal") return { text: ordinalWords(words) };
  if (options.mode === "ordinal-number") return { text: ordinalNumber(number) };
  return { text: words };
}

function integerToWords(number) {
  const belowTwenty = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];
  const tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"];
  if (number < 20) return belowTwenty[number];
  if (number < 100) return tens[Math.floor(number / 10)] + (number % 10 ? `-${belowTwenty[number % 10]}` : "");
  if (number < 1000) return `${belowTwenty[Math.floor(number / 100)]} hundred${number % 100 ? ` ${integerToWords(number % 100)}` : ""}`;
  const units = [
    [1000000000, "billion"],
    [1000000, "million"],
    [1000, "thousand"]
  ];
  for (const [value, label] of units) {
    if (number >= value) {
      return `${integerToWords(Math.floor(number / value))} ${label}${number % value ? ` ${integerToWords(number % value)}` : ""}`;
    }
  }
  return "";
}

function ordinalWords(words) {
  const replacements = {
    one: "first",
    two: "second",
    three: "third",
    five: "fifth",
    eight: "eighth",
    nine: "ninth",
    twelve: "twelfth"
  };
  const parts = words.split(/([ -])/);
  const lastIndex = parts.map((part) => /[a-z]/.test(part) ? part : null).lastIndexOf(parts.filter((part) => /[a-z]/.test(part)).pop());
  const last = parts[lastIndex];
  parts[lastIndex] = replacements[last] || (last.endsWith("y") ? `${last.slice(0, -1)}ieth` : `${last}th`);
  return parts.join("");
}

function ordinalNumber(number) {
  const lastTwo = number % 100;
  if (lastTwo >= 11 && lastTwo <= 13) return `${number}th`;
  const suffixes = { 1: "st", 2: "nd", 3: "rd" };
  return `${number}${suffixes[number % 10] || "th"}`;
}

function imageInputParts(input) {
  if (input && typeof input === "object" && !Array.isArray(input)) {
    return {
      url: input.url || input.imageUrl || "",
      base64: input.base64 || input.data || "",
      mimeType: input.mimeType || ""
    };
  }
  const value = requireText(input).trim();
  return /^https?:\/\//i.test(value)
    ? { url: value, base64: "", mimeType: "" }
    : { url: "", base64: value, mimeType: "" };
}

function isPrivateIp(address) {
  if (!address) return true;
  const normalized = address.replace(/^::ffff:/i, "");
  if (net.isIP(normalized) === 4) {
    const parts = normalized.split(".").map((part) => Number(part));
    return parts[0] === 0 ||
      parts[0] === 10 ||
      parts[0] === 127 ||
      (parts[0] === 169 && parts[1] === 254) ||
      (parts[0] === 172 && parts[1] >= 16 && parts[1] <= 31) ||
      (parts[0] === 192 && parts[1] === 168);
  }
  if (net.isIP(normalized) === 6) {
    const lower = normalized.toLowerCase();
    return lower === "::1" || lower.startsWith("fc") || lower.startsWith("fd") || lower.startsWith("fe80:");
  }
  return true;
}

async function assertPublicImageUrl(value) {
  let parsed;
  try {
    parsed = new URL(value);
  } catch (error) {
    throw new McpToolError("Image URL must be a valid http or https URL.");
  }
  if (parsed.protocol !== "http:" && parsed.protocol !== "https:") {
    throw new McpToolError("Image URL must use http or https.");
  }
  if (["localhost", "localhost.localdomain"].includes(parsed.hostname.toLowerCase())) {
    throw new McpToolError("Private or localhost image URLs are not allowed.");
  }
  const hostnameIsIp = net.isIP(parsed.hostname);
  let addresses;
  try {
    addresses = hostnameIsIp
      ? [{ address: parsed.hostname }]
      : await dns.lookup(parsed.hostname, { all: true });
  } catch (error) {
    throw new McpToolError(`Could not resolve image URL host: ${error.message}`);
  }
  if (addresses.some((entry) => isPrivateIp(entry.address))) {
    throw new McpToolError("Private network image URLs are not allowed.");
  }
}

async function fetchImageAsDataUri(url, options) {
  await assertPublicImageUrl(url);
  let response;
  try {
    response = await fetch(url, { signal: AbortSignal.timeout(8000) });
  } catch (error) {
    throw new McpToolError(`Could not fetch image URL: ${error.message}`);
  }
  if (!response.ok) {
    throw new McpToolError(`Image URL returned HTTP ${response.status}.`);
  }
  const contentLength = Number(response.headers.get("content-length") || 0);
  if (contentLength > MAX_IMAGE_BYTES) {
    throw new McpToolError("Image is too large. Maximum size is 5 MB.");
  }
  const mimeType = (response.headers.get("content-type") || options.mimeType || "image/png").split(";")[0].trim();
  if (!mimeType.startsWith("image/")) {
    throw new McpToolError("Image URL must return an image/* content type.");
  }
  const buffer = Buffer.from(await response.arrayBuffer());
  if (buffer.length > MAX_IMAGE_BYTES) {
    throw new McpToolError("Image is too large. Maximum size is 5 MB.");
  }
  return `data:${mimeType};base64,${buffer.toString("base64")}`;
}

async function imageToBase64(input, options) {
  const parts = imageInputParts(input);
  if (parts.url) return { text: await fetchImageAsDataUri(parts.url, options) };
  const value = requireText(parts.base64).trim();
  const mimeType = options.mimeType || parts.mimeType || "image/png";
  if (value.startsWith("data:")) return { text: value };
  if (!/^[A-Za-z0-9+/]+={0,2}$/.test(value)) {
    throw new McpToolError("Provide a public image URL, image bytes as a Base64 string, or a data URI.");
  }
  return { text: `data:${mimeType};base64,${value}` };
}

function textEditor(input) {
  const text = requireText(input);
  const data = {
    text,
    characters: Array.from(text).length,
    lines: text ? text.split(/\r\n|\r|\n/).length : 0
  };
  return { text, data };
}

async function executeMcpTool(toolId, args = {}) {
  if (!tools[toolId]) {
    throw new McpToolError(`Unknown tool: ${toolId}`);
  }

  const input = Object.prototype.hasOwnProperty.call(args, "input") ? args.input : "";
  const options = args.options || {};

  if (isRuntimeTool(toolId)) {
    return executeTool(toolId, input, options);
  }

  switch (toolId) {
    case "ascii-table": {
      const data = asciiTable();
      return { text: JSON.stringify(data, null, 2), data };
    }
    case "roman-numerals-chart": {
      const data = romanChart();
      return { text: JSON.stringify(data, null, 2), data };
    }
    case "text-editor":
      return textEditor(input);
    case "regex-tester":
      return regexTester(input, options);
    case "regex-replace":
      return regexReplace(input, options);
    case "url-encode":
      return urlEncode(input, options);
    case "url-decode":
      return urlDecode(input, options);
    case "json-diff":
      return jsonDiff(input, options);
    case "text-compare":
      return textCompare(input, options);
    case "number-to-words":
      return numberToWords(input, options);
    case "xml-formatter":
      return { text: formatXml(input) };
    case "xml-minifier":
      return { text: minifyMarkup(input) };
    case "json-to-xml":
      return { text: jsonToXml(input, options) };
    case "xml-to-json":
      return xmlToJson(input);
    case "html-beautifier":
      return { text: formatXml(input) };
    case "html-minifier":
      return { text: minifyMarkup(input) };
    case "javascript-beautifier":
      return { text: formatJavaScript(input) };
    case "javascript-minifier":
      return { text: minifyJavaScript(input) };
    case "css-beautifier":
      return { text: formatCss(input) };
    case "css-minifier":
      return { text: minifyCss(input) };
    case "sql-formatter":
      return { text: formatSql(input) };
    case "sql-minifier":
      return { text: minifySql(input) };
    case "image-to-base64":
      return imageToBase64(input, options);
    default:
      if (browserOnlyToolIds.has(toolId)) {
        throw new McpToolError(`${tools[toolId].title} requires browser image APIs and is available through the web UI: ${toolUrl(toolId)}`);
      }
      throw new McpToolError(`Tool "${toolId}" is not implemented in the MCP runtime.`);
  }
}

function toolResultToMcp(toolId, result) {
  const text = result.text === undefined ? "" : String(result.text);
  const content = [
    {
      type: "text",
      text
    }
  ];
  if (tools[toolId]) {
    content.push({
      type: "resource_link",
      uri: toolUrl(toolId),
      name: tools[toolId].title,
      description: tools[toolId].description,
      mimeType: "text/html"
    });
  }
  const response = {
    content,
    isError: false,
    structuredContent: makeStructuredContent(toolId, text, result.data)
  };
  return response;
}

function makeStructuredContent(toolId, text, data) {
  if (toolId === "password-generator") {
    return Object.assign({ password: text }, data && typeof data === "object" ? data : { generated: true });
  }
  if (data !== undefined) {
    return data && typeof data === "object" ? data : { result: data };
  }
  return { result: text };
}

function toolErrorToMcp(toolId, error) {
  const content = [
    {
      type: "text",
      text: error.message
    }
  ];
  if (tools[toolId]) {
    content.push({
      type: "resource_link",
      uri: toolUrl(toolId),
      name: tools[toolId].title,
      description: tools[toolId].description,
      mimeType: "text/html"
    });
  }
  return {
    content,
    isError: true
  };
}

async function callMcpTool(toolId, args = {}) {
  try {
    return toolResultToMcp(toolId, await executeMcpTool(toolId, args));
  } catch (error) {
    if (error instanceof ToolInputError || error instanceof McpToolError) {
      return toolErrorToMcp(toolId, error);
    }
    throw error;
  }
}

module.exports = {
  McpToolError,
  toolIds,
  listMcpTools,
  callMcpTool,
  executeMcpTool
};
