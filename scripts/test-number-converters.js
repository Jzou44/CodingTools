const { test } = require("node:test");
const assert = require("node:assert/strict");
const roman = require("../src/js/roman-numerals");
require("../src/js/bignumber-lite");
const { BigNumber } = globalThis;

test("standard Roman numerals round-trip throughout the supported range", () => {
  for (let number = 1; number <= 3999; number++) {
    assert.equal(roman.decode(roman.encode(number)), number);
  }
  assert.equal(roman.decode(" xlix "), 49);
  for (const value of ["", "MMMM", "IIV", "IXIX"]) assert.equal(roman.decode(value), null);
  for (const value of ["0", "4000", "1.9", "12abc", "1e2"]) assert.equal(roman.encode(value), null);
});

test("fraction tools preserve mixed signs, tiny values and large integer parts", () => {
  assert.equal(BigNumber.fromMixed("-1", "1", "2").toString(), "-1.5");
  assert.equal(BigNumber.fromMixed("-0", "1", "2").toString(), "-0.5");
  assert.throws(() => BigNumber.fromMixed("1", "1", "0"));
  assert.equal(new BigNumber(1).dividedBy("1e23").toString(), "1e-23");
  assert.equal(new BigNumber("-1e-23").multipliedBy(100).toString(), "-1e-21");
  assert.equal(BigNumber.mixedFraction("9007199254740993.5").text, "9007199254740993 1/2");
  assert.equal(BigNumber.mixedFraction("9007199254740993.5", true).text, "90071992547409 187/200");
  assert.equal(BigNumber.mixedFraction("-0.5").text, "-1/2");
  assert.equal(BigNumber.mixedFraction("-1.5").text, "-1 1/2");
  assert.equal(BigNumber.mixedFraction("100%", true).text, "1");
  for (const value of ["12abc", "1e-3", "12%"]) assert.throws(() => BigNumber.mixedFraction(value));
});

test("signed radix input accepts only the matching optional prefix", () => {
  for (const [radix, text] of [[16, "0xA"], [8, "0o12"], [2, "0b1010"]]) {
    assert.equal(BigNumber.fromInteger("-" + text, radix).toString(), "-10");
    assert.equal(BigNumber.fromInteger("+" + text.slice(2), radix).toString(), "10");
    assert.throws(() => BigNumber.fromInteger(text, 10));
  }
  assert.throws(() => BigNumber.fromInteger("0o12", 2));
});
