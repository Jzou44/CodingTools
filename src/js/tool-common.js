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

  function canUseClipboard() {
    return !!(navigator.clipboard && typeof navigator.clipboard.writeText === 'function');
  }

  function copyText(text) {
    if (!text) return Promise.resolve(false);
    if (canUseClipboard()) {
      return navigator.clipboard.writeText(text).then(function () { return true; }).catch(function () {
        return fallbackCopyText(text);
      });
    }
    return Promise.resolve(fallbackCopyText(text));
  }

  function fallbackCopyFromField(field) {
    if (!field || typeof field.select !== 'function' || typeof document.execCommand !== 'function') return false;
    var active = document.activeElement;
    field.select();
    if (typeof field.setSelectionRange === 'function') {
      field.setSelectionRange(0, field.value.length);
    }
    var copied = false;
    try {
      copied = document.execCommand('copy');
    } catch (e) {
      copied = false;
    }
    if (active && typeof active.focus === 'function') active.focus();
    return copied;
  }

  function fallbackCopyText(text) {
    if (typeof document.execCommand !== 'function') return false;
    var field = document.createElement('textarea');
    field.value = text;
    field.setAttribute('readonly', '');
    field.style.position = 'fixed';
    field.style.left = '-9999px';
    field.style.top = '0';
    document.body.appendChild(field);
    var copied = fallbackCopyFromField(field);
    document.body.removeChild(field);
    return copied;
  }

  function clearElement(element) {
    while (element && element.firstChild) {
      element.removeChild(element.firstChild);
    }
  }

  function sanitizeDownloadFilename(filename, fallback) {
    var value = String(filename || fallback || 'download.txt')
      .replace(/[\u0000-\u001f\u007f<>:"/\\|?*]+/g, '-')
      .replace(/\s+/g, ' ')
      .replace(/^\.+/, '')
      .trim();
    if (!value) value = String(fallback || 'download.txt');
    value = value.replace(/[. ]+$/g, '');
    if (/^(con|prn|aux|nul|com[1-9]|lpt[1-9])(\..*)?$/i.test(value)) {
      value = '_' + value;
    }
    return value.slice(0, 180) || 'download.txt';
  }

  function appendFileStatusItem(container, id, fileName, statusTextValue) {
    var item = document.createElement('div');
    item.className = 'file-item';
    item.id = id;

    var name = document.createElement('span');
    name.className = 'file-name';
    name.textContent = fileName || '';

    var status = document.createElement('span');
    status.className = 'file-status';
    status.textContent = statusTextValue || '';

    item.appendChild(name);
    item.appendChild(status);
    container.appendChild(item);
    return item;
  }

  function setDownloadStatus(statusElement, label, url, filename, downloadText) {
    clearElement(statusElement);
    if (label) {
      var rate = document.createElement('span');
      rate.className = 'compression-rate';
      rate.textContent = label;
      statusElement.appendChild(rate);
      statusElement.appendChild(document.createTextNode(' '));
    }
    var link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', sanitizeDownloadFilename(filename, 'download'));
    link.className = 'btn btn-ghost btn-sm';
    link.textContent = downloadText || 'Download';
    statusElement.appendChild(link);
  }

  function appendCheckIcon(element) {
    var svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('width', '16');
    svg.setAttribute('height', '16');
    svg.setAttribute('viewBox', '0 0 24 24');
    svg.setAttribute('fill', 'none');
    svg.setAttribute('stroke', 'currentColor');
    svg.setAttribute('stroke-width', '2');
    svg.setAttribute('stroke-linecap', 'round');
    svg.setAttribute('stroke-linejoin', 'round');
    var polyline = document.createElementNS('http://www.w3.org/2000/svg', 'polyline');
    polyline.setAttribute('points', '20 6 9 17 4 12');
    svg.appendChild(polyline);
    element.appendChild(svg);
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
    copyText(text).then(function (copied) {
      if (!copied && !fallbackCopyFromField(outputEditor)) return;
      var originalNodes = Array.prototype.map.call(btnCopy.childNodes, function (node) {
        return node.cloneNode(true);
      });
      var i18n = window.I18N || {};
      btnCopy.classList.add('copied');
      clearElement(btnCopy);
      appendCheckIcon(btnCopy);
      btnCopy.appendChild(document.createTextNode(' ' + (i18n.copied || 'Copied!')));
      setTimeout(function () {
        clearElement(btnCopy);
        originalNodes.forEach(function (node) {
          btnCopy.appendChild(node);
        });
        btnCopy.classList.remove('copied');
      }, 2000);
    }).catch(function () {
      fallbackCopyFromField(outputEditor);
    });
  }

  function downloadOutput(outputEditor, filename) {
    var text = outputEditor.value;
    if (!text) return;
    var blob = new Blob([text], { type: 'text/plain' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = sanitizeDownloadFilename(filename, 'output.txt');
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
      copyText(code).then(function (copied) {
        if (!copied) return;
        exampleCopy.textContent = i18n.copied || 'Copied!';
        setTimeout(function () {
          exampleCopy.textContent = i18n.copy || 'Copy';
        }, 2000);
      }).catch(function () {});
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

  function initInteractiveControls(root) {
    var scope = root || document;
    var controls = scope.querySelectorAll('#btn-convert, [role="button"]');

    controls.forEach(function (control) {
      if (/^(BUTTON|A|INPUT|SELECT|TEXTAREA)$/.test(control.tagName)) return;

      if (!control.hasAttribute('role')) control.setAttribute('role', 'button');
      if (!control.hasAttribute('tabindex')) control.setAttribute('tabindex', '0');
      if (!control.hasAttribute('aria-label') && control.getAttribute('title')) {
        control.setAttribute('aria-label', control.getAttribute('title'));
      }
    });
  }

  document.addEventListener('keydown', function (e) {
    if (e.defaultPrevented) return;

    var control = e.target.closest('[role="button"], #btn-convert');
    if (!control || /^(BUTTON|A|INPUT|SELECT|TEXTAREA)$/.test(control.tagName)) return;
    if (control.getAttribute('aria-disabled') === 'true' || control.hasAttribute('disabled')) return;
    if (e.key !== 'Enter' && e.key !== ' ') return;

    e.preventDefault();
    control.click();
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      initInteractiveControls(document);
    });
  } else {
    initInteractiveControls(document);
  }

  return {
    countLines: countLines,
    pluralise: pluralise,
    updateLineNumbers: updateLineNumbers,
    updateStatus: updateStatus,
    clearElement: clearElement,
    sanitizeDownloadFilename: sanitizeDownloadFilename,
    appendFileStatusItem: appendFileStatusItem,
    setDownloadStatus: setDownloadStatus,
    copyText: copyText,
    clearEditors: clearEditors,
    copyOutput: copyOutput,
    downloadOutput: downloadOutput,
    initExampleCopy: initExampleCopy,
    initTabKey: initTabKey,
    initScrollSync: initScrollSync,
    initInputLineNumbers: initInputLineNumbers,
    initKeyboardShortcut: initKeyboardShortcut,
    initInteractiveControls: initInteractiveControls
  };
})();
