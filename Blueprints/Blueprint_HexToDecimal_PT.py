from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_HexToDecimal_blueprint = Blueprint('Web_HexToDecimal_blueprint_PT', __name__)
template_dir = 'HexToDecimal/pt/'

def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'pt'
    return model

@Web_HexToDecimal_blueprint.route('/pt/hex-to-decimal')
def hex_to_decimal():
    model = get_default_model()
    model['url'] = '/pt/hex-to-decimal'
    model['enUrl'] = '/hex-to-decimal'
    model['headerTitle'] = 'Hexadecimal para Decimal Online Conversion Tool  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta de conversão hexadecimal para decimal online'
    model['description'] = 'Essa ferramenta online de conversão hexadecimal a decimal ajuda a converter um número hexadecimal em um número decimal.'
    model['keywords'] = 'Hex para decimal, hexadecimal para decimal'
    model['image'] = '/image/cartoon-hex-to-decimal.png'
    return render_template(template_dir + 'template_hex_to_decimal_pt.html', model=model)


@Web_HexToDecimal_blueprint.route('/pt/decimal-to-hex')
def decimal_to_hex():
    model = get_default_model()
    model['url'] = '/pt/decimal-to-hex'
    model['enUrl'] = '/decimal-to-hex'
    model['headerTitle'] = 'Decimal para ferramenta de conversão online hexadecimal  - Coding.Tools'
    model['bodyTitle'] = 'Decimal para ferramenta de conversão online hexadecimal'
    model['description'] = 'Essa ferramenta de conversão decimal para hexadecimal ajuda você a converter um número decimal em um número hexadecimal.'
    model['keywords'] = 'Decimal para Hex, decimal para hexadecimal'
    model['image'] = '/image/cartoon-decimal-to-hex.png'
    return render_template(template_dir + 'template_decimal_to_hex_pt.html', model=model)


@Web_HexToDecimal_blueprint.route('/pt/octal-to-decimal')
def octal_to_decimal():
    model = get_default_model()
    model['url'] = '/pt/octal-to-decimal'
    model['enUrl'] = '/octal-to-decimal'
    model['headerTitle'] = 'Octal para Decimal Online Conversion Tool  - Coding.Tools'
    model['bodyTitle'] = 'Octal para ferramenta de conversão decimal online'
    model['description'] = 'Essa ferramenta de conversão online para decimal ajuda a converter um número octal em um número decimal.'
    model['keywords'] = 'Octal para Decimal, octal para decimal'
    model['image'] = '/image/octal_to_decimal.png'
    return render_template(template_dir + 'template_octal_to_decimal_pt.html', model=model)


@Web_HexToDecimal_blueprint.route('/pt/decimal-to-octal')
def decimal_to_octal():
    model = get_default_model()
    model['url'] = '/pt/decimal-to-octal'
    model['enUrl'] = '/decimal-to-octal'
    model['headerTitle'] = 'Decimal para Octal Online Conversion Tool  - Coding.Tools'
    model['bodyTitle'] = 'Decimal para ferramenta de conversão on-line octal'
    model['description'] = 'Essa ferramenta online de conversão decimal para octal ajuda você a converter um número decimal em um número octal.'
    model['keywords'] = 'Decimal para Octal, decimal para octal'
    model['image'] = '/image/cartoon-decimal-to-octal.png'
    return render_template(template_dir + 'template_decimal_to_octal_pt.html', model=model)


@Web_HexToDecimal_blueprint.route('/pt/binary-to-decimal')
def binary_to_decimal():
    model = get_default_model()
    model['url'] = '/pt/binary-to-decimal'
    model['enUrl'] = '/binary-to-decimal'
    model['headerTitle'] = 'Ferramenta de conversão online binário para decimal  - Coding.Tools'
    model['bodyTitle'] = 'Binário para ferramenta de conversão online decimal'
    model['description'] = 'Essa ferramenta de conversão decimal para binário on-line ajuda a converter um número octal em um número decimal.'
    model['keywords'] = 'Binário para decimal, binário para decimal'
    model['image'] = '/image/cartoon-decimal-to-binary.png'
    return render_template(template_dir + 'template_binary_to_decimal_pt.html', model=model)


@Web_HexToDecimal_blueprint.route('/pt/decimal-to-binary')
def decimal_to_binary():
    model = get_default_model()
    model['url'] = '/pt/decimal-to-binary'
    model['enUrl'] = '/decimal-to-binary'
    model['headerTitle'] = 'Decimal para a ferramenta de conversão online binária  - Coding.Tools'
    model['bodyTitle'] = 'Decimal para ferramenta de conversão online binária'
    model['description'] = 'Essa ferramenta online de conversão decimal para binário ajuda você a converter um número decimal em um número binário.'
    model['keywords'] = 'Decimal para Binário, decimal para binário'
    model['image'] = '/image/cartoon-decimal-to-binary.png'
    return render_template(template_dir + 'template_decimal_to_binary_pt.html', model=model)


@Web_HexToDecimal_blueprint.route('/pt/ascii-table')
def ascii_table():
    model = get_default_model()
    model['url'] = '/pt/ascii-table'
    model['enUrl'] = '/ascii-table'
    model['headerTitle'] = 'Tabela de consulta ASCII  - Coding.Tools'
    model['bodyTitle'] = 'Tabela de consulta ASCII'
    model['description'] = 'Tabela de consulta ASCII completa (256 bits), incluindo caracteres de controle ASCII, símbolos ASCII e caracteres estendidos ASCII.'
    model['keywords'] = 'Tabela ASCII, tabela de extensão ASCII'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_ascii_table_pt.html', model=model)


@Web_HexToDecimal_blueprint.route('/pt/hex-to-ascii')
def hex_to_ascii():
    model = get_default_model()
    model['url'] = '/pt/hex-to-ascii'
    model['enUrl'] = '/hex-to-ascii'
    model['headerTitle'] = 'Hexadecimal para ferramenta de conversão online de string ASCII  - Coding.Tools'
    model['bodyTitle'] = 'Hexadecimal para ferramenta de conversão online de string ASCII'
    model['description'] = 'Esta ferramenta online hexadecimal para conversão de caracteres ASCII ajuda você a converter uma matriz hexadecimal em uma string ASCII.'
    model['keywords'] = 'Hex para ASCII, hex para ASCII'
    model['image'] = '/image/cartoon-hex-to-ascii.png'
    return render_template(template_dir + 'template_hex_to_ascii_pt.html', model=model)


@Web_HexToDecimal_blueprint.route('/pt/ascii-to-hex')
def ascii_to_hex():
    model = get_default_model()
    model['url'] = '/pt/ascii-to-hex'
    model['enUrl'] = '/ascii-to-hex'
    model['headerTitle'] = 'String ASCII para ferramenta de conversão on-line hexadecimal  - Coding.Tools'
    model['bodyTitle'] = 'String ASCII para ferramenta de conversão online hexadecimal'
    model['description'] = 'Esta ferramenta de conversão de string para hexadecimal ASCII on-line ajuda a converter uma string ASCII em uma matriz hexadecimal.'
    model['keywords'] = 'ASCII para Hex, ASCII para hexadecimal'
    model['image'] = '/image/cartoon-ascii-to-hex.png'
    return render_template(template_dir + 'template_ascii_to_hex_pt.html', model=model)


@Web_HexToDecimal_blueprint.route('/pt/fraction-to-decimal')
def fraction_to_decimal():
    model = get_default_model()
    model['url'] = '/pt/fraction-to-decimal'
    model['enUrl'] = '/fraction-to-decimal'
    model['headerTitle'] = 'Pontuação para ferramenta de conversão decimal online  - Coding.Tools'
    model['bodyTitle'] = 'Pontuação para a ferramenta de conversão decimal online'
    model['description'] = 'Essa pontuação online para a ferramenta de conversão decimal ajuda a converter uma pontuação em um decimal.O numerador de entrada e o denominador são exibidos na caixa de resultado.'
    model['keywords'] = 'Fração para decimal, fracionário para decimal'
    model['image'] = '/image/cartoon-fraction-to-decimal.png'
    return render_template(template_dir + 'template_fraction_to_decimal_pt.html', model=model)


@Web_HexToDecimal_blueprint.route('/pt/decimal-to-fraction')
def decimal_to_fraction():
    model = get_default_model()
    model['url'] = '/pt/decimal-to-fraction'
    model['enUrl'] = '/decimal-to-fraction'
    model['headerTitle'] = 'Decimal para pontuar a ferramenta de conversão online  - Coding.Tools'
    model['bodyTitle'] = 'Decimal para pontuar a ferramenta de conversão online'
    model['description'] = 'Essa ferramenta online de conversão decimal para pontuação ajuda você a converter um decimal em uma fração: insira o decimal e a pontuação será exibida na caixa de resultados.'
    model['keywords'] = 'Decimal para Fração, fracionária para Fração'
    model['image'] = '/image/cartoon-decimal-to-fraction.png'
    return render_template(template_dir + 'template_decimal_to_fraction_pt.html', model=model)


@Web_HexToDecimal_blueprint.route('/pt/percent-to-decimal')
def percent_to_decimal():
    model = get_default_model()
    model['url'] = '/pt/percent-to-decimal'
    model['enUrl'] = '/percent-to-decimal'
    model['headerTitle'] = 'Porcentagem para a ferramenta de conversão decimal online  - Coding.Tools'
    model['bodyTitle'] = 'Porcentagem para a ferramenta de conversão decimal online'
    model['description'] = 'Essa porcentagem online para a ferramenta de conversão decimal ajuda a converter uma porcentagem em um decimal Insira uma porcentagem e o decimal aparecerá na caixa de resultados.'
    model['keywords'] = 'Porcentagem para decimal, porcentagem para decimal'
    model['image'] = '/image/cartoon-percent-to-decimal.png'
    return render_template(template_dir + 'template_percent_to_decimal_pt.html', model=model)


@Web_HexToDecimal_blueprint.route('/pt/decimal-to-percent')
def decimal_to_percent():
    model = get_default_model()
    model['url'] = '/pt/decimal-to-percent'
    model['enUrl'] = '/decimal-to-percent'
    model['headerTitle'] = 'Decimal para porcentagem ferramenta de conversão on-line  - Coding.Tools'
    model['bodyTitle'] = 'Decimal para porcentagem ferramenta de conversão online'
    model['description'] = 'Essa ferramenta online de conversão decimal a porcentagem ajuda você a converter um decimal em uma porcentagem Insira o decimal e a porcentagem será exibida na caixa de resultados.'
    model['keywords'] = 'Decimal em Porcentagem, fracionária para porcentagem'
    model['image'] = '/image/cartoon-decimal-to-percent.png'
    return render_template(template_dir + 'template_decimal_to_percent_pt.html', model=model)


@Web_HexToDecimal_blueprint.route('/pt/percent-to-fraction')
def percent_to_fraction():
    model = get_default_model()
    model['url'] = '/pt/percent-to-fraction'
    model['enUrl'] = '/percent-to-fraction'
    model['headerTitle'] = 'Porcentagem para marcar ferramenta de conversão on-line  - Coding.Tools'
    model['bodyTitle'] = 'Porcentagem para pontuar a ferramenta de conversão online'
    model['description'] = 'Essa ferramenta de porcentagem de porcentagem para conversão de pontuação ajuda você a converter uma porcentagem em uma pontuação. Insira a porcentagem e a pontuação será exibida na caixa de resultados.'
    model['keywords'] = 'Porcentagem para Fração, Porcentagem para Fração'
    model['image'] = '/image/cartoon-percent-to-fraction.png'
    return render_template(template_dir + 'template_percent_to_fraction_pt.html', model=model)


@Web_HexToDecimal_blueprint.route('/pt/fraction-to-percent')
def fraction_to_percent():
    model = get_default_model()
    model['url'] = '/pt/fraction-to-percent'
    model['enUrl'] = '/fraction-to-percent'
    model['headerTitle'] = 'Pontuação para ferramenta de conversão on-line de porcentagem  - Coding.Tools'
    model['bodyTitle'] = 'Pontuação para ferramenta de conversão online'
    model['description'] = 'Essa pontuação online para a ferramenta de conversão de porcentagem ajuda você a converter uma pontuação em uma porcentagem. Insira o numerador e o denominador e a porcentagem será exibida na caixa de resultados.'
    model['keywords'] = 'Fração para porcentagem, porcentagem fracionária'
    model['image'] = '/image/cartoon-fraction-to-percent.png'
    return render_template(template_dir + 'template_fraction_to_percent_pt.html', model=model)


@Web_HexToDecimal_blueprint.route('/pt/hex-to-rgb')
def hex_to_rgb():
    model = get_default_model()
    model['url'] = '/pt/hex-to-rgb'
    model['enUrl'] = '/hex-to-rgb'
    model['headerTitle'] = 'Ferramenta de conversão on-line Hex Color to RGB Color  - Coding.Tools'
    model['bodyTitle'] = 'Hex cor para a ferramenta de conversão online de cores RGB'
    model['description'] = 'Esta ferramenta online de conversão de cores Hex para cores RGB ajuda-o a converter uma cor Hex na cor RGB e a testar a sua cor escolhida em tempo real.'
    model['keywords'] = 'Hex para RGB, cor Hex para cor RGB'
    model['image'] = '/image/cartoon-hex-to-rgb.png'
    return render_template(template_dir + 'template_hex_to_rgb_pt.html', model=model)


@Web_HexToDecimal_blueprint.route('/pt/rgb-to-hex')
def rgb_to_hex():
    model = get_default_model()
    model['url'] = '/pt/rgb-to-hex'
    model['enUrl'] = '/rgb-to-hex'
    model['headerTitle'] = 'Ferramenta de Conversão On-line de Cor RGB a Hex Cor  - Coding.Tools'
    model['bodyTitle'] = 'Cor RGB para Hex cor ferramenta de conversão on-line'
    model['description'] = 'Esta ferramenta de conversão de cores em cores Hex para RGB ajuda a converter uma cor RGB em uma cor Hex e testar a cor escolhida em tempo real.'
    model['keywords'] = 'RGB a Hex, cor RGB a cor hexadecimal'
    model['image'] = '/image/cartoon-rgb-to-hex.png'
    return render_template(template_dir + 'template_rgb_to_hex_pt.html', model=model)


@Web_HexToDecimal_blueprint.route('/pt/hex-to-rgba')
def hex_to_rgba():
    model = get_default_model()
    model['url'] = '/pt/hex-to-rgba'
    model['enUrl'] = '/hex-to-rgba'
    model['headerTitle'] = 'Cor Hex para RGBA Color Online Ferramenta de conversão  - Coding.Tools'
    model['bodyTitle'] = 'Hex cor para a ferramenta de conversão online de cores RGBA'
    model['description'] = 'Esta ferramenta online de conversão de cores Hex para RGBA ajuda você a converter uma cor Hex em uma cor RGBA (incluindo Opacidade de transparência) e testar sua cor escolhida em tempo real.'
    model['keywords'] = 'Hex para RGBA, cor Hex para cor RGBA'
    model['image'] = '/image/cartoon-hex-to-rgba.png'
    return render_template(template_dir + 'template_hex_to_rgba_pt.html', model=model)


@Web_HexToDecimal_blueprint.route('/pt/rgba-to-hex')
def rgba_to_hex():
    model = get_default_model()
    model['url'] = '/pt/rgba-to-hex'
    model['enUrl'] = '/rgba-to-hex'
    model['headerTitle'] = 'Cor RGBA para Hex cor ferramenta de conversão on-line  - Coding.Tools'
    model['bodyTitle'] = 'Cor RGBA para Hex cor ferramenta de conversão online'
    model['description'] = 'Esta ferramenta online de conversão de cores RGBA a cores Hex ajuda-o a converter uma cor RGBA (incluindo opacidade de transparência) em cores Hex e testa a sua cor escolhida em tempo real.'
    model['keywords'] = 'RGBA para Hex, cor RGBA para cor Hex'
    model['image'] = '/image/cartoon-rgba-to-hex.png'
    return render_template(template_dir + 'template_rgba_to_hex_pt.html', model=model)


@Web_HexToDecimal_blueprint.route('/pt/roman-numerals-chart')
def roman_numerals_chart():
    model = get_default_model()
    model['url'] = '/pt/roman-numerals-chart'
    model['enUrl'] = '/roman-numerals-chart'
    model['headerTitle'] = 'Tabela numeral romano 1-1000  - Coding.Tools'
    model['bodyTitle'] = 'Tabela de comparação numeral romano 1-1000'
    model['description'] = 'Uma tabela completa de comparação de numeral romano de 1 a 1000.'
    model['keywords'] = 'Carta dos numerais romanos, algarismos romanos'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_roman_numerals_chart_pt.html', model=model)


@Web_HexToDecimal_blueprint.route('/pt/roman-numerals-to-numbers')
def roman_numerals_to_numbers():
    model = get_default_model()
    model['url'] = '/pt/roman-numerals-to-numbers'
    model['enUrl'] = '/roman-numerals-to-numbers'
    model['headerTitle'] = 'Numerais romanos para numerais arábicos ferramenta de conversão on-line  - Coding.Tools'
    model['bodyTitle'] = 'Numeral romano para ferramenta de conversão online árabe digital'
    model['description'] = 'Este numeral romano on-line para a ferramenta de conversão de algarismos arábicos ajuda-o a converter um numeral romano num algarismo arábico, introduza o numeral romano e o algarismo arábico será apresentado na caixa de resultados.'
    model['keywords'] = 'Algarismos romanos se transformam em algarismos arábicos'
    model['image'] = '/image/cartoon-roman-numerals-to-numbers.png'
    return render_template(template_dir + 'template_roman_numerals_to_numbers_pt.html', model=model)


@Web_HexToDecimal_blueprint.route('/pt/numbers-to-roman-numerals')
def numbers_to_roman_numerals():
    model = get_default_model()
    model['url'] = '/pt/numbers-to-roman-numerals'
    model['enUrl'] = '/numbers-to-roman-numerals'
    model['headerTitle'] = 'Ferramenta de conversão online digital árabe para Roman Digital  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta de conversão online digital árabe para Roman Digital'
    model['description'] = 'Este numeral arábico on-line para a ferramenta de conversão de numeral romano ajuda você a converter um numeral arábico para um numeral romano.Inicie o número arábico e o numeral romano será exibido na caixa de resultado.'
    model['keywords'] = 'Algarismos arábicos se voltam para algarismos romanos'
    model['image'] = '/image/cartoon-numbers-to-roman-numerals.png'
    return render_template(template_dir + 'template_numbers_to_roman_numerals_pt.html', model=model)
