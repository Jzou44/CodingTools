(function () {
  "use strict";

  var MAX_SIZE = 10 * 1024 * 1024;
  var MIN_CROP = 10;
  var labelsNode = document.getElementById("image-tool-labels");
  var L = labelsNode ? JSON.parse(labelsNode.textContent) : {};
  var state = { file: null, image: null, resultUrl: "", blob: null, mime: "image/png", name: "image", crop: null, drag: null };
  var dropzone = document.getElementById("dropzone");
  var fileInput = document.getElementById("file-input");
  var stage = document.getElementById("crop-stage");
  var cropImage = document.getElementById("crop-image");
  var overlay = document.getElementById("crop-overlay");
  var resultPreview = document.getElementById("result-preview");
  var ratioSelect = document.getElementById("ratio-select");
  var xInput = document.getElementById("x-input");
  var yInput = document.getElementById("y-input");
  var widthInput = document.getElementById("width-input");
  var heightInput = document.getElementById("height-input");
  var qualityInput = document.getElementById("quality-input");
  var qualityValue = document.getElementById("quality-value");
  var btnReset = document.getElementById("btn-reset");
  var btnDownload = document.getElementById("btn-download");
  var originalSize = document.getElementById("original-size");
  var outputSize = document.getElementById("output-size");
  var cropMeta = document.getElementById("crop-meta");
  var formatMeta = document.getElementById("format-meta");
  var fileSizeMeta = document.getElementById("file-size-meta");
  var statusMessage = document.getElementById("status-message");
  var statusDot = document.getElementById("status-dot");
  var statusText = document.getElementById("status-text");
  var controls = [ratioSelect, xInput, yInput, widthInput, heightInput, qualityInput, btnReset];
  var syncing = false;
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

  function ratioValue() {
    return ratioSelect.value === "free" ? null : Number(ratioSelect.value);
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

  function resetResultUrl() {
    if (state.resultUrl) URL.revokeObjectURL(state.resultUrl);
    state.resultUrl = "";
    state.blob = null;
  }

  function clampCrop(crop, preserveRatio) {
    var image = state.image;
    var ratio = preserveRatio ? ratioValue() : null;
    crop.width = Math.max(MIN_CROP, Math.min(image.width, crop.width));
    crop.height = Math.max(MIN_CROP, Math.min(image.height, crop.height));
    if (ratio) {
      if (crop.width / crop.height > ratio) crop.width = crop.height * ratio;
      else crop.height = crop.width / ratio;
    }
    if (crop.width > image.width) crop.width = image.width;
    if (crop.height > image.height) crop.height = image.height;
    crop.x = Math.max(0, Math.min(image.width - crop.width, crop.x));
    crop.y = Math.max(0, Math.min(image.height - crop.height, crop.y));
    return {
      x: Math.round(crop.x),
      y: Math.round(crop.y),
      width: Math.round(crop.width),
      height: Math.round(crop.height)
    };
  }

  function setInitialCrop() {
    var ratio = ratioValue();
    var image = state.image;
    var width = Math.round(image.width * 0.8);
    var height = Math.round(image.height * 0.8);
    if (ratio) {
      if (width / height > ratio) width = Math.round(height * ratio);
      else height = Math.round(width / ratio);
    }
    state.crop = {
      x: Math.round((image.width - width) / 2),
      y: Math.round((image.height - height) / 2),
      width: width,
      height: height
    };
  }

  function imageRect() {
    var rect = cropImage.getBoundingClientRect();
    var stageRect = stage.getBoundingClientRect();
    return {
      left: rect.left - stageRect.left,
      top: rect.top - stageRect.top,
      width: rect.width,
      height: rect.height,
      scaleX: state.image.width / rect.width,
      scaleY: state.image.height / rect.height
    };
  }

  function renderCropBox() {
    if (!state.image || !state.crop) return;
    var rect = imageRect();
    overlay.classList.add("is-visible");
    overlay.style.left = (rect.left + state.crop.x / rect.scaleX) + "px";
    overlay.style.top = (rect.top + state.crop.y / rect.scaleY) + "px";
    overlay.style.width = (state.crop.width / rect.scaleX) + "px";
    overlay.style.height = (state.crop.height / rect.scaleY) + "px";
  }

  function syncFields() {
    if (!state.crop) return;
    syncing = true;
    xInput.value = state.crop.x;
    yInput.value = state.crop.y;
    widthInput.value = state.crop.width;
    heightInput.value = state.crop.height;
    cropMeta.textContent = state.crop.x + ", " + state.crop.y + " / " + state.crop.width + " x " + state.crop.height;
    syncing = false;
  }

  function setBlob(blob, width, height, mime) {
    resetResultUrl();
    state.blob = blob;
    state.mime = mime || state.mime;
    state.resultUrl = URL.createObjectURL(blob);
    resultPreview.src = state.resultUrl;
    outputSize.textContent = formatBytes(blob.size) + " / " + width + " x " + height;
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
    if (!state.image || !state.crop) return;
    var crop = clampCrop(Object.assign({}, state.crop), false);
    var canvas = document.createElement("canvas");
    var ctx = canvas.getContext("2d");
    canvas.width = crop.width;
    canvas.height = crop.height;
    if (state.mime === "image/jpeg") {
      ctx.fillStyle = "#fff";
      ctx.fillRect(0, 0, canvas.width, canvas.height);
    }
    ctx.imageSmoothingEnabled = true;
    ctx.imageSmoothingQuality = "high";
    ctx.drawImage(state.image, crop.x, crop.y, crop.width, crop.height, 0, 0, crop.width, crop.height);
    canvas.toBlob(function (blob) {
      if (!blob) {
        exportPng(canvas);
        return;
      }
      if (state.mime !== "image/png" && blob.type && blob.type !== state.mime) {
        exportPng(canvas);
        return;
      }
      setBlob(blob, crop.width, crop.height, blob.type || state.mime);
    }, state.mime, Number(qualityInput.value) / 100);
  }

  function applyRatio() {
    if (!state.crop) return;
    var ratio = ratioValue();
    if (!ratio) return;
    var centerX = state.crop.x + state.crop.width / 2;
    var centerY = state.crop.y + state.crop.height / 2;
    var width = state.crop.width;
    var height = width / ratio;
    if (height > state.image.height) {
      height = state.image.height;
      width = height * ratio;
    }
    if (width > state.image.width) {
      width = state.image.width;
      height = width / ratio;
    }
    state.crop = clampCrop({ x: centerX - width / 2, y: centerY - height / 2, width: width, height: height }, false);
  }

  function fieldsToCrop() {
    if (!state.image || syncing) return;
    state.crop = clampCrop({
      x: Number(xInput.value) || 0,
      y: Number(yInput.value) || 0,
      width: Number(widthInput.value) || MIN_CROP,
      height: Number(heightInput.value) || MIN_CROP
    }, true);
    syncFields();
    renderCropBox();
    scheduleRender();
  }

  function beginDrag(event) {
    if (!state.crop) return;
    event.preventDefault();
    overlay.setPointerCapture(event.pointerId);
    var rect = imageRect();
    state.drag = {
      pointerId: event.pointerId,
      handle: event.target.dataset.handle || "move",
      startX: event.clientX,
      startY: event.clientY,
      startCrop: Object.assign({}, state.crop),
      scaleX: rect.scaleX,
      scaleY: rect.scaleY
    };
    overlay.addEventListener("pointermove", onDrag);
    overlay.addEventListener("pointerup", endDrag);
    overlay.addEventListener("pointercancel", endDrag);
  }

  function onDrag(event) {
    if (!state.drag) return;
    var dx = (event.clientX - state.drag.startX) * state.drag.scaleX;
    var dy = (event.clientY - state.drag.startY) * state.drag.scaleY;
    var crop = Object.assign({}, state.drag.startCrop);
    var handle = state.drag.handle;
    if (handle === "move") {
      crop.x += dx;
      crop.y += dy;
    } else {
      if (handle.indexOf("w") !== -1) {
        crop.x += dx;
        crop.width -= dx;
      }
      if (handle.indexOf("e") !== -1) crop.width += dx;
      if (handle.indexOf("n") !== -1) {
        crop.y += dy;
        crop.height -= dy;
      }
      if (handle.indexOf("s") !== -1) crop.height += dy;
      var ratio = ratioValue();
      if (ratio) {
        if (handle === "n" || handle === "s") crop.width = crop.height * ratio;
        else crop.height = crop.width / ratio;
        if (handle.indexOf("w") !== -1) crop.x = state.drag.startCrop.x + state.drag.startCrop.width - crop.width;
        if (handle.indexOf("n") !== -1) crop.y = state.drag.startCrop.y + state.drag.startCrop.height - crop.height;
      }
    }
    state.crop = clampCrop(crop, false);
    syncFields();
    renderCropBox();
    scheduleRender();
  }

  function endDrag() {
    if (state.drag && overlay.hasPointerCapture(state.drag.pointerId)) overlay.releasePointerCapture(state.drag.pointerId);
    state.drag = null;
    overlay.removeEventListener("pointermove", onDrag);
    overlay.removeEventListener("pointerup", endDrag);
    overlay.removeEventListener("pointercancel", endDrag);
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
    resetResultUrl();
    setStatus("idle", L.processing);
    var reader = new FileReader();
    reader.onload = function (event) {
      var image = new Image();
      image.onload = function () {
        state.file = file;
        state.image = image;
        state.mime = supportedMime(file);
        state.name = file.name;
        cropImage.src = event.target.result;
        cropImage.onload = function () {
          setInitialCrop();
          syncFields();
          renderCropBox();
          renderResult();
        };
        originalSize.textContent = image.width + " x " + image.height;
        fileSizeMeta.textContent = formatBytes(file.size);
        formatMeta.textContent = state.mime.replace("image/", "").toUpperCase();
        enableControls(true);
        setStatus("valid", L.loaded);
      };
      image.onerror = function () {
        setStatus("invalid", L.invalidFile);
      };
      image.src = event.target.result;
    };
    reader.readAsDataURL(file);
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
  window.addEventListener("resize", renderCropBox);
  qualityInput.addEventListener("input", function () {
    qualityValue.textContent = qualityInput.value + "%";
    scheduleRender();
  });
  ratioSelect.addEventListener("change", function () {
    applyRatio();
    syncFields();
    renderCropBox();
    renderResult();
  });
  [xInput, yInput, widthInput, heightInput].forEach(function (input) {
    input.addEventListener("input", fieldsToCrop);
  });
  btnReset.addEventListener("click", function () {
    if (!state.image) return;
    setInitialCrop();
    syncFields();
    renderCropBox();
    renderResult();
  });
  btnDownload.addEventListener("click", function () {
    if (!state.blob) {
      setStatus("invalid", L.noImage);
      return;
    }
    var link = document.createElement("a");
    link.href = state.resultUrl;
    link.download = baseName(state.name) + "-cropped." + extensionFor(state.mime);
    link.click();
  });
  overlay.addEventListener("pointerdown", beginDrag);

  ToolCommon.initExampleCopy();
})();
