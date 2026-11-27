/* ============================================================
   Tool Common — Shared helpers for all tool pages
   ============================================================ */
var ToolCommon = (function () {
  'use strict';

  function editorBytes(editor) {
    return editor.importedBytes || new TextEncoder().encode(editor.value);
  }

  async function hashBytes(algorithm, bytes) {
    if (algorithm === 'MD5') return window.md5(bytes);
    var buffer = await crypto.subtle.digest(algorithm, bytes);
    return Array.from(new Uint8Array(buffer), function (byte) {
      return byte.toString(16).padStart(2, '0');
    }).join('');
  }

  function loadImage(file) {
    return new Promise(function (resolve, reject) {
      var reader = new FileReader();
      reader.onload = function (event) {
        var image = new Image();
        image.onload = function () {
          resolve({ image: image, dataUrl: event.target.result });
        };
        image.onerror = function () { reject(new Error(window.CodingToolsRuntimeI18n.invalidInput)); };
        image.src = event.target.result;
      };
      reader.onerror = function () { reject(new Error(window.CodingToolsRuntimeI18n.invalidInput)); };
      reader.readAsDataURL(file);
    });
  }

  function bytesToBase64(bytes) {
    var chunks = [];
    for (var i = 0; i < bytes.length; i += 0x8000) {
      chunks.push(String.fromCharCode.apply(null, bytes.subarray(i, i + 0x8000)));
    }
    return btoa(chunks.join(''));
  }

  function regexMatches(text, regex) {
    var matches = [];
    var found = regex.global ? text.matchAll(regex) : [regex.exec(text)];
    for (var match of found) {
      if (!match) break;
      matches.push({ index: match.index, length: match[0].length, value: match[0] });
      if (matches.length >= 10000) break;
    }
    return matches;
  }

  function reverseText(text) {
    if (!Intl.Segmenter) return Array.from(text).reverse().join('');
    var segments = new Intl.Segmenter(undefined, { granularity: 'grapheme' }).segment(text);
    return Array.from(segments, function (part) { return part.segment; }).reverse().join('');
  }

  function titleCase(text) {
    return text.toLowerCase().replace(/(^|[^\p{L}\p{M}\p{N}_])(\p{L})/gu, function (_, prefix, letter) {
      return prefix + letter.toUpperCase();
    });
  }

  function countWords(text) {
    if (!Intl.Segmenter) return (text.match(/[\p{L}\p{N}]+/gu) || []).length;
    var segments = new Intl.Segmenter(document.documentElement.lang, { granularity: 'word' }).segment(text);
    var count = 0;
    for (var part of segments) {
      if (part.isWordLike) count++;
    }
    return count;
  }

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
    if (inputEditor) {
      inputEditor.value = '';
      delete inputEditor.importedBytes;
    }
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
    var label = textarea.closest('.tool-editor-input')?.querySelector('.pane-label');
    if (label) {
      var hint = document.createElement('span');
      hint.className = 'editor-keyboard-hint';
      hint.id = textarea.id + '-keyboard-hint';
      hint.textContent = window.CodingToolsRuntimeI18n.leaveEditor;
      label.append(hint);
      textarea.setAttribute('aria-describedby', hint.id);
    }
    var leaveEditor = false;
    textarea.addEventListener('blur', function () { leaveEditor = false; });
    textarea.addEventListener('keydown', function (event) {
      if (event.key === 'Tab' && !event.shiftKey && !leaveEditor) {
        event.preventDefault();
        this.setRangeText('  ', this.selectionStart, this.selectionEnd, 'end');
        this.dispatchEvent(new Event('input', { bubbles: true }));
        if (lineNumsContainer) updateLineNumbers(this, lineNumsContainer);
      }
      leaveEditor = event.key === 'Escape';
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
    btnAction.setAttribute('aria-keyshortcuts', 'Control+Enter Meta+Enter');
    btnAction.dataset.shortcut = /Mac|iPhone|iPad/.test(navigator.platform) ? '⌘ ↵' : 'Ctrl ↵';
    document.addEventListener('keydown', function (e) {
      if ((e.ctrlKey || e.metaKey) && e.key === 'Enter' && !btnAction.disabled && btnAction.getClientRects().length) {
        e.preventDefault();
        btnAction.click();
      }
    });
  }

  function addFileToZip(zip, filename, content) {
    var used = new Set(Object.keys(zip.files).map(function (entry) { return entry.toLowerCase(); }));
    var dot = filename.lastIndexOf('.');
    var stem = dot > 0 ? filename.slice(0, dot) : filename;
    var extension = dot > 0 ? filename.slice(dot) : '';
    var name = filename;
    for (var n = 2; used.has(name.toLowerCase()); n++) {
      name = stem + '-' + n + extension;
    }
    zip.file(name, content);
  }

  function offerMapPreview(container, frame, label) {
    var button = document.createElement('button');
    button.type = 'button';
    button.className = 'btn btn-ghost';
    button.textContent = label;
    frame.title = label;
    frame.referrerPolicy = 'no-referrer';
    button.addEventListener('click', function () {
      button.replaceWith(frame);
    });
    container.appendChild(button);
  }

  function trackToolSuccess(operation) {
    if (typeof window.gtag === 'function') {
      window.gtag('event', 'tool_success', {
        tool_id: document.body.dataset.tool,
        tool_language: document.body.dataset.lang,
        operation: operation
      });
    }
  }

  function initInteractiveControls(root) {
    var scope = root || document;
    // Keep result actions beside the result, including in keyboard navigation order.
    var output = scope.querySelector('.tool-editor-output');
    var resultActions = scope.querySelector('.tool-editor-actions .tool-result-actions');
    if (output && resultActions) output.after(resultActions);

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
    trackToolSuccess: trackToolSuccess,
    offerMapPreview: offerMapPreview,
    addFileToZip: addFileToZip,
    editorBytes: editorBytes,
    hashBytes: hashBytes,
    loadImage: loadImage,
    bytesToBase64: bytesToBase64,
    regexMatches: regexMatches,
    reverseText: reverseText,
    titleCase: titleCase,
    countWords: countWords,
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
