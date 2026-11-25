const labels = {
  en: {
    "mode": "Encoding",
    "characterCodes": "UTF-16 code units (legacy)",
    "byteView": "Byte by byte (legacy)",
    "units": "code units",
    "fill": "Try an example",
    "errors": {
      "empty": "Enter a value first.",
      "hexDigit": "Expected a hexadecimal digit at position {position}.",
      "binaryDigit": "Expected 0 or 1 at position {position}.",
      "prefix": "The 0x prefix at position {position} must be followed by a byte.",
      "hexLength": "Byte {position} is missing a hexadecimal digit.",
      "binaryLength": "Byte {position} is missing {missing} bits.",
      "utf8": "Invalid or incomplete UTF-8 sequence at byte {position}.",
      "unicode": "Incomplete Unicode character at position {position}."
    }
  },
  kr: {
    "mode": "인코딩",
    "characterCodes": "UTF-16 코드 단위 (기존 방식)",
    "byteView": "바이트별 보기 (기존 방식)",
    "units": "코드 단위",
    "fill": "예제 입력",
    "errors": {
      "empty": "먼저 값을 입력하세요.",
      "hexDigit": "{position}번째 문자는 16진수 숫자가 아닙니다.",
      "binaryDigit": "{position}번째 문자는 0 또는 1이어야 합니다.",
      "prefix": "{position}번째 위치의 0x 다음에 바이트 값을 입력하세요.",
      "hexLength": "{position}번째 바이트에 16진수 한 자리가 부족합니다.",
      "binaryLength": "{position}번째 바이트에 {missing}비트가 부족합니다.",
      "utf8": "{position}번째 바이트의 UTF-8 시퀀스가 잘못되었거나 불완전합니다.",
      "unicode": "{position}번째 위치의 유니코드 문자가 불완전합니다."
    }
  },
  de: {
    "mode": "Kodierung",
    "characterCodes": "UTF-16-Codeeinheiten (bisheriger Modus)",
    "byteView": "Byteweise Ansicht (bisheriger Modus)",
    "units": "Codeeinheiten",
    "fill": "Beispiel einsetzen",
    "errors": {
      "empty": "Bitte zuerst einen Wert eingeben.",
      "hexDigit": "An Position {position} fehlt eine Hexadezimalziffer.",
      "binaryDigit": "An Position {position} wird 0 oder 1 erwartet.",
      "prefix": "Nach dem Präfix 0x an Position {position} muss ein Byte folgen.",
      "hexLength": "Bei Byte {position} fehlt eine Hexadezimalziffer.",
      "binaryLength": "Bei Byte {position} fehlen {missing} Bit.",
      "utf8": "Ungültige oder unvollständige UTF-8-Sequenz bei Byte {position}.",
      "unicode": "Unvollständiges Unicode-Zeichen an Position {position}."
    }
  },
  fr: {
    "mode": "Encodage",
    "characterCodes": "Unités de code UTF-16 (mode historique)",
    "byteView": "Octet par octet (mode historique)",
    "units": "unités de code",
    "fill": "Insérer un exemple",
    "errors": {
      "empty": "Saisissez d’abord une valeur.",
      "hexDigit": "Un chiffre hexadécimal est attendu à la position {position}.",
      "binaryDigit": "Un 0 ou un 1 est attendu à la position {position}.",
      "prefix": "Le préfixe 0x à la position {position} doit être suivi d’un octet.",
      "hexLength": "Il manque un chiffre hexadécimal dans l’octet {position}.",
      "binaryLength": "Il manque {missing} bits dans l’octet {position}.",
      "utf8": "Séquence UTF-8 incorrecte ou incomplète à l’octet {position}.",
      "unicode": "Caractère Unicode incomplet à la position {position}."
    }
  },
  es: {
    "mode": "Codificación",
    "characterCodes": "Unidades de código UTF-16 (modo clásico)",
    "byteView": "Byte por byte (modo clásico)",
    "units": "unidades de código",
    "fill": "Probar un ejemplo",
    "errors": {
      "empty": "Introduce un valor.",
      "hexDigit": "Se esperaba un dígito hexadecimal en la posición {position}.",
      "binaryDigit": "Se esperaba 0 o 1 en la posición {position}.",
      "prefix": "El prefijo 0x en la posición {position} debe ir seguido de un byte.",
      "hexLength": "Al byte {position} le falta un dígito hexadecimal.",
      "binaryLength": "Al byte {position} le faltan {missing} bits.",
      "utf8": "Secuencia UTF-8 no válida o incompleta en el byte {position}.",
      "unicode": "Carácter Unicode incompleto en la posición {position}."
    }
  },
  pt: {
    "mode": "Codificação",
    "characterCodes": "Unidades de código UTF-16 (modo original)",
    "byteView": "Byte a byte (modo original)",
    "units": "unidades de código",
    "fill": "Inserir exemplo",
    "errors": {
      "empty": "Introduza um valor.",
      "hexDigit": "Era esperado um dígito hexadecimal na posição {position}.",
      "binaryDigit": "Era esperado 0 ou 1 na posição {position}.",
      "prefix": "O prefixo 0x na posição {position} deve ser seguido de um byte.",
      "hexLength": "Falta um dígito hexadecimal no byte {position}.",
      "binaryLength": "Faltam {missing} bits no byte {position}.",
      "utf8": "Sequência UTF-8 inválida ou incompleta no byte {position}.",
      "unicode": "Carácter Unicode incompleto na posição {position}."
    }
  },
  cn: {
    mode: "编码模式", characterCodes: "字符代码（原模式）", byteView: "逐字节查看（原模式）", units: "个字符代码", fill: "填入示例",
    errors: {
      empty: "请先输入内容。",
      hexDigit: "第 {position} 个位置不是十六进制数字。",
      binaryDigit: "第 {position} 个位置不是 0 或 1。",
      prefix: "请检查第 {position} 个位置的 0x 前缀，每个前缀后须紧跟完整字节。",
      hexLength: "第 {position} 个字节还缺 1 个十六进制数字。",
      binaryLength: "第 {position} 个字节还缺 {missing} 个二进制位。",
      utf8: "第 {position} 个字节处的 UTF-8 序列无效或不完整。",
      unicode: "第 {position} 个位置有不完整的 Unicode 字符。"
    }
  },
  tw: {
    mode: "編碼模式", characterCodes: "字元碼（原模式）", byteView: "逐位元組檢視（原模式）", units: "個字元碼", fill: "填入範例",
    errors: {
      empty: "請先輸入內容。",
      hexDigit: "第 {position} 個位置不是十六進位數字。",
      binaryDigit: "第 {position} 個位置不是 0 或 1。",
      prefix: "請檢查第 {position} 個位置的 0x 前綴，每個前綴後須緊接完整位元組。",
      hexLength: "第 {position} 個位元組還缺 1 個十六進位數字。",
      binaryLength: "第 {position} 個位元組還缺 {missing} 個位元。",
      utf8: "第 {position} 個位元組處的 UTF-8 序列無效或不完整。",
      unicode: "第 {position} 個位置有不完整的 Unicode 字元。"
    }
  },
  jp: {
    mode: "文字コード", characterCodes: "文字コード値（従来方式）", byteView: "1 バイトずつ表示（従来方式）", units: "コード単位", fill: "入力例をセット",
    errors: {
      empty: "入力してください。",
      hexDigit: "{position} 文字目に 16 進数以外の文字があります。",
      binaryDigit: "{position} 文字目が 0 または 1 ではありません。",
      prefix: "{position} 文字目の 0x を確認してください。接頭辞の直後にバイト値が必要です。",
      hexLength: "{position} バイト目の 16 進数が 1 桁足りません。",
      binaryLength: "{position} バイト目に {missing} ビット足りません。",
      utf8: "{position} バイト目に不正または不完全な UTF-8 シーケンスがあります。",
      unicode: "{position} 文字目の Unicode サロゲートペアが不完全です。"
    }
  }
};

for (const [lang, entry] of Object.entries(labels)) {
  entry.samples = ["Hi", lang === "jp" ? "あ" : "中", "😀"].map((text, index) => {
    const bytes = Array.from(Buffer.from(text));
    return {
      text, mode: index === 0 ? "legacy" : "utf8",
      hex: bytes.map(byte => "0x" + byte.toString(16).toUpperCase().padStart(2, "0")).join(" "),
      binary: bytes.map(byte => byte.toString(2).padStart(8, "0")).join(" ")
    };
  });
}

module.exports = labels;
