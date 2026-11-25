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

  function setOutput(value) {
    output.value = value;
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
