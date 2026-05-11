const supportedToolIds = [
  "base64-encode",
  "base64-decode",
  "md5-generator",
  "sha1-generator",
  "sha256-generator",
  "sha384-generator",
  "sha512-generator",
  "password-generator",
  "hex-to-decimal",
  "decimal-to-hex",
  "octal-to-decimal",
  "decimal-to-octal",
  "binary-to-decimal",
  "decimal-to-binary",
  "binary-to-hex",
  "hex-to-binary",
  "ascii-to-hex",
  "hex-to-ascii",
  "binary-to-text",
  "text-to-binary",
  "fraction-to-decimal",
  "decimal-to-fraction",
  "percent-to-decimal",
  "decimal-to-percent",
  "percent-to-fraction",
  "fraction-to-percent",
  "hex-to-rgb",
  "rgb-to-hex",
  "hex-to-rgba",
  "rgba-to-hex",
  "roman-numerals-to-numbers",
  "numbers-to-roman-numerals",
  "json-formatter",
  "json-minifier",
  "reverse-text",
  "case-converter",
  "word-counter",
  "character-count"
];

const supportedToolIdSet = new Set(supportedToolIds);

function isRuntimeTool(toolId) {
  return supportedToolIdSet.has(toolId);
}

module.exports = {
  supportedToolIds,
  isRuntimeTool
};
