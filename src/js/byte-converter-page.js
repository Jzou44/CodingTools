(function () {
  'use strict';
  var page = document.querySelector('[data-byte-converter]');
  var tool = page.dataset.byteConverter;
  var input = document.getElementById('code1');
  var output = document.getElementById('code2');
  var inputLines = document.getElementById('input-line-numbers');
  var outputLines = document.getElementById('output-line-numbers');
  var mode = document.getElementById('single-byte-mode');
  var delimiter = document.getElementById('delimiter-select');
  var convert = document.getElementById('btn-convert');
  var copy = document.getElementById('btn-copy');
  var download = document.getElementById('btn-download');
  var messages = JSON.parse(page.dataset.errors);
  var example = null;

  function setStatus(state, message) {
    ToolCommon.updateStatus(document.getElementById('status-message'), document.getElementById('status-dot'), document.getElementById('status-text'), state, message);
  }

  function show(text, count) {
    output.value = text;
    ToolCommon.updateLineNumbers(output, outputLines);
    var chars = 0;
    for (var char of text) chars++;
    document.getElementById('char-count').textContent = ToolCommon.pluralise(chars, window.I18N.charSingular, window.I18N.charPlural);
    var units = (tool === 'ascii-to-hex' || tool === 'text-to-binary') && mode.value === 'legacy';
    document.getElementById('byte-count').textContent = units ? count + ' ' + page.dataset.unit : ToolCommon.pluralise(count, window.I18N.byteSingular, window.I18N.bytePlural);
    copy.disabled = download.disabled = !text;
  }

  function clearOutput() {
    show('', 0);
    setStatus('idle', '');
  }

  input.addEventListener('input', function () { example = null; clearOutput(); });
  mode.addEventListener('change', clearOutput);
  if (delimiter) delimiter.addEventListener('change', clearOutput);

  convert.addEventListener('click', function () {
    var separators = { space: ' ', none: '', comma: ',', colon: ':' };
    try {
      var result = CodingToolsByteConverter.convert(tool, input.value, mode.value, delimiter ? separators[delimiter.value] : ' ');
      show(result.text, result.count);
      setStatus('valid', page.dataset.success);
      if (example !== input.value) {
        var operations = { 'ascii-to-hex': 'hex_encode', 'hex-to-ascii': 'hex_decode', 'binary-to-text': 'binary_decode', 'text-to-binary': 'binary_encode' };
        ToolCommon.trackToolSuccess(operations[tool]);
      }
    } catch (error) {
      show('', 0);
      setStatus('invalid', CodingToolsByteConverter.explain(error, messages));
    }
  });
  page.querySelectorAll('[data-byte-example]').forEach(function (button) {
    button.addEventListener('click', function () {
      input.value = button.dataset.byteExample;
      example = input.value;
      mode.value = button.dataset.mode;
      clearOutput();
      ToolCommon.updateLineNumbers(input, inputLines);
      input.focus();
    });
  });
  document.getElementById('btn-clear').addEventListener('click', function () {
    input.value = '';
    example = null;
    ToolCommon.updateLineNumbers(input, inputLines);
    clearOutput();
  });
  copy.addEventListener('click', function () { ToolCommon.copyOutput(output, copy); });
  download.addEventListener('click', function () { ToolCommon.downloadOutput(output, tool + '-output.txt'); });
  ToolCommon.initInputLineNumbers(input, inputLines);
  ToolCommon.initScrollSync(input, inputLines);
  ToolCommon.initScrollSync(output, outputLines);
  page.addEventListener('keydown', function (event) {
    if (!event.isComposing && (event.ctrlKey || event.metaKey) && event.key === 'Enter') {
      event.preventDefault();
      convert.click();
    }
  });
  document.getElementById('status-message').setAttribute('role', 'status');
  ToolCommon.initExampleCopy();
  clearOutput();
})();
