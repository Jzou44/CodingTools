const tools = require("./tools.json");
const site = require("./site.js");
const toolDataAll = require("./toolData.js");

const sources = {
  browser: { name: "Browser JavaScript", url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript" },
  canvas: { name: "HTML Canvas API", url: "https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API" },
  cssColor: { name: "CSS Color Module Level 4", url: "https://www.w3.org/TR/css-color-4/" },
  ecma262: { name: "ECMAScript specification", url: "https://tc39.es/ecma262/" },
  exif: { name: "CIPA EXIF standard", url: "https://www.cipa.jp/std/std-sec_e.html" },
  fips180: { name: "NIST FIPS 180-4", url: "https://csrc.nist.gov/pubs/fips/180-4/upd1/final" },
  md5: { name: "IETF RFC 1321", url: "https://www.rfc-editor.org/rfc/rfc1321" },
  png: { name: "W3C PNG specification", url: "https://www.w3.org/TR/png/" },
  jpeg: { name: "JPEG standard family", url: "https://jpeg.org/jpeg/" },
  json: { name: "IETF RFC 8259", url: "https://www.rfc-editor.org/rfc/rfc8259" },
  base64: { name: "IETF RFC 4648", url: "https://www.rfc-editor.org/rfc/rfc4648" },
  url: { name: "WHATWG URL Standard", url: "https://url.spec.whatwg.org/" },
  unicode: { name: "Unicode Standard", url: "https://www.unicode.org/versions/latest/" },
  utf8: { name: "WHATWG Encoding Standard", url: "https://encoding.spec.whatwg.org/" },
  html: { name: "WHATWG HTML Standard", url: "https://html.spec.whatwg.org/" },
  xml: { name: "W3C XML 1.0", url: "https://www.w3.org/TR/xml/" }
};

const categoryBullets = {
  "hash-cryptography": [
    "<strong>Local processing:</strong> input is handled in the browser and is not uploaded by the static site.",
    "<strong>Developer workflow:</strong> use it for payload inspection, test data, verification, and repeatable copy/download output.",
    "<strong>Security boundary:</strong> encoding and hashing are not the same as encrypting secrets."
  ],
  "number-conversion": [
    "<strong>Local processing:</strong> values are converted in browser JavaScript with no server round trip.",
    "<strong>Developer workflow:</strong> use it to translate values between programming, protocol, color, and documentation formats.",
    "<strong>Validation:</strong> invalid digits, ranges, or formats should be corrected before using the output in production code."
  ],
  "string-text-utilities": [
    "<strong>Local processing:</strong> text stays in the browser while the tool transforms or analyzes it.",
    "<strong>Developer workflow:</strong> use it for copy editing, test fixtures, logs, code snippets, and content QA.",
    "<strong>Unicode awareness:</strong> visible characters, code units, words, lines, and bytes are different measurements."
  ],
  "formatter-minifier": [
    "<strong>Local processing:</strong> source text is formatted, minified, compared, or converted in the browser.",
    "<strong>Developer workflow:</strong> use it before commits, API debugging, config cleanup, or documentation examples.",
    "<strong>Validation:</strong> formatted output should preserve data meaning; minified output should be tested before deployment."
  ],
  "image-utilities": [
    "<strong>Local processing:</strong> images are handled with browser APIs instead of being uploaded to a server.",
    "<strong>Developer workflow:</strong> use it for quick asset preparation, previews, privacy cleanup, and HTML/CSS embedding.",
    "<strong>Format awareness:</strong> PNG, JPEG, WebP, Base64 data URIs, and EXIF metadata solve different problems."
  ]
};

const localizedText = {
  en: {
    question(title) { return `What does ${title} do?`; },
    topic: "Topic",
    directAnswer: "Direct answer",
    keyFact: "Key fact",
    processingModel: "Processing model",
    source: "Source",
    processingValue: "Runs locally in the browser; no production Node server receives the input.",
    categoryBullets
  },
  cn: {
    question(title) { return `${title}是什么工具？`; },
    topic: "主题",
    directAnswer: "直接答案",
    keyFact: "关键事实",
    processingModel: "处理方式",
    source: "来源",
    processingValue: "在浏览器本地运行；没有生产环境 Node 服务器接收输入内容。",
    categoryBullets: {
      "hash-cryptography": [
        "<strong>本地处理：</strong>输入在浏览器中处理，不会由静态站点上传。",
        "<strong>开发者工作流：</strong>适合用于载荷检查、测试数据、校验以及可重复的复制/下载输出。",
        "<strong>安全边界：</strong>编码和哈希并不等同于加密机密信息。"
      ],
      "number-conversion": [
        "<strong>本地处理：</strong>数值由浏览器 JavaScript 转换，不需要服务器往返。",
        "<strong>开发者工作流：</strong>适合在编程、协议、颜色和文档格式之间转换数值。",
        "<strong>校验：</strong>在把输出用于生产代码前，应修正无效数字、范围或格式。"
      ],
      "string-text-utilities": [
        "<strong>本地处理：</strong>文本在浏览器中完成转换或分析。",
        "<strong>开发者工作流：</strong>适合用于文案编辑、测试夹具、日志、代码片段和内容 QA。",
        "<strong>Unicode 意识：</strong>可见字符、代码单元、单词、行和字节是不同的计量方式。"
      ],
      "formatter-minifier": [
        "<strong>本地处理：</strong>源码文本在浏览器中格式化、压缩、比较或转换。",
        "<strong>开发者工作流：</strong>适合在提交前、API 调试、配置清理或文档示例中使用。",
        "<strong>校验：</strong>格式化输出应保持数据含义；压缩输出部署前应测试。"
      ],
      "image-utilities": [
        "<strong>本地处理：</strong>图片通过浏览器 API 处理，而不是上传到服务器。",
        "<strong>开发者工作流：</strong>适合快速准备资源、预览、隐私清理以及 HTML/CSS 嵌入。",
        "<strong>格式意识：</strong>PNG、JPEG、WebP、Base64 data URI 和 EXIF 元数据解决的问题不同。"
      ]
    }
  },
  tw: {
    question(title) { return `${title}是什麼工具？`; },
    topic: "主題",
    directAnswer: "直接答案",
    keyFact: "關鍵事實",
    processingModel: "處理方式",
    source: "來源",
    processingValue: "在瀏覽器本機執行；沒有正式環境 Node 伺服器接收輸入內容。",
    categoryBullets: {
      "hash-cryptography": [
        "<strong>本機處理：</strong>輸入在瀏覽器中處理，不會由靜態網站上傳。",
        "<strong>開發者工作流程：</strong>適合用於負載檢查、測試資料、驗證以及可重複的複製/下載輸出。",
        "<strong>安全邊界：</strong>編碼和雜湊並不等同於加密機密資訊。"
      ],
      "number-conversion": [
        "<strong>本機處理：</strong>數值由瀏覽器 JavaScript 轉換，不需要伺服器往返。",
        "<strong>開發者工作流程：</strong>適合在程式、協定、顏色和文件格式之間轉換數值。",
        "<strong>驗證：</strong>在把輸出用於正式程式碼前，應修正無效數字、範圍或格式。"
      ],
      "string-text-utilities": [
        "<strong>本機處理：</strong>文字在瀏覽器中完成轉換或分析。",
        "<strong>開發者工作流程：</strong>適合用於文案編輯、測試資料、日誌、程式片段和內容 QA。",
        "<strong>Unicode 意識：</strong>可見字元、碼元、單字、行和位元組是不同的計量方式。"
      ],
      "formatter-minifier": [
        "<strong>本機處理：</strong>原始碼文字在瀏覽器中格式化、壓縮、比較或轉換。",
        "<strong>開發者工作流程：</strong>適合在提交前、API 偵錯、設定清理或文件範例中使用。",
        "<strong>驗證：</strong>格式化輸出應保持資料含義；壓縮輸出部署前應測試。"
      ],
      "image-utilities": [
        "<strong>本機處理：</strong>圖片透過瀏覽器 API 處理，而不是上傳到伺服器。",
        "<strong>開發者工作流程：</strong>適合快速準備素材、預覽、隱私清理以及 HTML/CSS 嵌入。",
        "<strong>格式意識：</strong>PNG、JPEG、WebP、Base64 data URI 和 EXIF 中繼資料解決的問題不同。"
      ]
    }
  },
  jp: {
    question(title) { return `${title} は何をするツールですか？`; },
    topic: "項目",
    directAnswer: "直接回答",
    keyFact: "重要な事実",
    processingModel: "処理方式",
    source: "出典",
    processingValue: "ブラウザ内でローカルに実行され、本番用の Node サーバーは入力を受け取りません。",
    categoryBullets: {
      "hash-cryptography": [
        "<strong>ローカル処理：</strong>入力はブラウザで処理され、静的サイトからアップロードされません。",
        "<strong>開発者ワークフロー：</strong>ペイロード確認、テストデータ、検証、コピー/ダウンロード出力に使えます。",
        "<strong>セキュリティ境界：</strong>エンコードやハッシュ化は、秘密情報の暗号化とは異なります。"
      ],
      "number-conversion": [
        "<strong>ローカル処理：</strong>値はブラウザ JavaScript で変換され、サーバー往復は不要です。",
        "<strong>開発者ワークフロー：</strong>プログラミング、プロトコル、色、ドキュメント形式間の値変換に使えます。",
        "<strong>検証：</strong>出力を本番コードで使う前に、無効な桁、範囲、形式を修正してください。"
      ],
      "string-text-utilities": [
        "<strong>ローカル処理：</strong>テキストはブラウザ内で変換または分析されます。",
        "<strong>開発者ワークフロー：</strong>コピー編集、テストデータ、ログ、コード片、コンテンツ QA に使えます。",
        "<strong>Unicode の注意：</strong>見た目の文字、コード単位、単語、行、バイトは異なる指標です。"
      ],
      "formatter-minifier": [
        "<strong>ローカル処理：</strong>ソーステキストはブラウザ内で整形、圧縮、比較、変換されます。",
        "<strong>開発者ワークフロー：</strong>コミット前、API デバッグ、設定整理、ドキュメント例に使えます。",
        "<strong>検証：</strong>整形出力はデータの意味を保ち、圧縮出力はデプロイ前にテストしてください。"
      ],
      "image-utilities": [
        "<strong>ローカル処理：</strong>画像はサーバーへアップロードせず、ブラウザ API で処理されます。",
        "<strong>開発者ワークフロー：</strong>素材準備、プレビュー、プライバシー整理、HTML/CSS 埋め込みに使えます。",
        "<strong>形式の理解：</strong>PNG、JPEG、WebP、Base64 data URI、EXIF メタデータは用途が異なります。"
      ]
    }
  },
  kr: {
    question(title) { return `${title} 도구는 무엇을 하나요?`; },
    topic: "항목",
    directAnswer: "직접 답변",
    keyFact: "핵심 사실",
    processingModel: "처리 방식",
    source: "출처",
    processingValue: "브라우저에서 로컬로 실행되며 프로덕션 Node 서버가 입력을 받지 않습니다.",
    categoryBullets: {
      "hash-cryptography": [
        "<strong>로컬 처리:</strong> 입력은 브라우저에서 처리되며 정적 사이트가 업로드하지 않습니다.",
        "<strong>개발자 워크플로:</strong> 페이로드 검사, 테스트 데이터, 검증, 반복 가능한 복사/다운로드 출력에 적합합니다.",
        "<strong>보안 경계:</strong> 인코딩과 해싱은 비밀 정보를 암호화하는 것과 다릅니다."
      ],
      "number-conversion": [
        "<strong>로컬 처리:</strong> 값은 브라우저 JavaScript에서 변환되며 서버 왕복이 필요하지 않습니다.",
        "<strong>개발자 워크플로:</strong> 프로그래밍, 프로토콜, 색상, 문서 형식 사이의 값 변환에 적합합니다.",
        "<strong>검증:</strong> 출력을 프로덕션 코드에 사용하기 전에 잘못된 숫자, 범위, 형식을 수정하세요."
      ],
      "string-text-utilities": [
        "<strong>로컬 처리:</strong> 텍스트는 브라우저 안에서 변환되거나 분석됩니다.",
        "<strong>개발자 워크플로:</strong> 문구 편집, 테스트 픽스처, 로그, 코드 조각, 콘텐츠 QA에 적합합니다.",
        "<strong>Unicode 이해:</strong> 보이는 문자, 코드 단위, 단어, 줄, 바이트는 서로 다른 측정값입니다."
      ],
      "formatter-minifier": [
        "<strong>로컬 처리:</strong> 소스 텍스트는 브라우저에서 포맷, 압축, 비교 또는 변환됩니다.",
        "<strong>개발자 워크플로:</strong> 커밋 전, API 디버깅, 설정 정리, 문서 예제에 적합합니다.",
        "<strong>검증:</strong> 포맷된 출력은 데이터 의미를 보존해야 하며, 압축 출력은 배포 전에 테스트해야 합니다."
      ],
      "image-utilities": [
        "<strong>로컬 처리:</strong> 이미지는 서버에 업로드되지 않고 브라우저 API로 처리됩니다.",
        "<strong>개발자 워크플로:</strong> 빠른 에셋 준비, 미리보기, 개인정보 정리, HTML/CSS 임베딩에 적합합니다.",
        "<strong>형식 이해:</strong> PNG, JPEG, WebP, Base64 data URI, EXIF 메타데이터는 서로 다른 문제를 해결합니다."
      ]
    }
  },
  fr: {
    question(title) { return `À quoi sert l'outil ${title} ?`; },
    topic: "Sujet",
    directAnswer: "Réponse directe",
    keyFact: "Fait clé",
    processingModel: "Mode de traitement",
    source: "Source",
    processingValue: "S'exécute localement dans le navigateur ; aucun serveur Node de production ne reçoit l'entrée.",
    categoryBullets: {
      "hash-cryptography": [
        "<strong>Traitement local :</strong> l'entrée est traitée dans le navigateur et n'est pas téléversée par le site statique.",
        "<strong>Flux développeur :</strong> utile pour inspecter des charges utiles, créer des données de test, vérifier et copier/télécharger des résultats reproductibles.",
        "<strong>Limite de sécurité :</strong> l'encodage et le hachage ne sont pas du chiffrement de secrets."
      ],
      "number-conversion": [
        "<strong>Traitement local :</strong> les valeurs sont converties en JavaScript dans le navigateur, sans aller-retour serveur.",
        "<strong>Flux développeur :</strong> utile pour traduire des valeurs entre formats de programmation, protocoles, couleurs et documentation.",
        "<strong>Validation :</strong> corrigez les chiffres, plages ou formats invalides avant d'utiliser la sortie en production."
      ],
      "string-text-utilities": [
        "<strong>Traitement local :</strong> le texte reste dans le navigateur pendant la transformation ou l'analyse.",
        "<strong>Flux développeur :</strong> utile pour la rédaction, les jeux de test, les journaux, les extraits de code et la QA de contenu.",
        "<strong>Conscience Unicode :</strong> caractères visibles, unités de code, mots, lignes et octets sont des mesures différentes."
      ],
      "formatter-minifier": [
        "<strong>Traitement local :</strong> le texte source est formaté, minifié, comparé ou converti dans le navigateur.",
        "<strong>Flux développeur :</strong> utile avant les commits, le débogage d'API, le nettoyage de configuration ou les exemples de documentation.",
        "<strong>Validation :</strong> la sortie formatée doit préserver le sens des données ; la sortie minifiée doit être testée avant déploiement."
      ],
      "image-utilities": [
        "<strong>Traitement local :</strong> les images sont traitées avec les API du navigateur au lieu d'être téléversées vers un serveur.",
        "<strong>Flux développeur :</strong> utile pour préparer des ressources, prévisualiser, nettoyer la confidentialité et intégrer en HTML/CSS.",
        "<strong>Formats :</strong> PNG, JPEG, WebP, URI de données Base64 et métadonnées EXIF répondent à des besoins différents."
      ]
    }
  },
  de: {
    question(title) { return `Wofür ist ${title} gedacht?`; },
    topic: "Thema",
    directAnswer: "Direkte Antwort",
    keyFact: "Wichtige Tatsache",
    processingModel: "Verarbeitungsmodell",
    source: "Quelle",
    processingValue: "Läuft lokal im Browser; kein produktiver Node-Server empfängt die Eingabe.",
    categoryBullets: {
      "hash-cryptography": [
        "<strong>Lokale Verarbeitung:</strong> Eingaben werden im Browser verarbeitet und nicht von der statischen Website hochgeladen.",
        "<strong>Entwickler-Workflow:</strong> geeignet für Payload-Prüfung, Testdaten, Verifikation und wiederholbare Kopier-/Download-Ausgaben.",
        "<strong>Sicherheitsgrenze:</strong> Kodierung und Hashing sind nicht dasselbe wie das Verschlüsseln von Geheimnissen."
      ],
      "number-conversion": [
        "<strong>Lokale Verarbeitung:</strong> Werte werden in Browser-JavaScript konvertiert, ohne Server-Roundtrip.",
        "<strong>Entwickler-Workflow:</strong> geeignet zum Übersetzen von Werten zwischen Programmierung, Protokollen, Farben und Dokumentation.",
        "<strong>Validierung:</strong> ungültige Ziffern, Bereiche oder Formate sollten vor der Nutzung in Produktionscode korrigiert werden."
      ],
      "string-text-utilities": [
        "<strong>Lokale Verarbeitung:</strong> Text bleibt im Browser, während er transformiert oder analysiert wird.",
        "<strong>Entwickler-Workflow:</strong> geeignet für Textarbeit, Testdaten, Logs, Code-Snippets und Content-QA.",
        "<strong>Unicode-Bewusstsein:</strong> sichtbare Zeichen, Code-Einheiten, Wörter, Zeilen und Bytes sind unterschiedliche Messgrößen."
      ],
      "formatter-minifier": [
        "<strong>Lokale Verarbeitung:</strong> Quelltext wird im Browser formatiert, minifiziert, verglichen oder konvertiert.",
        "<strong>Entwickler-Workflow:</strong> geeignet vor Commits, beim API-Debugging, zur Konfigurationsbereinigung oder für Dokumentationsbeispiele.",
        "<strong>Validierung:</strong> formatierte Ausgabe sollte die Bedeutung erhalten; minifizierte Ausgabe sollte vor dem Deployment getestet werden."
      ],
      "image-utilities": [
        "<strong>Lokale Verarbeitung:</strong> Bilder werden mit Browser-APIs verarbeitet, statt auf einen Server hochgeladen zu werden.",
        "<strong>Entwickler-Workflow:</strong> geeignet für schnelle Asset-Vorbereitung, Vorschauen, Datenschutzbereinigung und HTML/CSS-Einbettung.",
        "<strong>Formatbewusstsein:</strong> PNG, JPEG, WebP, Base64-Data-URIs und EXIF-Metadaten lösen unterschiedliche Probleme."
      ]
    }
  },
  es: {
    question(title) { return `¿Para qué sirve ${title}?`; },
    topic: "Tema",
    directAnswer: "Respuesta directa",
    keyFact: "Dato clave",
    processingModel: "Modelo de procesamiento",
    source: "Fuente",
    processingValue: "Se ejecuta localmente en el navegador; ningún servidor Node de producción recibe la entrada.",
    categoryBullets: {
      "hash-cryptography": [
        "<strong>Procesamiento local:</strong> la entrada se procesa en el navegador y no se sube desde el sitio estático.",
        "<strong>Flujo de desarrollo:</strong> útil para inspección de payloads, datos de prueba, verificación y salida repetible de copia/descarga.",
        "<strong>Límite de seguridad:</strong> codificar y aplicar hash no es lo mismo que cifrar secretos."
      ],
      "number-conversion": [
        "<strong>Procesamiento local:</strong> los valores se convierten con JavaScript en el navegador, sin ida y vuelta al servidor.",
        "<strong>Flujo de desarrollo:</strong> útil para traducir valores entre formatos de programación, protocolos, color y documentación.",
        "<strong>Validación:</strong> corrija dígitos, rangos o formatos inválidos antes de usar la salida en código de producción."
      ],
      "string-text-utilities": [
        "<strong>Procesamiento local:</strong> el texto permanece en el navegador mientras se transforma o analiza.",
        "<strong>Flujo de desarrollo:</strong> útil para edición, datos de prueba, registros, fragmentos de código y QA de contenido.",
        "<strong>Conciencia Unicode:</strong> caracteres visibles, unidades de código, palabras, líneas y bytes son medidas diferentes."
      ],
      "formatter-minifier": [
        "<strong>Procesamiento local:</strong> el texto fuente se formatea, minifica, compara o convierte en el navegador.",
        "<strong>Flujo de desarrollo:</strong> útil antes de commits, depuración de APIs, limpieza de configuración o ejemplos de documentación.",
        "<strong>Validación:</strong> la salida formateada debe preservar el significado; la salida minificada debe probarse antes de desplegar."
      ],
      "image-utilities": [
        "<strong>Procesamiento local:</strong> las imágenes se procesan con APIs del navegador en lugar de subirse a un servidor.",
        "<strong>Flujo de desarrollo:</strong> útil para preparar recursos, previsualizar, limpiar privacidad e incrustar en HTML/CSS.",
        "<strong>Formatos:</strong> PNG, JPEG, WebP, data URI Base64 y metadatos EXIF resuelven problemas distintos."
      ]
    }
  },
  pt: {
    question(title) { return `Para que serve ${title}?`; },
    topic: "Tópico",
    directAnswer: "Resposta direta",
    keyFact: "Fato-chave",
    processingModel: "Modelo de processamento",
    source: "Fonte",
    processingValue: "Executa localmente no navegador; nenhum servidor Node de produção recebe a entrada.",
    categoryBullets: {
      "hash-cryptography": [
        "<strong>Processamento local:</strong> a entrada é tratada no navegador e não é enviada pelo site estático.",
        "<strong>Fluxo de desenvolvimento:</strong> útil para inspeção de payloads, dados de teste, verificação e saída repetível de cópia/download.",
        "<strong>Limite de segurança:</strong> codificação e hash não são o mesmo que criptografar segredos."
      ],
      "number-conversion": [
        "<strong>Processamento local:</strong> os valores são convertidos em JavaScript no navegador, sem ida e volta ao servidor.",
        "<strong>Fluxo de desenvolvimento:</strong> útil para traduzir valores entre formatos de programação, protocolos, cores e documentação.",
        "<strong>Validação:</strong> corrija dígitos, intervalos ou formatos inválidos antes de usar a saída em código de produção."
      ],
      "string-text-utilities": [
        "<strong>Processamento local:</strong> o texto permanece no navegador enquanto é transformado ou analisado.",
        "<strong>Fluxo de desenvolvimento:</strong> útil para edição, dados de teste, logs, trechos de código e QA de conteúdo.",
        "<strong>Consciência Unicode:</strong> caracteres visíveis, unidades de código, palavras, linhas e bytes são medidas diferentes."
      ],
      "formatter-minifier": [
        "<strong>Processamento local:</strong> o texto-fonte é formatado, minificado, comparado ou convertido no navegador.",
        "<strong>Fluxo de desenvolvimento:</strong> útil antes de commits, depuração de APIs, limpeza de configuração ou exemplos de documentação.",
        "<strong>Validação:</strong> a saída formatada deve preservar o significado; a saída minificada deve ser testada antes da implantação."
      ],
      "image-utilities": [
        "<strong>Processamento local:</strong> as imagens são tratadas com APIs do navegador em vez de serem enviadas a um servidor.",
        "<strong>Fluxo de desenvolvimento:</strong> útil para preparar recursos, visualizar, limpar privacidade e incorporar em HTML/CSS.",
        "<strong>Formatos:</strong> PNG, JPEG, WebP, data URI Base64 e metadados EXIF resolvem problemas diferentes."
      ]
    }
  }
};

const categorySource = {
  "hash-cryptography": sources.browser,
  "number-conversion": sources.browser,
  "string-text-utilities": sources.unicode,
  "formatter-minifier": sources.browser,
  "image-utilities": sources.canvas
};

const details = {
  "base64-encode": {
    answer: "<strong>Base64 Encode</strong> converts text to Base64 and decodes Base64 back to readable text in your browser.",
    fact: "Standard Base64 maps <strong>3 input bytes</strong> to <strong>4 output characters</strong>, so output is usually about <strong>33.3% larger</strong>.",
    source: sources.base64
  },
  "base64-decode": {
    answer: "<strong>Base64 Decode</strong> turns Base64 strings back into readable text and can also encode text for quick round-trip checks.",
    fact: "RFC 4648 Base64 uses <code>A-Z</code>, <code>a-z</code>, <code>0-9</code>, <code>+</code>, <code>/</code>, and optional <code>=</code> padding.",
    source: sources.base64
  },
  "md5-generator": {
    answer: "<strong>MD5 Generator</strong> creates a deterministic MD5 digest from text input for legacy checksums and non-security comparisons.",
    fact: "MD5 produces a <strong>128-bit</strong> message digest, commonly displayed as <strong>32 hexadecimal characters</strong>.",
    source: sources.md5
  },
  "sha1-generator": {
    answer: "<strong>SHA-1 Generator</strong> creates a SHA-1 digest for compatibility checks where SHA-1 is still expected.",
    fact: "SHA-1 produces a <strong>160-bit</strong> message digest in the Secure Hash Standard family.",
    source: sources.fips180
  },
  "sha256-generator": {
    answer: "<strong>SHA-256 Generator</strong> creates a SHA-256 digest for integrity checks, signatures, and modern hash workflows.",
    fact: "SHA-256 produces a <strong>256-bit</strong> digest and belongs to the SHA-2 family specified by NIST.",
    source: sources.fips180
  },
  "sha384-generator": {
    answer: "<strong>SHA-384 Generator</strong> creates a SHA-384 digest for systems that require a 384-bit SHA-2 output.",
    fact: "SHA-384 produces a <strong>384-bit</strong> digest and is a SHA-2 variant derived from the SHA-512 design.",
    source: sources.fips180
  },
  "sha512-generator": {
    answer: "<strong>SHA-512 Generator</strong> creates a SHA-512 digest for high-strength integrity and compatibility workflows.",
    fact: "SHA-512 produces a <strong>512-bit</strong> digest and is part of the NIST Secure Hash Standard.",
    source: sources.fips180
  },
  "password-generator": {
    answer: "<strong>Password Generator</strong> creates random passwords from configurable character sets, length, and symbol rules.",
    fact: "Password search space grows exponentially: a <strong>16-character</strong> password from <strong>94 printable ASCII characters</strong> has far more combinations than an 8-character one.",
    source: sources.browser
  },
  "url-encode": {
    answer: "<strong>URL Encode</strong> percent-encodes text so reserved or non-ASCII characters can be placed safely in URLs.",
    fact: "Percent-encoding represents bytes as <code>%HH</code>, where <code>HH</code> is a <strong>2-digit hexadecimal</strong> value.",
    source: sources.url
  },
  "url-decode": {
    answer: "<strong>URL Decode</strong> reverses percent-encoded text and parses query-string parameters into readable key/value pairs.",
    fact: "Query strings commonly use <code>&amp;</code> between parameters and <code>=</code> between a parameter name and value.",
    source: sources.url
  },
  "hex-to-decimal": { answer: "<strong>Hex to Decimal</strong> converts base-16 values into base-10 numbers.", fact: "Hexadecimal uses <strong>16 symbols</strong>: digits <code>0-9</code> and letters <code>A-F</code>.", source: sources.browser },
  "decimal-to-hex": { answer: "<strong>Decimal to Hex</strong> converts base-10 numbers into hexadecimal notation.", fact: "One hexadecimal digit represents exactly <strong>4 bits</strong>, so one byte is usually written as 2 hex digits.", source: sources.browser },
  "octal-to-decimal": { answer: "<strong>Octal to Decimal</strong> converts base-8 values into base-10 numbers.", fact: "Octal uses <strong>8 symbols</strong>, <code>0-7</code>, and each octal digit represents <strong>3 bits</strong>.", source: sources.browser },
  "decimal-to-octal": { answer: "<strong>Decimal to Octal</strong> converts base-10 numbers into octal notation.", fact: "Octal groups binary digits in sets of <strong>3 bits</strong>, which is why it appears in Unix-style file permissions.", source: sources.browser },
  "binary-to-decimal": { answer: "<strong>Binary to Decimal</strong> converts base-2 numbers into base-10 numbers.", fact: "Binary uses only <strong>2 digits</strong>, <code>0</code> and <code>1</code>; each position is a power of 2.", source: sources.browser },
  "decimal-to-binary": { answer: "<strong>Decimal to Binary</strong> converts base-10 numbers into base-2 notation.", fact: "A byte contains <strong>8 bits</strong>, so values from 0 to 255 fit in one unsigned byte.", source: sources.browser },
  "binary-to-hex": { answer: "<strong>Binary to Hex</strong> converts base-2 values into compact hexadecimal notation.", fact: "Every <strong>4 binary bits</strong> map to exactly <strong>1 hexadecimal digit</strong>.", source: sources.browser },
  "hex-to-binary": { answer: "<strong>Hex to Binary</strong> expands hexadecimal digits into their 4-bit binary representation.", fact: "A 2-digit hex byte such as <code>FF</code> maps to <code>11111111</code>, or decimal 255.", source: sources.browser },
  "ascii-table": { answer: "<strong>ASCII Table</strong> is a reference for decimal, hexadecimal, octal, and binary values for standard ASCII characters.", fact: "ASCII defines <strong>128 code points</strong>: 95 printable characters and 33 control characters.", source: sources.unicode },
  "hex-to-ascii": { answer: "<strong>Hex to ASCII</strong> converts hexadecimal byte values into readable ASCII text.", fact: "ASCII characters occupy values <strong>0-127</strong>; printable characters start at decimal 32.", source: sources.unicode },
  "ascii-to-hex": { answer: "<strong>ASCII to Hex</strong> converts text characters into hexadecimal byte values.", fact: "A printable ASCII character can be represented as a <strong>2-digit hex byte</strong>, such as <code>41</code> for <code>A</code>.", source: sources.unicode },
  "binary-to-text": { answer: "<strong>Binary to Text</strong> converts 8-bit binary byte groups into readable text.", fact: "One text byte is commonly shown as <strong>8 binary digits</strong>, for example <code>01000001</code> for <code>A</code>.", source: sources.utf8 },
  "text-to-binary": { answer: "<strong>Text to Binary</strong> converts text into binary byte notation for inspection and teaching.", fact: "UTF-8 stores ASCII characters in <strong>1 byte</strong>, while many non-ASCII characters use 2 to 4 bytes.", source: sources.utf8 },
  "fraction-to-decimal": { answer: "<strong>Fraction to Decimal</strong> converts numerator/denominator values into decimal numbers.", fact: "A fraction terminates in base 10 only when the reduced denominator has no prime factors except <strong>2</strong> and <strong>5</strong>.", source: sources.browser },
  "decimal-to-fraction": { answer: "<strong>Decimal to Fraction</strong> converts decimal values into simplified numerator/denominator form.", fact: "A finite decimal can be written as an integer over a power of <strong>10</strong>, then reduced by the greatest common divisor.", source: sources.browser },
  "percent-to-decimal": { answer: "<strong>Percent to Decimal</strong> converts percentages into decimal numbers.", fact: "Percent means per hundred, so <strong>75%</strong> equals <strong>0.75</strong>.", source: sources.browser },
  "decimal-to-percent": { answer: "<strong>Decimal to Percent</strong> converts decimal numbers into percentages.", fact: "Multiplying by <strong>100</strong> converts a decimal ratio into percent form.", source: sources.browser },
  "percent-to-fraction": { answer: "<strong>Percent to Fraction</strong> converts percentages into simplified fractions.", fact: "A percentage is first written over <strong>100</strong>, then reduced to lowest terms.", source: sources.browser },
  "fraction-to-percent": { answer: "<strong>Fraction to Percent</strong> converts fractions into percentage values.", fact: "Dividing numerator by denominator and multiplying by <strong>100</strong> gives the percent value.", source: sources.browser },
  "hex-to-rgb": { answer: "<strong>Hex to RGB</strong> converts CSS hexadecimal colors into red, green, and blue channel values.", fact: "<code>#RRGGBB</code> uses <strong>6 hexadecimal digits</strong>; each 2-digit pair maps to a 0-255 channel.", source: sources.cssColor },
  "rgb-to-hex": { answer: "<strong>RGB to Hex</strong> converts red, green, and blue channel values into CSS hex color notation.", fact: "Each RGB channel is commonly represented as an integer from <strong>0</strong> to <strong>255</strong>.", source: sources.cssColor },
  "hex-to-rgba": { answer: "<strong>Hex to RGBA</strong> converts CSS hex colors into red, green, blue, and alpha values.", fact: "<code>#RRGGBBAA</code> uses <strong>8 hexadecimal digits</strong>, with the last 2 digits representing alpha.", source: sources.cssColor },
  "rgba-to-hex": { answer: "<strong>RGBA to Hex</strong> converts RGBA color values into CSS hex notation with alpha.", fact: "CSS alpha can be expressed from <strong>0</strong> to <strong>1</strong>, then mapped to a hex byte from <code>00</code> to <code>FF</code>.", source: sources.cssColor },
  "roman-numerals-chart": { answer: "<strong>Roman Numerals Chart</strong> provides a quick reference for converting common decimal numbers into Roman numerals.", fact: "Standard Roman numerals use <strong>7 symbols</strong>: I, V, X, L, C, D, and M.", source: sources.browser },
  "roman-numerals-to-numbers": { answer: "<strong>Roman to Numbers</strong> converts Roman numerals into decimal numbers.", fact: "Subtractive pairs such as <code>IV</code>, <code>IX</code>, <code>XL</code>, <code>XC</code>, <code>CD</code>, and <code>CM</code> represent values before larger symbols.", source: sources.browser },
  "numbers-to-roman-numerals": { answer: "<strong>Numbers to Roman</strong> converts decimal numbers into Roman numeral notation.", fact: "Roman numeral conversion is usually limited to <strong>1-3999</strong> when using standard overline-free notation.", source: sources.browser },
  "text-editor": { answer: "<strong>Text Editor Online</strong> provides a browser-based scratchpad with line numbers, word wrap, and character counting.", fact: "Line-oriented editing is useful because many code reviews, logs, and compiler errors reference exact <strong>line numbers</strong>.", source: sources.browser },
  "regex-tester": { answer: "<strong>Regex Tester</strong> tests regular expressions against sample text with live match feedback.", fact: "JavaScript regular expressions are defined by ECMAScript and support flags such as <code>g</code>, <code>i</code>, <code>m</code>, <code>s</code>, <code>u</code>, and <code>y</code>.", source: sources.ecma262 },
  "regex-replace": { answer: "<strong>Regex Replace</strong> finds text patterns and replaces matches using JavaScript regular expressions.", fact: "Replacement strings can use capture groups, making regex replace useful for structured text rewrites.", source: sources.ecma262 },
  "text-compare": { answer: "<strong>Text Compare</strong> compares two text blocks line by line and highlights additions, removals, and changes.", fact: "Line-based diffs are the same comparison model used by many code review and version-control workflows.", source: sources.browser },
  "word-counter": { answer: "<strong>Word Counter</strong> counts words, characters, sentences, and paragraphs in pasted text.", fact: "Word counts depend on tokenization rules, while character counts depend on Unicode and whitespace handling.", source: sources.unicode },
  "character-count": { answer: "<strong>Character Count</strong> reports characters, words, lines, and UTF-8 bytes for pasted text.", fact: "UTF-8 uses <strong>1 to 4 bytes</strong> per Unicode code point, so byte count can exceed visible character count.", source: sources.utf8 },
  "case-converter": { answer: "<strong>Case Converter</strong> changes text between uppercase, lowercase, sentence case, title case, and inverted case.", fact: "Case mapping can be language-sensitive; Unicode defines more than simple ASCII <code>A-Z</code> transformations.", source: sources.unicode },
  "reverse-text": { answer: "<strong>Reverse Text</strong> reverses the order of text for quick string experiments and test cases.", fact: "Reversing Unicode text can differ from reversing visible grapheme clusters such as emoji sequences or accented characters.", source: sources.unicode },
  "number-to-words": { answer: "<strong>Number to Words</strong> converts numbers into English cardinal words, ordinal words, and ordinal suffixes.", fact: "English ordinals use suffix rules such as <code>1st</code>, <code>2nd</code>, <code>3rd</code>, and <code>4th</code>, with special cases for 11th-13th.", source: sources.browser },
  "json-formatter": { answer: "<strong>JSON Formatter</strong> formats JSON into readable indentation while preserving the data structure.", fact: "JSON has <strong>4 primitive types</strong> and <strong>2 structured types</strong>: objects and arrays.", source: sources.json },
  "json-diff": { answer: "<strong>JSON Diff</strong> compares two JSON documents and highlights structural value changes.", fact: "JSON objects are name/value collections, while arrays are ordered sequences, so object and array diffs must be interpreted differently.", source: sources.json },
  "json-minifier": { answer: "<strong>JSON Minifier</strong> removes insignificant whitespace from JSON to produce compact output.", fact: "Whitespace outside JSON strings is insignificant, but whitespace inside quoted strings is data and must be preserved.", source: sources.json },
  "xml-formatter": { answer: "<strong>XML Formatter</strong> formats XML markup with readable indentation and nested structure.", fact: "XML documents use elements, attributes, text nodes, and a single document root element.", source: sources.xml },
  "xml-minifier": { answer: "<strong>XML Minifier</strong> removes unnecessary spacing from XML while preserving markup meaning.", fact: "Whitespace can be meaningful in XML text nodes, so XML minification must avoid changing content data.", source: sources.xml },
  "json-to-xml": { answer: "<strong>JSON to XML</strong> converts JSON structures into XML markup for systems that require XML input.", fact: "JSON objects and arrays do not map one-to-one to XML elements and attributes, so conversion rules matter.", source: sources.json },
  "xml-to-json": { answer: "<strong>XML to JSON</strong> converts XML markup into JSON-like data for easier inspection or API use.", fact: "XML attributes, repeated elements, and text nodes need explicit mapping when represented as JSON.", source: sources.xml },
  "html-beautifier": { answer: "<strong>HTML Beautifier</strong> formats HTML markup into readable indentation and nested tags.", fact: "HTML parsing follows browser rules from the HTML Standard, including error recovery for many malformed documents.", source: sources.html },
  "html-minifier": { answer: "<strong>HTML Minifier</strong> removes comments and unnecessary whitespace from HTML for smaller markup.", fact: "HTML whitespace may affect inline layout, so minification should preserve text-rendering intent.", source: sources.html },
  "javascript-beautifier": { answer: "<strong>JavaScript Beautifier</strong> formats JavaScript source for readability without changing intended behavior.", fact: "JavaScript syntax is standardized by ECMAScript and includes statements, expressions, modules, and functions.", source: sources.ecma262 },
  "javascript-minifier": { answer: "<strong>JavaScript Minifier</strong> reduces JavaScript size by removing whitespace, comments, and optional syntax overhead.", fact: "Minification changes source text but should preserve runtime behavior; always test minified scripts before release.", source: sources.ecma262 },
  "css-beautifier": { answer: "<strong>CSS Beautifier</strong> formats CSS rules, selectors, declarations, and blocks for readability.", fact: "CSS declarations pair a property with a value, and rule blocks apply those declarations to selectors.", source: sources.cssColor },
  "css-minifier": { answer: "<strong>CSS Minifier</strong> removes unnecessary whitespace and comments from CSS to produce compact stylesheets.", fact: "CSS minification can shorten colors and spacing, but must preserve cascade, selector, and declaration behavior.", source: sources.cssColor },
  "sql-formatter": { answer: "<strong>SQL Formatter</strong> formats SQL queries with consistent indentation and keyword layout.", fact: "SQL statements commonly include DQL, DML, and DDL operations such as <code>SELECT</code>, <code>INSERT</code>, <code>UPDATE</code>, and <code>CREATE</code>.", source: sources.browser },
  "sql-minifier": { answer: "<strong>SQL Minifier</strong> removes unnecessary formatting from SQL queries for compact storage or embedding.", fact: "SQL whitespace separates tokens, so minification must preserve spaces where identifiers, literals, and keywords would otherwise merge.", source: sources.browser },
  "photo2pixel": {
    answer: "<strong>Photo2Pixel</strong> converts photos into pixel-art-style PNGs locally in the browser with ONNX/WASM processing.",
    fact: "Pixel size controls how chunky the result looks; edge density only affects Enhance Edge mode, where lower thresholds preserve more outline detail.",
    source: sources.canvas,
    bullets: [
      "Supports PNG, JPEG, and WebP uploads up to 10MB.",
      "Offers Enhance Edge, Isolate Pixel, and Raw Pixel style modes.",
      "Exports the generated pixel-art preview as a PNG without sending the source image to a server."
    ]
  },
  "image-resize": { answer: "<strong>Image Resize</strong> changes image dimensions in the browser for PNG, JPEG, and WebP files.", fact: "Resizing changes pixel dimensions; reducing width and height by <strong>50%</strong> cuts pixel count by <strong>75%</strong>.", source: sources.canvas },
  "image-crop": { answer: "<strong>Image Crop</strong> extracts a selected rectangular region from an image and exports the result.", fact: "Cropping changes composition and pixel dimensions without scaling the selected pixels unless an export size is applied.", source: sources.canvas },
  "compress-png": { answer: "<strong>Compress PNG</strong> reduces PNG file size by optimizing color representation for browser-generated output.", fact: "PNG is a lossless image format and supports alpha transparency.", source: sources.png },
  "compress-jpeg": { answer: "<strong>Compress JPEG</strong> reduces JPEG file size by re-encoding with adjustable quality.", fact: "JPEG compression is lossy, so lower quality usually means smaller files but more visible artifacts.", source: sources.jpeg },
  "progressive-jpeg": { answer: "<strong>Progressive JPEG</strong> converts baseline JPEG images into progressive JPEG output.", fact: "Progressive JPEG stores image data in multiple scans so a low-detail preview can appear before the full image finishes loading.", source: sources.jpeg },
  "image-to-base64": { answer: "<strong>Image to Base64</strong> converts image files into Base64 data URI strings for embedding in HTML or CSS.", fact: "Base64 data usually grows by about <strong>33.3%</strong> before the extra <code>data:</code> URI prefix is added.", source: sources.base64 },
  "exif-viewer": { answer: "<strong>EXIF Viewer</strong> reads photo metadata such as camera, timestamp, lens, orientation, and GPS fields when present.", fact: "EXIF metadata can include GPS coordinates, so it may reveal where a photo was taken.", source: sources.exif },
  "exif-remover": { answer: "<strong>EXIF Remover</strong> strips embedded photo metadata to reduce privacy leakage before sharing images.", fact: "Removing EXIF can delete camera, date, orientation, and GPS metadata while leaving image pixels intact.", source: sources.exif }
};

function defaultDetail(slug, tool) {
  return {
    answer: `<strong>${tool.title}</strong> ${tool.description.charAt(0).toLowerCase()}${tool.description.slice(1)}`,
    fact: "The tool runs entirely in the browser as part of a static Coding.Tools page.",
    source: categorySource[tool.category] || sources.browser
  };
}

function localizedTool(lang, slug, tool) {
  const langTools = toolDataAll[lang] || {};
  return langTools[slug] || (toolDataAll.en && toolDataAll.en[slug]) || {
    toolTitle: tool.title,
    toolDescription: tool.description,
    description: tool.description
  };
}

function localizedAnswer(lang, slug, tool, detail) {
  if (lang === "en" && detail.answer) return detail.answer;

  const td = localizedTool(lang, slug, tool);
  const title = td.toolTitle || tool.title;
  const description = td.toolDescription || td.description || tool.description;
  return `<strong>${title}</strong>: ${description}`;
}

function localizedFact(lang, slug, tool, detail) {
  if (lang === "en" && detail.fact) return detail.fact;

  const td = localizedTool(lang, slug, tool);
  const paragraphs = Array.isArray(td.whatIsParas) ? td.whatIsParas : [];
  return paragraphs[0] || td.inputNotesPara || td.description || detail.fact;
}

function localizedBullets(lang, category) {
  const text = localizedText[lang] || localizedText.en;
  return (text.categoryBullets && text.categoryBullets[category]) ||
    localizedText.en.categoryBullets[category] ||
    localizedText.en.categoryBullets["string-text-utilities"];
}

function englishAction(tool) {
  const actions = {
    "hash-cryptography": "Validate the result before using it in authentication, signing, checksum, or transport code.",
    "number-conversion": "Check accepted digits, ranges, signs, prefixes, and rounding before copying the converted value into code.",
    "string-text-utilities": "Review Unicode, whitespace, line break, and punctuation behavior before treating the output as production text.",
    "formatter-minifier": "Run the formatted or minified output through your parser, tests, or runtime when exact syntax behavior matters.",
    "image-utilities": "Compare visual quality, pixel dimensions, metadata, and exported file size before publishing the processed image."
  };

  return actions[tool.category] || "Validate the output before using it in production workflows.";
}

function englishBullets(tool, detail) {
  return [
    `<strong>Primary use:</strong> ${detail.answer}`,
    `<strong>Key technical fact:</strong> ${detail.fact}`,
    `<strong>Practical check:</strong> ${englishAction(tool)}`
  ];
}

function makeRows(lang, slug, tool, detail) {
  const text = localizedText[lang] || localizedText.en;
  const source = detail.source || categorySource[tool.category] || sources.browser;
  return [
    { label: text.directAnswer, value: localizedAnswer(lang, slug, tool, detail), source },
    { label: text.keyFact, value: localizedFact(lang, slug, tool, detail), source },
    { label: text.processingModel, value: text.processingValue, source: sources.browser }
  ];
}

function makeIntro(lang, slug, tool) {
  const text = localizedText[lang] || localizedText.en;
  const td = localizedTool(lang, slug, tool);
  const title = td.toolTitle || tool.title;
  const detail = details[slug] || defaultDetail(slug, tool);
  return {
    question: text.question(title),
    answer: localizedAnswer(lang, slug, tool, detail),
    bullets: lang === "en" ? (detail.bullets || englishBullets(tool, detail)) : localizedBullets(lang, tool.category),
    headers: {
      topic: text.topic,
      directAnswer: text.directAnswer,
      source: text.source
    },
    rows: makeRows(lang, slug, tool, detail)
  };
}

module.exports = Object.fromEntries(
  site.languageIds.map((lang) => [
    lang,
    Object.fromEntries(
      Object.entries(tools).map(([slug, tool]) => [slug, makeIntro(lang, slug, tool)])
    )
  ])
);
