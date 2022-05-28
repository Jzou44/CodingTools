from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_HexToDecimal_blueprint = Blueprint('Web_HexToDecimal_blueprint_JP', __name__)
template_dir = 'HexToDecimal/jp/'

def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'ja'
    return model

@Web_HexToDecimal_blueprint.route('/jp/hex-to-decimal')
def hex_to_decimal():
    model = get_default_model()
    model['url'] = '/jp/hex-to-decimal'
    model['enUrl'] = '/hex-to-decimal'
    model['headerTitle'] = '16進数から10進数へのオンライン変換ツール  - Coding.Tools'
    model['bodyTitle'] = '16進数から10進数へのオンライン変換ツール'
    model['description'] = 'このオンライン16進数 -  10進数変換ツールを使用すると、16進数を10進数に変換できます。'
    model['keywords'] = '10進数への16進数、10進数への16進数'
    model['image'] = '/image/cartoon-hex-to-decimal.png'
    return render_template(template_dir + 'template_hex_to_decimal_jp.html', model=model)


@Web_HexToDecimal_blueprint.route('/jp/decimal-to-hex')
def decimal_to_hex():
    model = get_default_model()
    model['url'] = '/jp/decimal-to-hex'
    model['enUrl'] = '/decimal-to-hex'
    model['headerTitle'] = '10進数から16進数へのオンライン変換ツール  - Coding.Tools'
    model['bodyTitle'] = '10進数から16進数へのオンライン変換ツール'
    model['description'] = 'このオンライン10進数 -  16進数変換ツールを使用すると、10進数を16進数に変換できます。'
    model['keywords'] = '10進数から16進数、10進数から16進数'
    model['image'] = '/image/cartoon-decimal-to-hex.png'
    return render_template(template_dir + 'template_decimal_to_hex_jp.html', model=model)


@Web_HexToDecimal_blueprint.route('/jp/octal-to-decimal')
def octal_to_decimal():
    model = get_default_model()
    model['url'] = '/jp/octal-to-decimal'
    model['enUrl'] = '/octal-to-decimal'
    model['headerTitle'] = '8進数から10進数へのオンライン変換ツール  - Coding.Tools'
    model['bodyTitle'] = '8進数から10進数へのオンライン変換ツール'
    model['description'] = 'このオンライン8進数 -  10進数変換ツールを使用すると、8進数を10進数に変換できます。'
    model['keywords'] = '8進数から8進数、10進数から8進数'
    model['image'] = '/image/octal_to_decimal.png'
    return render_template(template_dir + 'template_octal_to_decimal_jp.html', model=model)


@Web_HexToDecimal_blueprint.route('/jp/decimal-to-octal')
def decimal_to_octal():
    model = get_default_model()
    model['url'] = '/jp/decimal-to-octal'
    model['enUrl'] = '/decimal-to-octal'
    model['headerTitle'] = '10進数から8進数へのオンライン変換ツール  - Coding.Tools'
    model['bodyTitle'] = '10進数から8進数へのオンライン変換ツール'
    model['description'] = 'このオンラインの10進数から8進数への変換ツールは、10進数を8進数に変換するのに役立ちます。'
    model['keywords'] = '10進数から8進数、10進数から8進数'
    model['image'] = '/image/cartoon-decimal-to-octal.png'
    return render_template(template_dir + 'template_decimal_to_octal_jp.html', model=model)


@Web_HexToDecimal_blueprint.route('/jp/binary-to-decimal')
def binary_to_decimal():
    model = get_default_model()
    model['url'] = '/jp/binary-to-decimal'
    model['enUrl'] = '/binary-to-decimal'
    model['headerTitle'] = 'バイナリから10進オンラインへの変換ツール  - Coding.Tools'
    model['bodyTitle'] = 'バイナリから10進オンラインへの変換ツール'
    model['description'] = 'このオンライン2進数 -  10進数変換ツールは、8進数を10進数に変換するのに役立ちます。'
    model['keywords'] = '2進数から10進数、2進数から10進数'
    model['image'] = '/image/cartoon-decimal-to-binary.png'
    return render_template(template_dir + 'template_binary_to_decimal_jp.html', model=model)


@Web_HexToDecimal_blueprint.route('/jp/decimal-to-binary')
def decimal_to_binary():
    model = get_default_model()
    model['url'] = '/jp/decimal-to-binary'
    model['enUrl'] = '/decimal-to-binary'
    model['headerTitle'] = '10進数から2進数へのオンライン変換ツール  - Coding.Tools'
    model['bodyTitle'] = '10進数から2進数へのオンライン変換ツール'
    model['description'] = 'このオンライン10進数 -  2進数変換ツールを使用すると、10進数を2進数に変換できます。'
    model['keywords'] = '10進数から2進数、10進数から2進数'
    model['image'] = '/image/cartoon-decimal-to-binary.png'
    return render_template(template_dir + 'template_decimal_to_binary_jp.html', model=model)


@Web_HexToDecimal_blueprint.route('/jp/ascii-table')
def ascii_table():
    model = get_default_model()
    model['url'] = '/jp/ascii-table'
    model['enUrl'] = '/ascii-table'
    model['headerTitle'] = 'ASCIIルックアップテーブル  - Coding.Tools'
    model['bodyTitle'] = 'ASCIIルックアップテーブル'
    model['description'] = 'ASCII制御文字、ASCII記号、およびASCII拡張文字を含む、完全なASCIIルックアップテーブル（256ビット）。'
    model['keywords'] = 'ASCIIテーブル、ASCII拡張テーブル'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_ascii_table_jp.html', model=model)


@Web_HexToDecimal_blueprint.route('/jp/hex-to-ascii')
def hex_to_ascii():
    model = get_default_model()
    model['url'] = '/jp/hex-to-ascii'
    model['enUrl'] = '/hex-to-ascii'
    model['headerTitle'] = '16進数からASCII文字列へのオンライン変換ツール  - Coding.Tools'
    model['bodyTitle'] = '16進数からASCII文字列へのオンライン変換ツール'
    model['description'] = 'このオンライン16進数からASCII文字列への変換ツールを使用すると、16進数配列をASCII文字列に変換できます。'
    model['keywords'] = 'ASCIIから16進数、ASCIIから16進数'
    model['image'] = '/image/cartoon-hex-to-ascii.png'
    return render_template(template_dir + 'template_hex_to_ascii_jp.html', model=model)


@Web_HexToDecimal_blueprint.route('/jp/ascii-to-hex')
def ascii_to_hex():
    model = get_default_model()
    model['url'] = '/jp/ascii-to-hex'
    model['enUrl'] = '/ascii-to-hex'
    model['headerTitle'] = 'ASCII文字列から16進オンラインへの変換ツール  - Coding.Tools'
    model['bodyTitle'] = 'ASCII文字列から16進オンラインへの変換ツール'
    model['description'] = 'このオンラインASCII文字列から16進数への変換ツールを使用すると、ASCII文字列を16進数の配列に変換できます。'
    model['keywords'] = 'ASCIIから16進数、ASCIIから16進数'
    model['image'] = '/image/cartoon-ascii-to-hex.png'
    return render_template(template_dir + 'template_ascii_to_hex_jp.html', model=model)


@Web_HexToDecimal_blueprint.route('/jp/fraction-to-decimal')
def fraction_to_decimal():
    model = get_default_model()
    model['url'] = '/jp/fraction-to-decimal'
    model['enUrl'] = '/fraction-to-decimal'
    model['headerTitle'] = '十進オンライン変換ツールにスコア  - Coding.Tools'
    model['bodyTitle'] = '10進オンライン変換ツールへのスコア'
    model['description'] = 'このオンラインスコアから10進数への変換ツールを使用すると、スコアを10進数に変換でき、入力分子と分母が結果ボックスに表示されます。'
    model['keywords'] = '小数への小数、小数への小数'
    model['image'] = '/image/cartoon-fraction-to-decimal.png'
    return render_template(template_dir + 'template_fraction_to_decimal_jp.html', model=model)


@Web_HexToDecimal_blueprint.route('/jp/decimal-to-fraction')
def decimal_to_fraction():
    model = get_default_model()
    model['url'] = '/jp/decimal-to-fraction'
    model['enUrl'] = '/decimal-to-fraction'
    model['headerTitle'] = 'オンライン変換ツールを獲得する10進数  - Coding.Tools'
    model['bodyTitle'] = 'オンライン変換ツールを獲得する10進数'
    model['description'] = 'このオンラインの小数からスコアへの変換ツールを使用すると、小数を小数に変換できます小数点を入力すると、スコアが結果ボックスに表示されます。'
    model['keywords'] = '小数から小数、小数から小数'
    model['image'] = '/image/cartoon-decimal-to-fraction.png'
    return render_template(template_dir + 'template_decimal_to_fraction_jp.html', model=model)


@Web_HexToDecimal_blueprint.route('/jp/percent-to-decimal')
def percent_to_decimal():
    model = get_default_model()
    model['url'] = '/jp/percent-to-decimal'
    model['enUrl'] = '/percent-to-decimal'
    model['headerTitle'] = '10進オンライン変換ツールへの割合  - Coding.Tools'
    model['bodyTitle'] = '10進オンライン変換ツールの割合'
    model['description'] = 'このオンラインパーセンテージから10進数への変換ツールを使用すると、パーセンテージを10進数に変換できますパーセンテージを入力すると、結果ボックスに小数点が表示されます。'
    model['keywords'] = '10進数に対するパーセント、10進数に対するパーセント'
    model['image'] = '/image/cartoon-percent-to-decimal.png'
    return render_template(template_dir + 'template_percent_to_decimal_jp.html', model=model)


@Web_HexToDecimal_blueprint.route('/jp/decimal-to-percent')
def decimal_to_percent():
    model = get_default_model()
    model['url'] = '/jp/decimal-to-percent'
    model['enUrl'] = '/decimal-to-percent'
    model['headerTitle'] = 'パーセントからオンラインへの変換ツール  - Coding.Tools'
    model['bodyTitle'] = 'パーセントからオンラインへの変換ツール'
    model['description'] = 'このオンラインの10進数からパーセントへの変換ツールを使用すると、10進数をパーセンテージに変換できます小数点を入力すると、結果ボックスにそのパーセンテージが表示されます。'
    model['keywords'] = '小数からパーセント、小数からパーセント'
    model['image'] = '/image/cartoon-decimal-to-percent.png'
    return render_template(template_dir + 'template_decimal_to_percent_jp.html', model=model)


@Web_HexToDecimal_blueprint.route('/jp/percent-to-fraction')
def percent_to_fraction():
    model = get_default_model()
    model['url'] = '/jp/percent-to-fraction'
    model['enUrl'] = '/percent-to-fraction'
    model['headerTitle'] = 'オンライン変換ツールのスコアに対する割合  - Coding.Tools'
    model['bodyTitle'] = 'オンライン変換ツールの得点率'
    model['description'] = 'このオンラインのパーセンテージからスコアへの変換ツールを使用すると、パーセンテージをスコアに変換できますパーセンテージを入力すると、スコアが結果ボックスに表示されます。'
    model['keywords'] = '分数に対する割合、分数に対する割合'
    model['image'] = '/image/cartoon-percent-to-fraction.png'
    return render_template(template_dir + 'template_percent_to_fraction_jp.html', model=model)


@Web_HexToDecimal_blueprint.route('/jp/fraction-to-percent')
def fraction_to_percent():
    model = get_default_model()
    model['url'] = '/jp/fraction-to-percent'
    model['enUrl'] = '/fraction-to-percent'
    model['headerTitle'] = 'パーセントオンライン変換ツールにスコア  - Coding.Tools'
    model['bodyTitle'] = 'パーセンテージオンライン変換ツールへのスコア'
    model['description'] = 'パーセンテージ変換ツールへのこのオンラインスコアは、あなたがスコアをパーセンテージに変換するのを助けます分子と分母を入力すると、パーセンテージは結果ボックスに表示されます。'
    model['keywords'] = 'パーセント/分数、パーセント'
    model['image'] = '/image/cartoon-fraction-to-percent.png'
    return render_template(template_dir + 'template_fraction_to_percent_jp.html', model=model)


@Web_HexToDecimal_blueprint.route('/jp/hex-to-rgb')
def hex_to_rgb():
    model = get_default_model()
    model['url'] = '/jp/hex-to-rgb'
    model['enUrl'] = '/hex-to-rgb'
    model['headerTitle'] = '16進カラーからRGBカラーへのオンライン変換ツール  - Coding.Tools'
    model['bodyTitle'] = '16進カラーからRGBカラーへのオンライン変換ツール'
    model['description'] = 'このオンラインHexカラーからRGBカラーへの変換ツールを使用すると、HexカラーをRGBカラーに変換し、選択したカラーをリアルタイムでテストできます。'
    model['keywords'] = 'RGBから16進数、RGBから16進数の色'
    model['image'] = '/image/cartoon-hex-to-rgb.png'
    return render_template(template_dir + 'template_hex_to_rgb_jp.html', model=model)


@Web_HexToDecimal_blueprint.route('/jp/rgb-to-hex')
def rgb_to_hex():
    model = get_default_model()
    model['url'] = '/jp/rgb-to-hex'
    model['enUrl'] = '/rgb-to-hex'
    model['headerTitle'] = 'RGBカラーから16進カラーへのオンライン変換ツール  - Coding.Tools'
    model['bodyTitle'] = 'RGBカラーから16進カラーへのオンライン変換ツール'
    model['description'] = 'このオンラインRGBカラーから16進カラーへの変換ツールを使用すると、RGBカラーを16進カラーに変換し、選択したカラーをリアルタイムでテストできます。'
    model['keywords'] = 'RGBから16進数へ、RGBカラーから16進数へ'
    model['image'] = '/image/cartoon-rgb-to-hex.png'
    return render_template(template_dir + 'template_rgb_to_hex_jp.html', model=model)


@Web_HexToDecimal_blueprint.route('/jp/hex-to-rgba')
def hex_to_rgba():
    model = get_default_model()
    model['url'] = '/jp/hex-to-rgba'
    model['enUrl'] = '/hex-to-rgba'
    model['headerTitle'] = '16進カラーからRGBAカラーへのオンライン変換ツール  - Coding.Tools'
    model['bodyTitle'] = '16進カラーからRGBAカラーへのオンライン変換ツール'
    model['description'] = 'このオンラインHexカラーからRGBAカラーへの変換ツールを使用すると、HexカラーをRGBAカラー（透明度不透明度を含む）に変換し、選択したカラーをリアルタイムでテストできます。'
    model['keywords'] = 'RGBAカラーへの16進数、RGBAカラーへの16進数カラー'
    model['image'] = '/image/cartoon-hex-to-rgba.png'
    return render_template(template_dir + 'template_hex_to_rgba_jp.html', model=model)


@Web_HexToDecimal_blueprint.route('/jp/rgba-to-hex')
def rgba_to_hex():
    model = get_default_model()
    model['url'] = '/jp/rgba-to-hex'
    model['enUrl'] = '/rgba-to-hex'
    model['headerTitle'] = 'RGBAカラーから16進カラーへのオンライン変換ツール  - Coding.Tools'
    model['bodyTitle'] = 'RGBAカラーから16進カラーへのオンライン変換ツール'
    model['description'] = 'このオンラインRGBAカラーから16進カラーへの変換ツールを使用すると、RGBAカラー（透明度不透明度を含む）を16進カラーに変換し、選択したカラーをリアルタイムでテストできます。'
    model['keywords'] = 'RGBAから16進数、RGBAから16進数の色'
    model['image'] = '/image/cartoon-rgba-to-hex.png'
    return render_template(template_dir + 'template_rgba_to_hex_jp.html', model=model)


@Web_HexToDecimal_blueprint.route('/jp/roman-numerals-chart')
def roman_numerals_chart():
    model = get_default_model()
    model['url'] = '/jp/roman-numerals-chart'
    model['enUrl'] = '/roman-numerals-chart'
    model['headerTitle'] = 'ローマ数字表1-1000  - コーディングツール'
    model['bodyTitle'] = 'ローマ数字比較表1-1000'
    model['description'] = '1から1000までの完全なローマ数字比較表。'
    model['keywords'] = 'ローマ数字チャート、ローマ数字チャート'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_roman_numerals_chart_jp.html', model=model)


@Web_HexToDecimal_blueprint.route('/jp/roman-numerals-to-numbers')
def roman_numerals_to_numbers():
    model = get_default_model()
    model['url'] = '/jp/roman-numerals-to-numbers'
    model['enUrl'] = '/roman-numerals-to-numbers'
    model['headerTitle'] = 'ローマ数字からアラビア数字へのオンライン変換ツール  - Coding.Tools'
    model['bodyTitle'] = 'ローマ数字からアラビア語へのデジタルオンライン変換ツール'
    model['description'] = 'このオンラインローマ数字からアラビア数字への変換ツールを使用すると、ローマ数字をアラビア数字に変換でき、ローマ数字を入力すると結果ボックスにアラビア数字が表示されます。'
    model['keywords'] = 'ローマ数字はアラビア数字に変わる'
    model['image'] = '/image/cartoon-roman-numerals-to-numbers.png'
    return render_template(template_dir + 'template_roman_numerals_to_numbers_jp.html', model=model)


@Web_HexToDecimal_blueprint.route('/jp/numbers-to-roman-numerals')
def numbers_to_roman_numerals():
    model = get_default_model()
    model['url'] = '/jp/numbers-to-roman-numerals'
    model['enUrl'] = '/numbers-to-roman-numerals'
    model['headerTitle'] = 'アラビアデジタルからローマ数字へのデジタルオンライン変換ツール  - Coding.Tools'
    model['bodyTitle'] = 'アラビアデジタルからローマ数字へのデジタルオンライン変換ツール'
    model['description'] = 'このオンラインアラビア数字からローマ数字への変換ツールを使用すると、アラビア数字をローマ数字に変換できますアラビア数字を入力すると、ローマ数字が結果ボックスに表示されます。'
    model['keywords'] = 'アラビア数字はローマ数字に変わる'
    model['image'] = '/image/cartoon-numbers-to-roman-numerals.png'
    return render_template(template_dir + 'template_numbers_to_roman_numerals_jp.html', model=model)
