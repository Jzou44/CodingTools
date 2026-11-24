import encode from "/assets/jsquash-jpeg/encode.js";

// Skip length-prefixed segments (including EXIF and embedded thumbnails) to
// identify the actual frame, rather than looking for a byte pair in the file.
function hasProgressiveFrame(buffer) {
  const bytes = new Uint8Array(buffer);
  if (bytes[0] !== 0xff || bytes[1] !== 0xd8) return false;
  let pos = 2;
  while (pos + 4 <= bytes.length && bytes[pos++] === 0xff) {
    while (bytes[pos] === 0xff) pos++;
    const marker = bytes[pos++];
    if (marker === 0xda || marker === 0xd9) return false;
    const size = (bytes[pos] << 8) | bytes[pos + 1];
    if (size < 2 || pos + size > bytes.length) return false;
    if (marker >= 0xc0 && marker <= 0xcf && ![0xc4, 0xc8, 0xcc].includes(marker)) {
      return marker === 0xc2;
    }
    pos += size;
  }
  return false;
}

self.onmessage = async ({ data: pixels }) => {
  try {
    const jpeg = await encode(pixels, { quality: 100, progressive: true, baseline: false, arithmetic: false });
    if (!hasProgressiveFrame(jpeg)) throw new Error("Expected a progressive JPEG frame");
    self.postMessage(jpeg, [jpeg]);
  } catch {
    self.postMessage(null);
  }
};
