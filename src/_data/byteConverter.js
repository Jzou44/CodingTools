const labels = {
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
