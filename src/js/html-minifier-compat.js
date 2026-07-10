/* Legacy browser globals backed by the shared semantics-safe transformers. */
(function () {
  "use strict";

  var transforms = window.CodingToolsTextTransforms;
  if (!transforms) throw new Error("CodingToolsTextTransforms must load before html-minifier-compat.js.");

  function wrappedContents(text, tagName, transform) {
    var lower = text.toLowerCase();
    var openingEnd = text.indexOf(">");
    var closingStart = lower.lastIndexOf("</" + tagName + ">");
    if (openingEnd < 0 || closingStart < openingEnd) return null;
    return text.slice(0, openingEnd + 1) +
      transform(text.slice(openingEnd + 1, closingStart)) +
      text.slice(closingStart);
  }

  function minify(source, options) {
    var text = String(source == null ? "" : source);
    var settings = options || {};
    if (settings.minifyJS && /^<script\b[^>]*>/i.test(text) && /<\/script>$/i.test(text)) {
      return wrappedContents(text, "script", transforms.minifyJavaScript);
    }
    if (settings.minifyCSS && /^<style\b[^>]*>/i.test(text) && /<\/style>$/i.test(text)) {
      return wrappedContents(text, "style", transforms.minifyCss);
    }
    return transforms.minifyHtml(text);
  }

  function sourceFromXml(xml) {
    if (typeof xml === "string") return xml;
    if (xml && typeof xml.__codingToolsXmlSource === "string") return xml.__codingToolsXmlSource;
    if (typeof XMLSerializer === "function" && xml) return new XMLSerializer().serializeToString(xml);
    throw new TypeError("JXON expected an XML source string or document.");
  }

  function stringToXml(source) {
    var text = String(source == null ? "" : source);
    transforms.xmlToJson(text);
    return { __codingToolsXmlSource: text };
  }

  function xmlToJs(xml) {
    var result = transforms.xmlToJson(sourceFromXml(xml));
    var keys = Object.keys(result);
    if (keys.length === 1 && keys[0] === "RootDirectory") {
      return { rootdirectory: result.RootDirectory };
    }
    return result;
  }

  function serializeJsonValue(value) {
    return transforms.jsonToXml(value, { value: typeof value === "string" });
  }

  function jsToXml(value) {
    if (value && typeof value === "object" && !Array.isArray(value)) {
      var keys = Object.keys(value);
      if (keys.length === 1 && keys[0] === "RootDirectory") {
        return "<RootDirectory>" + serializeJsonValue(value.RootDirectory) + "</RootDirectory>";
      }
    }
    return serializeJsonValue(value);
  }

  window.htmlminifier = { minify: minify };
  window.JXON = {
    stringToXml: stringToXml,
    xmlToJs: xmlToJs,
    jsToString: jsToXml,
    jsToXml: jsToXml,
    xmlToString: sourceFromXml
  };
})();
