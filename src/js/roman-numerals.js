(function (root) {
  'use strict';

  const symbols = [
    [1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'], [90, 'XC'],
    [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']
  ];

  function encode(value) {
    const text = String(value).trim();
    if (!/^\+?\d+$/.test(text)) return null;
    let number = Number(text);
    if (number < 1 || number > 3999) return null;
    let result = '';
    for (const [amount, symbol] of symbols) {
      while (number >= amount) {
        result += symbol;
        number -= amount;
      }
    }
    return result;
  }

  function decode(value) {
    const text = String(value).trim().toUpperCase();
    if (!text || text.length > 15) return null;
    let position = 0;
    let result = 0;
    for (const [amount, symbol] of symbols) {
      while (text.startsWith(symbol, position)) {
        result += amount;
        position += symbol.length;
      }
    }
    return encode(result) === text ? result : null;
  }

  const api = { encode, decode };
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.RomanNumerals = api;
})(typeof window !== 'undefined' ? window : globalThis);
