(function () {
  "use strict";

  var MAX_SIZE = 10 * 1024 * 1024;
  var labelsNode = document.getElementById("image-tool-labels");
  var L = labelsNode ? JSON.parse(labelsNode.textContent) : {};
  var state = { file: null, image: null, originalUrl: "", resultUrl: "", blob: null, mime: "image/png", name: "image" };
  var dropzone = document.getElementById("dropzone");
  var fileInput = document.getElementById("file-input");
  var originalPreview = document.getElementById("original-preview");
  var resultPreview = document.getElementById("result-preview");
  var widthInput = document.getElementById("width-input");
  var heightInput = document.getElementById("height-input");
  var aspectInput = document.getElementById("aspect-input");
  var percentInput = document.getElementById("percent-input");
  var qualityInput = document.getElementById("quality-input");
  var qualityValue = document.getElementById("quality-value");
  var btnClear = document.getElementById("btn-clear");
  var btnDownload = document.getElementById("btn-download");
  var originalSize = document.getElementById("original-size");
  var outputSize = document.getElementById("output-size");
  var dimensionMeta = document.getElementById("dimension-meta");
  var formatMeta = document.getElementById("format-meta");
  var fileSizeMeta = document.getElementById("file-size-meta");
  var statusMessage = document.getElementById("status-message");
  var statusDot = document.getElementById("status-dot");
  var statusText = document.getElementById("status-text");
  var controls = [widthInput, heightInput, aspectInput, percentInput, qualityInput].concat(Array.from(document.querySelectorAll("[data-preset], [data-size]")));
  var updating = false;
  var timer = null;

  function setStatus(type, text) {
    ToolCommon.updateStatus(statusMessage, statusDot, statusText, type, text);
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

  function baseName(name) {
    return (name || "image").replace(/\.[^.]+$/, "");
  }

  function supportedMime(file) {
    return ["image/png", "image/jpeg", "image/webp"].indexOf(file.type) !== -1 ? file.type : "image/png";
  }

  function enableControls(enabled) {
    controls.forEach(function (control) {
      control.disabled = !enabled;
    });
  }

  function scheduleRender() {
    clearTimeout(timer);
    timer = setTimeout(renderResult, 80);
  }

  function resetUrls() {
    if (state.resultUrl) URL.revokeObjectURL(state.resultUrl);
    state.resultUrl = "";
    state.blob = null;
  }

  function syncPercent() {
    if (!state.image) return;
    var percent = Math.round((Number(widthInput.value) || state.image.width) / state.image.width * 100);
    percentInput.value = Math.max(1, Math.min(400, percent));
  }

  function setBlob(blob, width, height, mime) {
    if (state.resultUrl) URL.revokeObjectURL(state.resultUrl);
    state.blob = blob;
    state.mime = mime || state.mime;
    state.resultUrl = URL.createObjectURL(blob);
    resultPreview.src = state.resultUrl;
    outputSize.textContent = formatBytes(blob.size);
    dimensionMeta.textContent = width + " x " + height;
    formatMeta.textContent = state.mime.replace("image/", "").toUpperCase();
    btnDownload.disabled = false;
    setStatus("valid", L.updated);
  }

  function exportPng(canvas) {
    canvas.toBlob(function (blob) {
      if (blob) setBlob(blob, canvas.width, canvas.height, "image/png");
    }, "image/png");
  }

  function renderResult() {
    if (!state.image) return;
    var width = Math.max(1, Math.round(Number(widthInput.value) || state.image.width));
    var height = Math.max(1, Math.round(Number(heightInput.value) || state.image.height));
    var canvas = document.createElement("canvas");
    var ctx = canvas.getContext("2d");
    canvas.width = width;
    canvas.height = height;
    if (state.mime === "image/jpeg") {
      ctx.fillStyle = "#fff";
      ctx.fillRect(0, 0, width, height);
    }
    ctx.imageSmoothingEnabled = true;
    ctx.imageSmoothingQuality = "high";
    ctx.drawImage(state.image, 0, 0, width, height);
    canvas.toBlob(function (blob) {
      if (!blob) {
        exportPng(canvas);
        return;
      }
      if (state.mime !== "image/png" && blob.type && blob.type !== state.mime) {
        exportPng(canvas);
        return;
      }
      setBlob(blob, width, height, blob.type || state.mime);
    }, state.mime, Number(qualityInput.value) / 100);
  }

  function loadFile(file) {
    if (["image/png", "image/jpeg", "image/webp"].indexOf(file.type) === -1) {
      setStatus("invalid", L.invalidFile);
      return;
    }
    if (file.size > MAX_SIZE) {
      setStatus("invalid", L.tooLarge);
      return;
    }
    resetUrls();
    setStatus("idle", L.processing);
    var reader = new FileReader();
    reader.onload = function (event) {
      var image = new Image();
      image.onload = function () {
        state.file = file;
        state.image = image;
        state.originalUrl = event.target.result;
        state.mime = supportedMime(file);
        state.name = file.name;
        originalPreview.src = state.originalUrl;
        updating = true;
        widthInput.value = image.width;
        heightInput.value = image.height;
        percentInput.value = 100;
        updating = false;
        originalSize.textContent = image.width + " x " + image.height;
        fileSizeMeta.textContent = formatBytes(file.size);
        formatMeta.textContent = state.mime.replace("image/", "").toUpperCase();
        enableControls(true);
        renderResult();
        setStatus("valid", L.loaded);
      };
      image.onerror = function () {
        setStatus("invalid", L.invalidFile);
      };
      image.src = event.target.result;
    };
    reader.readAsDataURL(file);
  }

  function reset() {
    resetUrls();
    state = { file: null, image: null, originalUrl: "", resultUrl: "", blob: null, mime: "image/png", name: "image" };
    originalPreview.removeAttribute("src");
    resultPreview.removeAttribute("src");
    widthInput.value = "";
    heightInput.value = "";
    percentInput.value = 100;
    qualityInput.value = 90;
    qualityValue.textContent = "90%";
    originalSize.textContent = "-";
    outputSize.textContent = "-";
    dimensionMeta.textContent = "-";
    formatMeta.textContent = "-";
    fileSizeMeta.textContent = "-";
    btnDownload.disabled = true;
    enableControls(false);
    setStatus("idle", L.ready);
  }

  dropzone.addEventListener("click", function () { fileInput.click(); });
  dropzone.addEventListener("keydown", function (event) {
    if (event.key === "Enter" || event.key === " ") {
      event.preventDefault();
      fileInput.click();
    }
  });
  dropzone.addEventListener("dragover", function (event) {
    event.preventDefault();
    dropzone.classList.add("dragover");
  });
  dropzone.addEventListener("dragleave", function () { dropzone.classList.remove("dragover"); });
  dropzone.addEventListener("drop", function (event) {
    event.preventDefault();
    dropzone.classList.remove("dragover");
    if (event.dataTransfer.files[0]) loadFile(event.dataTransfer.files[0]);
  });
  fileInput.addEventListener("change", function () {
    if (this.files[0]) loadFile(this.files[0]);
    this.value = "";
  });
  widthInput.addEventListener("input", function () {
    if (!state.image || updating) return;
    var width = Math.max(1, Math.round(Number(widthInput.value) || 1));
    if (aspectInput.checked) {
      updating = true;
      heightInput.value = Math.max(1, Math.round(width / (state.image.width / state.image.height)));
      updating = false;
    }
    syncPercent();
    scheduleRender();
  });
  heightInput.addEventListener("input", function () {
    if (!state.image || updating) return;
    var height = Math.max(1, Math.round(Number(heightInput.value) || 1));
    if (aspectInput.checked) {
      updating = true;
      widthInput.value = Math.max(1, Math.round(height * (state.image.width / state.image.height)));
      updating = false;
    }
    syncPercent();
    scheduleRender();
  });
  percentInput.addEventListener("input", function () {
    if (!state.image || updating) return;
    var percent = Math.max(1, Math.min(400, Number(percentInput.value) || 1));
    updating = true;
    widthInput.value = Math.max(1, Math.round(state.image.width * percent / 100));
    heightInput.value = Math.max(1, Math.round(state.image.height * percent / 100));
    updating = false;
    scheduleRender();
  });
  qualityInput.addEventListener("input", function () {
    qualityValue.textContent = qualityInput.value + "%";
    scheduleRender();
  });
  document.querySelectorAll("[data-preset]").forEach(function (button) {
    button.addEventListener("click", function () {
      percentInput.value = button.dataset.preset;
      percentInput.dispatchEvent(new Event("input"));
    });
  });
  document.querySelectorAll("[data-size]").forEach(function (button) {
    button.addEventListener("click", function () {
      if (!state.image) return;
      var parts = button.dataset.size.split("x").map(Number);
      updating = true;
      widthInput.value = parts[0];
      heightInput.value = aspectInput.checked ? Math.max(1, Math.round(parts[0] / (state.image.width / state.image.height))) : parts[1];
      updating = false;
      syncPercent();
      scheduleRender();
    });
  });
  btnClear.addEventListener("click", reset);
  btnDownload.addEventListener("click", function () {
    if (!state.blob) {
      setStatus("invalid", L.noImage);
      return;
    }
    var link = document.createElement("a");
    link.href = state.resultUrl;
    link.download = baseName(state.name) + "-resized." + extensionFor(state.mime);
    link.click();
  });

  ToolCommon.initExampleCopy();
})();
