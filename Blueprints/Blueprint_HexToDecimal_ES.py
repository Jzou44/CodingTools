from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_HexToDecimal_blueprint = Blueprint('Web_HexToDecimal_blueprint_ES', __name__)
template_dir = 'HexToDecimal/es/'

def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'es'
    return model

@Web_HexToDecimal_blueprint.route('/es/hex-to-decimal')
def hex_to_decimal():
    model = get_default_model()
    model['url'] = '/es/hex-to-decimal'
    model['enUrl'] = '/hex-to-decimal'
    model['headerTitle'] = 'Herramienta de conversión en línea de hexadecimal a decimal - Codificación.Herramientas'
    model['bodyTitle'] = 'Herramienta de conversión en línea hexadecimal a decimal'
    model['description'] = 'Esta herramienta en línea de conversión de hexadecimal a decimal te ayuda a convertir un número hexadecimal en un número decimal.'
    model['keywords'] = 'De hexadecimal a decimal, de hexadecimal a decimal'
    model['image'] = '/image/cartoon-hex-to-decimal.png'
    return render_template(template_dir + 'template_hex_to_decimal_es.html', model=model)


@Web_HexToDecimal_blueprint.route('/es/decimal-to-hex')
def decimal_to_hex():
    model = get_default_model()
    model['url'] = '/es/decimal-to-hex'
    model['enUrl'] = '/decimal-to-hex'
    model['headerTitle'] = 'Herramienta de conversión en línea de decimal a hexadecimal  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta de conversión en línea de decimal a hexadecimal'
    model['description'] = 'Esta herramienta de conversión de decimal a hexadecimal en línea te ayuda a convertir un número decimal en un número hexadecimal.'
    model['keywords'] = 'Decimal a hexadecimal, decimal a hexadecimal'
    model['image'] = '/image/cartoon-decimal-to-hex.png'
    return render_template(template_dir + 'template_decimal_to_hex_es.html', model=model)


@Web_HexToDecimal_blueprint.route('/es/octal-to-decimal')
def octal_to_decimal():
    model = get_default_model()
    model['url'] = '/es/octal-to-decimal'
    model['enUrl'] = '/octal-to-decimal'
    model['headerTitle'] = 'Herramienta de conversión en línea de octal a decimal  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta de conversión de octal a decimal en línea'
    model['description'] = 'Esta herramienta de conversión en línea de octal a decimal le ayuda a convertir un número octal en un número decimal.'
    model['keywords'] = 'Octal a decimal, octal a decimal'
    model['image'] = '/image/octal_to_decimal.png'
    return render_template(template_dir + 'template_octal_to_decimal_es.html', model=model)


@Web_HexToDecimal_blueprint.route('/es/decimal-to-octal')
def decimal_to_octal():
    model = get_default_model()
    model['url'] = '/es/decimal-to-octal'
    model['enUrl'] = '/decimal-to-octal'
    model['headerTitle'] = 'Herramienta de conversión en línea de decimal a octal - Codificación.Herramientas'
    model['bodyTitle'] = 'Herramienta de conversión en línea de decimal a octal'
    model['description'] = 'Esta herramienta de conversión de decimal a octal en línea te ayuda a convertir un número decimal en un número octal.'
    model['keywords'] = 'Decimal a octal, decimal a octal'
    model['image'] = '/image/cartoon-decimal-to-octal.png'
    return render_template(template_dir + 'template_decimal_to_octal_es.html', model=model)


@Web_HexToDecimal_blueprint.route('/es/binary-to-decimal')
def binary_to_decimal():
    model = get_default_model()
    model['url'] = '/es/binary-to-decimal'
    model['enUrl'] = '/binary-to-decimal'
    model['headerTitle'] = 'Herramienta de conversión en línea de binario a decimal  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta de conversión en línea de binario a decimal'
    model['description'] = 'Esta herramienta de conversión de binario a decimal en línea le ayuda a convertir un número octal en un número decimal.'
    model['keywords'] = 'Binario a decimal, binario a decimal'
    model['image'] = '/image/cartoon-decimal-to-binary.png'
    return render_template(template_dir + 'template_binary_to_decimal_es.html', model=model)


@Web_HexToDecimal_blueprint.route('/es/decimal-to-binary')
def decimal_to_binary():
    model = get_default_model()
    model['url'] = '/es/decimal-to-binary'
    model['enUrl'] = '/decimal-to-binary'
    model['headerTitle'] = 'Herramienta de conversión de decimal a binario en línea  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta de conversión de decimal a binario en línea'
    model['description'] = 'Esta herramienta de conversión de decimal a binario en línea te ayuda a convertir un número decimal en un número binario.'
    model['keywords'] = 'De decimal a binario, de decimal a binario'
    model['image'] = '/image/cartoon-decimal-to-binary.png'
    return render_template(template_dir + 'template_decimal_to_binary_es.html', model=model)


@Web_HexToDecimal_blueprint.route('/es/ascii-table')
def ascii_table():
    model = get_default_model()
    model['url'] = '/es/ascii-table'
    model['enUrl'] = '/ascii-table'
    model['headerTitle'] = 'Tabla de búsqueda ASCII - Codificación.Herramientas'
    model['bodyTitle'] = 'Tabla de búsqueda ASCII'
    model['description'] = 'Tabla de búsqueda ASCII completa (256 bits), que incluye caracteres de control ASCII, símbolos ASCII y caracteres extendidos ASCII.'
    model['keywords'] = 'Tabla ASCII, tabla de extensión ASCII'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_ascii_table_es.html', model=model)


@Web_HexToDecimal_blueprint.route('/es/hex-to-ascii')
def hex_to_ascii():
    model = get_default_model()
    model['url'] = '/es/hex-to-ascii'
    model['enUrl'] = '/hex-to-ascii'
    model['headerTitle'] = 'Herramienta de conversión en línea de cadenas hexadecimales a ASCII  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta de conversión en línea hexadecimal a cadena ASCII'
    model['description'] = 'Esta herramienta de conversión de cadena hexadecimal a ASCII en línea le ayuda a convertir una matriz hexadecimal en una cadena ASCII.'
    model['keywords'] = 'Hexado a ASCII, hexadecimal a ASCII'
    model['image'] = '/image/cartoon-hex-to-ascii.png'
    return render_template(template_dir + 'template_hex_to_ascii_es.html', model=model)


@Web_HexToDecimal_blueprint.route('/es/ascii-to-hex')
def ascii_to_hex():
    model = get_default_model()
    model['url'] = '/es/ascii-to-hex'
    model['enUrl'] = '/ascii-to-hex'
    model['headerTitle'] = 'Herramienta de conversión en línea ASCII a hexadecimal en línea  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta de conversión ASCII de cadena a hexadecimal en línea'
    model['description'] = 'Esta herramienta de conversión en línea ASCII de cadena a hexadecimal le ayuda a convertir una cadena ASCII en una matriz hexadecimal.'
    model['keywords'] = 'ASCII a Hex, ASCII a hexadecimal'
    model['image'] = '/image/cartoon-ascii-to-hex.png'
    return render_template(template_dir + 'template_ascii_to_hex_es.html', model=model)


@Web_HexToDecimal_blueprint.route('/es/fraction-to-decimal')
def fraction_to_decimal():
    model = get_default_model()
    model['url'] = '/es/fraction-to-decimal'
    model['enUrl'] = '/fraction-to-decimal'
    model['headerTitle'] = 'Herramienta de conversión de puntuación a decimal en línea  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta de conversión de puntuación a decimal en línea'
    model['description'] = 'Esta herramienta de conversión de puntuación en línea a decimal le ayuda a convertir una puntuación en decimal. El numerador de entrada y el denominador se muestran en el cuadro de resultados.'
    model['keywords'] = 'Fracción a decimal, fraccional a decimal'
    model['image'] = '/image/cartoon-fraction-to-decimal.png'
    return render_template(template_dir + 'template_fraction_to_decimal_es.html', model=model)


@Web_HexToDecimal_blueprint.route('/es/decimal-to-fraction')
def decimal_to_fraction():
    model = get_default_model()
    model['url'] = '/es/decimal-to-fraction'
    model['enUrl'] = '/decimal-to-fraction'
    model['headerTitle'] = 'Decimal para puntuar la herramienta de conversión en línea  - Coding.Tools'
    model['bodyTitle'] = 'Decimal para puntuar la herramienta de conversión en línea'
    model['description'] = 'Esta herramienta de conversión de decimal para calificar en línea le ayuda a convertir un decimal en una puntuación. Ingrese el decimal y la puntuación se mostrará en el cuadro de resultados.'
    model['keywords'] = 'Decimal a Fracción, fraccional a Fracción'
    model['image'] = '/image/cartoon-decimal-to-fraction.png'
    return render_template(template_dir + 'template_decimal_to_fraction_es.html', model=model)


@Web_HexToDecimal_blueprint.route('/es/percent-to-decimal')
def percent_to_decimal():
    model = get_default_model()
    model['url'] = '/es/percent-to-decimal'
    model['enUrl'] = '/percent-to-decimal'
    model['headerTitle'] = 'Herramienta de conversión en línea de porcentaje a decimal - Codificación.Herramientas'
    model['bodyTitle'] = 'Herramienta de conversión en línea de porcentaje a decimal'
    model['description'] = 'Esta herramienta de conversión de porcentaje a decimal en línea le ayuda a convertir un porcentaje a decimal. Ingrese un porcentaje y el decimal aparecerá en el cuadro de resultados.'
    model['keywords'] = 'Porcentaje a decimal, porcentaje a decimal'
    model['image'] = '/image/cartoon-percent-to-decimal.png'
    return render_template(template_dir + 'template_percent_to_decimal_es.html', model=model)


@Web_HexToDecimal_blueprint.route('/es/decimal-to-percent')
def decimal_to_percent():
    model = get_default_model()
    model['url'] = '/es/decimal-to-percent'
    model['enUrl'] = '/decimal-to-percent'
    model['headerTitle'] = 'Herramienta de conversión de decimal a porcentaje en línea - Codificación.Herramientas'
    model['bodyTitle'] = 'Herramienta de conversión de decimal a porcentaje en línea'
    model['description'] = 'Esta herramienta de conversión de decimal a porcentaje en línea lo ayuda a convertir un decimal a un porcentaje. Ingrese el decimal y el porcentaje se mostrará en el cuadro de resultados.'
    model['keywords'] = 'Decimal a porcentaje, fraccional a porcentaje'
    model['image'] = '/image/cartoon-decimal-to-percent.png'
    return render_template(template_dir + 'template_decimal_to_percent_es.html', model=model)


@Web_HexToDecimal_blueprint.route('/es/percent-to-fraction')
def percent_to_fraction():
    model = get_default_model()
    model['url'] = '/es/percent-to-fraction'
    model['enUrl'] = '/percent-to-fraction'
    model['headerTitle'] = 'Porcentaje para puntuar en línea Herramienta de conversión  - Coding.Tools'
    model['bodyTitle'] = 'Porcentaje para puntuar la herramienta de conversión en línea'
    model['description'] = 'Este porcentaje en línea para puntuar la herramienta de conversión le ayuda a convertir un porcentaje en una puntuación. Ingrese el porcentaje y la puntuación se mostrará en el cuadro de resultados.'
    model['keywords'] = 'Porcentaje a Fracción, Porcentaje a Fracción'
    model['image'] = '/image/cartoon-percent-to-fraction.png'
    return render_template(template_dir + 'template_percent_to_fraction_es.html', model=model)


@Web_HexToDecimal_blueprint.route('/es/fraction-to-percent')
def fraction_to_percent():
    model = get_default_model()
    model['url'] = '/es/fraction-to-percent'
    model['enUrl'] = '/fraction-to-percent'
    model['headerTitle'] = 'Herramienta de conversión de puntaje a porcentaje en línea  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta de conversión de puntaje a porcentaje en línea'
    model['description'] = 'Esta herramienta de conversión de puntaje en línea a porcentaje le ayuda a convertir un puntaje en porcentaje. Ingrese el numerador y el denominador y el porcentaje se mostrará en el cuadro de resultados.'
    model['keywords'] = 'Fracción a porcentaje, porcentaje fraccional'
    model['image'] = '/image/cartoon-fraction-to-percent.png'
    return render_template(template_dir + 'template_fraction_to_percent_es.html', model=model)


@Web_HexToDecimal_blueprint.route('/es/hex-to-rgb')
def hex_to_rgb():
    model = get_default_model()
    model['url'] = '/es/hex-to-rgb'
    model['enUrl'] = '/hex-to-rgb'
    model['headerTitle'] = 'Herramienta de conversión en línea de color hexadecimal a color RGB - Codificación.Herramientas'
    model['bodyTitle'] = 'Herramienta de conversión en línea de color hexadecimal a color RGB'
    model['description'] = 'Esta herramienta de conversión de color hexadecimal en línea a color RGB te ayuda a convertir un color hexadecimal a color RGB y probar el color elegido en tiempo real.'
    model['keywords'] = 'De hex. A RGB, de hex. A color RGB'
    model['image'] = '/image/cartoon-hex-to-rgb.png'
    return render_template(template_dir + 'template_hex_to_rgb_es.html', model=model)


@Web_HexToDecimal_blueprint.route('/es/rgb-to-hex')
def rgb_to_hex():
    model = get_default_model()
    model['url'] = '/es/rgb-to-hex'
    model['enUrl'] = '/rgb-to-hex'
    model['headerTitle'] = 'Herramienta de conversión en línea de color RGB a color hexadecimal - Codificación.Herramientas'
    model['bodyTitle'] = 'Herramienta de conversión de color RGB a color Hex en línea'
    model['description'] = 'Esta herramienta de conversión de color RGB en línea a color hexadecimal te ayuda a convertir un color RGB a color hexadecimal y prueba el color elegido en tiempo real.'
    model['keywords'] = 'RGB a Hex, color RGB a Hex'
    model['image'] = '/image/cartoon-rgb-to-hex.png'
    return render_template(template_dir + 'template_rgb_to_hex_es.html', model=model)


@Web_HexToDecimal_blueprint.route('/es/hex-to-rgba')
def hex_to_rgba():
    model = get_default_model()
    model['url'] = '/es/hex-to-rgba'
    model['enUrl'] = '/hex-to-rgba'
    model['headerTitle'] = 'Herramienta de conversión en línea de color hexadecimal a color RGBA - Codificación.Herramientas'
    model['bodyTitle'] = 'Herramienta de conversión de color hexadecimal a color RGBA en línea'
    model['description'] = 'Esta herramienta de conversión de color hexadecimal en línea a color RGBA lo ayuda a convertir un color hexadecimal a color RGBA (incluida la opacidad de transparencia) y probar el color elegido en tiempo real.'
    model['keywords'] = 'Hex. A RGBA, color hex. A RGBA.'
    model['image'] = '/image/cartoon-hex-to-rgba.png'
    return render_template(template_dir + 'template_hex_to_rgba_es.html', model=model)


@Web_HexToDecimal_blueprint.route('/es/rgba-to-hex')
def rgba_to_hex():
    model = get_default_model()
    model['url'] = '/es/rgba-to-hex'
    model['enUrl'] = '/rgba-to-hex'
    model['headerTitle'] = 'Herramienta de conversión en línea de color RGBA a color hexadecimal - Codificación. Herramientas'
    model['bodyTitle'] = 'Herramienta de conversión de color RGBA a color hexadecimal en línea'
    model['description'] = 'Esta herramienta de conversión de color RGBA en línea a color hexadecimal le ayuda a convertir un color RGBA (incluida la opacidad de transparencia) en color hexadecimal y probar el color elegido en tiempo real.'
    model['keywords'] = 'RGBA a Hex, color RGBA a Hex color'
    model['image'] = '/image/cartoon-rgba-to-hex.png'
    return render_template(template_dir + 'template_rgba_to_hex_es.html', model=model)


@Web_HexToDecimal_blueprint.route('/es/roman-numerals-chart')
def roman_numerals_chart():
    model = get_default_model()
    model['url'] = '/es/roman-numerals-chart'
    model['enUrl'] = '/roman-numerals-chart'
    model['headerTitle'] = 'Tabla de números romanos 1-1000 - Codificación.Herramientas'
    model['bodyTitle'] = 'Tabla de comparación de números romanos 1-1000'
    model['description'] = 'Una tabla de comparación de números romanos completa del 1 al 1000.'
    model['keywords'] = 'Carta de números romanos, números romanos'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_roman_numerals_chart_es.html', model=model)


@Web_HexToDecimal_blueprint.route('/es/roman-numerals-to-numbers')
def roman_numerals_to_numbers():
    model = get_default_model()
    model['url'] = '/es/roman-numerals-to-numbers'
    model['enUrl'] = '/roman-numerals-to-numbers'
    model['headerTitle'] = 'Herramienta de conversión de números romanos a números arábigos en línea  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta de conversión de números romanos a árabe digital en línea'
    model['description'] = 'Esta herramienta de conversión de números romanos a números arábigos en línea le ayuda a convertir un número romano a números arábigos. Ingrese el número romano y el número árabe se mostrará en el cuadro de resultados.'
    model['keywords'] = 'Los números romanos se convierten en números arábigos.'
    model['image'] = '/image/cartoon-roman-numerals-to-numbers.png'
    return render_template(template_dir + 'template_roman_numerals_to_numbers_es.html', model=model)


@Web_HexToDecimal_blueprint.route('/es/numbers-to-roman-numerals')
def numbers_to_roman_numerals():
    model = get_default_model()
    model['url'] = '/es/numbers-to-roman-numerals'
    model['enUrl'] = '/numbers-to-roman-numerals'
    model['headerTitle'] = 'Herramienta de conversión en línea digital digital árabe a romana  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta de conversión en línea digital árabe a digital romana'
    model['description'] = 'Esta herramienta en línea para la conversión de números arábigos a números romanos lo ayuda a convertir un número árabe a números romanos. Ingrese el número árabe y el número romano se mostrará en el cuadro de resultados.'
    model['keywords'] = 'Los números arábigos se convierten en números romanos.'
    model['image'] = '/image/cartoon-numbers-to-roman-numerals.png'
    return render_template(template_dir + 'template_numbers_to_roman_numerals_es.html', model=model)
