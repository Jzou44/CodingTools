/* ============================================================
   Single Input Mode
   Adds text/file input-source switching for single-item tools.
   ============================================================ */
(function () {
  "use strict";

  var root = document.querySelector("[data-single-input-mode]");
  if (!root) return;

  var tool = root.getAttribute("data-single-file-tool");
  var fileInput = document.getElementById("single-file-input");
  var filePanel = root.querySelector("[data-single-file-panel]");
  var status = document.getElementById("single-file-status");
  var radios = root.querySelectorAll("input[name=\"single-input-source\"]");
  var maxBytes = 5 * 1024 * 1024;
  var L = window.CodingToolsRuntimeI18n || {};

  var inputSelectors = {
    "base64-encode": "#input-editor",
    "base64-decode": "#input-editor",
    "md5-generator": "#input-editor",
    "sha1-generator": "#input-editor",
    "sha256-generator": "#input-editor",
    "sha384-generator": "#input-editor",
    "sha512-generator": "#input-editor",
    "json-formatter": "#input-editor",
    "json-minifier": "#input-editor",
    "json-to-xml": "#input-editor",
    "xml-formatter": "#input-editor",
    "xml-minifier": "#input-editor",
    "xml-to-json": "#input-editor",
    "html-beautifier": "#input-editor",
    "html-minifier": "#input-editor",
    "javascript-beautifier": "#input-editor",
    "javascript-minifier": "#input-editor",
    "css-beautifier": "#input-editor",
    "css-minifier": "#input-editor",
    "sql-formatter": "#input-editor",
    "sql-minifier": "#input-editor",
    "url-encode": "#input-editor",
    "url-decode": "#input-editor",
    "case-converter": "#input-editor",
    "reverse-text": "#input-editor",
    "character-count": "#input-editor",
    "word-counter": "#input-editor",
    "regex-replace": "#code1",
    "regex-tester": "#code1",
    "text-editor": "#code1",
    "hex-to-decimal": "#hex-input",
    "decimal-to-hex": "#decimal-input",
    "octal-to-decimal": "#octal-input",
    "decimal-to-octal": "#decimal-input",
    "binary-to-decimal": "#binary-input",
    "decimal-to-binary": "#decimal-input",
    "binary-to-hex": "#binary-input",
    "hex-to-binary": "#hex-input",
    "hex-to-ascii": "#code1",
    "ascii-to-hex": "#code1",
    "binary-to-text": "#code1",
    "text-to-binary": "#code1",
    "roman-numerals-to-numbers": "#roman-input",
    "numbers-to-roman-numerals": "#number-input",
    "fraction-to-decimal": "#integer-input",
    "decimal-to-fraction": "#decimal-input",
    "percent-to-decimal": "#percent-input",
    "decimal-to-percent": "#decimal-input",
    "percent-to-fraction": "#percent-input",
    "fraction-to-percent": "#integer-input",
    "number-to-words": "#input-number",
    "hex-to-rgb": "#hex-input",
    "hex-to-rgba": "#hex-input",
    "rgb-to-hex": "#r-input",
    "rgba-to-hex": "#r-input"
  };

  var inputSelector = inputSelectors[tool];
  var target = inputSelector ? document.querySelector(inputSelector) : null;
  if (!target || !fileInput || !filePanel) {
    root.hidden = true;
    return;
  }

  function tr(key, fallback) {
    return L[key] || fallback || key;
  }

  function formatBytes(bytes) {
    if (bytes < 1024) return bytes + " B";
    if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + " KB";
    return (bytes / 1024 / 1024).toFixed(2) + " MB";
  }

  function setStatus(message, state) {
    if (!status) return;
    status.textContent = message;
    status.classList.toggle("is-loaded", state === "loaded");
    status.classList.toggle("is-error", state === "error");
  }

  function selectedMode() {
    var selected = root.querySelector("input[name=\"single-input-source\"]:checked");
    return selected ? selected.value : "text";
  }

  function syncModeUi() {
    var mode = selectedMode();
    root.querySelectorAll(".single-input-mode").forEach(function (label) {
      var input = label.querySelector("input");
      label.classList.toggle("is-active", input && input.value === mode);
    });
    filePanel.hidden = mode !== "file";
    if (mode === "text") {
      setStatus(tr("noFileSelected", "No file selected."), "");
    }
  }

  function codeMirrorFor(element) {
    if (element.CodeMirror) return element.CodeMirror;
    if (element.nextElementSibling && element.nextElementSibling.CodeMirror) {
      return element.nextElementSibling.CodeMirror;
    }
    var wrapper = element.parentElement ? element.parentElement.querySelector(".CodeMirror") : null;
    return wrapper && wrapper.CodeMirror ? wrapper.CodeMirror : null;
  }

  function dispatchEditorEvents(element) {
    ["input", "change", "keyup"].forEach(function (name) {
      element.dispatchEvent(new Event(name, { bubbles: true }));
    });
  }

  function parseDelimitedNumbers(value) {
    return String(value).trim().split(/[\s,;|/]+/).filter(Boolean);
  }

  function setFieldValue(id, value) {
    var element = document.getElementById(id);
    if (!element) return;
    element.value = String(value == null ? "" : value).trim();
    dispatchEditorEvents(element);
  }

  function setFractionFields(value) {
    var text = String(value).trim();
    var integer = "";
    var numerator = "";
    var denominator = "";
    var match = text.match(/^([+-]?\d+)\s+([+-]?\d+)\s*\/\s*([+-]?\d+)$/);
    if (match) {
      integer = match[1];
      numerator = match[2];
      denominator = match[3];
    } else {
      match = text.match(/^([+-]?\d+)\s*\/\s*([+-]?\d+)$/);
      if (match) {
        numerator = match[1];
        denominator = match[2];
      } else {
        var parts = parseDelimitedNumbers(text);
        if (parts.length >= 3) {
          integer = parts[0];
          numerator = parts[1];
          denominator = parts[2];
        } else if (parts.length === 2) {
          numerator = parts[0];
          denominator = parts[1];
        } else {
          integer = parts[0] || "";
        }
      }
    }
    setFieldValue("integer-input", integer);
    setFieldValue("numerator-input", numerator);
    setFieldValue("denominator-input", denominator);
    var convertButton = document.getElementById("btn-convert");
    if (convertButton) convertButton.click();
    return true;
  }

  function setColorFields(value) {
    var text = String(value).trim();
    var parts = [];
    var hexMatch = text.match(/^#?([0-9a-fA-F]{6})([0-9a-fA-F]{2})?$/);
    if (hexMatch) {
      parts = [
        parseInt(hexMatch[1].slice(0, 2), 16),
        parseInt(hexMatch[1].slice(2, 4), 16),
        parseInt(hexMatch[1].slice(4, 6), 16)
      ];
      if (hexMatch[2]) parts.push(Math.round(parseInt(hexMatch[2], 16) / 255 * 100));
    } else {
      parts = parseDelimitedNumbers(text);
    }
    setFieldValue("r-input", parts[0] || "");
    setFieldValue("g-input", parts[1] || "");
    setFieldValue("b-input", parts[2] || "");
    if (tool === "rgba-to-hex") setFieldValue("a-input", parts[3] == null ? "100" : parts[3]);
    var convertButton = document.getElementById("btn-convert");
    if (convertButton) convertButton.click();
    return true;
  }

  function setTargetValue(value) {
    if (tool === "fraction-to-decimal" || tool === "fraction-to-percent") {
      setFractionFields(value);
      return;
    }
    if (tool === "rgb-to-hex" || tool === "rgba-to-hex") {
      setColorFields(value);
      return;
    }
    var text = target.tagName === "INPUT" ? String(value).trim() : String(value);
    var cm = target.tagName === "TEXTAREA" ? codeMirrorFor(target) : null;
    if (cm) {
      cm.setValue(text);
      cm.refresh();
      cm.focus();
    } else {
      target.value = text;
      target.focus();
    }
    dispatchEditorEvents(target);
    if (window.ToolCommon && target.id === "input-editor") {
      var inputLineNums = document.getElementById("input-line-numbers");
      if (inputLineNums && typeof ToolCommon.updateLineNumbers === "function") {
        ToolCommon.updateLineNumbers(target, inputLineNums);
      }
    }
  }

  function readFile(file) {
    if (!file) return;
    if (file.size > maxBytes) {
      setStatus(tr("fileTooLarge", "Max file size") + " " + formatBytes(maxBytes) + ".", "error");
      fileInput.value = "";
      return;
    }

    setStatus(tr("processing", "Processing...") + " " + file.name, "");
    file.text().then(function (text) {
      setTargetValue(text);
      setStatus(file.name + " (" + formatBytes(file.size) + ")", "loaded");
    }).catch(function () {
      setStatus(tr("invalidInput", "Invalid input"), "error");
    }).finally(function () {
      fileInput.value = "";
    });
  }

  radios.forEach(function (radio) {
    radio.addEventListener("change", syncModeUi);
  });

  fileInput.addEventListener("change", function () {
    readFile(fileInput.files && fileInput.files[0]);
  });

  syncModeUi();
})();

(function () {
  "use strict";

  var root = document.querySelector("[data-dual-input-mode]");
  if (!root) return;

  var filePanel = root.querySelector("[data-dual-file-panel]");
  var radios = root.querySelectorAll("input[name=\"dual-input-source\"]");
  var maxBytes = 5 * 1024 * 1024;
  var leftInput = document.getElementById("single-left-file-input");
  var rightInput = document.getElementById("single-right-file-input");
  var leftStatus = document.getElementById("single-left-file-status");
  var rightStatus = document.getElementById("single-right-file-status");
  var leftTarget = document.getElementById("left-editor");
  var rightTarget = document.getElementById("right-editor");
  var L = window.CodingToolsRuntimeI18n || {};

  if (!filePanel || !leftInput || !rightInput || !leftTarget || !rightTarget) {
    root.hidden = true;
    return;
  }

  function tr(key, fallback) {
    return L[key] || fallback || key;
  }

  function formatBytes(bytes) {
    if (bytes < 1024) return bytes + " B";
    if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + " KB";
    return (bytes / 1024 / 1024).toFixed(2) + " MB";
  }

  function setStatus(element, message, state) {
    if (!element) return;
    element.textContent = message;
    element.classList.toggle("is-loaded", state === "loaded");
    element.classList.toggle("is-error", state === "error");
  }

  function selectedMode() {
    var selected = root.querySelector("input[name=\"dual-input-source\"]:checked");
    return selected ? selected.value : "text";
  }

  function syncModeUi() {
    var mode = selectedMode();
    root.querySelectorAll(".single-input-mode").forEach(function (label) {
      var input = label.querySelector("input");
      label.classList.toggle("is-active", input && input.value === mode);
    });
    filePanel.hidden = mode !== "file";
    if (mode === "text") {
      setStatus(leftStatus, tr("noLeftFileSelected", "No left file selected."), "");
      setStatus(rightStatus, tr("noRightFileSelected", "No right file selected."), "");
    }
  }

  function dispatchEditorEvents(element) {
    ["input", "change", "keyup"].forEach(function (name) {
      element.dispatchEvent(new Event(name, { bubbles: true }));
    });
  }

  function setTargetValue(target, value) {
    target.value = String(value);
    dispatchEditorEvents(target);
    if (window.ToolCommon && typeof ToolCommon.updateLineNumbers === "function") {
      var lineNums = target.id === "left-editor"
        ? document.getElementById("left-line-numbers")
        : document.getElementById("right-line-numbers");
      if (lineNums) ToolCommon.updateLineNumbers(target, lineNums);
    }
    target.focus();
  }

  function readFile(file, target, statusElement, label) {
    if (!file) return;
    if (file.size > maxBytes) {
      setStatus(statusElement, tr("fileTooLarge", "Max file size") + " " + formatBytes(maxBytes) + ".", "error");
      return;
    }

    setStatus(statusElement, tr("processing", "Processing...") + " " + file.name, "");
    file.text().then(function (text) {
      setTargetValue(target, text);
      setStatus(statusElement, file.name + " (" + formatBytes(file.size) + ").", "loaded");
    }).catch(function () {
      setStatus(statusElement, tr("invalidInput", "Invalid input"), "error");
    });
  }

  radios.forEach(function (radio) {
    radio.addEventListener("change", syncModeUi);
  });

  leftInput.addEventListener("change", function () {
    readFile(leftInput.files && leftInput.files[0], leftTarget, leftStatus, "Left");
    leftInput.value = "";
  });

  rightInput.addEventListener("change", function () {
    readFile(rightInput.files && rightInput.files[0], rightTarget, rightStatus, "Right");
    rightInput.value = "";
  });

  syncModeUi();
})();
