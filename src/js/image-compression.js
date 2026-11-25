import { compressJpeg } from "./compress-jpeg-image.js";

const byId = id => document.getElementById(id);
const labels = window.CodingToolsRuntimeI18n;
const input = byId("file-input");
const options = byId("jpeg-options");
const dropzone = byId("dropzone");
const list = byId("file-list");
const all = byId("btn-download-all");
const originalLabel = byId("compression-queue").dataset.original;
const maxFiles = 20;
const entries = [];
let controller = new AbortController();
let busy = false;
let packing = false;
let timer;

function status(type, message) {
  ToolCommon.updateStatus(byId("status-message"), byId("status-dot"), byId("status-text"), type, message);
}

function refresh() {
  const count = entries.filter(entry => entry.url).length;
  all.disabled = busy || packing || !count || entries.some(entry => entry.pending);
  byId("file-count").textContent = count + " " + labels.files;
}

function readSettings() {
  if (!options) return {};
  const mode = byId("compression-mode").value;
  const quality = Number(byId("jpeg-quality").value);
  const custom = byId("target-kb");
  if (mode === "custom" && (!custom.validity.valid || !Number.isSafeInteger(custom.valueAsNumber * 1000))) return null;
  const kb = mode === "custom" ? custom.valueAsNumber : Number(mode);
  return { quality, limit: mode === "quality" ? 0 : kb * 1000, resize: byId("allow-resize").checked };
}

async function compressPng(file, signal) {
  // One file per worker bounds WASM memory and lets Clear stop an active encode.
  const worker = new Worker("/js/compress-png-worker.js", { type: "module" });
  let cancel;
  try {
    return await new Promise((resolve, reject) => {
      cancel = () => reject(signal.reason);
      signal.addEventListener("abort", cancel, { once: true });
      worker.onerror = () => reject(new Error("PNG worker failed"));
      worker.onmessage = ({ data }) => {
        if (data.error) reject(new Error("Invalid PNG"));
        else resolve({ blob: data.original ? file : new Blob([data.bytes], { type: "image/png" }) });
      };
      worker.postMessage(file);
    });
  } finally {
    signal.removeEventListener("abort", cancel);
    worker.terminate();
  }
}

function showResult(entry, result) {
  if (result.unmet) {
    entry.status.textContent = options.dataset.unmet + " (" + result.unmet.toLocaleString() + " B)";
    status("invalid", entry.status.textContent);
    return;
  }
  const blob = result.blob;
  entry.blob = blob;
  entry.url = URL.createObjectURL(blob);
  const percent = ((entry.file.size - blob.size) * 100 / entry.file.size).toFixed(1);
  const info = [entry.file.size.toLocaleString() + " B → " + blob.size.toLocaleString() + " B",
    blob === entry.file ? originalLabel : "−" + percent + "%"];
  if (result.width) info.push(result.width + " × " + result.height);
  ToolCommon.setDownloadStatus(entry.status, info.join(" · "), entry.url, entry.name, labels.download);
  status("valid", entries.filter(item => item.url).length + " " + labels.filesProcessed);
}

async function processQueue() {
  if (busy) return;
  const settings = readSettings();
  if (!settings) {
    for (const entry of entries) entry.status.textContent = labels.invalidInput;
    status("invalid", labels.invalidInput);
    refresh();
    return;
  }
  const signal = controller.signal;
  busy = true;
  refresh();
  try {
    for (const entry of entries) {
      if (!entry.pending) continue;
      entry.pending = false;
      try {
        const result = options ? await compressJpeg(entry.file, settings, signal) : await compressPng(entry.file, signal);
        if (signal.aborted) return;
        showResult(entry, result);
      } catch {
        if (signal.aborted) return;
        entry.invalid = true;
        entry.file = null;
        entry.status.textContent = labels.invalidInput;
        status("invalid", labels.invalidInput);
      }
    }
  } finally {
    if (!signal.aborted) {
      busy = false;
      refresh();
    }
  }
}

function resetJobs() {
  clearTimeout(timer);
  controller.abort();
  controller = new AbortController();
  busy = packing = false;
  for (const entry of entries) {
    if (entry.url) URL.revokeObjectURL(entry.url);
    entry.blob = entry.url = null;
    if (!entry.invalid) {
      entry.pending = true;
      entry.status.textContent = labels.processing;
    }
  }
  refresh();
}

options?.addEventListener("input", () => {
  const mode = byId("compression-mode").value;
  byId("quality-setting").hidden = mode !== "quality";
  byId("custom-setting").hidden = mode !== "custom";
  byId("resize-setting").hidden = mode === "quality";
  options.querySelector("output").value = byId("jpeg-quality").value + "%";
  resetJobs();
  timer = setTimeout(processQueue, 180);
});

function addFiles(files) {
  let room = maxFiles - entries.filter(entry => !entry.invalid).length;
  for (const file of files) {
    if (!room) {
      status("invalid", labels.skippedFileLimit.replace("{max}", maxFiles));
      break;
    }
    const row = ToolCommon.appendFileStatusItem(list, "file-" + list.childElementCount, file.name, labels.processing);
    const field = row.querySelector(".file-status");
    if (file.size > 10 * 1024 * 1024) {
      field.textContent = labels.fileTooLarge + " 10 MB";
      status("invalid", field.textContent);
      continue;
    }
    const extension = options ? ".jpg" : ".png";
    const name = ToolCommon.sanitizeDownloadFilename(file.name.replace(options ? /\.jpe?g$/i : /\.png$/i, "") + "-compressed" + extension);
    entries.push({ file, name, status: field, pending: true });
    room--;
  }
  processQueue();
}

dropzone.addEventListener("click", () => input.click());
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
input.addEventListener("change", () => {
  addFiles(input.files);
  input.value = "";
});
byId("btn-clear").addEventListener("click", () => {
  resetJobs();
  entries.length = 0;
  list.replaceChildren();
  refresh();
  status("idle", "");
});

function download(url, name) {
  const link = document.createElement("a");
  link.href = url;
  link.download = name;
  link.click();
}

all.addEventListener("click", async () => {
  if (all.disabled) return;
  const ready = entries.filter(entry => entry.url);
  if (ready.length === 1) {
    download(ready[0].url, ready[0].name);
    return;
  }
  const signal = controller.signal;
  packing = true;
  refresh();
  try {
    const zip = new JSZip();
    ready.forEach(entry => ToolCommon.addFileToZip(zip, entry.name, entry.blob));
    const archive = await zip.generateAsync({ type: "blob" });
    if (signal.aborted) return;
    const url = URL.createObjectURL(archive);
    download(url, options ? "compressed-jpeg.zip" : "compressed-png.zip");
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  } catch {
    if (!signal.aborted) status("invalid", labels.error);
  } finally {
    if (!signal.aborted) {
      packing = false;
      refresh();
    }
  }
});
ToolCommon.initExampleCopy();
