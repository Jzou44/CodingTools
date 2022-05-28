from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_HexToDecimal_blueprint = Blueprint('Web_HexToDecimal_blueprint_DE', __name__)
template_dir = 'HexToDecimal/de/'

def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'de'
    return model

@Web_HexToDecimal_blueprint.route('/de/hex-to-decimal')
def hex_to_decimal():
    model = get_default_model()
    model['url'] = '/de/hex-to-decimal'
    model['enUrl'] = '/hex-to-decimal'
    model['headerTitle'] = 'Online-Konvertierungstool für Hexadezimal-Dezimalzahl  - Coding.Tools'
    model['bodyTitle'] = 'Online-Konvertierungstool für Hexadezimal-Dezimalzahl'
    model['description'] = 'Dieses Online-Tool zur Umwandlung von Hexadezimal nach Dezimalzahl hilft Ihnen, eine Hexadezimalzahl in eine Dezimalzahl umzuwandeln.'
    model['keywords'] = 'Hex bis Dezimal, Hexadezimal bis Dezimal'
    model['image'] = '/image/cartoon-hex-to-decimal.png'
    return render_template(template_dir + 'template_hex_to_decimal_de.html', model=model)


@Web_HexToDecimal_blueprint.route('/de/decimal-to-hex')
def decimal_to_hex():
    model = get_default_model()
    model['url'] = '/de/decimal-to-hex'
    model['enUrl'] = '/decimal-to-hex'
    model['headerTitle'] = 'Online-Konvertierungswerkzeug für Dezimal- zu Hexadezimalwert  - Coding.Tools'
    model['bodyTitle'] = 'Online-Konvertierungswerkzeug mit Dezimal- zu Hexadezimalwert'
    model['description'] = 'Dieses Online-Konvertierungswerkzeug von Dezimal zu Hex hilft Ihnen, eine Dezimalzahl in eine Hexadezimalzahl umzuwandeln.'
    model['keywords'] = 'Dezimal bis Hex, dezimal bis hexadezimal'
    model['image'] = '/image/cartoon-decimal-to-hex.png'
    return render_template(template_dir + 'template_decimal_to_hex_de.html', model=model)


@Web_HexToDecimal_blueprint.route('/de/octal-to-decimal')
def octal_to_decimal():
    model = get_default_model()
    model['url'] = '/de/octal-to-decimal'
    model['enUrl'] = '/octal-to-decimal'
    model['headerTitle'] = 'Online-Konvertierungswerkzeug für Oktal zu Dezimal  - Coding.Tools'
    model['bodyTitle'] = 'Oktal-Dezimal-Online-Konvertierungstool'
    model['description'] = 'Dieses Online-Tool zur Umwandlung von Oktal nach Dezimalzahl hilft Ihnen, eine Oktalzahl in eine Dezimalzahl umzuwandeln.'
    model['keywords'] = 'Oktal bis Dezimal, Oktal bis Dezimal'
    model['image'] = '/image/octal_to_decimal.png'
    return render_template(template_dir + 'template_octal_to_decimal_de.html', model=model)


@Web_HexToDecimal_blueprint.route('/de/decimal-to-octal')
def decimal_to_octal():
    model = get_default_model()
    model['url'] = '/de/decimal-to-octal'
    model['enUrl'] = '/decimal-to-octal'
    model['headerTitle'] = 'Online-Konvertierungstool von Decimal zu Octal  - Coding.Tools'
    model['bodyTitle'] = 'Online-Konvertierungswerkzeug für Dezimal- / Oktalumwandlung'
    model['description'] = 'Dieses Online-Konvertierungswerkzeug für Dezimalzahlen in Oktalwerte hilft Ihnen, eine Dezimalzahl in eine Oktalzahl umzuwandeln.'
    model['keywords'] = 'Dezimal nach Oktal, Dezimal nach Oktal'
    model['image'] = '/image/cartoon-decimal-to-octal.png'
    return render_template(template_dir + 'template_decimal_to_octal_de.html', model=model)


@Web_HexToDecimal_blueprint.route('/de/binary-to-decimal')
def binary_to_decimal():
    model = get_default_model()
    model['url'] = '/de/binary-to-decimal'
    model['enUrl'] = '/binary-to-decimal'
    model['headerTitle'] = 'Online-Konvertierungstool für Binär-Dezimalzahl  - Coding.Tools'
    model['bodyTitle'] = 'Online-Konvertierungstool für Binär- in Dezimalzahl'
    model['description'] = 'Mit diesem Online-Konvertierungswerkzeug für die Binär-Dezimalzahl können Sie eine Oktalzahl in eine Dezimalzahl konvertieren.'
    model['keywords'] = 'Binär bis dezimal, binär bis dezimal'
    model['image'] = '/image/cartoon-decimal-to-binary.png'
    return render_template(template_dir + 'template_binary_to_decimal_de.html', model=model)


@Web_HexToDecimal_blueprint.route('/de/decimal-to-binary')
def decimal_to_binary():
    model = get_default_model()
    model['url'] = '/de/decimal-to-binary'
    model['enUrl'] = '/decimal-to-binary'
    model['headerTitle'] = 'Online-Konvertierungstool für Dezimal- zu Binärcode  - Coding.Tools'
    model['bodyTitle'] = 'Dezimales zu binäres Online-Konvertierungswerkzeug'
    model['description'] = 'Dieses Online-Dezimal-Binär-Konvertierungstool hilft Ihnen, eine Dezimalzahl in eine Binärzahl umzuwandeln.'
    model['keywords'] = 'Dezimal zu Binär, Dezimal zu Binär'
    model['image'] = '/image/cartoon-decimal-to-binary.png'
    return render_template(template_dir + 'template_decimal_to_binary_de.html', model=model)


@Web_HexToDecimal_blueprint.route('/de/ascii-table')
def ascii_table():
    model = get_default_model()
    model['url'] = '/de/ascii-table'
    model['enUrl'] = '/ascii-table'
    model['headerTitle'] = 'ASCII-Lookup-Tabelle  - Coding.Tools'
    model['bodyTitle'] = 'ASCII-Lookup-Tabelle'
    model['description'] = 'Vollständige ASCII-Lookup-Tabelle (256 Bit), einschließlich ASCII-Steuerzeichen, ASCII-Symbole und erweiterte ASCII-Zeichen.'
    model['keywords'] = 'ASCII-Tabelle, ASCII-Erweiterungstabelle'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_ascii_table_de.html', model=model)


@Web_HexToDecimal_blueprint.route('/de/hex-to-ascii')
def hex_to_ascii():
    model = get_default_model()
    model['url'] = '/de/hex-to-ascii'
    model['enUrl'] = '/hex-to-ascii'
    model['headerTitle'] = 'Online-Konvertierungstool für Hexadezimal-ASCII-Zeichenfolge'
    model['bodyTitle'] = 'Online-Konvertierungstool für Hexadezimal in ASCII-Zeichenfolge'
    model['description'] = 'Mit diesem Online-Konvertierungswerkzeug für Hexadezimal-ASCII-Zeichenfolgen können Sie ein Hexadezimal-Array in eine ASCII-Zeichenfolge konvertieren.'
    model['keywords'] = 'Hex zu ASCII, Hex zu ASCII'
    model['image'] = '/image/cartoon-hex-to-ascii.png'
    return render_template(template_dir + 'template_hex_to_ascii_de.html', model=model)


@Web_HexToDecimal_blueprint.route('/de/ascii-to-hex')
def ascii_to_hex():
    model = get_default_model()
    model['url'] = '/de/ascii-to-hex'
    model['enUrl'] = '/ascii-to-hex'
    model['headerTitle'] = 'Online-Konvertierungstool für ASCII-Zeichenfolge in Hexadezimalwert'
    model['bodyTitle'] = 'Online-Konvertierungstool für ASCII-Zeichenfolge in Hexadezimalzahl'
    model['description'] = 'Dieses Online-Konvertierungswerkzeug für ASCII-Zeichenfolgen in Hex hilft Ihnen, eine ASCII-Zeichenfolge in ein Hexadezimal-Array umzuwandeln.'
    model['keywords'] = 'ASCII zu Hex, ASCII zu Hexadezimal'
    model['image'] = '/image/cartoon-ascii-to-hex.png'
    return render_template(template_dir + 'template_ascii_to_hex_de.html', model=model)


@Web_HexToDecimal_blueprint.route('/de/fraction-to-decimal')
def fraction_to_decimal():
    model = get_default_model()
    model['url'] = '/de/fraction-to-decimal'
    model['enUrl'] = '/fraction-to-decimal'
    model['headerTitle'] = 'Online-Konvertierungstool in Dezimalzahl  - Coding.Tools'
    model['bodyTitle'] = 'Online-Konvertierungstool in Dezimalzahlen'
    model['description'] = 'Mit diesem Online-Tool zur Umwandlung von Dezimalzahlen in Dezimalzahlen können Sie eine Bewertung in Dezimalzahlen konvertieren. Der Eingabezähler und der Nenner werden im Ergebnisfeld angezeigt.'
    model['keywords'] = 'Bruchteil zu Dezimalzahl, Bruchteil zu Dezimalzahl'
    model['image'] = '/image/cartoon-fraction-to-decimal.png'
    return render_template(template_dir + 'template_fraction_to_decimal_de.html', model=model)


@Web_HexToDecimal_blueprint.route('/de/decimal-to-fraction')
def decimal_to_fraction():
    model = get_default_model()
    model['url'] = '/de/decimal-to-fraction'
    model['enUrl'] = '/decimal-to-fraction'
    model['headerTitle'] = 'Dezimalwert für Online-Konvertierungstool  - Coding.Tools'
    model['bodyTitle'] = 'Dezimalwert für das Online-Konvertierungswerkzeug'
    model['description'] = 'Dieses Online-Tool zur Konvertierung von Dezimalzahlen in Punkte hilft Ihnen, eine Dezimalzahl in einen Bruch zu konvertieren. Geben Sie die Dezimalzahl ein, und die Bewertung wird im Ergebnisfeld angezeigt.'
    model['keywords'] = 'Dezimalzahl zu Bruchzahl, Bruchzahl zu Bruchzahl'
    model['image'] = '/image/cartoon-decimal-to-fraction.png'
    return render_template(template_dir + 'template_decimal_to_fraction_de.html', model=model)


@Web_HexToDecimal_blueprint.route('/de/percent-to-decimal')
def percent_to_decimal():
    model = get_default_model()
    model['url'] = '/de/percent-to-decimal'
    model['enUrl'] = '/percent-to-decimal'
    model['headerTitle'] = 'Online-Konvertierungstool in Dezimalzahlen  - Coding.Tools'
    model['bodyTitle'] = 'Online-Konvertierungstool in Prozent'
    model['description'] = 'Mit diesem Online-Tool zur Umwandlung von Prozenten in Dezimalzahlen können Sie einen Prozentsatz in Dezimalzahlen konvertieren. Geben Sie einen Prozentsatz ein, und die Dezimalzahl wird im Ergebnisfeld angezeigt.'
    model['keywords'] = 'Prozent bis Dezimal, Prozent bis Dezimal'
    model['image'] = '/image/cartoon-percent-to-decimal.png'
    return render_template(template_dir + 'template_percent_to_decimal_de.html', model=model)


@Web_HexToDecimal_blueprint.route('/de/decimal-to-percent')
def decimal_to_percent():
    model = get_default_model()
    model['url'] = '/de/decimal-to-percent'
    model['enUrl'] = '/decimal-to-percent'
    model['headerTitle'] = 'Online-Konvertierungstool in Dezimalzahlen  - Coding.Tools'
    model['bodyTitle'] = 'Online-Konvertierungstool in Prozent'
    model['description'] = 'Dieses Online-Konvertierungswerkzeug für Dezimalzahlen in Prozent hilft Ihnen bei der Konvertierung einer Dezimalzahl in Prozent.'
    model['keywords'] = 'Dezimal zu Prozent, Bruchteil zu Prozent'
    model['image'] = '/image/cartoon-decimal-to-percent.png'
    return render_template(template_dir + 'template_decimal_to_percent_de.html', model=model)


@Web_HexToDecimal_blueprint.route('/de/percent-to-fraction')
def percent_to_fraction():
    model = get_default_model()
    model['url'] = '/de/percent-to-fraction'
    model['enUrl'] = '/percent-to-fraction'
    model['headerTitle'] = 'Prozentsatz für das Online-Conversion-Tool  - Coding.Tools'
    model['bodyTitle'] = 'Prozentsatz für das Online-Conversion-Tool'
    model['description'] = 'Dieses Online-Tool zur Umwandlung von Prozentsätzen in Punkte hilft Ihnen, einen Prozentsatz in eine Bewertung umzuwandeln. Geben Sie den Prozentsatz ein und die Bewertung wird im Ergebnisfeld angezeigt.'
    model['keywords'] = 'Prozentsatz zu Bruchteil, Prozentsatz zu Bruchteil'
    model['image'] = '/image/cartoon-percent-to-fraction.png'
    return render_template(template_dir + 'template_percent_to_fraction_de.html', model=model)


@Web_HexToDecimal_blueprint.route('/de/fraction-to-percent')
def fraction_to_percent():
    model = get_default_model()
    model['url'] = '/de/fraction-to-percent'
    model['enUrl'] = '/fraction-to-percent'
    model['headerTitle'] = 'Online-Konvertierungstool in Prozent  - Coding.Tools'
    model['bodyTitle'] = 'Online-Konvertierungstool in Prozent berechnen'
    model['description'] = 'Mit diesem Online-Tool zum Konvertieren von Prozentsatz in Prozent können Sie einen Score in einen Prozentsatz umwandeln.'
    model['keywords'] = 'Bruchteil in Prozent, Bruchteil in Prozent'
    model['image'] = '/image/cartoon-fraction-to-percent.png'
    return render_template(template_dir + 'template_fraction_to_percent_de.html', model=model)


@Web_HexToDecimal_blueprint.route('/de/hex-to-rgb')
def hex_to_rgb():
    model = get_default_model()
    model['url'] = '/de/hex-to-rgb'
    model['enUrl'] = '/hex-to-rgb'
    model['headerTitle'] = 'Hex-Farbe in RGB-Farbe Online-Konvertierungstool  - Coding.Tools'
    model['bodyTitle'] = 'Online-Konvertierungstool für Hex-Farbe in RGB-Farbe'
    model['description'] = 'Mit diesem Online-Werkzeug zur Umwandlung der Farbe in RGB-Farbe in RGB können Sie eine Hex-Farbe in eine RGB-Farbe konvertieren und die von Ihnen gewählte Farbe in Echtzeit testen.'
    model['keywords'] = 'Hex zu RGB, Hex-Farbe zu RGB-Farbe'
    model['image'] = '/image/cartoon-hex-to-rgb.png'
    return render_template(template_dir + 'template_hex_to_rgb_de.html', model=model)


@Web_HexToDecimal_blueprint.route('/de/rgb-to-hex')
def rgb_to_hex():
    model = get_default_model()
    model['url'] = '/de/rgb-to-hex'
    model['enUrl'] = '/rgb-to-hex'
    model['headerTitle'] = 'Online-Konvertierungswerkzeug für RGB-Farbe in Hex-Farbe  - Coding.Tools'
    model['bodyTitle'] = 'Online-Konvertierungstool für RGB-Farbe in Hex-Farbe'
    model['description'] = 'Mit diesem Online-Konvertierungswerkzeug für die RGB-Farbe in Hex-Farbe können Sie eine RGB-Farbe in eine Hex-Farbe konvertieren und die ausgewählte Farbe in Echtzeit testen.'
    model['keywords'] = 'RGB zu Hex, RGB-Farbe zu Hex-Farbe'
    model['image'] = '/image/cartoon-rgb-to-hex.png'
    return render_template(template_dir + 'template_rgb_to_hex_de.html', model=model)


@Web_HexToDecimal_blueprint.route('/de/hex-to-rgba')
def hex_to_rgba():
    model = get_default_model()
    model['url'] = '/de/hex-to-rgba'
    model['enUrl'] = '/hex-to-rgba'
    model['headerTitle'] = 'Hex-Farbe zu RGBA-Online-Konvertierungswerkzeug  - Coding.Tools'
    model['bodyTitle'] = 'Hex-Farbe in RGBA-Online-Konvertierungstool'
    model['description'] = 'Mit diesem Online-Werkzeug zur Konvertierung von Hex-Farben in RGBA-Farben können Sie eine Hex-Farbe in eine RGBA-Farbe (einschließlich Transparenz-Deckkraft) konvertieren und die von Ihnen gewählte Farbe in Echtzeit testen.'
    model['keywords'] = 'Hex zu RGBA, Hex-Farbe zu RGBA-Farbe'
    model['image'] = '/image/cartoon-hex-to-rgba.png'
    return render_template(template_dir + 'template_hex_to_rgba_de.html', model=model)


@Web_HexToDecimal_blueprint.route('/de/rgba-to-hex')
def rgba_to_hex():
    model = get_default_model()
    model['url'] = '/de/rgba-to-hex'
    model['enUrl'] = '/rgba-to-hex'
    model['headerTitle'] = 'Online-Konvertierungswerkzeug für RGB-Farbe in Hex-Farbe  - Coding.Tools'
    model['bodyTitle'] = 'Online-Konvertierungstool für RGB-Farbe in Hex-Farbe'
    model['description'] = 'Mit diesem Online-Konvertierungswerkzeug für die RGB-Farbe in Hex-Farbe können Sie eine RGBA-Farbe (einschließlich Transparenz-Deckkraft) in Hex-Farbe konvertieren und die ausgewählte Farbe in Echtzeit testen.'
    model['keywords'] = 'RGBA zu Hex, RGBA-Farbe zu Hex-Farbe'
    model['image'] = '/image/cartoon-rgba-to-hex.png'
    return render_template(template_dir + 'template_rgba_to_hex_de.html', model=model)


@Web_HexToDecimal_blueprint.route('/de/roman-numerals-chart')
def roman_numerals_chart():
    model = get_default_model()
    model['url'] = '/de/roman-numerals-chart'
    model['enUrl'] = '/roman-numerals-chart'
    model['headerTitle'] = 'Römische Zahlentabelle 1-1000  - Coding.Tools'
    model['bodyTitle'] = 'Römische Zahlenvergleichstabelle 1-1000'
    model['description'] = 'Eine vollständige römische Zahlenvergleichstabelle von 1 bis 1000.'
    model['keywords'] = 'Diagramm der römischen Ziffern, römische Ziffern'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_roman_numerals_chart_de.html', model=model)


@Web_HexToDecimal_blueprint.route('/de/roman-numerals-to-numbers')
def roman_numerals_to_numbers():
    model = get_default_model()
    model['url'] = '/de/roman-numerals-to-numbers'
    model['enUrl'] = '/roman-numerals-to-numbers'
    model['headerTitle'] = 'Online-Konvertierungswerkzeug für römische Ziffern in arabische Ziffern  - Coding.Tools'
    model['bodyTitle'] = 'Digitales Online-Konvertierungswerkzeug für römische Ziffern in Arabisch'
    model['description'] = 'Dieses Online-Werkzeug zur Umwandlung der römischen Zahl in eine arabische Zahl hilft Ihnen bei der Umwandlung einer römischen Zahl in eine arabische Zahl. Geben Sie die römische Zahl ein und die arabische Zahl wird im Ergebnisfeld angezeigt.'
    model['keywords'] = 'Römische Ziffern werden zu arabischen Ziffern'
    model['image'] = '/image/cartoon-roman-numerals-to-numbers.png'
    return render_template(template_dir + 'template_roman_numerals_to_numbers_de.html', model=model)


@Web_HexToDecimal_blueprint.route('/de/numbers-to-roman-numerals')
def numbers_to_roman_numerals():
    model = get_default_model()
    model['url'] = '/de/numbers-to-roman-numerals'
    model['enUrl'] = '/numbers-to-roman-numerals'
    model['headerTitle'] = 'Digitales Online-Konvertierungswerkzeug für Arabisch digital in römisch  - Coding.Tools'
    model['bodyTitle'] = 'Digitales Online-Konvertierungswerkzeug für Arabisch Digital in Roman'
    model['description'] = 'Dieses Online-Konvertierungswerkzeug für die arabische Zahl in eine römische Zahl hilft Ihnen bei der Umwandlung einer arabischen Zahl in eine römische Zahl. Geben Sie die arabische Zahl ein, und die römische Zahl wird im Ergebnisfeld angezeigt.'
    model['keywords'] = 'Arabische Ziffern werden zu römischen Ziffern'
    model['image'] = '/image/cartoon-numbers-to-roman-numerals.png'
    return render_template(template_dir + 'template_numbers_to_roman_numerals_de.html', model=model)
