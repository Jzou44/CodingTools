/* ============================================================
   Batch Tools
   Optional batch mode for selected tool pages.
   ============================================================ */
(function () {
  "use strict";

  var panel = document.querySelector("[data-batch-panel=\"batch\"]");
  if (!panel) return;

  var tool = panel.getAttribute("data-batch-tool");
  var body = document.getElementById("batch-results-body");
  var summary = document.getElementById("batch-summary");
  var btnRun = document.getElementById("batch-run");
  var btnClear = document.getElementById("batch-clear");
  var btnCopy = document.getElementById("batch-copy");
  var btnDownload = document.getElementById("batch-download");
  var fileInput = document.getElementById("batch-file-input");
  var filePicker = document.getElementById("batch-file-picker");
  var fileStatus = document.getElementById("batch-file-status");
  var textInput = document.getElementById("batch-text-input");
  var byteMode = document.getElementById("batch-byte-mode");
  var byteErrors = byteMode ? JSON.parse(document.querySelector("[data-byte-converter]").dataset.errors) : null;
  var dropzone = document.getElementById("batch-dropzone");
  var results = [];
  var droppedFiles = null;
  var maxImageFiles = 20;
  var L = window.CodingToolsRuntimeI18n || {};

  var structuredTextTools = {
    "json-formatter": true,
    "json-minifier": true,
    "json-to-xml": true,
    "xml-formatter": true,
    "xml-minifier": true,
    "xml-to-json": true,
    "html-beautifier": true,
    "html-minifier": true,
    "javascript-beautifier": true,
    "javascript-minifier": true,
    "css-beautifier": true,
    "css-minifier": true,
    "sql-formatter": true,
    "sql-minifier": true
  };

  var outputExtensions = {
    "base64-encode": "txt",
    "base64-decode": "txt",
    "md5-generator": "txt",
    "sha1-generator": "txt",
    "sha256-generator": "txt",
    "sha384-generator": "txt",
    "sha512-generator": "txt",
    "json-formatter": "json",
    "json-minifier": "json",
    "json-to-xml": "xml",
    "xml-formatter": "xml",
    "xml-minifier": "xml",
    "xml-to-json": "json",
    "html-beautifier": "html",
    "html-minifier": "html",
    "javascript-beautifier": "js",
    "javascript-minifier": "js",
    "css-beautifier": "css",
    "css-minifier": "css",
    "sql-formatter": "sql",
    "sql-minifier": "sql",
    "url-encode": "txt",
    "url-decode": "txt",
    "case-converter": "txt",
    "reverse-text": "txt",
    "regex-replace": "txt",
    "hex-to-decimal": "txt",
    "decimal-to-hex": "txt",
    "octal-to-decimal": "txt",
    "decimal-to-octal": "txt",
    "binary-to-decimal": "txt",
    "decimal-to-binary": "txt",
    "binary-to-hex": "txt",
    "hex-to-binary": "txt",
    "hex-to-ascii": "txt",
    "ascii-to-hex": "txt",
    "binary-to-text": "txt",
    "text-to-binary": "txt",
    "roman-numerals-to-numbers": "txt",
    "numbers-to-roman-numerals": "txt",
    "fraction-to-decimal": "txt",
    "decimal-to-fraction": "txt",
    "percent-to-decimal": "txt",
    "decimal-to-percent": "txt",
    "percent-to-fraction": "txt",
    "fraction-to-percent": "txt",
    "number-to-words": "txt"
  };

  function tr(key, fallback) {
    return L[key] || fallback || key;
  }

  function formatMessage(key, fallback, values) {
    var text = tr(key, fallback);
    Object.keys(values || {}).forEach(function (name) {
      text = text.replace(new RegExp("\\{" + name + "\\}", "g"), values[name]);
    });
    return text;
  }

  function initTabs() {
    var tabs = document.querySelectorAll("[data-batch-tab]");
    var panels = document.querySelectorAll("[data-batch-panel]");
    function activate(tab) {
      var target = tab.getAttribute("data-batch-tab");
      tabs.forEach(function (item) {
        var active = item === tab;
        item.classList.toggle("is-active", active);
        item.setAttribute("aria-selected", active ? "true" : "false");
        item.setAttribute("tabindex", active ? "0" : "-1");
      });
      panels.forEach(function (item) {
        var active = item.getAttribute("data-batch-panel") === target;
        item.classList.toggle("is-active", active);
        item.hidden = !active;
      });
      if ((location.hash === "#batch-tab-single" || location.hash === "#batch-tab-batch") && location.hash !== "#" + tab.id) {
        history.replaceState(history.state, "", "#" + tab.id);
      }
    }
    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        activate(tab);
      });
      tab.addEventListener("keydown", function (event) {
        var current = Array.prototype.indexOf.call(tabs, tab);
        var next = null;
        if (event.key === "ArrowRight") next = tabs[(current + 1) % tabs.length];
        if (event.key === "ArrowLeft") next = tabs[(current + tabs.length - 1) % tabs.length];
        if (event.key === "Home") next = tabs[0];
        if (event.key === "End") next = tabs[tabs.length - 1];
        if (!next) return;
        event.preventDefault();
        activate(next);
        next.focus();
      });
    });
    function activateLinkedTab() {
      if (location.hash === "#batch-tab-single" || location.hash === "#batch-tab-batch") {
        activate(document.getElementById(location.hash.slice(1)));
      }
    }
    window.addEventListener("hashchange", activateLinkedTab);
    activateLinkedTab();
  }

  function setSummary(count, message) {
    if (!summary) return;
    summary.innerHTML = "<span>" + count + " " + escapeHtml(tr("items", "items")) + "</span><span>" + escapeHtml(message || tr("ready", "Ready")) + "</span>";
  }

  function selectedFileCount() {
    var sourceFiles = droppedFiles || (fileInput && fileInput.files ? fileInput.files : []);
    return sourceFiles ? sourceFiles.length : 0;
  }

  function selectedFilesMessage(count) {
    if (!count) return tr("noFilesSelected", "No files selected");
    return count + " " + tr("files", "files");
  }

  function setFileStatus(count) {
    if (fileStatus) fileStatus.textContent = selectedFilesMessage(count);
  }

  function clearResults() {
    results.forEach(function (item) {
      if (item.url) URL.revokeObjectURL(item.url);
    });
    results = [];
    if (body) body.innerHTML = "<tr><td colspan=\"4\" class=\"batch-empty\">" + emptyResultsMessage() + "</td></tr>";
    if (btnCopy) btnCopy.disabled = true;
    if (btnDownload) btnDownload.disabled = true;
    setSummary(0, tr("ready", "Ready"));
  }

  function emptyResultsMessage() {
    return tr("batchResultsAppearHere", "Batch results will appear here.");
  }

  function escapeHtml(value) {
    return String(value == null ? "" : value).replace(/[&<>"']/g, function (char) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", "\"": "&quot;", "'": "&#39;" }[char];
    });
  }

  function baseName(name) {
    return String(name || "item").replace(/\.[^.]+$/, "");
  }

  function makeOutputName(name, fallback, extension) {
    var ext = extension || "txt";
    return ToolCommon.sanitizeDownloadFilename(baseName(name || fallback || "item") + "-batch." + ext, "batch-result." + ext);
  }

  function renderResults() {
    if (!body) return;
    if (!results.length) {
      body.innerHTML = "<tr><td colspan=\"4\" class=\"batch-empty\">" + emptyResultsMessage() + "</td></tr>";
      return;
    }
    body.innerHTML = results.map(function (item, index) {
      var statusClass = item.ok ? "batch-status-ok" : "batch-status-error";
      var output = "<pre class=\"batch-output\">" + escapeHtml(item.preview || item.output || item.error || "") + "</pre>";
      if (item.url) {
        output += "<a class=\"btn btn-ghost btn-sm\" href=\"" + item.url + "\" download=\"" + escapeHtml(item.filename) + "\">" + escapeHtml(tr("download", "Download")) + "</a>";
      }
      return "<tr><td>" + (index + 1) + "</td><td>" + escapeHtml(item.name) + "</td><td class=\"" + statusClass + "\">" + (item.ok ? escapeHtml(tr("done", "Done")) : escapeHtml(tr("error", "Error"))) + "</td><td>" + output + "</td></tr>";
    }).join("");
  }

  function resultText() {
    return results.map(function (item, index) {
      var value = item.ok ? item.output : tr("error", "ERROR") + ": " + item.error;
      return "### " + (index + 1) + ". " + item.name + "\n" + value;
    }).join("\n\n");
  }

  function downloadText(filename, text) {
    var blob = new Blob([text], { type: "text/plain;charset=utf-8" });
    var url = URL.createObjectURL(blob);
    var link = document.createElement("a");
    link.href = url;
    link.download = ToolCommon.sanitizeDownloadFilename(filename, "batch-results.txt");
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  }

  function inputBytes(value) {
    return value instanceof Uint8Array ? value : new TextEncoder().encode(value);
  }

  function base64ToUtf8(value) {
    var binary = atob(String(value).trim());
    var bytes = new Uint8Array(binary.length);
    for (var i = 0; i < binary.length; i += 1) bytes[i] = binary.charCodeAt(i);
    return new TextDecoder("utf-8", { fatal: true }).decode(bytes);
  }

  function bytesToHex(buffer) {
    return Array.from(new Uint8Array(buffer)).map(function (byte) {
      return byte.toString(16).padStart(2, "0");
    }).join("");
  }

  function digest(algorithm, value) {
    if (!window.crypto || !crypto.subtle) {
      return Promise.reject(new Error(tr("invalidInput", "Invalid input")));
    }
    return crypto.subtle.digest(algorithm, inputBytes(value)).then(bytesToHex);
  }

  function textTransforms() {
    if (!window.CodingToolsTextTransforms) throw new Error(tr("invalidInput", "Invalid input"));
    return window.CodingToolsTextTransforms;
  }

  function requireGlobal(name, label) {
    if (typeof window[name] !== "function") throw new Error((label || name) + " " + tr("invalidInput", "is unavailable"));
    return window[name];
  }

  function requireBigNumber() {
    if (typeof window.BigNumber !== "function") throw new Error(tr("invalidInput", "Invalid input"));
    return window.BigNumber;
  }

  function getDelimiter() {
    var select = document.getElementById("batch-delimiter");
    var value = select ? select.value : "space";
    return { space: " ", comma: ",", colon: ":", none: "" }[value] || " ";
  }

  function cleanNumberInput(value) {
    return String(value).trim().replace(/\s+/g, "");
  }

  function convertBase(value, fromBase, toBase) {
    try {
      return requireBigNumber().fromInteger(cleanNumberInput(value), fromBase).toString(toBase).toUpperCase();
    } catch (error) {
      throw new Error(tr("invalidInput", "Invalid input"));
    }
  }

  function toSentenceCase(value) {
    return String(value).toLowerCase().replace(/(^\s*\w|[.!?]\s*\w)/g, function (match) {
      return match.toUpperCase();
    });
  }

  function invertCase(value) {
    return String(value).split("").map(function (char) {
      return char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase();
    }).join("");
  }

  function convertCase(value) {
    var select = document.getElementById("batch-case-mode");
    var mode = select ? select.value : "upper";
    if (mode === "lower") return String(value).toLowerCase();
    if (mode === "sentence") return toSentenceCase(value);
    if (mode === "title") return ToolCommon.titleCase(value);
    if (mode === "invert") return invertCase(value);
    return String(value).toUpperCase();
  }

  function regexReplace(value) {
    var pattern = document.getElementById("batch-regex-pattern");
    var replacement = document.getElementById("batch-regex-replacement");
    var source = pattern ? pattern.value : "";
    if (!source) throw new Error(tr("invalidInput", "Invalid input"));
    var flags = ["g", "i", "m", "s", "u", "y"].filter(function (flag) {
      var input = document.getElementById("batch-regex-flag-" + flag);
      return input && input.checked;
    }).join("");
    return String(value).replace(new RegExp(source, flags), replacement ? replacement.value : "");
  }

  function decodeUrlText(value) {
    var plusAsSpaceInput = document.getElementById("batch-url-plus-space");
    var includeQueryInput = document.getElementById("batch-url-parse-query");
    var plusAsSpace = !plusAsSpaceInput || plusAsSpaceInput.checked;
    var includeQuery = !includeQueryInput || includeQueryInput.checked;
    var decoded = textTransforms().decodeUrl(value, plusAsSpace);

    if (!includeQuery) return decoded;
    var queryRows = textTransforms().queryParameters(value, plusAsSpace);
    if (!queryRows.length) return decoded;
    return [decoded, "", "Query parameters"].concat(queryRows.map(function (row) {
      return row.index + ". " + row.key + " = " + row.value;
    })).join("\n");
  }

  function encodeUrlText(value) {
    var mode = document.getElementById("batch-url-encode-mode");
    var plus = document.getElementById("batch-url-space-plus");
    var encoder = mode && mode.value === "uri" ? encodeURI : encodeURIComponent;
    var output = encoder(value);
    return plus && plus.checked ? output.replace(/%20/g, "+") : output;
  }

  function parseFraction(value) {
    var text = String(value).trim();
    var match = text.match(/^([+-]?\d+)\s+(\d+)\s*\/\s*(\d+)$/);
    if (match) {
      if (BigInt(match[3]) === 0n) throw new Error(tr("denominatorCannotBeZero", "Denominator cannot be zero"));
      return requireBigNumber().fromMixed(match[1], match[2], match[3]);
    }
    match = text.match(/^([+-]?\d+)\s*\/\s*(\d+)$/);
    if (match) {
      var num = new (requireBigNumber())(match[1]);
      var den = new (requireBigNumber())(match[2]);
      if (den.isZero()) throw new Error(tr("denominatorCannotBeZero", "Denominator cannot be zero"));
      return num.dividedBy(den);
    }
    throw new Error(tr("invalidInput", "Invalid input"));
  }

  function mixedFraction(value, percent) {
    try {
      return requireBigNumber().mixedFraction(value, percent).text;
    } catch (error) {
      throw new Error(tr("invalidDecimalInput", "Invalid decimal input"));
    }
  }

  function numberToWordsBatch(value) {
    var text = String(value).trim();
    var num = Number(text);
    if (!/^[+-]?\d+$/.test(text) || !Number.isSafeInteger(num)) throw new Error(tr("invalidDecimalInput", "Invalid decimal input"));
    if (!window.numberToWords || typeof window.numberToWords.toWords !== "function") throw new Error(tr("invalidInput", "Invalid input"));
    return window.numberToWords.toWords(num) + "\n" +
      window.numberToWords.toWordsOrdinal(num) + "\n" +
      window.numberToWords.toOrdinal(num);
  }

  function transformText(value) {
    if (tool === "base64-encode") return Promise.resolve(ToolCommon.bytesToBase64(inputBytes(value)));
    if (tool === "base64-decode") return Promise.resolve(base64ToUtf8(value));
    if (tool === "md5-generator") return Promise.resolve(requireGlobal("md5", "MD5 library")(value));
    if (tool === "sha1-generator") return digest("SHA-1", value);
    if (tool === "sha256-generator") return digest("SHA-256", value);
    if (tool === "sha384-generator") return digest("SHA-384", value);
    if (tool === "sha512-generator") return digest("SHA-512", value);
    if (tool === "json-formatter") return Promise.resolve(textTransforms().formatJson(value, 2, window.CodingToolsJsonMessages));
    if (tool === "json-minifier") return Promise.resolve(textTransforms().formatJson(value, 0));
    if (tool === "json-to-xml") return Promise.resolve(textTransforms().formatXml(textTransforms().jsonToXml(value)));
    if (tool === "xml-formatter") {
      return Promise.resolve(textTransforms().formatXml(value));
    }
    if (tool === "xml-minifier") return Promise.resolve(textTransforms().minifyXml(value, document.getElementById("batch-remove-xml-indent").checked));
    if (tool === "xml-to-json") return Promise.resolve(JSON.stringify(textTransforms().xmlToJson(value), null, 2));
    if (tool === "html-beautifier") return Promise.resolve(requireGlobal("html_beautify", "HTML beautifier")(value, { indent_size: 2 }));
    if (tool === "html-minifier") return Promise.resolve(textTransforms().minifyHtml(value));
    if (tool === "javascript-beautifier") return Promise.resolve(requireGlobal("js_beautify", "JavaScript beautifier")(value, { indent_size: 2 }));
    if (tool === "javascript-minifier") return Promise.resolve(textTransforms().minifyJavaScript(value));
    if (tool === "css-beautifier") return Promise.resolve(requireGlobal("css_beautify", "CSS beautifier")(value, { indent_size: 2 }));
    if (tool === "css-minifier") return Promise.resolve(textTransforms().minifyCss(value));
    if (tool === "sql-formatter") return Promise.resolve(sqlFormatter.format(value, { language: document.getElementById("batch-sql-dialect").value, tabWidth: 4 }));
    if (tool === "sql-minifier") return Promise.resolve(textTransforms().minifySql(value, document.getElementById("batch-sql-dialect").value));
    if (tool === "url-encode") return Promise.resolve(encodeUrlText(value));
    if (tool === "url-decode") return Promise.resolve(decodeUrlText(value));
    if (tool === "case-converter") return Promise.resolve(convertCase(value));
    if (tool === "reverse-text") return Promise.resolve(ToolCommon.reverseText(String(value)));
    if (tool === "regex-replace") return Promise.resolve(regexReplace(value));
    if (tool === "hex-to-decimal") return Promise.resolve(convertBase(value, 16, 10));
    if (tool === "decimal-to-hex") return Promise.resolve(convertBase(value, 10, 16));
    if (tool === "octal-to-decimal") return Promise.resolve(convertBase(value, 8, 10));
    if (tool === "decimal-to-octal") return Promise.resolve(convertBase(value, 10, 8));
    if (tool === "binary-to-decimal") return Promise.resolve(convertBase(value, 2, 10));
    if (tool === "decimal-to-binary") return Promise.resolve(convertBase(value, 10, 2));
    if (tool === "binary-to-hex") return Promise.resolve(convertBase(value, 2, 16));
    if (tool === "hex-to-binary") return Promise.resolve(convertBase(value, 16, 2));
    if (tool === "hex-to-ascii" || tool === "ascii-to-hex" || tool === "binary-to-text" || tool === "text-to-binary") {
      var delimiter = document.getElementById("batch-delimiter");
      var separator = delimiter && delimiter.value === "none" ? "" : getDelimiter();
      try {
        return Promise.resolve(window.CodingToolsByteConverter.convert(tool, value, byteMode.value, separator).text);
      } catch (error) {
        throw new Error(window.CodingToolsByteConverter.explain(error, byteErrors));
      }
    }
    if (tool === "roman-numerals-to-numbers") {
      var number = window.RomanNumerals.decode(value);
      if (number === null) throw new Error(tr("invalidRomanNumeral", "Invalid Roman numeral"));
      return Promise.resolve(String(number));
    }
    if (tool === "numbers-to-roman-numerals") {
      var roman = window.RomanNumerals.encode(value);
      if (!roman) throw new Error(tr("enterNumberBetween1And3999", "Enter a number between 1 and 3999"));
      return Promise.resolve(roman);
    }
    if (tool === "fraction-to-decimal") return Promise.resolve(parseFraction(value).toString(10));
    if (tool === "decimal-to-fraction") return Promise.resolve(mixedFraction(value, false));
    if (tool === "percent-to-decimal") return Promise.resolve(new (requireBigNumber())(String(value).trim().replace(/%$/, "")).dividedBy(100).toString(10));
    if (tool === "decimal-to-percent") return Promise.resolve(new (requireBigNumber())(String(value).trim()).multipliedBy(100).toString(10) + "%");
    if (tool === "percent-to-fraction") return Promise.resolve(mixedFraction(value, true));
    if (tool === "fraction-to-percent") return Promise.resolve(parseFraction(value).multipliedBy(100).toString(10) + "%");
    if (tool === "number-to-words") return Promise.resolve(numberToWordsBatch(value));
    return Promise.reject(new Error(tr("invalidInput", "Invalid input")));
  }

  function selectedInputMode() {
    var selected = document.querySelector("input[name=\"batch-input-mode\"]:checked");
    return selected ? selected.value : "lines";
  }

  function readTextFile(file) {
    var rawBytes = /^(?:base64-encode|(?:md5|sha1|sha256|sha384|sha512)-generator)$/.test(tool);
    var read = rawBytes ? file.arrayBuffer() : file.text();
    return read.then(function (content) {
      return { name: file.name, input: rawBytes ? new Uint8Array(content) : content };
    });
  }

  function collectTextItems() {
    if (selectedInputMode() === "files") {
      var sourceFiles = droppedFiles || (fileInput && fileInput.files ? fileInput.files : []);
      var files = Array.prototype.slice.call(sourceFiles);
      return Promise.all(files.map(readTextFile));
    }

    var value = textInput ? textInput.value : "";
    if (!value.trim()) return Promise.resolve([]);
    if (structuredTextTools[tool]) {
      return Promise.resolve([{ name: tr("input", "Input"), input: value }]);
    }
    return Promise.resolve(value.split(/\r?\n/).filter(function (line) {
      return line.length > 0;
    }).map(function (line, index) {
      return { name: tr("line", "Line") + " " + (index + 1), input: line };
    }));
  }

  function updateTextModeUi() {
    var mode = selectedInputMode();
    var modePanels = document.querySelectorAll("[data-batch-mode-panel]");
    modePanels.forEach(function (modePanel) {
      modePanel.classList.toggle("is-active", modePanel.getAttribute("data-batch-mode-panel") === mode);
    });

    if (mode === "files") {
      var fileCount = selectedFileCount();
      setSummary(fileCount, fileCount ? tr("ready", "Ready") : tr("eachFileBatchHint", "Each selected file becomes one batch item."));
      setFileStatus(fileCount);
    } else if (structuredTextTools[tool]) {
      setSummary(0, tr("pasteDocumentBatchHint", "This tool treats the text box as one complete document."));
    } else {
      setSummary(0, tr("eachLineBatchHint", "Each non-empty line becomes one batch item."));
    }
    renderResults();
  }

  function runTextBatch() {
    clearResults();
    collectTextItems().then(function (items) {
      if (!items.length) {
        setSummary(0, tr("noInput", "No input"));
        return;
      }
      setSummary(items.length, tr("processing", "Processing..."));
      return Promise.all(items.map(function (item) {
        return Promise.resolve().then(function () {
          return transformText(item.input);
        }).then(function (output) {
          return {
            ok: true,
            name: item.name,
            input: item.input,
            output: output,
            filename: makeOutputName(item.name, "batch-result", outputExtensions[tool])
          };
        }).catch(function (error) {
          return {
            ok: false,
            name: item.name,
            input: item.input,
            output: "",
            error: error.message || String(error)
          };
        });
      })).then(function (processed) {
        results = processed;
        renderResults();
        var ok = results.filter(function (item) { return item.ok; }).length;
        setSummary(results.length, "✓ " + ok + " / ✕ " + (results.length - ok));
        btnCopy.disabled = ok === 0;
        btnDownload.disabled = ok === 0;
        if (ok > 0 && (tool === "json-formatter" || document.querySelector("[data-byte-converter]"))) {
          ToolCommon.trackToolSuccess("batch_convert");
        }
      });
    }).catch(function (error) {
      results = [{
        ok: false,
        name: tr("file", "File"),
        output: "",
        error: error.message || String(error)
      }];
      renderResults();
      setSummary(1, tr("error", "Error"));
      btnCopy.disabled = true;
      btnDownload.disabled = true;
    });
  }

  function formatBytes(bytes) {
    if (!bytes) return "-";
    if (bytes < 1024) return bytes + " B";
    if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + " KB";
    return (bytes / 1024 / 1024).toFixed(2) + " MB";
  }

  function extensionFor(mime) {
    if (mime === "image/jpeg") return "jpg";
    if (mime === "image/webp") return "webp";
    return "png";
  }

  function supportedResizeMime(file) {
    return ["image/png", "image/jpeg", "image/webp"].indexOf(file.type) !== -1;
  }

  function canvasToBlob(canvas, mime, quality) {
    return new Promise(function (resolve, reject) {
      if (typeof canvas.toBlob !== "function") {
        reject(new Error(tr("invalidInput", "Invalid input")));
        return;
      }
      canvas.toBlob(function (blob) {
        if (!blob) reject(new Error(tr("invalidInput", "Invalid input")));
        else resolve(blob);
      }, mime, quality);
    });
  }

  function resizeDimensions(image) {
    var widthInput = document.getElementById("batch-width");
    var heightInput = document.getElementById("batch-height");
    var percentInput = document.getElementById("batch-percent");
    var keepAspect = document.getElementById("batch-keep-aspect");
    var requestedWidth = Math.round(Number(widthInput && widthInput.value) || 0);
    var requestedHeight = Math.round(Number(heightInput && heightInput.value) || 0);
    var percent = Math.max(1, Math.min(400, Number(percentInput && percentInput.value) || 100));
    var width = requestedWidth;
    var height = requestedHeight;

    if (!width && !height) {
      width = Math.max(1, Math.round(image.width * percent / 100));
      height = Math.max(1, Math.round(image.height * percent / 100));
    } else if (keepAspect && keepAspect.checked && width) {
      height = Math.max(1, Math.round(width / (image.width / image.height)));
    } else if (keepAspect && keepAspect.checked && height) {
      width = Math.max(1, Math.round(height * (image.width / image.height)));
    }

    return {
      width: Math.max(1, width || image.width),
      height: Math.max(1, height || image.height)
    };
  }

  function processResizeFile(file) {
    if (!supportedResizeMime(file)) return Promise.reject(new Error(tr("unsupportedImageType", "Unsupported image type")));
    if (file.size > 10 * 1024 * 1024) return Promise.reject(new Error(tr("fileTooLarge", "Max file size") + " 10MB"));

    return ToolCommon.loadImage(file).then(function (loaded) {
      var image = loaded.image;
      var dimensions = resizeDimensions(image);
      var qualityInput = document.getElementById("batch-quality");
      var quality = Math.max(1, Math.min(100, Number(qualityInput && qualityInput.value) || 90)) / 100;
      var mime = file.type || "image/png";
      var canvas = document.createElement("canvas");
      var ctx = canvas.getContext("2d");
      canvas.width = dimensions.width;
      canvas.height = dimensions.height;
      if (mime === "image/jpeg") {
        ctx.fillStyle = "#fff";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
      }
      ctx.imageSmoothingEnabled = true;
      ctx.imageSmoothingQuality = "high";
      ctx.drawImage(image, 0, 0, canvas.width, canvas.height);
      return canvasToBlob(canvas, mime, quality).then(function (blob) {
        var filename = ToolCommon.sanitizeDownloadFilename(baseName(file.name) + "-resized." + extensionFor(blob.type || mime), "image-resized.png");
        return {
          ok: true,
          name: file.name,
          output: formatBytes(file.size) + " -> " + formatBytes(blob.size) + " / " + dimensions.width + " x " + dimensions.height,
          filename: filename,
          blob: blob,
          url: URL.createObjectURL(blob)
        };
      });
    });
  }

  function processImageBase64File(file) {
    if (!/^image\//.test(file.type || "")) return Promise.reject(new Error(tr("unsupportedImageType", "Unsupported image type")));
    if (file.size > 2 * 1024 * 1024) return Promise.reject(new Error(tr("fileTooLarge", "Max file size") + " 2MB"));
    return ToolCommon.loadImage(file).then(function (loaded) {
      var dataUrl = loaded.dataUrl;
      return {
        ok: true,
        name: file.name,
        output: dataUrl,
        preview: dataUrl.length > 500 ? dataUrl.slice(0, 500) + "\n..." : dataUrl,
        filename: makeOutputName(file.name, "image-base64", "txt")
      };
    });
  }

  function runImageBatch() {
    clearResults();
    var sourceFiles = droppedFiles || (fileInput && fileInput.files ? fileInput.files : []);
    var allFiles = Array.prototype.slice.call(sourceFiles);
    var files = allFiles.slice(0, maxImageFiles);
    var skipped = allFiles.slice(maxImageFiles).map(function (file) {
      return {
        ok: false,
        name: file.name,
        output: "",
        error: formatMessage("skippedFileLimit", "Skipped: maximum {max} files", { max: maxImageFiles })
      };
    });
    if (!files.length) {
      setSummary(0, tr("noFilesSelected", "No files selected"));
      return;
    }
    setSummary(allFiles.length, tr("processing", "Processing..."));
    var processor = tool === "image-resize" ? processResizeFile : processImageBase64File;
    Promise.all(files.map(function (file) {
      return processor(file).catch(function (error) {
        return {
          ok: false,
          name: file.name,
          output: "",
          error: error.message || String(error)
        };
      });
    })).then(function (processed) {
      results = processed.concat(skipped);
      renderResults();
      var ok = results.filter(function (item) { return item.ok; }).length;
      setSummary(results.length, "✓ " + ok + " / ✕ " + (results.length - ok));
      btnCopy.disabled = ok === 0 || tool === "image-resize";
      btnDownload.disabled = ok === 0;
    });
  }

  function downloadResizeResults() {
    var completed = results.filter(function (item) { return item.ok && item.blob; });
    if (!completed.length) return;
    if (completed.length === 1) {
      var single = completed[0];
      var link = document.createElement("a");
      link.href = single.url;
      link.download = single.filename;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      return;
    }
    if (!window.JSZip) {
      setSummary(results.length, tr("invalidInput", "Invalid input"));
      return;
    }
    var zip = new JSZip();
    completed.forEach(function (item) {
      ToolCommon.addFileToZip(zip, item.filename, item.blob);
    });
    zip.generateAsync({ type: "blob" }).then(function (content) {
      var url = URL.createObjectURL(content);
      var link = document.createElement("a");
      link.href = url;
      link.download = "resized-images.zip";
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      ToolCommon.trackToolSuccess("resize_zip");
      setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
    });
  }

  function handleDownload() {
    if (tool === "image-resize") {
      downloadResizeResults();
      return;
    }
    if (tool === "image-to-base64") {
      var data = results.filter(function (item) { return item.ok; }).map(function (item) {
        return { name: item.name, dataUri: item.output };
      });
      downloadText("image-base64-batch.json", JSON.stringify(data, null, 2));
      return;
    }
    downloadText("batch-results.txt", resultText());
  }

  function handleCopy() {
    if (!results.length || tool === "image-resize") return;
    var text = tool === "image-to-base64"
      ? JSON.stringify(results.filter(function (item) { return item.ok; }).map(function (item) {
        return { name: item.name, dataUri: item.output };
      }), null, 2)
      : resultText();
    ToolCommon.copyText(text).then(function () {
      setSummary(results.length, tr("copied", "Copied!"));
    });
  }

  function initFileDrag() {
    if (!dropzone || !fileInput) return;
    ["dragover", "dragleave", "drop"].forEach(function (eventName) {
      dropzone.addEventListener(eventName, function (event) {
        event.preventDefault();
        if (eventName === "dragover") dropzone.classList.add("dragover");
        else dropzone.classList.remove("dragover");
        if (eventName === "drop" && event.dataTransfer.files.length) {
          droppedFiles = event.dataTransfer.files;
          setSummary(droppedFiles.length, tr("ready", "Ready"));
          setFileStatus(droppedFiles.length);
        }
      });
    });
    dropzone.addEventListener("keydown", function (event) {
      if (event.key !== "Enter" && event.key !== " ") return;
      event.preventDefault();
      fileInput.click();
    });
  }

  function initFileInput() {
    if (!fileInput) return;
    setFileStatus(selectedFileCount());
    if (filePicker) {
      filePicker.addEventListener("keydown", function (event) {
        if (event.key !== "Enter" && event.key !== " ") return;
        event.preventDefault();
        fileInput.click();
      });
    }
    fileInput.addEventListener("change", function () {
      droppedFiles = null;
      var count = selectedFileCount();
      setFileStatus(count);
      if (count) setSummary(count, tr("ready", "Ready"));
    });
  }

  function initPlaceholders() {
    if (!textInput) return;
    var linesHint = document.getElementById("batch-lines-hint");
    if (structuredTextTools[tool]) {
      textInput.placeholder = tr("pasteDocumentBatchPlaceholder", "Paste one complete document here, or switch to Files for multiple documents.");
      if (linesHint) linesHint.textContent = tr("pasteDocumentBatchHint", "This tool treats the text box as one complete document. Use Files mode when you want multiple documents.");
    } else if (/generator$/.test(tool)) {
      textInput.placeholder = tr("enterOneValuePerLine", "Enter one value per line.");
      if (linesHint) linesHint.textContent = tr("eachLineBatchHint", "Each non-empty line becomes one batch item. Results are mapped as Line 1, Line 2, and so on.");
    } else {
      textInput.placeholder = tr("enterOneItemPerLine", "Enter one item per line.");
      if (linesHint) linesHint.textContent = tr("eachLineBatchHint", "Each non-empty line becomes one batch item. Results are mapped as Line 1, Line 2, and so on.");
    }
  }

  function initTextModeControls() {
    var radios = document.querySelectorAll("input[name=\"batch-input-mode\"]");
    if (!radios.length) return;
    radios.forEach(function (radio) {
      radio.addEventListener("change", function () {
        droppedFiles = null;
        clearResults();
        updateTextModeUi();
      });
    });
    updateTextModeUi();
  }

  initTabs();
  initPlaceholders();
  initTextModeControls();
  initFileInput();
  initFileDrag();

  if (btnRun) {
    btnRun.addEventListener("click", function () {
      if (tool === "image-resize" || tool === "image-to-base64") runImageBatch();
      else runTextBatch();
    });
  }
  if (btnClear) {
    btnClear.addEventListener("click", function () {
      if (textInput) textInput.value = "";
      if (fileInput) fileInput.value = "";
      droppedFiles = null;
      setFileStatus(0);
      clearResults();
    });
  }
  if (btnCopy) btnCopy.addEventListener("click", handleCopy);
  if (btnDownload) btnDownload.addEventListener("click", handleDownload);
})();
