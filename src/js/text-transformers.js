/* Shared semantics-safe text transformations for browser and Node runtimes. */
(function (root, factory) {
  if (typeof module === "object" && module.exports) {
    module.exports = factory();
  } else {
    root.CodingToolsTextTransforms = factory();
  }
})(typeof window !== "undefined" ? window : globalThis, function () {
  "use strict";

  var REGEX_PREFIX_KEYWORDS = {
    await: true,
    case: true,
    delete: true,
    in: true,
    instanceof: true,
    new: true,
    of: true,
    return: true,
    throw: true,
    typeof: true,
    void: true,
    yield: true
  };

  function requireString(value, label) {
    if (typeof value !== "string") {
      throw new TypeError((label || "Input") + " must be a string.");
    }
    return value;
  }

  function isIdentifierStart(character) {
    return /[A-Za-z_$]/.test(character);
  }

  function isIdentifierPart(character) {
    return /[A-Za-z0-9_$]/.test(character);
  }

  function isHorizontalWhitespace(character) {
    return character === " " || character === "\t" || character === "\v" || character === "\f" || character === "\u00a0";
  }

  function isLineBreak(character) {
    return character === "\n" || character === "\r" || character === "\u2028" || character === "\u2029";
  }

  function consumeQuoted(source, start, quote, label) {
    var output = quote;
    for (var index = start + 1; index < source.length; index += 1) {
      var character = source.charAt(index);
      output += character;
      if (character === "\\") {
        if (index + 1 >= source.length) break;
        output += source.charAt(index + 1);
        index += 1;
      } else if (character === quote) {
        return { output: output, end: index };
      } else if (isLineBreak(character) && quote !== "`") {
        throw new SyntaxError("Unterminated " + label + " string literal.");
      }
    }
    throw new SyntaxError("Unterminated " + label + " string literal.");
  }

  function consumeRegexLiteral(source, start) {
    var output = "/";
    var inClass = false;
    for (var index = start + 1; index < source.length; index += 1) {
      var character = source.charAt(index);
      output += character;
      if (character === "\\") {
        if (index + 1 >= source.length) break;
        output += source.charAt(index + 1);
        index += 1;
        continue;
      }
      if (isLineBreak(character)) {
        throw new SyntaxError("Unterminated JavaScript regular expression literal.");
      }
      if (character === "[") {
        inClass = true;
      } else if (character === "]") {
        inClass = false;
      } else if (character === "/" && !inClass) {
        while (index + 1 < source.length && /[A-Za-z]/.test(source.charAt(index + 1))) {
          output += source.charAt(index + 1);
          index += 1;
        }
        return { output: output, end: index };
      }
    }
    throw new SyntaxError("Unterminated JavaScript regular expression literal.");
  }

  function consumeTemplateLiteral(source, start) {
    var output = "`";
    var expressionDepth = 0;
    var regexAllowed = true;

    for (var index = start + 1; index < source.length; index += 1) {
      var character = source.charAt(index);
      var next = source.charAt(index + 1);

      if (character === "\\") {
        output += character;
        if (index + 1 < source.length) {
          output += next;
          index += 1;
        }
        continue;
      }

      if (expressionDepth === 0) {
        output += character;
        if (character === "`") return { output: output, end: index };
        if (character === "$" && next === "{") {
          output += next;
          index += 1;
          expressionDepth = 1;
          regexAllowed = true;
        }
        continue;
      }

      if (character === "'" || character === '"') {
        var quoted = consumeQuoted(source, index, character, "JavaScript");
        output += quoted.output;
        index = quoted.end;
        regexAllowed = false;
        continue;
      }

      if (character === "`") {
        var nestedTemplate = consumeTemplateLiteral(source, index);
        output += nestedTemplate.output;
        index = nestedTemplate.end;
        regexAllowed = false;
        continue;
      }

      if (character === "/" && next === "/") {
        var lineEnd = index + 2;
        while (lineEnd < source.length && !isLineBreak(source.charAt(lineEnd))) lineEnd += 1;
        output += source.slice(index, lineEnd);
        index = lineEnd - 1;
        continue;
      }

      if (character === "/" && next === "*") {
        var commentEnd = source.indexOf("*/", index + 2);
        if (commentEnd < 0) throw new SyntaxError("Unterminated JavaScript block comment.");
        output += source.slice(index, commentEnd + 2);
        index = commentEnd + 1;
        continue;
      }

      if (character === "/" && regexAllowed) {
        var regex = consumeRegexLiteral(source, index);
        output += regex.output;
        index = regex.end;
        regexAllowed = false;
        continue;
      }

      output += character;
      if (character === "{") {
        expressionDepth += 1;
        regexAllowed = true;
      } else if (character === "}") {
        expressionDepth -= 1;
        regexAllowed = false;
      } else if (!/\s/.test(character)) {
        regexAllowed = /[({[=,:;!?&|+\-*%~^<>]/.test(character);
      }
    }

    throw new SyntaxError("Unterminated JavaScript template literal.");
  }

  function appendJavaScriptWhitespace(output, whitespace) {
    if (/[\r\n\u2028\u2029]/.test(whitespace)) {
      output = output.replace(/[ \t\v\f\u00a0]+$/, "");
      if (!/[\r\n\u2028\u2029]$/.test(output)) output += "\n";
      return output;
    }
    if (output && !/\s$/.test(output)) output += " ";
    return output;
  }

  function minifyJavaScript(value) {
    var source = requireString(value, "JavaScript input");
    var output = "";
    var regexAllowed = true;

    for (var index = 0; index < source.length; index += 1) {
      var character = source.charAt(index);
      var next = source.charAt(index + 1);

      if (character === "'" || character === '"') {
        var quoted = consumeQuoted(source, index, character, "JavaScript");
        output += quoted.output;
        index = quoted.end;
        regexAllowed = false;
        continue;
      }

      if (character === "`") {
        var template = consumeTemplateLiteral(source, index);
        output += template.output;
        index = template.end;
        regexAllowed = false;
        continue;
      }

      if (character === "/" && next === "/") {
        index += 2;
        while (index < source.length && !isLineBreak(source.charAt(index))) index += 1;
        if (index < source.length) {
          output = appendJavaScriptWhitespace(output, source.charAt(index));
          if (source.charAt(index) === "\r" && source.charAt(index + 1) === "\n") index += 1;
        } else {
          index -= 1;
        }
        continue;
      }

      if (character === "/" && next === "*") {
        var blockEnd = source.indexOf("*/", index + 2);
        if (blockEnd < 0) throw new SyntaxError("Unterminated JavaScript block comment.");
        var block = source.slice(index, blockEnd + 2);
        output = appendJavaScriptWhitespace(output, /[\r\n\u2028\u2029]/.test(block) ? "\n" : " ");
        index = blockEnd + 1;
        continue;
      }

      if (character === "/" && regexAllowed) {
        var regex = consumeRegexLiteral(source, index);
        output += regex.output;
        index = regex.end;
        regexAllowed = false;
        continue;
      }

      if (/\s/.test(character)) {
        var whitespaceEnd = index + 1;
        while (whitespaceEnd < source.length && /\s/.test(source.charAt(whitespaceEnd))) whitespaceEnd += 1;
        output = appendJavaScriptWhitespace(output, source.slice(index, whitespaceEnd));
        index = whitespaceEnd - 1;
        continue;
      }

      if (isIdentifierStart(character)) {
        var identifierEnd = index + 1;
        while (identifierEnd < source.length && isIdentifierPart(source.charAt(identifierEnd))) identifierEnd += 1;
        var identifier = source.slice(index, identifierEnd);
        output += identifier;
        regexAllowed = Boolean(REGEX_PREFIX_KEYWORDS[identifier]);
        index = identifierEnd - 1;
        continue;
      }

      if (/[0-9]/.test(character)) {
        var numberEnd = index + 1;
        while (numberEnd < source.length && /[A-Za-z0-9_.]/.test(source.charAt(numberEnd))) numberEnd += 1;
        output += source.slice(index, numberEnd);
        regexAllowed = false;
        index = numberEnd - 1;
        continue;
      }

      output += character;
      regexAllowed = /[({[=,:;!?&|+\-*%~^<>]/.test(character);
    }

    return output.trim();
  }

  function minifyCss(value) {
    var source = requireString(value, "CSS input");
    var output = "";
    var pendingSpace = false;
    var compactPunctuation = "{}:;,";

    for (var index = 0; index < source.length; index += 1) {
      var character = source.charAt(index);
      var next = source.charAt(index + 1);

      if (character === "'" || character === '"') {
        if (pendingSpace && output && compactPunctuation.indexOf(output.charAt(output.length - 1)) < 0) output += " ";
        pendingSpace = false;
        var quoted = consumeQuoted(source, index, character, "CSS");
        output += quoted.output;
        index = quoted.end;
        continue;
      }

      if (character === "/" && next === "*") {
        var blockEnd = source.indexOf("*/", index + 2);
        if (blockEnd < 0) throw new SyntaxError("Unterminated CSS comment.");
        pendingSpace = true;
        index = blockEnd + 1;
        continue;
      }

      if (/\s/.test(character)) {
        pendingSpace = true;
        continue;
      }

      if (compactPunctuation.indexOf(character) >= 0) {
        output = output.replace(/\s+$/, "");
        output += character;
        pendingSpace = false;
        continue;
      }

      if (pendingSpace && output && compactPunctuation.indexOf(output.charAt(output.length - 1)) < 0) output += " ";
      pendingSpace = false;
      output += character;
    }

    return output.trim().replace(/;}$/, "}");
  }

  function consumeSqlQuoted(source, start, closer, label) {
    var opener = source.charAt(start);
    var output = opener;
    for (var index = start + 1; index < source.length; index += 1) {
      var character = source.charAt(index);
      output += character;
      if (character === "\\" && closer !== "]" && index + 1 < source.length) {
        output += source.charAt(index + 1);
        index += 1;
      } else if (character === closer) {
        if (source.charAt(index + 1) === closer) {
          output += source.charAt(index + 1);
          index += 1;
        } else {
          return { output: output, end: index };
        }
      }
    }
    throw new SyntaxError("Unterminated SQL " + label + ".");
  }

  function minifySql(value) {
    var source = requireString(value, "SQL input");
    var output = "";
    var pendingSpace = false;

    function flushSpace() {
      if (pendingSpace && output && !/\s$/.test(output)) output += " ";
      pendingSpace = false;
    }

    for (var index = 0; index < source.length; index += 1) {
      var character = source.charAt(index);
      var next = source.charAt(index + 1);

      if (character === "'" || character === '"' || character === "`") {
        flushSpace();
        var quoted = consumeSqlQuoted(source, index, character, "quoted value");
        output += quoted.output;
        index = quoted.end;
        continue;
      }

      if (character === "[") {
        flushSpace();
        var bracketed = consumeSqlQuoted(source, index, "]", "bracket identifier");
        output += bracketed.output;
        index = bracketed.end;
        continue;
      }

      if (character === "$") {
        var dollarMatch = source.slice(index).match(/^(\$[A-Za-z_][A-Za-z0-9_]*\$|\$\$)/);
        if (dollarMatch) {
          flushSpace();
          var delimiter = dollarMatch[1];
          var dollarEnd = source.indexOf(delimiter, index + delimiter.length);
          if (dollarEnd < 0) throw new SyntaxError("Unterminated SQL dollar-quoted string.");
          output += source.slice(index, dollarEnd + delimiter.length);
          index = dollarEnd + delimiter.length - 1;
          continue;
        }
      }

      if (character === "-" && next === "-") {
        index += 2;
        while (index < source.length && !isLineBreak(source.charAt(index))) index += 1;
        if (source.charAt(index) === "\r" && source.charAt(index + 1) === "\n") index += 1;
        pendingSpace = true;
        continue;
      }

      if (character === "/" && next === "*") {
        var depth = 1;
        index += 2;
        while (index < source.length && depth > 0) {
          if (source.charAt(index) === "/" && source.charAt(index + 1) === "*") {
            depth += 1;
            index += 2;
          } else if (source.charAt(index) === "*" && source.charAt(index + 1) === "/") {
            depth -= 1;
            index += 2;
          } else {
            index += 1;
          }
        }
        if (depth > 0) throw new SyntaxError("Unterminated SQL block comment.");
        index -= 1;
        pendingSpace = true;
        continue;
      }

      if (/\s/.test(character)) {
        pendingSpace = true;
        continue;
      }

      flushSpace();
      output += character;
    }

    return output.trim();
  }

  function findMarkupEnd(source, start, declaration) {
    var quote = "";
    var bracketDepth = 0;
    for (var index = start; index < source.length; index += 1) {
      var character = source.charAt(index);
      if (quote) {
        if (character === quote) quote = "";
        continue;
      }
      if (character === "'" || character === '"') {
        quote = character;
      } else if (declaration && character === "[") {
        bracketDepth += 1;
      } else if (declaration && character === "]" && bracketDepth > 0) {
        bracketDepth -= 1;
      } else if (character === ">" && bracketDepth === 0) {
        return index;
      }
    }
    throw new SyntaxError("Unterminated markup tag or declaration.");
  }

  function normalizeMarkupTag(tag) {
    var output = "";
    var quote = "";
    var pendingSpace = false;
    for (var index = 0; index < tag.length; index += 1) {
      var character = tag.charAt(index);
      if (quote) {
        output += character;
        if (character === quote) quote = "";
        continue;
      }
      if (character === "'" || character === '"') {
        if (pendingSpace && output && output.charAt(output.length - 1) !== "<") output += " ";
        pendingSpace = false;
        quote = character;
        output += character;
      } else if (/\s/.test(character)) {
        pendingSpace = true;
      } else {
        if (pendingSpace && output && output.charAt(output.length - 1) !== "<" && character !== ">" && !(character === "/" && tag.charAt(index + 1) === ">")) {
          output += " ";
        }
        pendingSpace = false;
        output += character;
      }
    }
    if (quote) throw new SyntaxError("Unterminated markup attribute value.");
    return output;
  }

  function markupTagDetails(tag) {
    var inner = tag.slice(1, -1).trim();
    var closing = inner.charAt(0) === "/";
    if (closing) inner = inner.slice(1).trim();
    var selfClosing = !closing && /\/$/.test(inner);
    if (selfClosing) inner = inner.slice(0, -1).trim();
    var match = inner.match(/^([^\s/>]+)/);
    if (!match) throw new SyntaxError("Markup tag is missing a name.");
    return { name: match[1], closing: closing, selfClosing: selfClosing };
  }

  function minifyMarkup(value, xmlMode) {
    var source = requireString(value, xmlMode ? "XML input" : "HTML input");
    var output = "";
    var stack = [];
    var rootCount = 0;
    var lowerSource = xmlMode ? "" : source.toLowerCase();

    for (var index = 0; index < source.length;) {
      if (source.charAt(index) !== "<") {
        var textEnd = source.indexOf("<", index);
        if (textEnd < 0) textEnd = source.length;
        var text = source.slice(index, textEnd);
        if (xmlMode && stack.length === 0 && text.trim()) {
          throw new SyntaxError("XML input must have one root element.");
        }
        output += text;
        index = textEnd;
        continue;
      }

      if (source.slice(index, index + 4) === "<!--") {
        var commentEnd = source.indexOf("-->", index + 4);
        if (commentEnd < 0) throw new SyntaxError("Unterminated markup comment.");
        index = commentEnd + 3;
        continue;
      }

      if (source.slice(index, index + 9) === "<![CDATA[") {
        var cdataEnd = source.indexOf("]]>", index + 9);
        if (cdataEnd < 0) throw new SyntaxError("Unterminated XML CDATA section.");
        if (xmlMode && stack.length === 0) throw new SyntaxError("CDATA must be inside the XML root element.");
        output += source.slice(index, cdataEnd + 3);
        index = cdataEnd + 3;
        continue;
      }

      if (source.slice(index, index + 2) === "<?") {
        var processingEnd = source.indexOf("?>", index + 2);
        if (processingEnd < 0) throw new SyntaxError("Unterminated XML processing instruction.");
        output += source.slice(index, processingEnd + 2);
        index = processingEnd + 2;
        continue;
      }

      if (source.slice(index, index + 2) === "<!") {
        var declarationEnd = findMarkupEnd(source, index + 2, true);
        output += source.slice(index, declarationEnd + 1);
        index = declarationEnd + 1;
        continue;
      }

      var tagEnd = findMarkupEnd(source, index + 1, false);
      var rawTag = source.slice(index, tagEnd + 1);
      var details = markupTagDetails(rawTag);
      output += normalizeMarkupTag(rawTag);

      if (xmlMode) {
        if (details.closing) {
          var expected = stack.pop();
          if (!expected || expected !== details.name) {
            throw new SyntaxError("Expected </" + (expected || "none") + "> before </" + details.name + ">.");
          }
        } else {
          if (stack.length === 0) {
            rootCount += 1;
            if (rootCount > 1) throw new SyntaxError("XML input must have one root element.");
          }
          if (!details.selfClosing) stack.push(details.name);
        }
      }

      index = tagEnd + 1;

      if (!xmlMode && !details.closing && !details.selfClosing && (details.name.toLowerCase() === "script" || details.name.toLowerCase() === "style")) {
        var closingNeedle = "</" + details.name.toLowerCase();
        var rawEnd = lowerSource.indexOf(closingNeedle, index);
        if (rawEnd < 0) throw new SyntaxError("Unterminated HTML " + details.name.toLowerCase() + " element.");
        output += source.slice(index, rawEnd);
        index = rawEnd;
      }
    }

    if (xmlMode) {
      if (stack.length) throw new SyntaxError("Expected </" + stack[stack.length - 1] + "> before end of input.");
      if (rootCount !== 1) throw new SyntaxError("XML input must have one root element.");
    }

    return output;
  }

  function minifyHtml(value) {
    return minifyMarkup(value, false);
  }

  function minifyXml(value) {
    return minifyMarkup(value, true);
  }

  return {
    minifyJavaScript: minifyJavaScript,
    minifyCss: minifyCss,
    minifySql: minifySql,
    minifyHtml: minifyHtml,
    minifyXml: minifyXml
  };
});
