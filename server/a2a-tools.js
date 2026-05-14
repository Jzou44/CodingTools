const crypto = require("crypto");
const { supportedToolIds, isRuntimeTool } = require("./tool-registry");

const MAX_TEXT_CHARS = 200000;
const MAX_INTEGER_DIGITS = 4096;

class ToolInputError extends Error {
  constructor(message) {
    super(message);
    this.name = "ToolInputError";
  }
}

function requireText(input) {
  if (input === undefined || input === null) return "";
  const text = typeof input === "string" ? input : JSON.stringify(input);
  if (text.length > MAX_TEXT_CHARS) {
    throw new ToolInputError(`Input is too large. Maximum text input is ${MAX_TEXT_CHARS} characters.`);
  }
  return text;
}

function parseInteger(value, label, base) {
  const text = requireText(value).trim();
  const patterns = {
    2: /^-?[01]+$/,
    8: /^-?[0-7]+$/,
    10: /^-?\d+$/,
    16: /^-?(?:0x)?[0-9a-f]+$/i
  };
  if (!patterns[base].test(text)) {
    throw new ToolInputError(`${label} must be a valid base-${base} integer.`);
  }
  const digitCount = text.replace(/^-/, "").replace(/^0x/i, "").length;
  if (digitCount > MAX_INTEGER_DIGITS) {
    throw new ToolInputError(`${label} is too large. Maximum integer input is ${MAX_INTEGER_DIGITS} digits.`);
  }
  const isNegative = text.startsWith("-");
  const normalized = text.replace(/^-/, "").replace(/^0x/i, "");
  const prefixes = { 2: "0b", 8: "0o", 10: "", 16: "0x" };
  const parsed = BigInt(`${prefixes[base]}${normalized}`);
  return isNegative ? -parsed : parsed;
}

function integerToBase(value, base) {
  return value.toString(base).toUpperCase();
}

function parseFiniteNumber(value, label) {
  const number = Number(requireText(value).trim().replace(/%$/, ""));
  if (!Number.isFinite(number)) {
    throw new ToolInputError(`${label} must be a finite number.`);
  }
  return number;
}

function gcd(a, b) {
  let x = Math.abs(a);
  let y = Math.abs(b);
  while (y) {
    const t = y;
    y = x % y;
    x = t;
  }
  return x || 1;
}

function decimalToFractionValue(value) {
  const number = parseFiniteNumber(value, "Input");
  if (Number.isInteger(number)) return `${number}/1`;
  const text = String(number);
  const decimals = text.includes(".") ? text.split(".")[1].length : 0;
  const denominator = 10 ** decimals;
  const numerator = Math.round(number * denominator);
  const divisor = gcd(numerator, denominator);
  return `${numerator / divisor}/${denominator / divisor}`;
}

function parseFraction(value) {
  const text = requireText(value).trim();
  const match = text.match(/^(-?\d+)\s*\/\s*(-?\d+)$/);
  if (!match) {
    throw new ToolInputError("Input must be a fraction like 3/4.");
  }
  const numerator = Number(match[1]);
  const denominator = Number(match[2]);
  if (!denominator) {
    throw new ToolInputError("Fraction denominator cannot be zero.");
  }
  return { numerator, denominator };
}

function normalizeHex(value) {
  const text = requireText(value).trim().replace(/^#/, "");
  if (!/^[0-9a-f]{3,8}$/i.test(text)) {
    throw new ToolInputError("Input must be a valid 3, 4, 6, or 8 digit hex color.");
  }
  if (text.length === 3 || text.length === 4) {
    return text.split("").map((char) => char + char).join("");
  }
  return text;
}

function hexToRgbObject(input) {
  const hex = normalizeHex(input);
  return {
    r: parseInt(hex.slice(0, 2), 16),
    g: parseInt(hex.slice(2, 4), 16),
    b: parseInt(hex.slice(4, 6), 16),
    a: hex.length >= 8 ? Math.round((parseInt(hex.slice(6, 8), 16) / 255) * 1000) / 1000 : 1
  };
}

function parseRgb(input) {
  if (input && typeof input === "object" && !Array.isArray(input)) {
    return input;
  }
  const text = requireText(input);
  const match = text.match(/rgba?\s*\(([^)]+)\)/i);
  const parts = (match ? match[1] : text).split(/[\s,]+/).filter(Boolean);
  if (parts.length < 3) {
    throw new ToolInputError("Input must provide red, green, and blue values.");
  }
  return { r: parts[0], g: parts[1], b: parts[2], a: parts[3] };
}

function colorChannel(value, label) {
  const number = Number(value);
  if (!Number.isInteger(number) || number < 0 || number > 255) {
    throw new ToolInputError(`${label} must be an integer from 0 to 255.`);
  }
  return number;
}

function alphaChannel(value) {
  if (value === undefined || value === null || value === "") return 1;
  const number = Number(value);
  if (!Number.isFinite(number) || number < 0 || number > 1) {
    throw new ToolInputError("Alpha must be a number from 0 to 1.");
  }
  return number;
}

function rgbToHexValue(input, includeAlpha) {
  const rgb = parseRgb(input);
  const channels = [
    colorChannel(rgb.r, "Red"),
    colorChannel(rgb.g, "Green"),
    colorChannel(rgb.b, "Blue")
  ];
  if (includeAlpha) channels.push(Math.round(alphaChannel(rgb.a) * 255));
  return `#${channels.map((value) => value.toString(16).padStart(2, "0")).join("").toUpperCase()}`;
}

const romanValues = [
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

function numberToRoman(input) {
  let number = Number(requireText(input).trim());
  if (!Number.isInteger(number) || number < 1 || number > 3999) {
    throw new ToolInputError("Input must be an integer from 1 to 3999.");
  }
  let result = "";
  romanValues.forEach(([value, numeral]) => {
    while (number >= value) {
      result += numeral;
      number -= value;
    }
  });
  return result;
}

function romanToNumber(input) {
  const text = requireText(input).trim().toUpperCase();
  if (!/^[IVXLCDM]+$/.test(text)) {
    throw new ToolInputError("Input must be a valid Roman numeral.");
  }
  let index = 0;
  let total = 0;
  romanValues.forEach(([value, numeral]) => {
    while (text.slice(index, index + numeral.length) === numeral) {
      total += value;
      index += numeral.length;
    }
  });
  if (numberToRoman(String(total)) !== text) {
    throw new ToolInputError("Input must use standard Roman numeral form.");
  }
  return String(total);
}

function titleCase(text) {
  return text.toLowerCase().replace(/\b\w/g, (char) => char.toUpperCase());
}

function sentenceCase(text) {
  const lower = text.toLowerCase();
  return lower.replace(/(^\s*\w|[.!?]\s+\w)/g, (match) => match.toUpperCase());
}

function invertCase(text) {
  return Array.from(text).map((char) => {
    const upper = char.toUpperCase();
    const lower = char.toLowerCase();
    return char === upper ? lower : upper;
  }).join("");
}

function countWords(text) {
  const matches = text.trim().match(/\S+/g);
  return matches ? matches.length : 0;
}

function countSentences(text) {
  const matches = text.match(/[.!?]+(?:\s|$)/g);
  return matches ? matches.length : 0;
}

function countParagraphs(text) {
  return text.trim() ? text.trim().split(/\n\s*\n/).length : 0;
}

function makePassword(options) {
  const length = Math.min(Math.max(Number(options.length || 16), 8), 128);
  const includeUppercase = options.uppercase !== false;
  const includeLowercase = options.lowercase !== false;
  const includeNumbers = options.numbers !== false;
  const includeSymbols = options.symbols !== false;
  let alphabet = "";
  if (includeUppercase) alphabet += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  if (includeLowercase) alphabet += "abcdefghijklmnopqrstuvwxyz";
  if (includeNumbers) alphabet += "0123456789";
  if (includeSymbols) alphabet += "!@#$%^&*()-_=+[]{};:,.?";
  if (!alphabet) {
    throw new ToolInputError("At least one character group must be enabled.");
  }
  const bytes = crypto.randomBytes(length);
  return Array.from(bytes).map((byte) => alphabet[byte % alphabet.length]).join("");
}

function minifyJson(input) {
  try {
    return JSON.stringify(JSON.parse(requireText(input)));
  } catch (error) {
    throw new ToolInputError(`Invalid JSON: ${error.message}`);
  }
}

function formatJson(input, options) {
  const spaces = Math.min(Math.max(Number(options.spaces || 2), 0), 8);
  try {
    return JSON.stringify(JSON.parse(requireText(input)), null, spaces);
  } catch (error) {
    throw new ToolInputError(`Invalid JSON: ${error.message}`);
  }
}

function executeTool(toolId, input, options = {}) {
  if (!isRuntimeTool(toolId)) {
    throw new ToolInputError(`Tool "${toolId}" is not available in the A2A runtime.`);
  }

  switch (toolId) {
    case "base64-encode":
      return { text: Buffer.from(requireText(input), "utf8").toString("base64") };
    case "base64-decode": {
      const text = requireText(input).trim();
      if (!/^[A-Za-z0-9+/]*={0,2}$/.test(text) || text.length % 4 !== 0) {
        throw new ToolInputError("Input must be a valid Base64 string.");
      }
      return { text: Buffer.from(text, "base64").toString("utf8") };
    }
    case "md5-generator":
      return { text: crypto.createHash("md5").update(requireText(input)).digest("hex") };
    case "sha1-generator":
      return { text: crypto.createHash("sha1").update(requireText(input)).digest("hex") };
    case "sha256-generator":
      return { text: crypto.createHash("sha256").update(requireText(input)).digest("hex") };
    case "sha384-generator":
      return { text: crypto.createHash("sha384").update(requireText(input)).digest("hex") };
    case "sha512-generator":
      return { text: crypto.createHash("sha512").update(requireText(input)).digest("hex") };
    case "password-generator":
      return { text: makePassword(options), data: { generated: true } };
    case "hex-to-decimal":
      return { text: parseInteger(input, "Input", 16).toString(10) };
    case "decimal-to-hex":
      return { text: integerToBase(parseInteger(input, "Input", 10), 16) };
    case "octal-to-decimal":
      return { text: parseInteger(input, "Input", 8).toString(10) };
    case "decimal-to-octal":
      return { text: integerToBase(parseInteger(input, "Input", 10), 8) };
    case "binary-to-decimal":
      return { text: parseInteger(input, "Input", 2).toString(10) };
    case "decimal-to-binary":
      return { text: integerToBase(parseInteger(input, "Input", 10), 2) };
    case "binary-to-hex":
      return { text: integerToBase(parseInteger(input, "Input", 2), 16) };
    case "hex-to-binary":
      return { text: integerToBase(parseInteger(input, "Input", 16), 2) };
    case "ascii-to-hex":
      return { text: (Buffer.from(requireText(input), "utf8").toString("hex").match(/.{1,2}/g) || []).join(" ") };
    case "hex-to-ascii": {
      const hex = requireText(input).replace(/\s+/g, "");
      if (!/^(?:[0-9a-f]{2})+$/i.test(hex)) {
        throw new ToolInputError("Input must contain complete hexadecimal byte pairs.");
      }
      return { text: Buffer.from(hex, "hex").toString("utf8") };
    }
    case "binary-to-text": {
      const bits = requireText(input).trim().split(/\s+/).filter(Boolean);
      if (!bits.length || bits.some((byte) => !/^[01]{8}$/.test(byte))) {
        throw new ToolInputError("Input must contain 8-bit binary bytes separated by whitespace.");
      }
      return { text: Buffer.from(bits.map((byte) => parseInt(byte, 2))).toString("utf8") };
    }
    case "text-to-binary":
      return { text: Array.from(Buffer.from(requireText(input), "utf8")).map((byte) => byte.toString(2).padStart(8, "0")).join(" ") };
    case "fraction-to-decimal": {
      const fraction = parseFraction(input);
      return { text: String(fraction.numerator / fraction.denominator) };
    }
    case "decimal-to-fraction":
      return { text: decimalToFractionValue(input) };
    case "percent-to-decimal":
      return { text: String(parseFiniteNumber(input, "Input") / 100) };
    case "decimal-to-percent":
      return { text: `${parseFiniteNumber(input, "Input") * 100}%` };
    case "percent-to-fraction":
      return { text: decimalToFractionValue(parseFiniteNumber(input, "Input") / 100) };
    case "fraction-to-percent": {
      const fraction = parseFraction(input);
      return { text: `${(fraction.numerator / fraction.denominator) * 100}%` };
    }
    case "hex-to-rgb": {
      const rgb = hexToRgbObject(input);
      return { text: `rgb(${rgb.r}, ${rgb.g}, ${rgb.b})`, data: { r: rgb.r, g: rgb.g, b: rgb.b } };
    }
    case "hex-to-rgba": {
      const rgb = hexToRgbObject(input);
      const alpha = options.alpha !== undefined ? alphaChannel(options.alpha) : rgb.a;
      return { text: `rgba(${rgb.r}, ${rgb.g}, ${rgb.b}, ${alpha})`, data: { r: rgb.r, g: rgb.g, b: rgb.b, a: alpha } };
    }
    case "rgb-to-hex":
      return { text: rgbToHexValue(input, false) };
    case "rgba-to-hex":
      return { text: rgbToHexValue(input, true) };
    case "roman-numerals-to-numbers":
      return { text: romanToNumber(input) };
    case "numbers-to-roman-numerals":
      return { text: numberToRoman(input) };
    case "json-formatter":
      return { text: formatJson(input, options) };
    case "json-minifier":
      return { text: minifyJson(input) };
    case "reverse-text":
      return { text: Array.from(requireText(input)).reverse().join("") };
    case "case-converter": {
      const text = requireText(input);
      const mode = String(options.mode || "all").toLowerCase();
      const conversions = {
        uppercase: text.toUpperCase(),
        lowercase: text.toLowerCase(),
        title: titleCase(text),
        sentence: sentenceCase(text),
        inverted: invertCase(text)
      };
      return mode === "all"
        ? { text: JSON.stringify(conversions, null, 2), data: conversions }
        : { text: conversions[mode] || conversions.uppercase, data: { mode, result: conversions[mode] || conversions.uppercase } };
    }
    case "word-counter": {
      const text = requireText(input);
      const data = {
        words: countWords(text),
        characters: Array.from(text).length,
        charactersNoSpaces: Array.from(text.replace(/\s/g, "")).length,
        lines: text ? text.split(/\r\n|\r|\n/).length : 0,
        sentences: countSentences(text),
        paragraphs: countParagraphs(text)
      };
      return { text: JSON.stringify(data, null, 2), data };
    }
    case "character-count": {
      const text = requireText(input);
      const data = {
        characters: Array.from(text).length,
        charactersNoSpaces: Array.from(text.replace(/\s/g, "")).length,
        bytesUtf8: Buffer.byteLength(text, "utf8"),
        words: countWords(text),
        lines: text ? text.split(/\r\n|\r|\n/).length : 0
      };
      return { text: JSON.stringify(data, null, 2), data };
    }
    default:
      throw new ToolInputError(`Tool "${toolId}" is not implemented.`);
  }
}

module.exports = {
  ToolInputError,
  supportedToolIds,
  executeTool
};
