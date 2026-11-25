const { test } = require("node:test");
const assert = require("node:assert/strict");
const { convert, explain } = require("../src/js/byte-converter");
const labels = require("../src/_data/byteConverter");

test("hex accepts existing separators and common 0x notations", () => {
  for (const input of ["4869", "48-69", "48:69", "48,69", "48\t69", "0x4869", "0x48 0X69"]) {
    for (const mode of ["legacy", "utf8"]) {
      assert.deepEqual(convert("hex-to-ascii", input, mode), { text: "Hi", count: 2 });
    }
  }
});

test("encoding preserves the selected representation and delimiter", () => {
  assert.equal(convert("ascii-to-hex", "Hi", "legacy", "").text, "4869");
  assert.equal(convert("ascii-to-hex", "中", "legacy", " ").text, "4E2D");
  assert.equal(convert("ascii-to-hex", "😀", "legacy", " ").text, "D83D DE00");
  assert.equal(convert("text-to-binary", "あ", "legacy", " ").text, "11000001000010");
  assert.equal(convert("text-to-binary", "あ", "utf8", " ").text, "11100011 10000001 10000010");
  assert.equal(convert("ascii-to-hex", "\0\r\n ", "utf8", ":").text, "00:0D:0A:20");
  assert.equal(convert("ascii-to-hex", "中", "utf8", ",").text, "E4,B8,AD");
  assert.equal(convert("hex-to-ascii", "00FF", "legacy").text, "\0\u00ff");
  assert.throws(() => convert("ascii-to-hex", "a\ud800", "utf8", ""), { code: "unicode", position: 2 });
});

test("all translated examples work and UTF-8 round trips", () => {
  for (const { samples } of Object.values(labels)) {
    for (const sample of samples) {
      assert.equal(convert("hex-to-ascii", sample.hex, sample.mode).text, sample.text);
      assert.equal(convert("binary-to-text", sample.binary, sample.mode).text, sample.text);
      const hex = convert("ascii-to-hex", sample.text, "utf8", "").text;
      assert.equal(convert("hex-to-ascii", hex, "utf8").text, sample.text);
      const binary = convert("text-to-binary", sample.text, "utf8", " ").text;
      assert.equal(convert("binary-to-text", binary, "utf8").text, sample.text);
    }
  }
});

test("malformed digits, lengths, prefixes and UTF-8 errors have useful positions", () => {
  for (const [tool, input, expected] of [
    ["hex-to-ascii", "48 4G", { code: "hexDigit", position: 5 }],
    ["hex-to-ascii", "0x", { code: "prefix", position: 1 }],
    ["hex-to-ascii", "00 0xf", { code: "hexLength", position: 2, missing: 1 }],
    ["binary-to-text", "00000000 010", { code: "binaryLength", position: 2, missing: 5 }],
    ["binary-to-text", "00110002", { code: "binaryDigit", position: 8 }],
    ["hex-to-ascii", "41FF", { code: "utf8", position: 2 }],
    ["hex-to-ascii", "E4B8", { code: "utf8", position: 1 }],
    ["hex-to-ascii", "41E4B841", { code: "utf8", position: 4 }],
    ["hex-to-ascii", "EDA080", { code: "utf8", position: 2 }]
  ]) {
    assert.throws(() => convert(tool, input, "utf8"), expected);
  }
  const message = explain({ code: "binaryLength", position: 2, missing: 5 }, labels.cn.errors);
  assert.equal(message, "第 2 个字节还缺 5 个二进制位。");
});
