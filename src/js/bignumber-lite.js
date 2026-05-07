(function (global) {
  'use strict';

  var DEFAULT_DECIMAL_PLACES = 20;
  var DIGITS = '0123456789abcdefghijklmnopqrstuvwxyz';

  function abs(value) {
    return value < 0n ? -value : value;
  }

  function gcd(a, b) {
    a = abs(a);
    b = abs(b);
    while (b !== 0n) {
      var t = b;
      b = a % b;
      a = t;
    }
    return a || 1n;
  }

  function normalizeParts(numerator, denominator) {
    if (denominator === 0n) {
      throw new Error('Division by zero');
    }
    if (denominator < 0n) {
      numerator = -numerator;
      denominator = -denominator;
    }
    var divisor = gcd(numerator, denominator);
    return {
      numerator: numerator / divisor,
      denominator: denominator / divisor
    };
  }

  function expandExponent(input) {
    var match = String(input).trim().match(/^([+-]?)(\d*\.?\d+)[eE]([+-]?\d+)$/);
    if (!match) return String(input).trim();

    var sign = match[1];
    var number = match[2];
    var exponent = parseInt(match[3], 10);
    var point = number.indexOf('.');
    var digits = number.replace('.', '');
    var decimalPlaces = point === -1 ? 0 : number.length - point - 1;
    var newPlaces = decimalPlaces - exponent;

    if (newPlaces <= 0) {
      return sign + digits + '0'.repeat(-newPlaces);
    }
    if (newPlaces >= digits.length) {
      return sign + '0.' + '0'.repeat(newPlaces - digits.length) + digits;
    }
    return sign + digits.slice(0, digits.length - newPlaces) + '.' + digits.slice(digits.length - newPlaces);
  }

  function parseDecimal(value) {
    var text = expandExponent(value);
    var match = text.match(/^([+-]?)(?:(\d+)(?:\.(\d*))?|\.(\d+))$/);
    if (!match) {
      throw new Error('Invalid number');
    }

    var sign = match[1] === '-' ? -1n : 1n;
    var integer = match[2] || '0';
    var fraction = match[3] !== undefined ? match[3] : (match[4] || '');
    var digits = (integer + fraction).replace(/^0+(?=\d)/, '') || '0';
    var denominator = 10n ** BigInt(fraction.length);
    return normalizeParts(sign * BigInt(digits), denominator);
  }

  function parseBase(value, base) {
    var radix = Number(base);
    if (!Number.isInteger(radix) || radix < 2 || radix > 36) {
      throw new Error('Invalid base');
    }

    var text = String(value).trim().toLowerCase();
    var sign = 1n;
    if (text.charAt(0) === '-' || text.charAt(0) === '+') {
      sign = text.charAt(0) === '-' ? -1n : 1n;
      text = text.slice(1);
    }
    if (!text) throw new Error('Invalid number');

    var result = 0n;
    for (var i = 0; i < text.length; i++) {
      var digit = DIGITS.indexOf(text.charAt(i));
      if (digit < 0 || digit >= radix) {
        throw new Error('Invalid number');
      }
      result = result * BigInt(radix) + BigInt(digit);
    }

    return { numerator: sign * result, denominator: 1n };
  }

  function coerce(value) {
    return value instanceof BigNumber ? value : new BigNumber(value);
  }

  function roundDecimalParts(integer, fraction, roundDigit) {
    if (roundDigit < 5) {
      return { integer: integer, fraction: fraction };
    }

    var carry = 1;
    var chars = fraction.split('');
    for (var i = chars.length - 1; i >= 0; i--) {
      var next = Number(chars[i]) + carry;
      if (next === 10) {
        chars[i] = '0';
      } else {
        chars[i] = String(next);
        carry = 0;
        break;
      }
    }

    if (carry) {
      integer = (BigInt(integer) + 1n).toString();
    }

    return { integer: integer, fraction: chars.join('') };
  }

  function toDecimalString(numerator, denominator, decimalPlaces, fixed) {
    var negative = numerator < 0n;
    numerator = abs(numerator);

    var integer = numerator / denominator;
    var remainder = numerator % denominator;
    var fraction = '';
    var roundDigit = 0;

    for (var i = 0; i < decimalPlaces; i++) {
      if (remainder === 0n && !fixed) break;
      remainder *= 10n;
      fraction += (remainder / denominator).toString();
      remainder %= denominator;
    }

    if (remainder !== 0n) {
      remainder *= 10n;
      roundDigit = Number(remainder / denominator);
    }

    var rounded = roundDecimalParts(integer.toString(), fraction, roundDigit);
    var outputFraction = fixed ? rounded.fraction.padEnd(decimalPlaces, '0') : rounded.fraction.replace(/0+$/, '');
    var result = rounded.integer + (outputFraction ? '.' + outputFraction : '');

    return negative && result !== '0' ? '-' + result : result;
  }

  function toBaseString(numerator, denominator, base) {
    if (denominator !== 1n) {
      return toDecimalString(numerator, denominator, DEFAULT_DECIMAL_PLACES, false);
    }
    return numerator.toString(base);
  }

  function BigNumber(value, base) {
    if (!(this instanceof BigNumber)) {
      return new BigNumber(value, base);
    }

    var parts;
    if (value instanceof BigNumber) {
      parts = { numerator: value.numerator, denominator: value.denominator };
    } else if (base !== undefined && base !== 10) {
      parts = parseBase(value, base);
    } else {
      parts = parseDecimal(value);
    }

    this.numerator = parts.numerator;
    this.denominator = parts.denominator;
  }

  BigNumber.prototype.plus = function (other) {
    other = coerce(other);
    var parts = normalizeParts(
      this.numerator * other.denominator + other.numerator * this.denominator,
      this.denominator * other.denominator
    );
    return BigNumber._fromParts(parts.numerator, parts.denominator);
  };

  BigNumber.prototype.dividedBy = function (other) {
    other = coerce(other);
    var parts = normalizeParts(this.numerator * other.denominator, this.denominator * other.numerator);
    return BigNumber._fromParts(parts.numerator, parts.denominator);
  };

  BigNumber.prototype.multipliedBy = function (other) {
    other = coerce(other);
    var parts = normalizeParts(this.numerator * other.numerator, this.denominator * other.denominator);
    return BigNumber._fromParts(parts.numerator, parts.denominator);
  };

  BigNumber.prototype.isZero = function () {
    return this.numerator === 0n;
  };

  BigNumber.prototype.toString = function (base) {
    var radix = base === undefined ? 10 : Number(base);
    if (!Number.isInteger(radix) || radix < 2 || radix > 36) {
      throw new Error('Invalid base');
    }
    return radix === 10
      ? toDecimalString(this.numerator, this.denominator, DEFAULT_DECIMAL_PLACES, false)
      : toBaseString(this.numerator, this.denominator, radix);
  };

  BigNumber.prototype.toFixed = function (decimalPlaces) {
    var places = decimalPlaces === undefined ? DEFAULT_DECIMAL_PLACES : Number(decimalPlaces);
    if (!Number.isInteger(places) || places < 0) {
      throw new Error('Invalid decimal places');
    }
    return toDecimalString(this.numerator, this.denominator, places, true);
  };

  BigNumber._fromParts = function (numerator, denominator) {
    var number = Object.create(BigNumber.prototype);
    var parts = normalizeParts(numerator, denominator);
    number.numerator = parts.numerator;
    number.denominator = parts.denominator;
    return number;
  };

  global.BigNumber = BigNumber;
})(typeof window !== 'undefined' ? window : globalThis);
