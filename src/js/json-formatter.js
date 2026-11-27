(function () {
  "use strict";

  var messages = JSON.parse(document.getElementById("json-formatter-runtime").dataset.messages);
  window.CodingToolsJsonMessages = messages;
  var input = document.getElementById("input-editor");
  var output = document.getElementById("output-editor");
  var inputLines = document.getElementById("input-line-numbers");
  var outputLines = document.getElementById("output-line-numbers");
  var generate = document.getElementById("btn-generate");
  var copy = document.getElementById("btn-copy");
  var download = document.getElementById("btn-download");
  var statusMessage = document.getElementById("status-message");
  var statusDot = document.getElementById("status-dot");
  var statusText = document.getElementById("status-text");
  var characterCount = document.getElementById("char-count");
  var lineCount = document.getElementById("line-count");
  var demoInput = null;
  statusMessage.setAttribute("role", "status");

  // The textarea stays selectable and provides the accessible text, clipboard and download.
  var colors = document.createElement("pre");
  colors.className = "json-colors";
  colors.setAttribute("aria-hidden", "true");
  colors.hidden = true;
  var tokens = document.createElement("code");
  colors.append(tokens);
  output.before(colors);
  output.wrap = "off";

  function syncColors() {
    tokens.style.transform = "translate(" + -output.scrollLeft + "px, " + -output.scrollTop + "px)";
  }
  output.addEventListener("scroll", syncColors);

  function colorOutput(value) {
    // Many thousands of spans would slow down large files. Keep the full plain result for those.
    colors.hidden = !value || value.length > 65536;
    tokens.replaceChildren();
    if (colors.hidden) return;
    var fragment = document.createDocumentFragment();
    var end = 0;
    for (var match of value.matchAll(/"(?:[^"\\]|\\.)*"/g)) {
      fragment.append(value.slice(end, match.index));
      var string = document.createElement("span");
      end = match.index + match[0].length;
      string.className = value[end] === ":" ? "json-key" : "json-string";
      string.textContent = match[0];
      fragment.append(string);
    }
    fragment.append(value.slice(end));
    tokens.append(fragment);
    syncColors();
  }

  function setOutput(value) {
    output.value = value;
    colorOutput(value);
    copy.disabled = download.disabled = !value;
    characterCount.textContent = ToolCommon.pluralise(value.length, window.I18N.charSingular, window.I18N.charPlural);
    lineCount.textContent = ToolCommon.pluralise(value ? ToolCommon.countLines(value) : 0, window.I18N.lineSingular, window.I18N.linePlural);
    ToolCommon.updateLineNumbers(output, outputLines);
  }

  function run() {
    try {
      setOutput(CodingToolsTextTransforms.formatJson(input.value, 2, messages));
    } catch (error) {
      setOutput("");
      input.setAttribute("aria-invalid", "true");
      ToolCommon.updateStatus(statusMessage, statusDot, statusText, "invalid", error.message);
      return;
    }
    input.removeAttribute("aria-invalid");
    ToolCommon.updateStatus(statusMessage, statusDot, statusText, "valid", messages.success);
    if (input.value !== demoInput) ToolCommon.trackToolSuccess("json_format");
  }

  function clearResult() {
    input.removeAttribute("aria-invalid");
    ToolCommon.updateStatus(statusMessage, statusDot, statusText, "idle", "");
    setOutput("");
  }

  generate.addEventListener("click", run);
  input.addEventListener("input", function () {
    demoInput = null;
    clearResult();
  });
  document.querySelectorAll("[data-json-example]").forEach(function (button) {
    button.addEventListener("click", function () {
      var textMode = document.querySelector('input[name="single-input-source"][value="text"]');
      if (textMode && !textMode.checked) textMode.click();
      input.value = button.dataset.jsonExample;
      input.dispatchEvent(new Event("input", { bubbles: true }));
      demoInput = input.value;
      run();
      input.focus();
    });
  });
  document.getElementById("btn-clear").addEventListener("click", function () {
    input.value = "";
    input.dispatchEvent(new Event("input", { bubbles: true }));
    input.focus();
  });
  copy.addEventListener("click", function () { ToolCommon.copyOutput(output, copy); });
  download.addEventListener("click", function () { ToolCommon.downloadOutput(output, "result.json"); });
  ToolCommon.initInputLineNumbers(input, inputLines);
  ToolCommon.initScrollSync(input, inputLines);
  ToolCommon.initScrollSync(output, outputLines);
  ToolCommon.initTabKey(input, inputLines);
  ToolCommon.initExampleCopy();
  ToolCommon.initKeyboardShortcut(generate);
  setOutput("");
})();
