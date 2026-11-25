(function () {
  "use strict";

  var panel = document.querySelector(".hash-comparison");
  var algorithm = panel.dataset.algorithm;
  var length = Number(panel.dataset.length);
  var messages = JSON.parse(panel.dataset.messages);
  var input = document.getElementById("input-editor");
  var output = document.getElementById("output-editor");
  var inputLines = document.getElementById("input-line-numbers");
  var outputLines = document.getElementById("output-line-numbers");
  var generate = document.getElementById("btn-generate");
  var copy = document.getElementById("btn-copy");
  var download = document.getElementById("btn-download");
  var expected = document.getElementById("expected-hash");
  var comparison = document.getElementById("hash-comparison-status");
  var status = document.getElementById("status-message");
  var dot = document.getElementById("status-dot");
  var statusText = document.getElementById("status-text");
  var charCount = document.getElementById("char-count");
  var lineCount = document.getElementById("line-count");
  var revision = 0;

  function compare() {
    var hex = expected.value.trim();
    var invalid = !!hex && (hex.length !== length || !/^[0-9a-f]+$/i.test(hex));
    expected.setAttribute("aria-invalid", String(invalid));
    var message = "";
    if (invalid) message = messages.format.replace("{length}", length);
    else if (hex && !output.value) message = messages.pending;
    else if (hex) message = hex.toLowerCase() === output.value ? messages.match : messages.mismatch;
    comparison.textContent = message;
  }

  function setOutput(value) {
    output.value = value;
    copy.disabled = download.disabled = !value;
    charCount.textContent = ToolCommon.pluralise(value.length, I18N.charSingular, I18N.charPlural);
    lineCount.textContent = ToolCommon.pluralise(value ? 1 : 0, I18N.lineSingular, I18N.linePlural);
    ToolCommon.updateLineNumbers(output, outputLines);
    compare();
  }

  function invalidate() {
    revision++;
    setOutput("");
    ToolCommon.updateStatus(status, dot, statusText, "idle", "");
  }

  generate.addEventListener("click", async function () {
    var request = ++revision;
    try {
      var value = await ToolCommon.hashBytes(algorithm, ToolCommon.editorBytes(input));
      if (request !== revision) return;
      setOutput(value);
      ToolCommon.updateStatus(status, dot, statusText, "valid", window.CodingToolsRuntimeI18n.done);
    } catch (error) {
      if (request !== revision) return;
      setOutput("");
      ToolCommon.updateStatus(status, dot, statusText, "invalid", messages.failed);
    }
  });
  input.addEventListener("input", invalidate);
  document.querySelector("[data-single-input-mode]").addEventListener("change", invalidate);
  expected.addEventListener("input", compare);
  document.getElementById("btn-clear").addEventListener("click", function () {
    expected.value = "";
    ToolCommon.clearEditors(input, output, status, dot, statusText, charCount, lineCount, inputLines, outputLines);
    invalidate();
  });
  copy.addEventListener("click", function () { ToolCommon.copyOutput(output, copy); });
  download.addEventListener("click", function () {
    ToolCommon.downloadOutput(output, algorithm.toLowerCase().replace("-", "") + "-hash.txt");
  });

  status.setAttribute("role", "status");
  ToolCommon.initInputLineNumbers(input, inputLines);
  ToolCommon.initScrollSync(input, inputLines);
  ToolCommon.initScrollSync(output, outputLines);
  ToolCommon.initTabKey(input, inputLines);
  ToolCommon.initExampleCopy();
  ToolCommon.initKeyboardShortcut(generate);
  setOutput("");
})();
