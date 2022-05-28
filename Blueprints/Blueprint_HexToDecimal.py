from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_HexToDecimal_blueprint = Blueprint('Web_HexToDecimal_blueprint', __name__)
template_dir = 'HexToDecimal/en/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'en'
    return model


@Web_HexToDecimal_blueprint.route('/hex-to-decimal')
def hex_to_decimal():
    model = get_default_model()
    model['url'] = '/hex-to-decimal'
    model['enUrl'] = '/hex-to-decimal'
    model['headerTitle'] = 'Hex to Decimal Converter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Hex to Decimal Converter Online Tool'
    model['description'] = 'This online hex to decimal converter tool helps you to convert one input hex number (base 16) into a decimal number (base 10).'
    model['keywords'] = 'Hex to Decimal, Hex Converter'
    model['image'] = '/image/cartoon-hex-to-decimal.png'
    return render_template(template_dir + 'template_hex_to_decimal.html', model=model)


@Web_HexToDecimal_blueprint.route('/decimal-to-hex')
def decimal_to_hex():
    model = get_default_model()
    model['url'] = '/decimal-to-hex'
    model['enUrl'] = '/decimal-to-hex'
    model['headerTitle'] = 'Decimal to Hex Converter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Decimal to Hex Converter Online Tool'
    model['description'] = 'This online decimal to hex converter tool helps you to convert one input decimal number (base 10) into a hex number (base 16).'
    model['keywords'] = 'Decimal to Hex, Hex Converter'
    model['image'] = '/image/cartoon-decimal-to-hex.png'
    return render_template(template_dir + 'template_decimal_to_hex.html', model=model)


@Web_HexToDecimal_blueprint.route('/octal-to-decimal')
def octal_to_decimal():
    model = get_default_model()
    model['url'] = '/octal-to-decimal'
    model['enUrl'] = '/octal-to-decimal'
    model['headerTitle'] = 'Octal to Decimal Converter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Octal to Decimal Converter Online Tool'
    model['description'] = 'This online hex to decimal converter tool helps you to convert one input hex number (base 16) into a decimal number (base 10).'
    model['keywords'] = 'Octal to Decimal, Octal Converter'
    model['image'] = '/image/cartoon-octal-to-decimal.png'
    return render_template(template_dir + 'template_octal_to_decimal.html', model=model)


@Web_HexToDecimal_blueprint.route('/decimal-to-octal')
def decimal_to_octal():
    model = get_default_model()
    model['url'] = '/decimal-to-octal'
    model['enUrl'] = '/decimal-to-octal'
    model['headerTitle'] = 'Decimal to Octal Converter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Decimal to Octal Converter Online Tool'
    model['description'] = 'This online decimal to octal converter tool helps you to convert one input decimal number (base 10) into a octal number (base 8).'
    model['keywords'] = 'Decimal to Octal, Octal Converter'
    model['image'] = '/image/cartoon-decimal-to-octal.png'
    return render_template(template_dir + 'template_decimal_to_octal.html', model=model)


@Web_HexToDecimal_blueprint.route('/binary-to-decimal')
def binary_to_decimal():
    model = get_default_model()
    model['url'] = '/binary-to-decimal'
    model['enUrl'] = '/binary-to-decimal'
    model['headerTitle'] = 'Binary to Decimal Converter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Binary to Decimal Converter Online Tool'
    model['description'] = 'This online binary to decimal converter tool helps you to convert one input binary number (base 2) into a decimal number (base 10).'
    model['keywords'] = 'Binary to Decimal, Binary Converter'
    model['image'] = '/image/cartoon-binary-to-decimal.png'
    return render_template(template_dir + 'template_binary_to_decimal.html', model=model)


@Web_HexToDecimal_blueprint.route('/decimal-to-binary')
def decimal_to_binary():
    model = get_default_model()
    model['url'] = '/decimal-to-binary'
    model['enUrl'] = '/decimal-to-binary'
    model['headerTitle'] = 'Decimal to Binary Converter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Decimal to Binary Converter Online Tool'
    model['description'] = 'This online decimal to binary converter tool helps you to convert one input decimal number (base 10) into a binary number (base 2).'
    model['keywords'] = 'Decimal to Binary, Binary Converter'
    model['image'] = '/image/cartoon-decimal-to-binary.png'
    return render_template(template_dir + 'template_decimal_to_binary.html', model=model)


@Web_HexToDecimal_blueprint.route('/binary-to-hex')
def binary_to_hex():
    model = get_default_model()
    model['url'] = '/binary-to-hex'
    model['enUrl'] = '/binary-to-hex'
    model['headerTitle'] = 'Binary to Hex Converter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Binary to Hex Converter Online Tool'
    model['description'] = 'This online binary to hex converter tool helps you to convert one input binary number (base 2) into a hex number (base 16).'
    model['keywords'] = 'Binary to Hex'
    model['image'] = '/image/20190308/cartoon_binary_to_hex.png'
    return render_template(template_dir + 'template_binary_to_hex.html', model=model)


@Web_HexToDecimal_blueprint.route('/hex-to-binary')
def hex_to_binary():
    model = get_default_model()
    model['url'] = '/hex-to-binary'
    model['enUrl'] = '/hex-to-binary'
    model['headerTitle'] = 'Hex to Binary Converter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Hex to Binary Converter Online Tool'
    model['description'] = 'This online hex to binary converter tool helps you to convert one input hex number (base 16) into a binary number (base 2).'
    model['keywords'] = 'Hex to Binary'
    model['image'] = '/image/20190308/cartoon_hex_to_binary.png'
    return render_template(template_dir + 'template_hex_to_binary.html', model=model)


@Web_HexToDecimal_blueprint.route('/ascii-table')
def ascii_table():
    model = get_default_model()
    model['url'] = '/ascii-table'
    model['enUrl'] = '/ascii-table'
    model['headerTitle'] = 'Standard and Extended ASCII Online Table  - Coding.Tools'
    model['bodyTitle'] = 'Standard and Extended ASCII Online Table'
    model['description'] = 'The complete ASCII Table (256 digits), include ASCII control characters, ASCII symbol & signs characters and ASCII Extended characters.'
    model['keywords'] = 'ASCII Table, Extended ASCII'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_ascii_table.html', model=model)


@Web_HexToDecimal_blueprint.route('/hex-to-ascii')
def hex_to_ascii():
    model = get_default_model()
    model['url'] = '/hex-to-ascii'
    model['enUrl'] = '/hex-to-ascii'
    model['headerTitle'] = 'Hex to ASCII String Converter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Hex to ASCII String Converter Online Tool'
    model['description'] = 'This online Hex to ASCII string converter tool helps you to convert one input Hex string (base 16) into a ASCII String.'
    model['keywords'] = 'Hex to ASCII, Hex to String, hex to text'
    model['image'] = '/image/cartoon-hex-to-ascii.png'
    return render_template(template_dir + 'template_hex_to_ascii.html', model=model)


@Web_HexToDecimal_blueprint.route('/ascii-to-hex')
def ascii_to_hex():
    model = get_default_model()
    model['url'] = '/ascii-to-hex'
    model['enUrl'] = '/ascii-to-hex'
    model['headerTitle'] = 'ASCII to Hex String Converter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'ASCII to Hex String Converter Online Tool'
    model['description'] = 'This online ASCII to Hex string converter tool helps you to convert one input ASCII string into a Hex (base 16) String.'
    model['keywords'] = 'ASCII to Hex, String to Hex, text to hex'
    model['image'] = '/image/cartoon-ascii-to-hex.png'
    return render_template(template_dir + 'template_ascii_to_hex.html', model=model)


@Web_HexToDecimal_blueprint.route('/binary-to-text')
def binary_to_text():
    model = get_default_model()
    model['url'] = '/binary-to-text'
    model['enUrl'] = '/binary-to-text'
    model['headerTitle'] = 'Binary to Text Converter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Binary to Text Converter Online Tool'
    model['description'] = 'This online Binary to Text converter tool helps you to convert one input Binary string (base 2) into a ASCII text String.'
    model['keywords'] = 'binary to ASCII, binary to String, binary to text'
    model['image'] = '/image/20190308/cartoon_binary_to_text.png'
    return render_template(template_dir + 'template_binary_to_text.html', model=model)


@Web_HexToDecimal_blueprint.route('/text-to-binary')
def text_to_binary():
    model = get_default_model()
    model['url'] = '/text-to-binary'
    model['enUrl'] = '/text-to-binary'
    model['headerTitle'] = 'Text to Binary Converter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Text to Binary Converter Online Tool'
    model['description'] = 'This online Text to Binary converter tool helps you to convert one input ASCII text string into a Binary (base 2) String.'
    model['keywords'] = 'ASCII to binary, String to binary, text to binary'
    model['image'] = '/image/20190308/cartoon_text_to_binary.png'
    return render_template(template_dir + 'template_text_to_binary.html', model=model)


@Web_HexToDecimal_blueprint.route('/fraction-to-decimal')
def fraction_to_decimal():
    model = get_default_model()
    model['url'] = '/fraction-to-decimal'
    model['enUrl'] = '/fraction-to-decimal'
    model['headerTitle'] = 'Fraction to Decimal Calculator Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Fraction to Decimal Calculator Online Tool'
    model['description'] = 'This online Fraction to Decimal Calculator helps you to convert one Fraction number into a decimal number. Put numerator and denominator into the textbox, the decimal result will show below.'
    model['keywords'] = 'Fraction to Decimal, Fraction Calculator'
    model['image'] = '/image/cartoon-fraction-to-decimal.png'
    return render_template(template_dir + 'template_fraction_to_decimal.html', model=model)


@Web_HexToDecimal_blueprint.route('/decimal-to-fraction')
def decimal_to_fraction():
    model = get_default_model()
    model['url'] = '/decimal-to-fraction'
    model['enUrl'] = '/decimal-to-fraction'
    model['headerTitle'] = 'Decimal to Fraction Calculator Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Decimal to Fraction Calculator Online Tool'
    model['description'] = 'This online Decimal to Fraction Calculator helps you to convert one decimal number into a fraction number. the numerator and denominator result will show in the textbox.'
    model['keywords'] = 'Decimal to Fraction, Fraction Calculator'
    model['image'] = '/image/cartoon-decimal-to-fraction.png'
    return render_template(template_dir + 'template_decimal_to_fraction.html', model=model)


@Web_HexToDecimal_blueprint.route('/percent-to-decimal')
def percent_to_decimal():
    model = get_default_model()
    model['url'] = '/percent-to-decimal'
    model['enUrl'] = '/percent-to-decimal'
    model['headerTitle'] = 'Percent to Decimal Calculator Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Percent to Decimal Calculator Online Tool'
    model['description'] = 'This online Percent to Decimal Calculator helps you to convert one percent number into a decimal number. Put percent into the first textbox, the decimal result will show in the second textbox.'
    model['keywords'] = 'Percent to Decimal, Percent Calculator'
    model['image'] = '/image/cartoon-percent-to-decimal.png'
    return render_template(template_dir + 'template_percent_to_decimal.html', model=model)


@Web_HexToDecimal_blueprint.route('/decimal-to-percent')
def decimal_to_percent():
    model = get_default_model()
    model['url'] = '/decimal-to-percent'
    model['enUrl'] = '/decimal-to-percent'
    model['headerTitle'] = 'Decimal to Percent Calculator Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Decimal to Percent Calculator Online Tool'
    model['description'] = 'This online Decimal to Percent Calculator helps you to convert one decimal number into a percent number. Put decimal into the first textbox, the percent result will show in the second textbox.'
    model['keywords'] = 'Decimal to Percent, Percent Calculator'
    model['image'] = '/image/cartoon-decimal-to-percent.png'
    return render_template(template_dir + 'template_decimal_to_percent.html', model=model)


@Web_HexToDecimal_blueprint.route('/percent-to-fraction')
def percent_to_fraction():
    model = get_default_model()
    model['url'] = '/percent-to-fraction'
    model['enUrl'] = '/percent-to-fraction'
    model['headerTitle'] = 'Percent to Fraction Calculator Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Percent to Fraction Calculator Online Tool'
    model['description'] = 'This online Percent to Fraction Calculator helps you to convert one percent number into a fraction number. the numerator and denominator result will show in the textbox.'
    model['keywords'] = 'Percent to Fraction, Percent Calculator'
    model['image'] = '/image/cartoon-percent-to-fraction.png'
    return render_template(template_dir + 'template_percent_to_fraction.html', model=model)


@Web_HexToDecimal_blueprint.route('/fraction-to-percent')
def fraction_to_percent():
    model = get_default_model()
    model['url'] = '/fraction-to-percent'
    model['enUrl'] = '/fraction-to-percent'
    model['headerTitle'] = 'Fraction to Percent Calculator Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Fraction to Percent Calculator Online Tool'
    model['description'] = 'This online Fraction to Percent Calculator helps you to convert one Fraction number into a percent number. Put numerator and denominator into the textbox, the percent result will show below.'
    model['keywords'] = 'Fraction to Percent, Fraction Calculator'
    model['image'] = '/image/cartoon-fraction-to-percent.png'
    return render_template(template_dir + 'template_fraction_to_percent.html', model=model)


@Web_HexToDecimal_blueprint.route('/hex-to-rgb')
def hex_to_rgb():
    model = get_default_model()
    model['url'] = '/hex-to-rgb'
    model['enUrl'] = '/hex-to-rgb'
    model['headerTitle'] = 'Hex to RGB Converter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Hex to RGB Converter Online Tool'
    model['description'] = 'This online Hex to RGB converter tool helps you to convert one Hex color (base 16) into a RGB color (base 10), and test the result color within the website.'
    model['keywords'] = 'Hex to RGB, RGB Converter'
    model['image'] = '/image/cartoon-hex-to-rgb.png'
    return render_template(template_dir + 'template_hex_to_rgb.html', model=model)


@Web_HexToDecimal_blueprint.route('/rgb-to-hex')
def rgb_to_hex():
    model = get_default_model()
    model['url'] = '/rgb-to-hex'
    model['enUrl'] = '/rgb-to-hex'
    model['headerTitle'] = 'RGB to Hex Converter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'RGB to Hex Converter Online Tool'
    model['description'] = 'This online RGB to Hex converter tool helps you to convert one RGB color (base 10) into a Hex color (base 16), and test the result color within the website.'
    model['keywords'] = 'RGB to Hex, RGB Converter'
    model['image'] = '/image/cartoon-rgb-to-hex.png'
    return render_template(template_dir + 'template_rgb_to_hex.html', model=model)


@Web_HexToDecimal_blueprint.route('/hex-to-rgba')
def hex_to_rgba():
    model = get_default_model()
    model['url'] = '/hex-to-rgba'
    model['enUrl'] = '/hex-to-rgba'
    model['headerTitle'] = 'Hex to RGBA Converter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Hex to RGBA Converter Online Tool'
    model['description'] = 'This online Hex to RGBA converter tool helps you to convert one Hex color (base 16) into a RGBA color (base 10, with Opacity), and test the result color within the website.'
    model['keywords'] = 'Hex to RGBA, RGBA Converter'
    model['image'] = '/image/cartoon-hex-to-rgba.png'
    return render_template(template_dir + 'template_hex_to_rgba.html', model=model)


@Web_HexToDecimal_blueprint.route('/rgba-to-hex')
def rgba_to_hex():
    model = get_default_model()
    model['url'] = '/rgba-to-hex'
    model['enUrl'] = '/rgba-to-hex'
    model['headerTitle'] = 'RGBA to Hex Converter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'RGBA to Hex Converter Online Tool'
    model['description'] = 'This online RGBA to Hex converter tool helps you to convert one RGBA color (base 10) into a Hex color (base 16), and test the result color within the website.'
    model['keywords'] = 'RGBA to Hex, RGBA Converter'
    model['image'] = '/image/cartoon-rgba-to-hex.png'
    return render_template(template_dir + 'template_rgba_to_hex.html', model=model)


@Web_HexToDecimal_blueprint.route('/roman-numerals-chart')
def roman_numerals_chart():
    model = get_default_model()
    model['url'] = '/roman-numerals-chart'
    model['enUrl'] = '/roman-numerals-chart'
    model['headerTitle'] = 'Roman Numerals Chart 1-1000 Online  - Coding.Tools'
    model['bodyTitle'] = 'Roman Numerals Chart 1-1000 Online'
    model['description'] = 'The complete Roman Numerals Chart from 1 to 1000, include every Roman Numeral and its corresponding number from 1 to 1000.'
    model['keywords'] = 'Roman Numerals Chart'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_roman_numerals_chart.html', model=model)


@Web_HexToDecimal_blueprint.route('/roman-numerals-to-numbers')
def roman_numerals_to_numbers():
    model = get_default_model()
    model['url'] = '/roman-numerals-to-numbers'
    model['enUrl'] = '/roman-numerals-to-numbers'
    model['headerTitle'] = 'Roman Numerals to Numbers Converter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Roman Numerals to Numbers Converter Online Tool'
    model['description'] = 'This online Roman Numerals to Numbers Converter helps you to convert one Roman Numeral into a number (base 10). Put Roman Numeral into the first textbox, the number result will show in the second textbox.'
    model['keywords'] = 'Roman Numerals to Numbers, Roman Numerals Converter'
    model['image'] = '/image/cartoon-roman-numerals-to-numbers.png'
    return render_template(template_dir + 'template_roman_numerals_to_numbers.html', model=model)


@Web_HexToDecimal_blueprint.route('/numbers-to-roman-numerals')
def numbers_to_roman_numerals():
    model = get_default_model()
    model['url'] = '/numbers-to-roman-numerals'
    model['enUrl'] = '/numbers-to-roman-numerals'
    model['headerTitle'] = 'Numbers to Roman Numerals Converter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Numbers to Roman Numerals Converter Online Tool'
    model['description'] = 'This online Roman Numerals to Numbers Converter helps you to convert one Roman Numeral into a number (base 10). Put Roman Numeral into the first textbox, the number result will show in the second textbox.'
    model['keywords'] = 'Numbers to Roman Numerals, Roman Numerals Converter'
    model['image'] = '/image/cartoon-numbers-to-roman-numerals.png'
    return render_template(template_dir + 'template_numbers_to_roman_numerals.html', model=model)
