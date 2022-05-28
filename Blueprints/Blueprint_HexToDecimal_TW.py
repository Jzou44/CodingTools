from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_HexToDecimal_blueprint = Blueprint('Web_HexToDecimal_blueprint_TW', __name__)
template_dir = 'HexToDecimal/tw/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'zh-Hant'
    return model


@Web_HexToDecimal_blueprint.route('/tw/hex-to-decimal')
def hex_to_decimal():
    model = get_default_model()
    model['url'] = '/tw/hex-to-decimal'
    model['enUrl'] = '/hex-to-decimal'
    model['headerTitle'] = '16進製到10進制在線轉換工具 - Coding.Tools'
    model['bodyTitle'] = '16進製到10進制在線轉換工具'
    model['description'] = '這個在線16進製到10進制轉換工具可幫助您將一個十六進制數轉換為十進制數.'
    model['keywords'] = 'Hex to Decimal, 16進制轉10進制'
    model['image'] = '/image/cartoon-hex-to-decimal.png'
    return render_template(template_dir + 'template_hex_to_decimal_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/decimal-to-hex')
def decimal_to_hex():
    model = get_default_model()
    model['url'] = '/tw/decimal-to-hex'
    model['enUrl'] = '/decimal-to-hex'
    model['headerTitle'] = '10進製到16進制在線轉換工具 - Coding.Tools'
    model['bodyTitle'] = '10進製到16進制在線轉換工具'
    model['description'] = '這個在線10進製到16進制轉換工具可幫助您將一個十進制數轉換為十六進制數.'
    model['keywords'] = 'Decimal to Hex, 10進制轉16進制'
    model['image'] = '/image/cartoon-decimal-to-hex.png'
    return render_template(template_dir + 'template_decimal_to_hex_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/octal-to-decimal')
def octal_to_decimal():
    model = get_default_model()
    model['url'] = '/tw/octal-to-decimal'
    model['enUrl'] = '/octal-to-decimal'
    model['headerTitle'] = '8進製到10進制在線轉換工具 - Coding.Tools'
    model['bodyTitle'] = '8進製到10進制在線轉換工具'
    model['description'] = '這個在線8進製到10進制轉換工具可幫助您將一個八進制數轉換為十進制數.'
    model['keywords'] = 'Octal to Decimal, 8進制轉10進制'
    model['image'] = '/image/octal_to_decimal.png'
    return render_template(template_dir + 'template_octal_to_decimal_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/decimal-to-octal')
def decimal_to_octal():
    model = get_default_model()
    model['url'] = '/tw/decimal-to-octal'
    model['enUrl'] = '/decimal-to-octal'
    model['headerTitle'] = '10進製到8進制在線轉換工具 - Coding.Tools'
    model['bodyTitle'] = '10進製到8進制在線轉換工具'
    model['description'] = '這個在線10進製到8進制轉換工具可幫助您將一個十進制數轉換為八進制數.'
    model['keywords'] = 'Decimal to Octal, 10進制轉8進制'
    model['image'] = '/image/cartoon-decimal-to-octal.png'
    return render_template(template_dir + 'template_decimal_to_octal_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/binary-to-decimal')
def binary_to_decimal():
    model = get_default_model()
    model['url'] = '/tw/binary-to-decimal'
    model['enUrl'] = '/binary-to-decimal'
    model['headerTitle'] = '2進製到10進制在線轉換工具 - Coding.Tools'
    model['bodyTitle'] = '2進製到10進制在線轉換工具'
    model['description'] = '這個在線2進製到10進制轉換工具可幫助您將一個八進制數轉換為十進制數.'
    model['keywords'] = 'Binary to Decimal, 2進制轉10進制'
    model['image'] = '/image/cartoon-binary-to-decimal.png'
    return render_template(template_dir + 'template_binary_to_decimal_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/decimal-to-binary')
def decimal_to_binary():
    model = get_default_model()
    model['url'] = '/tw/decimal-to-binary'
    model['enUrl'] = '/decimal-to-binary'
    model['headerTitle'] = '10進製到2進制在線轉換工具 - Coding.Tools'
    model['bodyTitle'] = '10進製到2進制在線轉換工具'
    model['description'] = '這個在線10進製到2進制轉換工具可幫助您將一個十進制數轉換為二進制數.'
    model['keywords'] = 'Decimal to Binary, 10進制轉2進制'
    model['image'] = '/image/cartoon-decimal-to-binary.png'
    return render_template(template_dir + 'template_decimal_to_binary_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/binary-to-hex')
def binary_to_hex():
    model = get_default_model()
    model['url'] = '/tw/binary-to-hex'
    model['enUrl'] = '/binary-to-hex'
    model['headerTitle'] = '2進製到16進制在線轉換工具  - Coding.Tools'
    model['bodyTitle'] = '2進製到16進制在線轉換工具'
    model['description'] = '這個在線2進製到16進制轉換工具可幫助您將一個2進制數轉換為16進制數.'
    model['keywords'] = 'Binary to Hex,2進制轉16進制'
    model['image'] = '/image/20190308/cartoon_binary_to_hex.png'
    return render_template(template_dir + 'template_binary_to_hex_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/hex-to-binary')
def hex_to_binary():
    model = get_default_model()
    model['url'] = '/tw/hex-to-binary'
    model['enUrl'] = '/hex-to-binary'
    model['headerTitle'] = '16進製到2進制在線轉換工具  - Coding.Tools'
    model['bodyTitle'] = '16進製到2進制在線轉換工具'
    model['description'] = '這個在線16進製到2進制轉換工具可幫助您將一個16進制數轉換為2進制數.'
    model['keywords'] = 'Hex to Binary,16進制轉2進制'
    model['image'] = '/image/20190308/cartoon_hex_to_binary.png'
    return render_template(template_dir + 'template_hex_to_binary_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/ascii-table')
def ascii_table():
    model = get_default_model()
    model['url'] = '/tw/ascii-table'
    model['enUrl'] = '/ascii-table'
    model['headerTitle'] = 'ASCII查詢表 - Coding.Tools'
    model['bodyTitle'] = 'ASCII查詢表'
    model['description'] = '完整的ASCII查詢表(256位),包括ASCII控製字符,ASCII符號以及ASCII擴展字符.'
    model['keywords'] = 'ASCII表, ASCII擴展表'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_ascii_table_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/hex-to-ascii')
def hex_to_ascii():
    model = get_default_model()
    model['url'] = '/tw/hex-to-ascii'
    model['enUrl'] = '/hex-to-ascii'
    model['headerTitle'] = '16進製到ASCII字符串在線轉換工具 - Coding.Tools'
    model['bodyTitle'] = '16進製到ASCII字符串在線轉換工具'
    model['description'] = '這個在線16進製到ASCII字符串轉換工具可幫助您將一個16進制數組轉換為ASCII字符串.'
    model['keywords'] = 'Hex to ASCII, 16進制轉ASCII'
    model['image'] = '/image/cartoon-hex-to-ascii.png'
    return render_template(template_dir + 'template_hex_to_ascii_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/ascii-to-hex')
def ascii_to_hex():
    model = get_default_model()
    model['url'] = '/tw/ascii-to-hex'
    model['enUrl'] = '/ascii-to-hex'
    model['headerTitle'] = 'ASCII字符串到16進制在線轉換工具 - Coding.Tools'
    model['bodyTitle'] = 'ASCII字符串到16進制在線轉換工具'
    model['description'] = '這個在線ASCII字符串到16進制轉換工具可幫助您將一個ASCII字符串轉換為16進制數組.'
    model['keywords'] = 'ASCII to Hex, ASCII轉16進制'
    model['image'] = '/image/cartoon-ascii-to-hex.png'
    return render_template(template_dir + 'template_ascii_to_hex_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/binary-to-text')
def binary_to_text():
    model = get_default_model()
    model['url'] = '/tw/binary-to-text'
    model['enUrl'] = '/binary-to-text'
    model['headerTitle'] = '2進製到ASCII字符串在線轉換工具  - Coding.Tools'
    model['bodyTitle'] = '2進製到ASCII字符串在線轉換工具'
    model['description'] = '這個在線2進製到ASCII字符串轉換工具可幫助您將一個2進制數組轉換為ASCII字符串.'
    model['keywords'] = '2進製轉字符串, binary to text'
    model['image'] = '/image/20190308/cartoon_binary_to_text.png'
    return render_template(template_dir + 'template_binary_to_text_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/text-to-binary')
def text_to_binary():
    model = get_default_model()
    model['url'] = '/tw/text-to-binary'
    model['enUrl'] = '/text-to-binary'
    model['headerTitle'] = 'ASCII字符串到2進制在線轉換工具  - Coding.Tools'
    model['bodyTitle'] = 'ASCII字符串到2進制在線轉換工具'
    model['description'] = '這個在線ASCII字符串到2進制轉換工具可幫助您將一個ASCII字符串轉換為2進制數組.'
    model['keywords'] = 'ASCII to binary, ASCII轉2進制'
    model['image'] = '/image/20190308/cartoon_text_to_binary.png'
    return render_template(template_dir + 'template_text_to_binary_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/fraction-to-decimal')
def fraction_to_decimal():
    model = get_default_model()
    model['url'] = '/tw/fraction-to-decimal'
    model['enUrl'] = '/fraction-to-decimal'
    model['headerTitle'] = '分數到小數在線轉換工具 - Coding.Tools'
    model['bodyTitle'] = '分數到小數在線轉換工具'
    model['description'] = '這個在線分數到小數轉換工具可幫助您將一個分數轉換為小數.輸入分子和分母,小數會顯示在結果框中.'
    model['keywords'] = 'Fraction to Decimal, 分數轉小數'
    model['image'] = '/image/cartoon-fraction-to-decimal.png'
    return render_template(template_dir + 'template_fraction_to_decimal_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/decimal-to-fraction')
def decimal_to_fraction():
    model = get_default_model()
    model['url'] = '/tw/decimal-to-fraction'
    model['enUrl'] = '/decimal-to-fraction'
    model['headerTitle'] = '小數到分數在線轉換工具 - Coding.Tools'
    model['bodyTitle'] = '小數到分數在線轉換工具'
    model['description'] = '這個在線小數到分數轉換工具可幫助您將一個小數轉換為分數.輸入小數,分數會顯示在結果框中.'
    model['keywords'] = 'Decimal to Fraction, 小數轉分數'
    model['image'] = '/image/cartoon-decimal-to-fraction.png'
    return render_template(template_dir + 'template_decimal_to_fraction_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/percent-to-decimal')
def percent_to_decimal():
    model = get_default_model()
    model['url'] = '/tw/percent-to-decimal'
    model['enUrl'] = '/percent-to-decimal'
    model['headerTitle'] = '百分比到小數在線轉換工具 - Coding.Tools'
    model['bodyTitle'] = '百分比到小數在線轉換工具'
    model['description'] = '這個在線百分比到小數轉換工具可幫助您將一個百分比數轉換為小數.輸入百分比數,小數會顯示在結果框中.'
    model['keywords'] = 'Percent to Decimal, 百分比轉小數'
    model['image'] = '/image/cartoon-percent-to-decimal.png'
    return render_template(template_dir + 'template_percent_to_decimal_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/decimal-to-percent')
def decimal_to_percent():
    model = get_default_model()
    model['url'] = '/tw/decimal-to-percent'
    model['enUrl'] = '/decimal-to-percent'
    model['headerTitle'] = '小數到百分比在線轉換工具 - Coding.Tools'
    model['bodyTitle'] = '小數到百分比在線轉換工具'
    model['description'] = '這個在線小數到百分比轉換工具可幫助您將一個小數轉換為百分比.輸入小數,百分比會顯示在結果框中.'
    model['keywords'] = 'Decimal to Percent, 小數轉百分比'
    model['image'] = '/image/cartoon-decimal-to-percent.png'
    return render_template(template_dir + 'template_decimal_to_percent_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/percent-to-fraction')
def percent_to_fraction():
    model = get_default_model()
    model['url'] = '/tw/percent-to-fraction'
    model['enUrl'] = '/percent-to-fraction'
    model['headerTitle'] = '百分比到分數在線轉換工具 - Coding.Tools'
    model['bodyTitle'] = '百分比到分數在線轉換工具'
    model['description'] = '這個在線百分比到分數轉換工具可幫助您將一個百分比數轉換為分數.輸入百分比,分數會顯示在結果框中.'
    model['keywords'] = 'Percent to Fraction, 百分比轉分數'
    model['image'] = '/image/cartoon-percent-to-fraction.png'
    return render_template(template_dir + 'template_percent_to_fraction_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/fraction-to-percent')
def fraction_to_percent():
    model = get_default_model()
    model['url'] = '/tw/fraction-to-percent'
    model['enUrl'] = '/fraction-to-percent'
    model['headerTitle'] = '分數到百分比在線轉換工具 - Coding.Tools'
    model['bodyTitle'] = '分數到百分比在線轉換工具'
    model['description'] = '這個在線分數到百分比轉換工具可幫助您將一個分數轉換為百分比.輸入分子和分母,百分比會顯示在結果框中.'
    model['keywords'] = 'Fraction to Percent, 分數轉百分比'
    model['image'] = '/image/cartoon-fraction-to-percent.png'
    return render_template(template_dir + 'template_fraction_to_percent_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/hex-to-rgb')
def hex_to_rgb():
    model = get_default_model()
    model['url'] = '/tw/hex-to-rgb'
    model['enUrl'] = '/hex-to-rgb'
    model['headerTitle'] = 'Hex顏色到RGB顏色在線轉換工具 - Coding.Tools'
    model['bodyTitle'] = 'Hex顏色到RGB顏色在線轉換工具'
    model['description'] = '這個在線Hex顏色到RGB顏色轉換工具可幫助您將一個Hex顏色轉換為RGB顏色, 並實時測試您選擇的顏色.'
    model['keywords'] = 'Hex to RGB, Hex顏色轉RGB顏色'
    model['image'] = '/image/cartoon-hex-to-rgb.png'
    return render_template(template_dir + 'template_hex_to_rgb_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/rgb-to-hex')
def rgb_to_hex():
    model = get_default_model()
    model['url'] = '/tw/rgb-to-hex'
    model['enUrl'] = '/rgb-to-hex'
    model['headerTitle'] = 'RGB顏色到Hex顏色在線轉換工具 - Coding.Tools'
    model['bodyTitle'] = 'RGB顏色到Hex顏色在線轉換工具'
    model['description'] = '這個在線RGB顏色到Hex顏色轉換工具可幫助您將一個RGB顏色轉換為Hex顏色, 並實時測試您選擇的顏色.'
    model['keywords'] = 'RGB to Hex, RGB顏色轉Hex顏色'
    model['image'] = '/image/cartoon-rgb-to-hex.png'
    return render_template(template_dir + 'template_rgb_to_hex_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/hex-to-rgba')
def hex_to_rgba():
    model = get_default_model()
    model['url'] = '/tw/hex-to-rgba'
    model['enUrl'] = '/hex-to-rgba'
    model['headerTitle'] = 'Hex顏色到RGBA顏色在線轉換工具 - Coding.Tools'
    model['bodyTitle'] = 'Hex顏色到RGBA顏色在線轉換工具'
    model['description'] = '這個在線Hex顏色到RGBA顏色轉換工具可幫助您將一個Hex顏色轉換為RGBA顏色(包括透明度Opacity), 並實時測試您選擇的顏色.'
    model['keywords'] = 'Hex to RGBA, Hex顏色轉RGBA顏色'
    model['image'] = '/image/cartoon-hex-to-rgba.png'
    return render_template(template_dir + 'template_hex_to_rgba_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/rgba-to-hex')
def rgba_to_hex():
    model = get_default_model()
    model['url'] = '/tw/rgba-to-hex'
    model['enUrl'] = '/rgba-to-hex'
    model['headerTitle'] = 'RGBA顏色轉Hex顏色在線轉換工具 - Coding.Tools'
    model['bodyTitle'] = 'RGBA顏色轉Hex顏色在線轉換工具'
    model['description'] = '這個在線RGBA顏色轉Hex顏色轉換工具可幫助您將一個RGBA顏色(包括透明度Opacity)轉換為Hex顏色, 並實時測試您選擇的顏色.'
    model['keywords'] = 'RGBA to Hex, RGBA顏色轉Hex顏色'
    model['image'] = '/image/cartoon-rgba-to-hex.png'
    return render_template(template_dir + 'template_rgba_to_hex_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/roman-numerals-chart')
def roman_numerals_chart():
    model = get_default_model()
    model['url'] = '/tw/roman-numerals-chart'
    model['enUrl'] = '/roman-numerals-chart'
    model['headerTitle'] = '羅馬數字對照表1-1000  - Coding.Tools'
    model['bodyTitle'] = '羅馬數字對照表1-1000'
    model['description'] = '從1到1000完整的羅馬數字對照表.'
    model['keywords'] = 'Roman Numerals Chart, 羅馬數字對照表'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_roman_numerals_chart_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/roman-numerals-to-numbers')
def roman_numerals_to_numbers():
    model = get_default_model()
    model['url'] = '/tw/roman-numerals-to-numbers'
    model['enUrl'] = '/roman-numerals-to-numbers'
    model['headerTitle'] = '羅馬數字到阿拉伯數字在線轉換工具 - Coding.Tools'
    model['bodyTitle'] = '羅馬數字到阿拉伯數字在線轉換工具'
    model['description'] = '這個在線羅馬數字到阿拉伯數字轉換工具可幫助您將一個羅馬數字轉換為阿拉伯數字. 輸入羅馬數字, 阿拉伯數字會顯示在結果框中.'
    model['keywords'] = '羅馬數字轉阿拉伯數字'
    model['image'] = '/image/cartoon-roman-numerals-to-numbers.png'
    return render_template(template_dir + 'template_roman_numerals_to_numbers_tw.html', model=model)


@Web_HexToDecimal_blueprint.route('/tw/numbers-to-roman-numerals')
def numbers_to_roman_numerals():
    model = get_default_model()
    model['url'] = '/tw/numbers-to-roman-numerals'
    model['enUrl'] = '/numbers-to-roman-numerals'
    model['headerTitle'] = '阿拉伯數字到羅馬數字在線轉換工具 - Coding.Tools'
    model['bodyTitle'] = '阿拉伯數字到羅馬數字在線轉換工具'
    model['description'] = '這個在線阿拉伯數字到羅馬數字轉換工具可幫助您將一個阿拉伯數字轉換為羅馬數字. 輸入阿拉伯數字, 羅馬數字會顯示在結果框中.'
    model['keywords'] = '阿拉伯數字轉羅馬數字'
    model['image'] = '/image/cartoon-numbers-to-roman-numerals.png'
    return render_template(template_dir + 'template_numbers_to_roman_numerals_tw.html', model=model)
