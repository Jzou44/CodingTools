// JPEG APP1 segments contain a TIFF header preceded by the six-byte EXIF identifier.
window.readPhotoExif = (function () {
  'use strict';

  var TAGS = {
    0x010F: 'Make', 0x0110: 'Model', 0x0112: 'Orientation',
    0x011A: 'XResolution', 0x011B: 'YResolution', 0x0128: 'ResolutionUnit',
    0x0131: 'Software', 0x0132: 'DateTime', 0x013E: 'WhitePoint',
    0x013F: 'PrimaryChromaticities', 0x0211: 'YCbCrCoefficients',
    0x0213: 'YCbCrPositioning', 0x0214: 'ReferenceBlackWhite',
    0x8298: 'Copyright', 0x829A: 'ExposureTime', 0x829D: 'FNumber',
    0x8822: 'ExposureProgram', 0x8827: 'ISOSpeedRatings',
    0x9000: 'ExifVersion', 0x9003: 'DateTimeOriginal',
    0x9004: 'DateTimeDigitized', 0x920A: 'FocalLength',
    0xA001: 'ColorSpace', 0xA002: 'ExifImageWidth',
    0xA003: 'ExifImageHeight', 0xA405: 'FocalLengthIn35mmFilm',
    0xA420: 'ImageUniqueID', 0x010E: 'ImageDescription',
    0x0100: 'ImageWidth', 0x0101: 'ImageHeight',
    0x9209: 'Flash', 0xA431: 'SerialNumber', 0xA432: 'LensInfo',
    0xA433: 'LensMake', 0xA434: 'LensModel'
  };

  var GPS_TAGS = {
    0x0001: 'GPSLatitudeRef', 0x0002: 'GPSLatitude',
    0x0003: 'GPSLongitudeRef', 0x0004: 'GPSLongitude',
    0x0005: 'GPSAltitudeRef', 0x0006: 'GPSAltitude',
    0x0007: 'GPSTimeStamp', 0x001D: 'GPSDateStamp'
  };

  var typeSizes = { 1: 1, 2: 1, 3: 2, 4: 4, 5: 8, 7: 1, 9: 4, 10: 8 };

  function readTiff(view) {
    if (view.byteLength < 8) return {};
    var byteOrder = view.getUint16(0);
    var little = byteOrder === 0x4949;
    if ((!little && byteOrder !== 0x4d4d) || view.getUint16(2, little) !== 42) return {};
    var tags = {};

    function readValue(offset, type, count, name) {
      if (type === 2) {
        var bytes = new Uint8Array(view.buffer, view.byteOffset + offset, count);
        var end = bytes.indexOf(0);
        return new TextDecoder().decode(end < 0 ? bytes : bytes.subarray(0, end));
      }
      if (type === 5 || type === 10) {
        var read = type === 5 ? 'getUint32' : 'getInt32';
        var values = [];
        for (var i = 0; i < Math.min(count, 4); i++) {
          var pos = offset + i * 8;
          var denominator = view[read](pos + 4, little);
          if (!denominator) return null;
          values.push(view[read](pos, little) / denominator);
        }
        if (name === 'GPSLatitude' || name === 'GPSLongitude') {
          if (values.length !== 3) return null;
          return (values[0] + values[1] / 60 + values[2] / 3600).toFixed(6);
        }
        return values.map(function (n) { return n.toFixed(6); }).join(', ');
      }
      if (type === 3) return view.getUint16(offset, little);
      if (type === 4) return view.getUint32(offset, little);
      if (type === 9) return view.getInt32(offset, little);
      return view.getUint8(offset);
    }

    function readDirectory(offset, names, followPointers) {
      if (offset < 8 || offset + 2 > view.byteLength) return;
      var entries = view.getUint16(offset, little);
      for (var i = 0; i < entries && i < 512; i++) {
        var entry = offset + 2 + i * 12;
        if (entry + 12 > view.byteLength) break;
        var tag = view.getUint16(entry, little);
        var type = view.getUint16(entry + 2, little);
        var count = view.getUint32(entry + 4, little);
        if (!typeSizes[type] || !count) continue;
        var size = typeSizes[type] * count;
        var pos = size > 4 ? view.getUint32(entry + 8, little) : entry + 8;
        if (pos + size > view.byteLength) continue;
        if (tag === 0x8769 || tag === 0x8825) {
          if (followPointers && type === 4 && count === 1) {
            readDirectory(view.getUint32(pos, little), tag === 0x8825 ? GPS_TAGS : TAGS, false);
          }
          continue;
        }
        var name = names[tag] || 'Tag_0x' + tag.toString(16).toUpperCase();
        var value = readValue(pos, type, count, name);
        if (value !== null) tags[name] = value;
      }
    }

    readDirectory(view.getUint32(4, little), TAGS, true);
    if (tags.GPSLatitudeRef === 'S' && tags.GPSLatitude) tags.GPSLatitude = (-Number(tags.GPSLatitude)).toFixed(6);
    if (tags.GPSLongitudeRef === 'W' && tags.GPSLongitude) tags.GPSLongitude = (-Number(tags.GPSLongitude)).toFixed(6);
    if (tags.GPSAltitude !== undefined) {
      var altitude = Number(tags.GPSAltitude) * (tags.GPSAltitudeRef === 1 ? -1 : 1);
      tags.GPSAltitude = altitude.toFixed(1) + 'm';
    }
    return tags;
  }

  return function readPhotoExif(buffer) {
    var view = new DataView(buffer);
    if (view.byteLength < 2) return {};
    if (view.getUint16(0) !== 0xffd8) return readTiff(view);
    var pos = 2;
    while (pos < view.byteLength && view.getUint8(pos) === 0xff) {
      while (pos < view.byteLength && view.getUint8(pos) === 0xff) pos++;
      if (pos + 3 > view.byteLength) break;
      var marker = view.getUint8(pos++);
      if (marker === 0xda || marker === 0xd9) break;
      if (marker === 1 || (marker >= 0xd0 && marker <= 0xd7)) continue;
      var length = view.getUint16(pos);
      if (length < 2 || pos + length > view.byteLength) break;
      if (marker === 0xe1 && length >= 16 && view.getUint32(pos + 2) === 0x45786966 && view.getUint16(pos + 6) === 0) {
        var tags = readTiff(new DataView(buffer, pos + 8, length - 8));
        if (Object.keys(tags).length) return tags;
      }
      pos += length;
    }
    return {};
  };
})();
