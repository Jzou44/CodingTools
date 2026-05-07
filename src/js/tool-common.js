/* ============================================================
   Tool Common — Shared helpers for all tool pages
   ============================================================ */
var ToolCommon = (function () {
  'use strict';

  function countLines(text) {
    if (!text) return 1;
    return text.split('\n').length;
  }

  function pluralise(count, singular, plural) {
    var w = (count !== 1 && plural) ? plural : singular;
    return count + ' ' + w;
  }

  function updateLineNumbers(textarea, container) {
    var lines = countLines(textarea.value);
    var html = '';
    for (var i = 1; i <= Math.max(lines, 1); i++) {
      html += i + '\n';
    }
    container.textContent = html.trimEnd();
  }

  function updateStatus(statusMessage, statusDot, statusText, type, message) {
    statusMessage.className = 'status-message ' + type;
    statusText.textContent = message;
    if (type === 'valid' || type === 'invalid') {
      statusDot.style.display = 'inline-block';
      statusDot.className = 'status-dot ' + type;
    } else {
      statusDot.style.display = 'none';
    }
  }

  function clearEditors(inputEditor, outputEditor, statusMessage, statusDot, statusText, charCount, lineCount, inputLineNums, outputLineNums) {
    if (inputEditor) inputEditor.value = '';
    if (outputEditor) outputEditor.value = '';
    updateStatus(statusMessage, statusDot, statusText, 'idle', '');
    var i18n = window.I18N || {};
    if (charCount) charCount.textContent = '0 ' + (i18n.charPlural || 'characters');
    if (lineCount) lineCount.textContent = '0 ' + (i18n.linePlural || 'lines');
    if (inputEditor && inputLineNums) updateLineNumbers(inputEditor, inputLineNums);
    if (outputEditor && outputLineNums) updateLineNumbers(outputEditor, outputLineNums);
    if (inputEditor) inputEditor.focus();
  }

  function copyOutput(outputEditor, btnCopy) {
    var text = outputEditor.value;
    if (!text) return;
    navigator.clipboard.writeText(text).then(function () {
      var originalHTML = btnCopy.innerHTML;
      var i18n = window.I18N || {};
      btnCopy.classList.add('copied');
      btnCopy.innerHTML =
        '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> ' + (i18n.copied || 'Copied!');
      setTimeout(function () {
        btnCopy.innerHTML = originalHTML;
        btnCopy.classList.remove('copied');
      }, 2000);
    }).catch(function () {
      outputEditor.select();
      document.execCommand('copy');
    });
  }

  function downloadOutput(outputEditor, filename) {
    var text = outputEditor.value;
    if (!text) return;
    var blob = new Blob([text], { type: 'text/plain' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = filename || 'output.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  function initExampleCopy() {
    var exampleCopy = document.getElementById('example-copy');
    if (!exampleCopy) return;
    exampleCopy.addEventListener('click', function () {
      var code = document.getElementById('example-code').textContent;
      var i18n = window.I18N || {};
      navigator.clipboard.writeText(code).then(function () {
        exampleCopy.textContent = i18n.copied || 'Copied!';
        setTimeout(function () {
          exampleCopy.textContent = i18n.copy || 'Copy';
        }, 2000);
      });
    });
  }

  function initTabKey(textarea, lineNumsContainer) {
    textarea.addEventListener('keydown', function (e) {
      if (e.key === 'Tab') {
        e.preventDefault();
        var start = this.selectionStart;
        var end = this.selectionEnd;
        this.value = this.value.substring(0, start) + '  ' + this.value.substring(end);
        this.selectionStart = this.selectionEnd = start + 2;
        if (lineNumsContainer) updateLineNumbers(this, lineNumsContainer);
      }
    });
  }

  function initScrollSync(textarea, lineNumsContainer) {
    textarea.addEventListener('scroll', function () {
      lineNumsContainer.scrollTop = textarea.scrollTop;
    });
  }

  function initInputLineNumbers(textarea, lineNumsContainer) {
    textarea.addEventListener('input', function () {
      updateLineNumbers(textarea, lineNumsContainer);
    });
  }

  function initKeyboardShortcut(btnAction) {
    document.addEventListener('keydown', function (e) {
      if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        e.preventDefault();
        btnAction.click();
      }
    });
  }

  function initTextTool(options) {
    var opts = options || {};
    var inputEditor = opts.inputEditor || document.getElementById(opts.inputId || 'input-editor');
    var outputEditor = opts.outputEditor || document.getElementById(opts.outputId || 'output-editor');
    var btnAction = opts.actionButton || document.getElementById(opts.actionId || 'btn-generate');
    var btnClear = opts.clearButton || document.getElementById(opts.clearId || 'btn-clear');
    var btnCopy = opts.copyButton || document.getElementById(opts.copyId || 'btn-copy');
    var btnDownload = opts.downloadButton || document.getElementById(opts.downloadId || 'btn-download');
    var statusMessage = opts.statusMessage || document.getElementById(opts.statusMessageId || 'status-message');
    var statusDot = opts.statusDot || document.getElementById(opts.statusDotId || 'status-dot');
    var statusText = opts.statusText || document.getElementById(opts.statusTextId || 'status-text');
    var charCount = opts.charCount || document.getElementById(opts.charCountId || 'char-count');
    var lineCount = opts.lineCount || document.getElementById(opts.lineCountId || 'line-count');
    var inputLineNums = opts.inputLineNums || document.getElementById(opts.inputLineNumsId || 'input-line-numbers');
    var outputLineNums = opts.outputLineNums || document.getElementById(opts.outputLineNumsId || 'output-line-numbers');
    var i18n = window.I18N || {};

    function setStatus(type, message) {
      if (statusMessage && statusDot && statusText) {
        updateStatus(statusMessage, statusDot, statusText, type, message || '');
      }
    }

    function updateCounts() {
      var text = outputEditor ? outputEditor.value : '';
      if (charCount) {
        charCount.textContent = pluralise(text.length, opts.charSingular || i18n.charSingular || 'character', opts.charPlural || i18n.charPlural || 'characters');
      }
      if (lineCount) {
        lineCount.textContent = pluralise(countLines(text), opts.lineSingular || i18n.lineSingular || 'line', opts.linePlural || i18n.linePlural || 'lines');
      }
      if (outputEditor && outputLineNums) updateLineNumbers(outputEditor, outputLineNums);
    }

    function runAction() {
      if (!opts.onAction || !inputEditor || !outputEditor) return;

      try {
        var result = opts.onAction({
          input: inputEditor.value,
          inputEditor: inputEditor,
          outputEditor: outputEditor,
          setStatus: setStatus,
          updateCounts: updateCounts
        });

        if (typeof result === 'string') {
          outputEditor.value = result;
        } else if (result && Object.prototype.hasOwnProperty.call(result, 'output')) {
          outputEditor.value = result.output == null ? '' : String(result.output);
          if (result.statusType || result.statusMessage) {
            setStatus(result.statusType || 'valid', result.statusMessage || '');
          }
        }

        updateCounts();
      } catch (e) {
        setStatus('invalid', (opts.errorPrefix || 'Operation failed: ') + e.message);
      }
    }

    if (btnAction) {
      btnAction.addEventListener('click', runAction);
      initKeyboardShortcut(btnAction);
    }

    if (btnClear) {
      btnClear.addEventListener('click', function () {
        clearEditors(inputEditor, outputEditor, statusMessage, statusDot, statusText, charCount, lineCount, inputLineNums, outputLineNums);
      });
    }

    if (btnCopy && outputEditor) {
      btnCopy.addEventListener('click', function () {
        copyOutput(outputEditor, btnCopy);
      });
    }

    if (btnDownload && outputEditor) {
      btnDownload.addEventListener('click', function () {
        downloadOutput(outputEditor, opts.downloadFilename || 'output.txt');
      });
    }

    if (inputEditor && inputLineNums) {
      initInputLineNumbers(inputEditor, inputLineNums);
      initScrollSync(inputEditor, inputLineNums);
      initTabKey(inputEditor, inputLineNums);
      updateLineNumbers(inputEditor, inputLineNums);
    }

    if (outputEditor && outputLineNums) {
      initScrollSync(outputEditor, outputLineNums);
      updateLineNumbers(outputEditor, outputLineNums);
    }

    initExampleCopy();
    updateCounts();

    if (opts.autoRun && btnAction) {
      btnAction.click();
    }

    return {
      inputEditor: inputEditor,
      outputEditor: outputEditor,
      btnAction: btnAction,
      btnClear: btnClear,
      btnCopy: btnCopy,
      btnDownload: btnDownload,
      setStatus: setStatus,
      updateCounts: updateCounts,
      runAction: runAction
    };
  }

  return {
    countLines: countLines,
    pluralise: pluralise,
    updateLineNumbers: updateLineNumbers,
    updateStatus: updateStatus,
    clearEditors: clearEditors,
    copyOutput: copyOutput,
    downloadOutput: downloadOutput,
    initExampleCopy: initExampleCopy,
    initTabKey: initTabKey,
    initScrollSync: initScrollSync,
    initInputLineNumbers: initInputLineNumbers,
    initKeyboardShortcut: initKeyboardShortcut,
    initTextTool: initTextTool
  };
})();
