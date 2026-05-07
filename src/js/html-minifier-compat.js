/* Local html-minifier compatibility shim for browser-only tools. */
(function () {
  'use strict';

  function stripComments(text) {
    return String(text || '').replace(/<!--[\s\S]*?-->/g, '').replace(/\/\*[\s\S]*?\*\//g, '');
  }

  function minifyCss(css) {
    return stripComments(css)
      .replace(/\s+/g, ' ')
      .replace(/\s*([{}:;,>+~])\s*/g, '$1')
      .replace(/;}/g, '}')
      .trim();
  }

  function stripJsComments(js) {
    var output = '';
    var quote = '';
    var escaped = false;
    var regexAllowed = true;

    for (var i = 0; i < js.length; i++) {
      var ch = js[i];
      var next = js[i + 1];

      if (quote) {
        output += ch;
        if (escaped) {
          escaped = false;
        } else if (ch === '\\') {
          escaped = true;
        } else if (ch === quote) {
          quote = '';
        }
        continue;
      }

      if (ch === '"' || ch === '\'' || ch === '`') {
        quote = ch;
        output += ch;
        continue;
      }

      if (ch === '/' && next === '/') {
        while (i < js.length && js[i] !== '\n') i++;
        output += '\n';
        continue;
      }

      if (ch === '/' && next === '*') {
        i += 2;
        while (i < js.length && !(js[i] === '*' && js[i + 1] === '/')) i++;
        i++;
        continue;
      }

      if (ch === '/' && regexAllowed) {
        output += ch;
        i++;
        var inClass = false;
        for (; i < js.length; i++) {
          ch = js[i];
          output += ch;
          if (ch === '\\') {
            i++;
            if (i < js.length) output += js[i];
          } else if (ch === '[') {
            inClass = true;
          } else if (ch === ']') {
            inClass = false;
          } else if (ch === '/' && !inClass) {
            break;
          }
        }
        continue;
      }

      if (!/\s/.test(ch)) regexAllowed = /[({[=,:;!&|?+\-*~^<>]/.test(ch);
      output += ch;
    }

    return output;
  }

  function minifyJs(js) {
    return stripJsComments(String(js || ''))
      .replace(/\s+/g, ' ')
      .replace(/\s*([{}()[\];,:+\-*\/%=<>!&|?])\s*/g, '$1')
      .trim();
  }

  function minifyHtml(source, options) {
    var opts = options || {};
    var result = String(source || '');

    if (opts.removeComments) {
      result = result.replace(/<!--[\s\S]*?-->/g, '');
    }

    if (opts.minifyCSS) {
      result = result.replace(/<style\b([^>]*)>([\s\S]*?)<\/style>/gi, function (_, attrs, css) {
        return '<style' + attrs + '>' + minifyCss(css) + '</style>';
      });
    }

    if (opts.minifyJS) {
      result = result.replace(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi, function (_, attrs, js) {
        return '<script' + attrs + '>' + minifyJs(js) + '</script>';
      });
    }

    if (opts.collapseWhitespace) {
      result = result
        .replace(/>\s+</g, '><')
        .replace(/\s{2,}/g, ' ')
        .trim();
    }

    return result;
  }

  window.htmlminifier = window.htmlminifier || {
    minify: minifyHtml
  };

  function xmlName(name) {
    return String(name || '').toLowerCase();
  }

  function escapeXml(value) {
    return String(value == null ? '' : value)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&apos;');
  }

  function stringToXml(source) {
    var parser = new DOMParser();
    var doc = parser.parseFromString(String(source || ''), 'application/xml');
    var parseError = doc.querySelector('parsererror');
    if (parseError) {
      throw new Error('Invalid XML: ' + parseError.textContent.substring(0, 100));
    }
    return doc;
  }

  function elementToObject(element) {
    var childElements = Array.prototype.filter.call(element.childNodes, function (node) {
      return node.nodeType === 1;
    });
    var text = Array.prototype.map.call(element.childNodes, function (node) {
      return node.nodeType === 3 || node.nodeType === 4 ? node.nodeValue : '';
    }).join('').trim();

    if (!childElements.length) {
      return text;
    }

    var obj = {};
    if (text) obj._text = text;

    childElements.forEach(function (child) {
      var name = xmlName(child.nodeName);
      var value = elementToObject(child);
      if (Object.prototype.hasOwnProperty.call(obj, name)) {
        if (!Array.isArray(obj[name])) obj[name] = [obj[name]];
        obj[name].push(value);
      } else {
        obj[name] = value;
      }
    });

    return obj;
  }

  function xmlToJs(xml) {
    var root = xml && xml.nodeType === 9 ? xml.documentElement : xml;
    if (!root) return {};
    var result = {};
    result[xmlName(root.nodeName)] = elementToObject(root);
    return result;
  }

  function valueToXml(name, value) {
    if (Array.isArray(value)) {
      return value.map(function (item) {
        return valueToXml(name, item);
      }).join('');
    }

    if (value !== null && typeof value === 'object') {
      var body = Object.keys(value).map(function (key) {
        if (key === '_text') return escapeXml(value[key]);
        return valueToXml(key, value[key]);
      }).join('');
      return '<' + name + '>' + body + '</' + name + '>';
    }

    return '<' + name + '>' + escapeXml(value) + '</' + name + '>';
  }

  function jsToString(obj) {
    if (obj === null || typeof obj !== 'object') {
      return valueToXml('value', obj);
    }
    return Object.keys(obj).map(function (key) {
      return valueToXml(key, obj[key]);
    }).join('');
  }

  window.JXON = window.JXON || {
    stringToXml: stringToXml,
    xmlToJs: xmlToJs,
    jsToString: jsToString,
    jsToXml: jsToString,
    xmlToString: function (xml) {
      return typeof xml === 'string' ? xml : new XMLSerializer().serializeToString(xml);
    }
  };
})();
