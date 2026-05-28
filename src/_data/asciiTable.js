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
    printableTitle: "Caractères imprimables (32-126)",
    controlTitle: "Caractères de contrôle (0-31 et 127)",
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
    uppercase: (value) => `Großbuchstabe ${value}`,
    lowercase: (value) => `Kleinbuchstabe ${value}`
  },
  es: {
    printableTitle: "Caractères imprimibles (32-126)",
    controlTitle: "Caractères de control (0-31 y 127)",
    dec: "Dec",
    hex: "Hex",
    oct: "Oct",
    bin: "Bin",
    char: "Car.",
    abbr: "Abr.",
    description: "Descripción",
    space: "Espacio",
    digit: (value) => `Dígito ${value}`,
    uppercase: (value) => `Letra mayúscula ${value}`,
    lowercase: (value) => `Letra minuscula ${value}`
  },
  pt: {
    printableTitle: "Caractères imprimiveis (32-126)",
    controlTitle: "Caractères de contrôle (0-31 e 127)",
    dec: "Dec",
    hex: "Hex",
    oct: "Oct",
    bin: "Bin",
    char: "Car.",
    abbr: "Abr.",
    description: "Descrição",
    space: "Espaço",
    digit: (value) => `Dígito ${value}`,
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
  },
  jp: {
    33: "感嘆符", 34: "二重引用符", 35: "番号記号", 36: "ドル記号", 37: "パーセント記号",
    38: "アンパサンド", 39: "単一引用符", 40: "左丸括弧", 41: "右丸括弧", 42: "アスタリスク",
    43: "プラス記号", 44: "コンマ", 45: "ハイフン / マイナス", 46: "ピリオド / ドット", 47: "スラッシュ",
    58: "コロン", 59: "セミコロン", 60: "小なり記号", 61: "等号", 62: "大なり記号",
    63: "疑問符", 64: "アットマーク", 91: "左角括弧", 92: "バックスラッシュ", 93: "右角括弧",
    94: "キャレット", 95: "アンダースコア", 96: "グレーブアクセント", 123: "左波括弧",
    124: "縦線", 125: "右波括弧", 126: "チルダ"
  },
  kr: {
    33: "느낌표", 34: "큰따옴표", 35: "번호 기호", 36: "달러 기호", 37: "퍼센트 기호",
    38: "앰퍼샌드", 39: "작은따옴표", 40: "왼쪽 괄호", 41: "오른쪽 괄호", 42: "별표",
    43: "더하기 기호", 44: "쉼표", 45: "하이픈 / 빼기", 46: "마침표 / 점", 47: "슬래시",
    58: "콜론", 59: "세미콜론", 60: "보다 작음 기호", 61: "등호", 62: "보다 큼 기호",
    63: "물음표", 64: "앳 기호", 91: "왼쪽 대괄호", 92: "백슬래시", 93: "오른쪽 대괄호",
    94: "캐럿", 95: "밑줄", 96: "그레이브 악센트", 123: "왼쪽 중괄호",
    124: "세로줄", 125: "오른쪽 중괄호", 126: "틸드"
  },
  fr: {
    33: "Point d'exclamation", 34: "Guillemet double", 35: "Diese / signe numéro", 36: "Signe dollar",
    37: "Signe pourcentage", 38: "Esperluette", 39: "Apostrophe", 40: "Parenthèse gauche",
    41: "Parenthèse droite", 42: "Asterisque", 43: "Signe plus", 44: "Virgule", 45: "Trait d'union / moins",
    46: "Point", 47: "Barre oblique", 58: "Deux-points", 59: "Point-virgule", 60: "Signe inférieur à",
    61: "Signe egal", 62: "Signe superieur a", 63: "Point d'interrogation", 64: "Arobase",
    91: "Crochet gauche", 92: "Barre oblique inverse", 93: "Crochet droit", 94: "Accent circonflexe",
    95: "Trait de soulignement", 96: "Accent grave", 123: "Accolade gauche", 124: "Barre verticale",
    125: "Accolade droite", 126: "Tilde"
  },
  de: {
    33: "Ausrufezeichen", 34: "Doppeltes Anführungszeichen", 35: "Raute / Nummernzeichen", 36: "Dollarzeichen",
    37: "Prozentzeichen", 38: "Kaufmännisches Und", 39: "Einfaches Anführungszeichen", 40: "Linke Klammer",
    41: "Rechte Klammer", 42: "Sternchen", 43: "Pluszeichen", 44: "Komma", 45: "Bindestrich / Minus",
    46: "Punkt", 47: "Schrägstrich", 58: "Doppelpunkt", 59: "Semikolon", 60: "Kleiner-als-Zeichen",
    61: "Gleichheitszeichen", 62: "Groesser-als-Zeichen", 63: "Fragezeichen", 64: "At-Zeichen",
    91: "Linke eckige Klammer", 92: "Rückwärtsschrägstrich", 93: "Rechte eckige Klammer", 94: "Zirkumflex",
    95: "Unterstrich", 96: "Gravis", 123: "Linke geschweifte Klammer", 124: "Senkrechter Strich",
    125: "Rechte geschweifte Klammer", 126: "Tilde"
  },
  es: {
    33: "Signo de exclamación", 34: "Comillas dobles", 35: "Almohadilla / numeral", 36: "Signo de dolar",
    37: "Signo de porcentaje", 38: "Ampersand", 39: "Comilla simple", 40: "Paréntesis izquierdo",
    41: "Paréntesis derecho", 42: "Asterisco", 43: "Signo mas", 44: "Coma", 45: "Guion / menos",
    46: "Punto", 47: "Barra diagonal", 58: "Dos puntos", 59: "Punto y coma", 60: "Signo menor que",
    61: "Signo igual", 62: "Signo mayor que", 63: "Signo de interrogacion", 64: "Arroba",
    91: "Corchete izquierdo", 92: "Barra invertida", 93: "Corchete derecho", 94: "Acento circunflejo",
    95: "Guion bajo", 96: "Acento grave", 123: "Llave izquierda", 124: "Barra vertical",
    125: "Llave derecha", 126: "Tilde"
  },
  pt: {
    33: "Ponto de exclamacao", 34: "Aspas duplas", 35: "Cerquilha / sinal de numero", 36: "Sinal de dolar",
    37: "Sinal de porcentagem", 38: "E comercial", 39: "Aspas simples", 40: "Parêntese esquerdo",
    41: "Parêntese direito", 42: "Asterisco", 43: "Sinal de mais", 44: "Vírgula", 45: "Hifen / menos",
    46: "Ponto", 47: "Barra", 58: "Dois-pontos", 59: "Ponto e virgula", 60: "Sinal de menor que",
    61: "Sinal de igual", 62: "Sinal de maior que", 63: "Ponto de interrogacao", 64: "Arroba",
    91: "Colchete esquerdo", 92: "Barra invertida", 93: "Colchete direito", 94: "Acento circunflexo",
    95: "Sublinhado", 96: "Acento grave", 123: "Chave esquerda", 124: "Barra vertical",
    125: "Chave direita", 126: "Til"
  }
};

const controlAbbrs = [
  "NUL", "SOH", "STX", "ETX", "EOT", "ENQ", "ACK", "BEL",
  "BS", "HT", "LF", "VT", "FF", "CR", "SO", "SI",
  "DLE", "DC1", "DC2", "DC3", "DC4", "NAK", "SYN", "ETB",
  "CAN", "EM", "SUB", "ESC", "FS", "GS", "RS", "US"
];

const controlDescriptions = {
  en: [
    "Null character", "Start of heading", "Start of text", "End of text",
    "End of transmission", "Enquiry", "Acknowledge", "Bell", "Backspace",
    "Horizontal tab", "Line feed", "Vertical tab", "Form feed", "Carriage return",
    "Shift out", "Shift in", "Data link escape", "Device control 1",
    "Device control 2", "Device control 3", "Device control 4", "Negative acknowledge",
    "Synchronous idle", "End of transmission block", "Cancel", "End of medium",
    "Substitute", "Escape", "File separator", "Group separator", "Record separator",
    "Unit separator"
  ],
  cn: [
    "空字符", "标题开始", "正文开始", "正文结束", "传输结束", "询问", "确认", "响铃",
    "退格", "水平制表符", "换行", "垂直制表符", "换页", "回车", "移出", "移入",
    "数据链路转义", "设备控制 1", "设备控制 2", "设备控制 3", "设备控制 4", "否定确认",
    "同步空闲", "传输块结束", "取消", "介质结束", "替换", "转义", "文件分隔符",
    "组分隔符", "记录分隔符", "单元分隔符"
  ],
  tw: [
    "空字元", "標題開始", "本文開始", "本文結束", "傳輸結束", "詢問", "確認", "響鈴",
    "退格", "水平定位字元", "換行", "垂直定位字元", "換頁", "歸位", "移出", "移入",
    "資料鏈路跳脫", "裝置控制 1", "裝置控制 2", "裝置控制 3", "裝置控制 4", "否定確認",
    "同步閒置", "傳輸區塊結束", "取消", "媒體結束", "替代", "跳脫", "檔案分隔符",
    "群組分隔符", "記錄分隔符", "單元分隔符"
  ],
  jp: [
    "ヌル文字", "ヘッダー開始", "テキスト開始", "テキスト終了", "転送終了", "問い合わせ",
    "肯定応答", "ベル", "バックスペース", "水平タブ", "改行", "垂直タブ", "改ページ",
    "キャリッジリターン", "シフトアウト", "シフトイン", "データリンクエスケープ",
    "装置制御 1", "装置制御 2", "装置制御 3", "装置制御 4", "否定応答", "同期アイドル",
    "転送ブロック終了", "キャンセル", "媒体終了", "置換", "エスケープ", "ファイル区切り",
    "グループ区切り", "レコード区切り", "ユニット区切り"
  ],
  kr: [
    "널 문자", "헤더 시작", "텍스트 시작", "텍스트 끝", "전송 끝", "문의", "승인", "벨",
    "백스페이스", "수평 탭", "줄 바꿈", "수직 탭", "폼 피드", "캐리지 리턴",
    "시프트 아웃", "시프트 인", "데이터 링크 이스케이프", "장치 제어 1", "장치 제어 2",
    "장치 제어 3", "장치 제어 4", "부정 응답", "동기 유휴", "전송 블록 끝",
    "취소", "매체 끝", "대체", "이스케이프", "파일 구분자", "그룹 구분자",
    "레코드 구분자", "단위 구분자"
  ],
  fr: [
    "Caractère nul", "Début d'en-tete", "Début du texte", "Fin du texte",
    "Fin de transmission", "Demande", "Accuse de reception", "Sonnerie", "Retour arriere",
    "Tabulation horizontale", "Saut de ligne", "Tabulation verticale", "Saut de page",
    "Retour chariot", "Shift out", "Shift in", "Échappement de liaison de donnees",
    "Controle de peripherique 1", "Controle de peripherique 2", "Controle de peripherique 3",
    "Controle de peripherique 4", "Accuse negatif", "Synchronisation inactive",
    "Fin de bloc de transmission", "Annuler", "Fin de support", "Substitution",
    "Échappement", "Séparateur de fichier", "Séparateur de groupe", "Séparateur d'enregistrement",
    "Séparateur d'unite"
  ],
  de: [
    "Nullzeichen", "Kopfzeilenbeginn", "Textbeginn", "Textende", "Übertragungsende",
    "Anfrage", "Bestaetigung", "Glocke", "Rueckschritt", "Horizontaler Tabulator",
    "Zeilenvorschub", "Vertikaler Tabulator", "Seitenvorschub", "Wagenruecklauf",
    "Shift out", "Shift in", "Datenlink-Escape", "Geraetesteuerung 1", "Geraetesteuerung 2",
    "Geraetesteuerung 3", "Geraetesteuerung 4", "Negative Bestaetigung", "Synchroner Leerlauf",
    "Ende des Uebertragungsblocks", "Abbrechen", "Ende des Mediums", "Ersatz",
    "Escape", "Dateitrenner", "Gruppentrenner", "Datensatztrenner", "Einheitentrenner"
  ],
  es: [
    "Carácter nulo", "Inicio de encabezado", "Inicio de texto", "Fin de texto",
    "Fin de transmision", "Consulta", "Confirmacion", "Campana", "Retroceso",
    "Tabulacion horizontal", "Salto de linea", "Tabulacion vertical", "Salto de pagina",
    "Retorno de carro", "Desplazar fuera", "Desplazar dentro", "Escape de enlace de datos",
    "Control de dispositivo 1", "Control de dispositivo 2", "Control de dispositivo 3",
    "Control de dispositivo 4", "Confirmacion negativa", "Inactivo sincronico",
    "Fin de bloque de transmision", "Cancelar", "Fin de medio", "Sustituto", "Escape",
    "Separador de archivo", "Separador de grupo", "Separador de registro", "Separador de unidad"
  ],
  pt: [
    "Caractère nulo", "Início do cabeçalho", "Inicio do texto", "Fim do texto",
    "Fim da transmissao", "Consulta", "Confirmacao", "Campainha", "Backspace",
    "Tabulacao horizontal", "Quebra de linha", "Tabulacao vertical", "Avanco de pagina",
    "Retorno de carro", "Shift out", "Shift in", "Escape de enlace de dados",
    "Controle de dispositivo 1", "Controle de dispositivo 2", "Controle de dispositivo 3",
    "Controle de dispositivo 4", "Confirmacao negativa", "Ocioso sincrono",
    "Fim do bloco de transmissao", "Cancelar", "Fim do meio", "Substituto", "Escape",
    "Separador de arquivo", "Separador de grupo", "Separador de registro", "Separador de unidade"
  ]
};

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

function controlRows(lang) {
  const descriptions = controlDescriptions[lang] || controlDescriptions.en;
  return controlAbbrs.map((abbr, code) => ({
    ...numberCells(code),
    abbr,
    description: descriptions[code]
  })).concat({
    ...numberCells(127),
    abbr: "DEL",
    description: {
      en: "Delete", cn: "删除", tw: "刪除", jp: "削除", kr: "삭제",
      fr: "Supprimer", de: "Löschen", es: "Eliminar", pt: "Excluir"
    }[lang] || "Delete"
  });
}

module.exports = Object.fromEntries(
  Object.keys(labels).map((lang) => [lang, {
    labels: labels[lang],
    printableRows: printableRows(lang),
    controlRows: controlRows(lang)
  }])
);
