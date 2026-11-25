import initialize, { optimise } from "/assets/jsquash-oxipng/codec/pkg/squoosh_oxipng.js";

// Preserve animated PNGs byte for byte. Detect the animation control chunk
// before IDAT rather than searching for its name inside compressed data.
function isAnimated(bytes) {
  const view = new DataView(bytes.buffer);
  if (view.getUint32(0) !== 0x89504e47 || view.getUint32(4) !== 0x0d0a1a0a) throw new Error("Invalid PNG");
  for (let offset = 8; offset + 12 <= bytes.length;) {
    const length = view.getUint32(offset);
    const type = view.getUint32(offset + 4);
    if (offset + 12 + length > bytes.length) throw new Error("Truncated PNG");
    if (type === 0x6163544c) return true; // acTL
    if (type === 0x49444154) return false; // IDAT
    offset += 12 + length;
  }
  throw new Error("Missing image data");
}

self.onmessage = async ({ data: file }) => {
  try {
    const bytes = new Uint8Array(await file.arrayBuffer());
    if (isAnimated(bytes)) {
      const bitmap = await createImageBitmap(file);
      bitmap.close();
      self.postMessage({ original: true });
      return;
    }
    await initialize();
    const optimized = optimise(bytes, 2, false, false);
    if (optimized.length >= file.size) self.postMessage({ original: true });
    else self.postMessage({ bytes: optimized }, [optimized.buffer]);
  } catch {
    self.postMessage({ error: true });
  }
};
