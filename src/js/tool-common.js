/* ============================================================
   Tool Common — Shared helpers for all tool pages
   ============================================================ */
var ToolCommon = (function () {
  'use strict';

  function countLines(text) {
    if (!text) return 1;
    return text.split('\n').length;
  }

  function pluralise(count, word) {
    return count + ' ' + word + (count !== 1 ? 's' : '');
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
    if (charCount) charCount.textContent = '0 characters';
    if (lineCount) lineCount.textContent = '0 lines';
    if (inputEditor && inputLineNums) updateLineNumbers(inputEditor, inputLineNums);
    if (outputEditor && outputLineNums) updateLineNumbers(outputEditor, outputLineNums);
    if (inputEditor) inputEditor.focus();
  }

  function copyOutput(outputEditor, btnCopy) {
    var text = outputEditor.value;
    if (!text) return;
    navigator.clipboard.writeText(text).then(function () {
      var originalHTML = btnCopy.innerHTML;
      btnCopy.classList.add('copied');
      btnCopy.innerHTML =
        '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Copied!';
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
      navigator.clipboard.writeText(code).then(function () {
        exampleCopy.textContent = 'Copied!';
        setTimeout(function () {
          exampleCopy.textContent = 'Copy';
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
    initKeyboardShortcut: initKeyboardShortcut
  };
})();
