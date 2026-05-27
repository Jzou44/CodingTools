const labels = {
  en: {
    printableTitle: "Printable Characters (32-126)",
    controlTitle: "Control Characters (0-31 and 127)",
    dec: "Dec",
    hex: "Hex",
    oct: "Oct",
    bin: "Bin",
    char: "Char",
    abbr: "Abbr",
    description: "Description",
    space: "Space",
    digit: (value) => `Digit ${value}`,
    uppercase: (value) => `Uppercase ${value}`,
    lowercase: (value) => `Lowercase ${value}`
  },
  cn: {
    printableTitle: "可打印字符（32-126）",
    controlTitle: "控制字符（0-31 和 127）",
    dec: "十进制",
    hex: "十六进制",
    oct: "八进制",
    bin: "二进制",
    char: "字符",
    abbr: "缩写",
    description: "说明",
    space: "空格",
    digit: (value) => `数字 ${value}`,
    uppercase: (value) => `大写字母 ${value}`,
    lowercase: (value) => `小写字母 ${value}`
  },
  tw: {
    printableTitle: "可列印字元（32-126）",
    controlTitle: "控制字元（0-31 和 127）",
    dec: "十進位",
    hex: "十六進位",
    oct: "八進位",
    bin: "二進位",
    char: "字元",
    abbr: "縮寫",
    description: "說明",
    space: "空格",
    digit: (value) => `數字 ${value}`,
    uppercase: (value) => `大寫字母 ${value}`,
    lowercase: (value) => `小寫字母 ${value}`
  },
  jp: {
    printableTitle: "印字可能文字（32-126）",
    controlTitle: "制御文字（0-31 と 127）",
    dec: "10進",
    hex: "16進",
    oct: "8進",
    bin: "2進",
    char: "文字",
    abbr: "略称",
    description: "説明",
    space: "スペース",
    digit: (value) => `数字 ${value}`,
    uppercase: (value) => `大文字 ${value}`,
    lowercase: (value) => `小文字 ${value}`
  },
  kr: {
    printableTitle: "출력 가능 문자(32-126)",
    controlTitle: "제어 문자(0-31 및 127)",
    dec: "10진수",
    hex: "16진수",
    oct: "8진수",
    bin: "2진수",
    char: "문자",
    abbr: "약어",
    description: "설명",
    space: "공백",
    digit: (value) => `숫자 ${value}`,
    uppercase: (value) => `대문자 ${value}`,
    lowercase: (value) => `소문자 ${value}`
  },
  fr: {
    printableTitle: "Caracteres imprimables (32-126)",
    controlTitle: "Caracteres de controle (0-31 et 127)",
    dec: "Dec",
    hex: "Hex",
    oct: "Oct",
    bin: "Bin",
    char: "Car.",
    abbr: "Abr.",
    description: "Description",
    space: "Espace",
    digit: (value) => `Chiffre ${value}`,
    uppercase: (value) => `Lettre majuscule ${value}`,
    lowercase: (value) => `Lettre minuscule ${value}`
  },
  de: {
    printableTitle: "Druckbare Zeichen (32-126)",
    controlTitle: "Steuerzeichen (0-31 und 127)",
    dec: "Dez",
    hex: "Hex",
    oct: "Okt",
    bin: "Bin",
    char: "Zeichen",
    abbr: "Abk.",
    description: "Beschreibung",
    space: "Leerzeichen",
    digit: (value) => `Ziffer ${value}`,
    uppercase: (value) => `Grossbuchstabe ${value}`,
    lowercase: (value) => `Kleinbuchstabe ${value}`
  },
  es: {
    printableTitle: "Caracteres imprimibles (32-126)",
    controlTitle: "Caracteres de control (0-31 y 127)",
    dec: "Dec",
    hex: "Hex",
    oct: "Oct",
    bin: "Bin",
    char: "Car.",
    abbr: "Abr.",
    description: "Descripcion",
    space: "Espacio",
    digit: (value) => `Digito ${value}`,
    uppercase: (value) => `Letra mayuscula ${value}`,
    lowercase: (value) => `Letra minuscula ${value}`
  },
  pt: {
    printableTitle: "Caracteres imprimiveis (32-126)",
    controlTitle: "Caracteres de controle (0-31 e 127)",
    dec: "Dec",
    hex: "Hex",
    oct: "Oct",
    bin: "Bin",
    char: "Car.",
    abbr: "Abr.",
    description: "Descricao",
    space: "Espaco",
    digit: (value) => `Digito ${value}`,
    uppercase: (value) => `Letra maiuscula ${value}`,
    lowercase: (value) => `Letra minuscula ${value}`
  }
};

const punctuation = {
  en: {
    33: "Exclamation mark", 34: "Double quote", 35: "Hash / number sign", 36: "Dollar sign",
    37: "Percent sign", 38: "Ampersand", 39: "Single quote", 40: "Left parenthesis",
    41: "Right parenthesis", 42: "Asterisk", 43: "Plus sign", 44: "Comma", 45: "Hyphen / minus",
    46: "Period / dot", 47: "Slash", 58: "Colon", 59: "Semicolon", 60: "Less-than sign",
    61: "Equals sign", 62: "Greater-than sign", 63: "Question mark", 64: "At sign",
    91: "Left bracket", 92: "Backslash", 93: "Right bracket", 94: "Caret / circumflex",
    95: "Underscore", 96: "Grave accent", 123: "Left brace", 124: "Vertical bar",
    125: "Right brace", 126: "Tilde"
  },
  cn: {
    33: "感叹号", 34: "双引号", 35: "井号 / 数字符号", 36: "美元符号", 37: "百分号",
    38: "与号", 39: "单引号", 40: "左圆括号", 41: "右圆括号", 42: "星号",
    43: "加号", 44: "逗号", 45: "连字符 / 减号", 46: "句点 / 点号", 47: "斜杠",
    58: "冒号", 59: "分号", 60: "小于号", 61: "等号", 62: "大于号",
    63: "问号", 64: "at 符号", 91: "左方括号", 92: "反斜杠", 93: "右方括号",
    94: "插入符 / 脱字符", 95: "下划线", 96: "重音符", 123: "左花括号",
    124: "竖线", 125: "右花括号", 126: "波浪号"
  },
  tw: {
    33: "驚嘆號", 34: "雙引號", 35: "井字號 / 數字符號", 36: "美元符號", 37: "百分號",
    38: "與號", 39: "單引號", 40: "左圓括號", 41: "右圓括號", 42: "星號",
    43: "加號", 44: "逗號", 45: "連字號 / 減號", 46: "句點 / 點號", 47: "斜線",
    58: "冒號", 59: "分號", 60: "小於號", 61: "等號", 62: "大於號",
    63: "問號", 64: "at 符號", 91: "左方括號", 92: "反斜線", 93: "右方括號",
    94: "插入符 / 抑揚符", 95: "底線", 96: "重音符", 123: "左大括號",
    124: "垂直線", 125: "右大括號", 126: "波浪號"
  }
};

punctuation.jp = punctuation.en;
punctuation.kr = punctuation.en;
punctuation.fr = punctuation.en;
punctuation.de = punctuation.en;
punctuation.es = punctuation.en;
punctuation.pt = punctuation.en;

const controlDescriptions = [
  ["NUL", "Null character"], ["SOH", "Start of heading"], ["STX", "Start of text"],
  ["ETX", "End of text"], ["EOT", "End of transmission"], ["ENQ", "Enquiry"],
  ["ACK", "Acknowledge"], ["BEL", "Bell"], ["BS", "Backspace"],
  ["HT", "Horizontal tab"], ["LF", "Line feed"], ["VT", "Vertical tab"],
  ["FF", "Form feed"], ["CR", "Carriage return"], ["SO", "Shift out"],
  ["SI", "Shift in"], ["DLE", "Data link escape"], ["DC1", "Device control 1"],
  ["DC2", "Device control 2"], ["DC3", "Device control 3"], ["DC4", "Device control 4"],
  ["NAK", "Negative acknowledge"], ["SYN", "Synchronous idle"], ["ETB", "End of transmission block"],
  ["CAN", "Cancel"], ["EM", "End of medium"], ["SUB", "Substitute"],
  ["ESC", "Escape"], ["FS", "File separator"], ["GS", "Group separator"],
  ["RS", "Record separator"], ["US", "Unit separator"]
];

function numberCells(code) {
  return {
    dec: String(code),
    hex: code.toString(16).toUpperCase().padStart(2, "0"),
    oct: code.toString(8).padStart(3, "0"),
    bin: code.toString(2).padStart(8, "0")
  };
}

function printableDescription(lang, code, char) {
  const text = labels[lang] || labels.en;
  if (code === 32) return text.space;
  if (code >= 48 && code <= 57) return text.digit(char);
  if (code >= 65 && code <= 90) return text.uppercase(char);
  if (code >= 97 && code <= 122) return text.lowercase(char);
  return (punctuation[lang] && punctuation[lang][code]) || punctuation.en[code] || "";
}

function printableRows(lang) {
  return Array.from({ length: 95 }, (_, index) => {
    const code = index + 32;
    const char = String.fromCharCode(code);
    return {
      ...numberCells(code),
      char,
      display: code === 32 ? "sp" : char,
      isSpace: code === 32,
      description: printableDescription(lang, code, char)
    };
  });
}

function controlRows() {
  return controlDescriptions.map(([abbr, description], code) => ({
    ...numberCells(code),
    abbr,
    description
  })).concat({
    ...numberCells(127),
    abbr: "DEL",
    description: "Delete"
  });
}

module.exports = Object.fromEntries(
  Object.keys(labels).map((lang) => [lang, {
    labels: labels[lang],
    printableRows: printableRows(lang),
    controlRows: controlRows()
  }])
);
