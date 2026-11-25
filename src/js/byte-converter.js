/* Shared by the single and batch byte converters. */
(function (root) {
  'use strict';

  function fail(code, position, missing) {
    var error = new Error(code);
    error.code = code;
    error.position = position;
    error.missing = missing;
    throw error;
  }

  function readBytes(text, binary) {
    var width = binary ? 8 : 2;
    var radix = binary ? 2 : 16;
    var separator = binary ? /\s/ : /[\s,:-]/;
    var digit = binary ? /^[01]$/ : /^[0-9A-Fa-f]$/;
    var bytes = [];
    var size = 0;
    var value = 0;
    var prefixStart = -1;
    for (var i = 0; i < text.length; i++) {
      var char = text[i];
      if (separator.test(char)) {
        if (prefixStart !== -1) fail('prefix', prefixStart + 1);
        continue;
      }
      if (!binary && char === '0' && /[xX]/.test(text.charAt(i + 1))) {
        if (size || prefixStart !== -1) fail('prefix', i + 1);
        prefixStart = i++;
        continue;
      }
      if (!digit.test(char)) fail(binary ? 'binaryDigit' : 'hexDigit', i + 1);
      prefixStart = -1;
      value = value * radix + parseInt(char, radix);
      if (++size === width) {
        bytes.push(value);
        value = 0;
        size = 0;
      }
    }
    if (prefixStart !== -1) fail('prefix', prefixStart + 1);
    if (size) fail(binary ? 'binaryLength' : 'hexLength', bytes.length + 1, width - size);
    if (!bytes.length) fail('empty');
    return Uint8Array.from(bytes);
  }

  // Called only on a decoding error. Locate a bad continuation, invalid lead or
  // truncated sequence without allocating a second decoded string.
  function invalidUtf8Byte(bytes) {
    for (var i = 0; i < bytes.length; i++) {
      var lead = bytes[i];
      if (lead < 0x80) continue;
      if (lead < 0xc2 || lead > 0xf4) return i + 1;
      var start = i;
      var count = lead < 0xe0 ? 1 : lead < 0xf0 ? 2 : 3;
      for (var n = 0; n < count; n++) {
        if (++i >= bytes.length) return start + 1;
        var low = 0x80;
        var high = 0xbf;
        if (n === 0) {
          if (lead === 0xe0) low = 0xa0;
          if (lead === 0xed) high = 0x9f;
          if (lead === 0xf0) low = 0x90;
          if (lead === 0xf4) high = 0x8f;
        }
        if (bytes[i] < low || bytes[i] > high) return i + 1;
      }
    }
  }

  function convert(tool, text, mode, delimiter) {
    if (tool === 'ascii-to-hex') {
      if (!text.length) fail('empty');
      var codes;
      if (mode === 'utf8') {
        // TextEncoder silently replaces an unpaired UTF-16 surrogate.
        var unpaired = /[\uD800-\uDFFF]/u.exec(text);
        if (unpaired) fail('unicode', unpaired.index + 1);
        codes = new TextEncoder().encode(text);
      } else {
        codes = Array.from({ length: text.length }, function (_, index) { return text.charCodeAt(index); });
      }
      var parts = Array.from(codes, function (code) { return code.toString(16).toUpperCase().padStart(2, '0'); });
      return { text: parts.join(delimiter), count: codes.length };
    }
    var bytes = readBytes(text, tool === 'binary-to-text');
    var output = '';
    if (mode === 'utf8') {
      try {
        output = new TextDecoder('utf-8', { fatal: true }).decode(bytes);
      } catch (error) {
        fail('utf8', invalidUtf8Byte(bytes));
      }
    } else {
      for (var i = 0; i < bytes.length; i += 8192) {
        output += String.fromCharCode.apply(null, bytes.subarray(i, i + 8192));
      }
    }
    return { text: output, count: bytes.length };
  }

  function explain(error, messages) {
    if (!messages[error.code]) return error.message;
    return messages[error.code].replace('{position}', error.position).replace('{missing}', error.missing);
  }

  var api = { convert: convert, explain: explain };
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.CodingToolsByteConverter = api;
})(typeof window === 'undefined' ? globalThis : window);
