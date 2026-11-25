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
    var controlHeader = false;
    var parentheses = [];
    var previousToken = "";

    for (var index = 0; index < source.length; index += 1) {
      var character = source.charAt(index);
      var next = source.charAt(index + 1);

      if (character === "'" || character === '"') {
        var quoted = consumeQuoted(source, index, character, "JavaScript");
        output += quoted.output;
        index = quoted.end;
        regexAllowed = false;
        previousToken = "literal";
        continue;
      }

      if (character === "`") {
        var template = consumeTemplateLiteral(source, index);
        output += template.output;
        index = template.end;
        regexAllowed = false;
        previousToken = "literal";
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
        previousToken = "literal";
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
        controlHeader = previousToken !== "." && /^(if|while|for|with|switch|catch)$/.test(identifier);
        regexAllowed = previousToken !== "." && Object.hasOwn(REGEX_PREFIX_KEYWORDS, identifier);
        previousToken = identifier;
        index = identifierEnd - 1;
        continue;
      }

      if (/[0-9]/.test(character)) {
        var numberEnd = index + 1;
        while (numberEnd < source.length && /[A-Za-z0-9_.]/.test(source.charAt(numberEnd))) numberEnd += 1;
        output += source.slice(index, numberEnd);
        regexAllowed = false;
        previousToken = "literal";
        index = numberEnd - 1;
        continue;
      }

      output += character;
      if (character === "(") parentheses.push(controlHeader);
      regexAllowed = character === ")" ? parentheses.pop() : /[({[=,:;!?&|+\-*%~^<>]/.test(character);
      controlHeader = false;
      previousToken = character;
    }

    return output.trim();
  }

  function minifyCss(value) {
    var source = requireString(value, "CSS input");
    var output = "";
    var pendingSpace = false;
    // A space before a colon can be a descendant combinator (div :hover).
    var compactPunctuation = "{};,";

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
        // A comment separates tokens without creating a descendant combinator.
        // Keep an empty separator when otherwise adjacent tokens would touch.
        if (!pendingSpace && output && blockEnd + 2 < source.length && !/\s/.test(source.charAt(blockEnd + 2))) {
          output += "/**/";
        }
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

      if (pendingSpace && output && (compactPunctuation + ":").indexOf(output.charAt(output.length - 1)) < 0) output += " ";
      pendingSpace = false;
      output += character;
    }

    return output.trim().replace(/;}$/, "}");
  }

  function consumeSqlQuoted(source, start, closer, label, backslashEscapes) {
    var opener = source.charAt(start);
    var output = opener;
    for (var index = start + 1; index < source.length; index += 1) {
      var character = source.charAt(index);
      output += character;
      if (backslashEscapes && character === "\\" && index + 1 < source.length) {
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

  function minifySql(value, dialect) {
    var source = requireString(value, "SQL input");
    var output = "";
    var pendingSpace = false;
    var mysql = dialect === "mysql";

    function flushSpace() {
      if (pendingSpace && output && !/\s$/.test(output)) output += " ";
      pendingSpace = false;
    }

    for (var index = 0; index < source.length; index += 1) {
      var character = source.charAt(index);
      var next = source.charAt(index + 1);

      if (character === "'" || character === '"' || character === "`") {
        flushSpace();
        var quoted = consumeSqlQuoted(source, index, character, "quoted value", mysql);
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

      if (!mysql && dialect !== "sqlite" && character === "$") {
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

      var dashComment = character === "-" && next === "-" && (!mysql || /[\x00-\x20\x7f]/.test(source.charAt(index + 2)));
      if (dashComment || (mysql && character === "#")) {
        index += dashComment ? 2 : 1;
        while (index < source.length && !isLineBreak(source.charAt(index))) index += 1;
        if (source.charAt(index) === "\r" && source.charAt(index + 1) === "\n") index += 1;
        pendingSpace = true;
        continue;
      }

      if (character === "/" && next === "*") {
        if (mysql || dialect === "sqlite") {
          var commentEnd = source.indexOf("*/", index + 2);
          if (commentEnd < 0) throw new SyntaxError("Unterminated SQL block comment.");
          if (mysql && (source.charAt(index + 2) === "!" || source.charAt(index + 2) === "+")) {
            flushSpace();
            output += source.slice(index, commentEnd + 2);
          }
          index = commentEnd + 1;
          pendingSpace = true;
          continue;
        }
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

  function minifyMarkup(value, xmlMode, layout) {
    var source = requireString(value, xmlMode ? "XML input" : "HTML input");
    var output = "";
    var stack = [];
    var rootCount = 0;

    function append(value, markup) {
      if (xmlMode && stack.length) stack[stack.length - 1].children.push({ value: value, markup: markup });
      else output += value;
    }

    function finishElement(frame, closing) {
      var children = frame.children;
      var changeIndent = layout && !frame.preserve && children.some(function (child) { return child.markup; })
        && children.every(function (child) {
          // Inline spaces and mixed text may separate words and must survive.
          return child.markup || (/^[\x20\t\r\n]+$/.test(child.value) && /[\r\n]/.test(child.value));
        });
      var indent = changeIndent && layout === "format" ? "\n" + "  ".repeat(stack.length) : "";
      var parts = children.map(function (child) {
        if (!changeIndent) return child.value;
        if (!child.markup) return "";
        return (indent ? indent + "  " : "") + child.value;
      });
      append(frame.start + parts.join("") + indent + closing, true);
    }

    for (var index = 0; index < source.length;) {
      if (source.charAt(index) !== "<") {
        var textEnd = source.indexOf("<", index);
        if (textEnd < 0) textEnd = source.length;
        var text = source.slice(index, textEnd);
        if (xmlMode && stack.length === 0 && text.trim()) {
          throw new SyntaxError("XML input must have one root element.");
        }
        append(text, false);
        index = textEnd;
        continue;
      }

      if (source.slice(index, index + 4) === "<!--") {
        var commentEnd = source.indexOf("-->", index + 4);
        if (commentEnd < 0) throw new SyntaxError("Unterminated markup comment.");
        if (layout === "format") append(source.slice(index, commentEnd + 3), true);
        index = commentEnd + 3;
        continue;
      }

      if (source.slice(index, index + 9) === "<![CDATA[") {
        var cdataEnd = source.indexOf("]]>", index + 9);
        if (cdataEnd < 0) throw new SyntaxError("Unterminated XML CDATA section.");
        if (xmlMode && stack.length === 0) throw new SyntaxError("CDATA must be inside the XML root element.");
        append(source.slice(index, cdataEnd + 3), false);
        index = cdataEnd + 3;
        continue;
      }

      if (source.slice(index, index + 2) === "<?") {
        var processingEnd = source.indexOf("?>", index + 2);
        if (processingEnd < 0) throw new SyntaxError("Unterminated XML processing instruction.");
        append(source.slice(index, processingEnd + 2), true);
        index = processingEnd + 2;
        continue;
      }

      if (source.slice(index, index + 2) === "<!") {
        var declarationEnd = findMarkupEnd(source, index + 2, true);
        append(source.slice(index, declarationEnd + 1), true);
        index = declarationEnd + 1;
        continue;
      }

      var tagEnd = findMarkupEnd(source, index + 1, false);
      var rawTag = source.slice(index, tagEnd + 1);
      var details = markupTagDetails(rawTag);
      var tag = layout === "format" ? rawTag : normalizeMarkupTag(rawTag);

      if (xmlMode) {
        if (details.closing) {
          var expected = stack.pop();
          if (!expected || expected.name !== details.name) {
            throw new SyntaxError("Expected </" + (expected ? expected.name : "none") + "> before </" + details.name + ">.");
          }
          finishElement(expected, tag);
        } else {
          if (stack.length === 0) {
            rootCount += 1;
            if (rootCount > 1) throw new SyntaxError("XML input must have one root element.");
          }
          if (details.selfClosing) {
            append(tag, true);
          } else {
            var preserve = stack.length > 0 && stack[stack.length - 1].preserve;
            if (layout && rawTag.indexOf("xml:space") >= 0) {
              var space = parseXmlTag(rawTag).attributes.find(function (attribute) { return attribute.name === "xml:space"; });
              if (space) preserve = space.value === "preserve";
            }
            stack.push({ start: tag, name: details.name, preserve: preserve, children: [] });
          }
        }
      } else append(tag, true);

      index = tagEnd + 1;

      if (!xmlMode && !details.closing && /^(script|style|textarea|title|xmp|iframe|noembed|noframes)$/i.test(details.name)) {
        var closingTag = new RegExp("</" + details.name + "(?=[\\s/>])", "ig");
        closingTag.lastIndex = index;
        var match = closingTag.exec(source);
        if (!match) throw new SyntaxError("Unterminated HTML " + details.name.toLowerCase() + " element.");
        var rawEnd = match.index;
        output += source.slice(index, rawEnd);
        index = rawEnd;
      }
    }

    if (xmlMode) {
      if (stack.length) throw new SyntaxError("Expected </" + stack[stack.length - 1].name + "> before end of input.");
      if (rootCount !== 1) throw new SyntaxError("XML input must have one root element.");
    }

    return output;
  }

  function minifyHtml(value) {
    return minifyMarkup(value, false);
  }

  function minifyXml(value, removeIndentation) {
    return minifyMarkup(value, true, removeIndentation ? "compact" : "");
  }

  function formatXml(value) {
    return minifyMarkup(value, true, "format");
  }

  var XML_NAME = /^[:_\p{L}][:_\p{L}\p{N}.\-\u00B7\u0300-\u036F\u203F-\u2040]*$/u;
  var XML_ENTITIES = {
    amp: "&",
    apos: "'",
    gt: ">",
    lt: "<",
    quot: '"'
  };

  function assertXmlName(name) {
    var value = String(name);
    if (!XML_NAME.test(value)) {
      throw new SyntaxError('Invalid XML name: "' + value + '".');
    }
    return value;
  }

  function escapeXmlText(value) {
    return String(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }

  function escapeXmlAttribute(value) {
    return escapeXmlText(value)
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&apos;");
  }

  function isXmlCodePoint(codePoint) {
    return codePoint === 0x9 || codePoint === 0xa || codePoint === 0xd ||
      (codePoint >= 0x20 && codePoint <= 0xd7ff) ||
      (codePoint >= 0xe000 && codePoint <= 0xfffd) ||
      (codePoint >= 0x10000 && codePoint <= 0x10ffff);
  }

  function decodeXmlEntity(entity) {
    if (Object.prototype.hasOwnProperty.call(XML_ENTITIES, entity)) return XML_ENTITIES[entity];
    var codePoint;
    if (/^#x[0-9A-Fa-f]+$/.test(entity)) {
      codePoint = parseInt(entity.slice(2), 16);
    } else if (/^#[0-9]+$/.test(entity)) {
      codePoint = parseInt(entity.slice(1), 10);
    } else {
      throw new SyntaxError("Unknown XML entity: &" + entity + ";");
    }
    if (!isXmlCodePoint(codePoint)) {
      throw new SyntaxError("Invalid XML character reference: &" + entity + ";");
    }
    return String.fromCodePoint(codePoint);
  }

  function decodeXmlEntities(value) {
    var output = "";
    var index = 0;
    while (index < value.length) {
      var entityStart = value.indexOf("&", index);
      if (entityStart < 0) return output + value.slice(index);
      output += value.slice(index, entityStart);
      var entityEnd = value.indexOf(";", entityStart + 1);
      if (entityEnd < 0) throw new SyntaxError("Unterminated XML entity reference.");
      var entity = value.slice(entityStart + 1, entityEnd);
      if (!entity) throw new SyntaxError("Empty XML entity reference.");
      output += decodeXmlEntity(entity);
      index = entityEnd + 1;
    }
    return output;
  }

  function skipXmlWhitespace(source, index) {
    while (index < source.length && /\s/.test(source.charAt(index))) index += 1;
    return index;
  }

  function parseXmlTag(rawTag) {
    var inner = rawTag.slice(1, -1);
    var index = 0;
    var closing = false;
    var selfClosing = false;

    if (inner.charAt(index) === "/") {
      closing = true;
      index += 1;
    }
    if (/\s/.test(inner.charAt(index))) throw new SyntaxError("XML tag names cannot be preceded by whitespace.");

    var nameStart = index;
    while (index < inner.length && !/[\s/>]/.test(inner.charAt(index))) index += 1;
    var name = assertXmlName(inner.slice(nameStart, index));

    if (closing) {
      index = skipXmlWhitespace(inner, index);
      if (index !== inner.length) throw new SyntaxError("Closing XML tags cannot contain attributes.");
      return { name: name, closing: true, selfClosing: false, attributes: [] };
    }

    var attributes = [];
    var attributeNames = Object.create(null);
    while (index < inner.length) {
      var beforeWhitespace = index;
      index = skipXmlWhitespace(inner, index);
      if (inner.charAt(index) === "/") {
        index += 1;
        index = skipXmlWhitespace(inner, index);
        if (index !== inner.length) throw new SyntaxError("Unexpected content after an XML self-closing slash.");
        selfClosing = true;
        break;
      }
      if (index >= inner.length) break;
      if (index === beforeWhitespace) throw new SyntaxError("XML attributes must be separated by whitespace.");

      var attributeStart = index;
      while (index < inner.length && !/[\s=/>]/.test(inner.charAt(index))) index += 1;
      var attributeName = assertXmlName(inner.slice(attributeStart, index));
      if (attributeNames[attributeName]) throw new SyntaxError('Duplicate XML attribute: "' + attributeName + '".');
      attributeNames[attributeName] = true;

      index = skipXmlWhitespace(inner, index);
      if (inner.charAt(index) !== "=") throw new SyntaxError('XML attribute "' + attributeName + '" is missing "=".');
      index += 1;
      index = skipXmlWhitespace(inner, index);
      var quote = inner.charAt(index);
      if (quote !== "'" && quote !== '"') throw new SyntaxError('XML attribute "' + attributeName + '" must be quoted.');
      index += 1;
      var valueStart = index;
      while (index < inner.length && inner.charAt(index) !== quote) index += 1;
      if (index >= inner.length) throw new SyntaxError('Unterminated XML attribute "' + attributeName + '".');
      attributes.push({ name: attributeName, value: decodeXmlEntities(inner.slice(valueStart, index)) });
      index += 1;
    }

    return { name: name, closing: false, selfClosing: selfClosing, attributes: attributes };
  }

  function parseXml(value, options) {
    var source = requireString(value, "XML input");
    var settings = options || {};
    var maxDepth = settings.maxDepth === undefined ? 100 : Number(settings.maxDepth);
    if (!Number.isInteger(maxDepth) || maxDepth < 1) throw new TypeError("maxDepth must be a positive integer.");

    var index = source.charCodeAt(0) === 0xfeff ? 1 : 0;
    var stack = [];
    var root = null;
    var declarationSeen = false;

    function appendChild(node) {
      if (!stack.length) {
        if (node.type === "element") {
          if (root) throw new SyntaxError("XML input must have one root element.");
          root = node;
        } else if (node.value.trim()) {
          throw new SyntaxError("XML text must be inside the root element.");
        }
        return;
      }
      var children = stack[stack.length - 1].children;
      var previous = children[children.length - 1];
      if (previous && previous.type !== "element" && node.type !== "element" && previous.type === node.type) {
        previous.value += node.value;
      } else {
        children.push(node);
      }
    }

    while (index < source.length) {
      if (source.charAt(index) !== "<") {
        var textEnd = source.indexOf("<", index);
        if (textEnd < 0) textEnd = source.length;
        appendChild({ type: "text", value: decodeXmlEntities(source.slice(index, textEnd)) });
        index = textEnd;
        continue;
      }

      if (source.slice(index, index + 4) === "<!--") {
        var commentEnd = source.indexOf("-->", index + 4);
        if (commentEnd < 0) throw new SyntaxError("Unterminated XML comment.");
        if (source.slice(index + 4, commentEnd).indexOf("--") >= 0) throw new SyntaxError("XML comments cannot contain --.");
        index = commentEnd + 3;
        continue;
      }

      if (source.slice(index, index + 9) === "<![CDATA[") {
        if (!stack.length) throw new SyntaxError("CDATA must be inside the XML root element.");
        var cdataEnd = source.indexOf("]]>", index + 9);
        if (cdataEnd < 0) throw new SyntaxError("Unterminated XML CDATA section.");
        appendChild({ type: "cdata", value: source.slice(index + 9, cdataEnd) });
        index = cdataEnd + 3;
        continue;
      }

      if (source.slice(index, index + 2) === "<?") {
        var processingEnd = source.indexOf("?>", index + 2);
        if (processingEnd < 0) throw new SyntaxError("Unterminated XML processing instruction.");
        var processing = source.slice(index + 2, processingEnd).trim();
        if (!/^xml(?:\s|$)/i.test(processing) || declarationSeen || root || stack.length) {
          throw new SyntaxError("Processing instructions are not supported.");
        }
        declarationSeen = true;
        index = processingEnd + 2;
        continue;
      }

      if (source.slice(index, index + 9).toUpperCase() === "<!DOCTYPE") {
        throw new SyntaxError("DOCTYPE is not supported.");
      }
      if (source.slice(index, index + 2) === "<!") {
        throw new SyntaxError("Unsupported XML declaration.");
      }

      var tagEnd = findMarkupEnd(source, index + 1, false);
      var tag = parseXmlTag(source.slice(index, tagEnd + 1));
      if (tag.closing) {
        var expected = stack[stack.length - 1];
        if (!expected || expected.name !== tag.name) {
          throw new SyntaxError("Expected </" + (expected ? expected.name : "none") + "> before </" + tag.name + ">.");
        }
        stack.pop();
      } else {
        var node = { type: "element", name: tag.name, attributes: tag.attributes, children: [] };
        appendChild(node);
        if (!tag.selfClosing) {
          stack.push(node);
          if (stack.length > maxDepth) throw new SyntaxError("XML nesting is too deep. Maximum depth is " + maxDepth + ".");
        }
      }
      index = tagEnd + 1;
    }

    if (stack.length) throw new SyntaxError("Expected </" + stack[stack.length - 1].name + "> before end of input.");
    if (!root) throw new SyntaxError("XML input must have one root element.");
    return root;
  }

  function attributesToObject(attributes) {
    var result = {};
    attributes.forEach(function (attribute) {
      result[attribute.name] = attribute.value;
    });
    return result;
  }

  function elementToJson(element, preserve) {
    var attributes = attributesToObject(element.attributes);
    if (attributes["xml:space"]) preserve = attributes["xml:space"] === "preserve";
    var significant = element.children.filter(function (child) {
      return preserve || child.type === "element" || child.type === "cdata" || child.value.trim() !== "";
    });
    var hasElements = significant.some(function (child) { return child.type === "element"; });
    var hasText = significant.some(function (child) { return child.type !== "element"; });

    if (!element.attributes.length && !hasElements) {
      return significant.map(function (child) { return child.value; }).join("");
    }

    var result = {};
    if (element.attributes.length) result["@attributes"] = attributes;
    if (hasElements && hasText) {
      result["#content"] = significant.map(function (child) {
        if (child.type !== "element") return child.value;
        var entry = {};
        entry[child.name] = elementToJson(child, preserve);
        return entry;
      });
      return result;
    }

    if (hasText) result["#text"] = significant.map(function (child) { return child.value; }).join("");
    significant.filter(function (child) { return child.type === "element"; }).forEach(function (child) {
      var childValue = elementToJson(child, preserve);
      if (Object.prototype.hasOwnProperty.call(result, child.name)) {
        if (!Array.isArray(result[child.name])) result[child.name] = [result[child.name]];
        result[child.name].push(childValue);
      } else {
        result[child.name] = childValue;
      }
    });
    return result;
  }

  function xmlToJson(value, options) {
    var root = parseXml(value, options);
    var result = {};
    result[root.name] = elementToJson(root);
    return result;
  }

  function isPlainObject(value) {
    if (!value || typeof value !== "object" || Array.isArray(value)) return false;
    var prototype = Object.getPrototypeOf(value);
    return prototype === Object.prototype || prototype === null;
  }

  function maxSerializationDepth(settings) {
    var maxDepth = settings.maxDepth === undefined ? 100 : Number(settings.maxDepth);
    if (!Number.isInteger(maxDepth) || maxDepth < 1) throw new TypeError("maxDepth must be a positive integer.");
    return maxDepth;
  }

  function scalarXmlText(value, label) {
    if (value === null || value === undefined) return "";
    if (typeof value === "object") throw new TypeError(label + " must be a scalar value.");
    return escapeXmlText(value);
  }

  function serializeAttributes(value) {
    if (value === undefined) return "";
    if (!isPlainObject(value)) throw new TypeError("@attributes must be an object.");
    return Object.keys(value).map(function (name) {
      assertXmlName(name);
      var attributeValue = value[name];
      if (attributeValue !== null && typeof attributeValue === "object") {
        throw new TypeError('XML attribute "' + name + '" must be a scalar value.');
      }
      return " " + name + '="' + escapeXmlAttribute(attributeValue === null || attributeValue === undefined ? "" : attributeValue) + '"';
    }).join("");
  }

  function serializeContent(content, depth, settings) {
    if (!Array.isArray(content)) throw new TypeError("#content must be an array.");
    return content.map(function (entry) {
      if (entry === null || typeof entry !== "object") return scalarXmlText(entry, "#content entry");
      if (!isPlainObject(entry)) throw new TypeError("#content element entries must be objects.");
      var keys = Object.keys(entry);
      if (keys.length !== 1) throw new TypeError("#content element entries must contain exactly one element name.");
      return serializeElement(keys[0], entry[keys[0]], depth + 1, settings);
    }).join("");
  }

  function serializeProperty(name, value, depth, settings) {
    assertXmlName(name);
    if (Array.isArray(value)) {
      return value.map(function (entry) {
        return serializeElement(name, entry, depth + 1, settings);
      }).join("");
    }
    return serializeElement(name, value, depth + 1, settings);
  }

  function serializeElement(name, value, depth, settings) {
    var elementName = assertXmlName(name);
    if (depth > settings.__maxDepth) {
      throw new SyntaxError("JSON nesting is too deep. Maximum depth is " + settings.__maxDepth + ".");
    }

    var attributes = "";
    var body = "";
    if (Array.isArray(value)) {
      body = value.map(function (entry) {
        return serializeElement("item", entry, depth + 1, settings);
      }).join("");
    } else if (isPlainObject(value)) {
      attributes = serializeAttributes(value["@attributes"]);
      if (Object.prototype.hasOwnProperty.call(value, "#content")) {
        body = serializeContent(value["#content"], depth, settings);
      } else {
        if (Object.prototype.hasOwnProperty.call(value, "#text")) {
          body += scalarXmlText(value["#text"], "#text");
        }
        Object.keys(value).forEach(function (key) {
          if (key === "@attributes" || key === "#text" || key === "#content") return;
          body += serializeProperty(key, value[key], depth, settings);
        });
      }
    } else {
      body = scalarXmlText(value, "Element value");
    }

    return "<" + elementName + attributes + ">" + body + "</" + elementName + ">";
  }

  function jsonToXml(sourceOrValue, options) {
    var settings = Object.assign({}, options || {});
    settings.__maxDepth = maxSerializationDepth(settings);
    var value;
    if (typeof sourceOrValue === "string" && settings.value !== true) {
      try {
        value = parseJsonNumbers(sourceOrValue, function (literal) { return literal; });
      } catch (error) {
        throw new SyntaxError("Invalid JSON: " + error.message);
      }
    } else {
      value = sourceOrValue;
    }

    if (settings.rootName !== undefined && settings.rootName !== null && settings.rootName !== "") {
      return serializeElement(assertXmlName(settings.rootName), value, 0, settings);
    }
    if (isPlainObject(value)) {
      var keys = Object.keys(value);
      if (keys.length === 1 && XML_NAME.test(keys[0])) {
        return serializeElement(assertXmlName(keys[0]), value[keys[0]], 0, settings);
      }
    }
    return serializeElement("root", value, 0, settings);
  }

  // Read JSON tokens from the source. Converting numbers to JavaScript values
  // and back can silently change IDs, exponents, and negative zero.
  function formatJson(source, spaces, messages, replaceNumber) {
    var indent = " ".repeat(spaces === undefined ? 2 : spaces);
    var pattern = /[ \t\r\n]+|"(?:[^"\\\u0000-\u001f]|\\(?:["\\/bfnrt]|u[0-9a-fA-F]{4}))*"|true|false|null|-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?|[{}\[\],:]/y;
    var closing = [];
    var expected = "value";
    var previous = "";
    var output = [];
    var addedSpaces = 0;
    var index = 0;

    function fail(detail) {
      var lines = source.slice(0, index).split(/\r\n|\r|\n/);
      var line = lines.length;
      var column = lines[line - 1].length + 1;
      var template = messages && messages.position || "Line {line}, column {column}.";
      var error = new SyntaxError(template.replace("{line}", line).replace("{column}", column)
        + " " + (messages && messages[detail] || {
          key: "Use a double-quoted property name.",
          value: "Check the JSON value and double-quoted strings.",
          colon: "Insert a colon after the property name.",
          separator: "Check the comma or closing bracket.",
          trailing: "Remove the trailing comma.",
          extra: "Only one JSON value is allowed."
        }[detail]));
      error.line = line;
      error.column = column;
      throw error;
    }

    function newline(depth) {
      if (!indent) return;
      addedSpaces += depth * indent.length + 1;
      // Deep nesting can expand a small document to gigabytes of indentation.
      if (addedSpaces > 16 * 1024 * 1024) {
        throw new RangeError(messages && messages.tooLarge || "Formatted indentation exceeds 16 MiB.");
      }
      output.push("\n", indent.repeat(depth));
    }

    while (index < source.length) {
      pattern.lastIndex = index;
      var match = pattern.exec(source);
      if (!match) fail(expected === "keyOrEnd" ? "key" : expected === "valueOrEnd" ? "value" : expected);
      var token = match[0];
      var first = token[0];
      if (first === " " || first === "\t" || first === "\r" || first === "\n") {
        index = pattern.lastIndex;
        continue;
      }
      if (token === "}" || token === "]") {
        if (previous === ",") fail("trailing");
        if (token !== closing[closing.length - 1]) fail("separator");
        if (expected !== "separator" && expected !== "keyOrEnd" && expected !== "valueOrEnd") fail(expected);
        closing.pop();
        if (previous !== "{" && previous !== "[") newline(closing.length);
        expected = closing.length ? "separator" : "extra";
      } else if (expected === "separator") {
        if (token !== ",") fail("separator");
        expected = closing[closing.length - 1] === "}" ? "key" : "value";
      } else if (expected === "colon") {
        if (token !== ":") fail("colon");
        expected = "value";
      } else {
        if (expected === "extra") fail("extra");
        if (previous === "," || previous === "{" || previous === "[") newline(closing.length);
        if (previous === ":" && indent) output.push(" ");
        if (expected === "key" || expected === "keyOrEnd") {
          if (first !== '"') fail("key");
          expected = "colon";
        } else if (token === "{" || token === "[") {
          closing.push(token === "{" ? "}" : "]");
          expected = token === "{" ? "keyOrEnd" : "valueOrEnd";
        } else {
          if (token === "," || token === ":") fail("value");
          expected = closing.length ? "separator" : "extra";
        }
      }
      output.push(replaceNumber && /^[-0-9]/.test(first) ? replaceNumber(token) : token);
      previous = token;
      index = pattern.lastIndex;
    }
    if (expected !== "extra") {
      fail(expected === "keyOrEnd" || expected === "valueOrEnd" ? "separator" : expected);
    }
    return output.join("");
  }

  // Parse the structure with the native parser but recover numbers from their
  // source tokens, even on browsers without JSON.parse reviver context.
  function parseJsonNumbers(source, readNumber) {
    var literals = [];
    var indexed = formatJson(source, 0, null, function (literal) {
      return String(literals.push(literal) - 1);
    });
    return JSON.parse(indexed, function (key, value) {
      return typeof value === "number" ? readNumber(literals[value]) : value;
    });
  }

  function JsonNumber(literal) {
    this.literal = literal;
  }

  function normalizedNumber(literal) {
    var parts = /^(-?)(\d+)(?:\.(\d+))?(?:[eE]([+-]?\d+))?$/.exec(literal);
    var fraction = parts[3] || "";
    var digits = (parts[2] + fraction).replace(/^0+/, "");
    if (!digits) return "0";
    var significand = digits.replace(/0+$/, "");
    var exponent = BigInt(parts[4] || 0) + BigInt(digits.length - significand.length - fraction.length);
    return parts[1] + significand + "e" + exponent;
  }

  function stringifyExactJson(value, sortKeys, normalize) {
    if (value instanceof JsonNumber) return normalize ? normalizedNumber(value.literal) : value.literal;
    if (Array.isArray(value)) {
      return "[" + value.map(function (item) { return stringifyExactJson(item, sortKeys, normalize); }).join(",") + "]";
    }
    if (value && typeof value === "object") {
      var keys = Object.keys(value);
      if (sortKeys) keys.sort();
      return "{" + keys.map(function (key) {
        return JSON.stringify(key) + ":" + stringifyExactJson(value[key], sortKeys, normalize);
      }).join(",") + "}";
    }
    return JSON.stringify(value);
  }

  function decodeUrlPart(text, plusAsSpace) {
    return decodeURIComponent(plusAsSpace ? text.replace(/\+/g, " ") : text);
  }

  function queryParameters(input, plusAsSpace) {
    var beforeHash = input.trim().split("#")[0];
    var question = beforeHash.indexOf("?");
    // The tool accepts both full URLs and bare query strings such as a=1&b=2.
    if (question < 0 && (/^(?:[a-z][\w+.-]*:|\/)/i.test(beforeHash) || !/[=&]/.test(beforeHash))) return [];
    var query = beforeHash.slice(question + 1);
    return query.split("&").filter(Boolean).map(function (pair, index) {
      var equals = pair.indexOf("=");
      return {
        index: index + 1,
        key: decodeUrlPart(equals < 0 ? pair : pair.slice(0, equals), plusAsSpace),
        value: equals < 0 ? "" : decodeUrlPart(pair.slice(equals + 1), plusAsSpace)
      };
    });
  }

  function decodeUrl(input, plusAsSpace) {
    if (!/^(?:[a-z][\w+.-]*:\/\/|\/)/i.test(input)) return decodeUrlPart(input, plusAsSpace);
    var delimiter = input.search(/[?#]/);
    if (delimiter < 0) return decodeUrlPart(input, false);
    return decodeUrlPart(input.slice(0, delimiter), false) + decodeUrlPart(input.slice(delimiter), plusAsSpace);
  }

  return {
    formatJson: formatJson,
    parseExactJson: function (source) { return parseJsonNumbers(source, function (literal) { return new JsonNumber(literal); }); },
    isJsonNumber: function (value) { return value instanceof JsonNumber; },
    stringifyExactJson: stringifyExactJson,
    queryParameters: queryParameters,
    decodeUrl: decodeUrl,
    formatXml: formatXml,
    minifyJavaScript: minifyJavaScript,
    minifyCss: minifyCss,
    minifySql: minifySql,
    minifyHtml: minifyHtml,
    minifyXml: minifyXml,
    jsonToXml: jsonToXml,
    xmlToJson: xmlToJson
  };
});
