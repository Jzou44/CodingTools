(() => {
  "use strict";

  const labels = window.CodingToolsRuntimeI18n;
  const fileInput = document.getElementById("file-input");
  const dropzone = document.getElementById("dropzone");
  const fileList = document.getElementById("file-list");
  const downloadAll = document.getElementById("btn-download-all");
  const fileCount = document.getElementById("file-count");
  const status = document.getElementById("status-message");
  const dot = document.getElementById("status-dot");
  const statusText = document.getElementById("status-text");
  const maxFiles = 20;
  const maxBytes = 10 * 1024 * 1024;
  const pending = [];
  let active = null;
  let worker = null;
  let results = [];
  let packing = false;

  function showStatus(type, message) {
    ToolCommon.updateStatus(status, dot, statusText, type, message);
  }

  function refreshDownloads() {
    downloadAll.disabled = !!active || pending.length > 0 || packing || results.length === 0;
    fileCount.textContent = results.length + " " + labels.files;
  }

  function stopWorker() {
    if (worker) worker.terminate();
    worker = null;
  }

  function finish(bytes, errorMessage) {
    if (bytes) {
      const file = active.file;
      const blob = new Blob([bytes], { type: "image/jpeg" });
      const name = ToolCommon.sanitizeDownloadFilename(file.name.replace(/\.jpe?g$/i, "") + "-progressive.jpg");
      const url = URL.createObjectURL(blob);
      const change = ((blob.size - file.size) * 100 / file.size).toFixed(1) + "%";
      results.push({ name, blob, url });
      ToolCommon.setDownloadStatus(active.status, change, url, name, labels.download);
      showStatus("valid", results.length + " " + labels.filesProcessed);
    } else {
      active.status.textContent = errorMessage;
      showStatus("invalid", errorMessage);
    }
    active = null;
    if (!pending.length) stopWorker();
    refreshDownloads();
    processNext();
  }

  async function readPixels(file) {
    const signature = new Uint8Array(await file.slice(0, 2).arrayBuffer());
    if (signature[0] !== 0xff || signature[1] !== 0xd8) throw new Error(labels.unsupportedImageType);
    const url = URL.createObjectURL(file);
    try {
      const image = new Image();
      image.src = url;
      await image.decode();
      const canvas = document.createElement("canvas");
      canvas.width = image.naturalWidth;
      canvas.height = image.naturalHeight;
      const ctx = canvas.getContext("2d");
      ctx.drawImage(image, 0, 0);
      return ctx.getImageData(0, 0, canvas.width, canvas.height);
    } finally {
      URL.revokeObjectURL(url);
    }
  }

  async function processNext() {
    if (active || !pending.length) return;
    const job = pending.shift();
    active = job;
    try {
      const pixels = await readPixels(job.file);
      if (active !== job) return; // The queue was cleared during decode.
      if (!worker) worker = new Worker("/js/progressive-jpeg-worker.js", { type: "module" });
      worker.onmessage = event => {
        if (active === job) finish(event.data, labels.invalidInput);
      };
      worker.onerror = () => {
        if (active !== job) return;
        stopWorker();
        finish(null, labels.invalidInput);
      };
      worker.postMessage({ data: pixels.data, width: pixels.width, height: pixels.height }, [pixels.data.buffer]);
    } catch (error) {
      if (active === job) finish(null, error.message === labels.unsupportedImageType ? error.message : labels.invalidInput);
    }
  }

  function addFiles(files) {
    const available = maxFiles - results.length - pending.length - (active ? 1 : 0);
    for (const file of Array.from(files).slice(0, available)) {
      const row = ToolCommon.appendFileStatusItem(fileList, "file-" + fileList.childElementCount, file.name, labels.processing);
      const fileStatus = row.querySelector(".file-status");
      if (file.size > maxBytes) {
        fileStatus.textContent = labels.fileTooLarge + " 10 MB";
        showStatus("invalid", fileStatus.textContent);
      } else {
        pending.push({ file, status: fileStatus });
      }
    }
    if (files.length > available) showStatus("invalid", labels.skippedFileLimit.replace("{max}", maxFiles));
    refreshDownloads();
    processNext();
  }

  dropzone.addEventListener("click", () => fileInput.click());
  dropzone.addEventListener("dragover", event => {
    event.preventDefault();
    dropzone.classList.add("dragover");
  });
  dropzone.addEventListener("dragleave", () => dropzone.classList.remove("dragover"));
  dropzone.addEventListener("drop", event => {
    event.preventDefault();
    dropzone.classList.remove("dragover");
    addFiles(event.dataTransfer.files);
  });
  fileInput.addEventListener("change", () => {
    addFiles(fileInput.files);
    fileInput.value = "";
  });
  document.getElementById("btn-clear").addEventListener("click", () => {
    stopWorker();
    active = null;
    pending.length = 0;
    results.forEach(item => URL.revokeObjectURL(item.url));
    results = [];
    packing = false;
    fileList.replaceChildren();
    refreshDownloads();
    showStatus("idle", "");
  });

  function download(url, name) {
    const link = document.createElement("a");
    link.href = url;
    link.download = name;
    link.click();
  }

  downloadAll.addEventListener("click", async () => {
    if (downloadAll.disabled) return;
    if (results.length === 1) {
      download(results[0].url, results[0].name);
      return;
    }
    const batch = results;
    packing = true;
    refreshDownloads();
    try {
      const zip = new JSZip();
      batch.forEach(item => ToolCommon.addFileToZip(zip, item.name, item.blob));
      const blob = await zip.generateAsync({ type: "blob" });
      if (results !== batch) return;
      const url = URL.createObjectURL(blob);
      download(url, "progressive-jpeg.zip");
      setTimeout(() => URL.revokeObjectURL(url), 1000);
    } catch {
      if (results === batch) showStatus("invalid", labels.error);
    } finally {
      if (results === batch) {
        packing = false;
        refreshDownloads();
      }
    }
  });
  ToolCommon.initExampleCopy();
})();
