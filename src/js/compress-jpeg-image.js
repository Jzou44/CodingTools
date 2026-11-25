// Target sizes use decimal KB, as in upload forms. Test each encoded Blob.
export async function compressJpeg(file, settings, signal) {
  const signature = new Uint8Array(await file.slice(0, 2).arrayBuffer());
  if (signature[0] !== 0xff || signature[1] !== 0xd8) throw new Error("Invalid JPEG");
  const url = URL.createObjectURL(file);
  const image = new Image();
  const canvas = document.createElement("canvas");
  try {
    image.src = url;
    await image.decode();
    signal.throwIfAborted();
    if (settings.limit && file.size <= settings.limit) return { blob: file };

    let width = image.naturalWidth;
    let height = image.naturalHeight;
    const ctx = canvas.getContext("2d");
    function draw() {
      canvas.width = width;
      canvas.height = height;
      ctx.imageSmoothingQuality = "high";
      ctx.drawImage(image, 0, 0, width, height);
    }
    async function encode(quality) {
      signal.throwIfAborted();
      const blob = await new Promise(resolve => canvas.toBlob(resolve, "image/jpeg", quality / 100));
      signal.throwIfAborted();
      if (!blob || blob.type !== "image/jpeg") throw new Error("JPEG encoding failed");
      return blob;
    }
    draw();
    if (!settings.limit) {
      const blob = await encode(settings.quality);
      return { blob: blob.size < file.size ? blob : file };
    }

    let best = await encode(1);
    let scale = 1;
    while (best.size > settings.limit) {
      if (!settings.resize || (width === 1 && height === 1)) {
        return { unmet: Math.min(file.size, best.size) };
      }
      scale *= Math.min(0.85, Math.sqrt(settings.limit / best.size));
      width = Math.max(1, Math.floor(image.naturalWidth * scale));
      height = Math.max(1, Math.floor(image.naturalHeight * scale));
      draw();
      best = await encode(1);
    }

    let low = 2;
    let high = 100;
    while (low <= high) {
      const quality = Math.floor((low + high) / 2);
      const candidate = await encode(quality);
      if (candidate.size <= settings.limit) {
        best = candidate;
        low = quality + 1;
      } else {
        high = quality - 1;
      }
    }
    return { blob: best, width, height };
  } finally {
    URL.revokeObjectURL(url);
    canvas.width = canvas.height = 0;
  }
}
