from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_HexToDecimal_blueprint = Blueprint('Web_HexToDecimal_blueprint_CN', __name__)
template_dir = 'HexToDecimal/cn/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'zh-Hans'
    return model


@Web_HexToDecimal_blueprint.route('/cn/hex-to-decimal')
def hex_to_decimal():
    model = get_default_model()
    model['url'] = '/cn/hex-to-decimal'
    model['enUrl'] = '/hex-to-decimal'
    model['headerTitle'] = '16进制到10进制在线转换工具  - Coding.Tools'
    model['bodyTitle'] = '16进制到10进制在线转换工具'
    model['description'] = '这个在线16进制到10进制转换工具可帮助您将一个十六进制数转换为十进制数.'
    model['keywords'] = 'Hex to Decimal, 16进制转10进制'
    model['image'] = '/image/cartoon-hex-to-decimal.png'
    return render_template(template_dir + 'template_hex_to_decimal_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/decimal-to-hex')
def decimal_to_hex():
    model = get_default_model()
    model['url'] = '/cn/decimal-to-hex'
    model['enUrl'] = '/decimal-to-hex'
    model['headerTitle'] = '10进制到16进制在线转换工具  - Coding.Tools'
    model['bodyTitle'] = '10进制到16进制在线转换工具'
    model['description'] = '这个在线10进制到16进制转换工具可帮助您将一个十进制数转换为十六进制数.'
    model['keywords'] = 'Decimal to Hex, 10进制转16进制'
    model['image'] = '/image/cartoon-decimal-to-hex.png'
    return render_template(template_dir + 'template_decimal_to_hex_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/octal-to-decimal')
def octal_to_decimal():
    model = get_default_model()
    model['url'] = '/cn/octal-to-decimal'
    model['enUrl'] = '/octal-to-decimal'
    model['headerTitle'] = '8进制到10进制在线转换工具  - Coding.Tools'
    model['bodyTitle'] = '8进制到10进制在线转换工具'
    model['description'] = '这个在线8进制到10进制转换工具可帮助您将一个八进制数转换为十进制数.'
    model['keywords'] = 'Octal to Decimal, 8进制转10进制'
    model['image'] = '/image/octal_to_decimal.png'
    return render_template(template_dir + 'template_octal_to_decimal_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/decimal-to-octal')
def decimal_to_octal():
    model = get_default_model()
    model['url'] = '/cn/decimal-to-octal'
    model['enUrl'] = '/decimal-to-octal'
    model['headerTitle'] = '10进制到8进制在线转换工具  - Coding.Tools'
    model['bodyTitle'] = '10进制到8进制在线转换工具'
    model['description'] = '这个在线10进制到8进制转换工具可帮助您将一个十进制数转换为八进制数.'
    model['keywords'] = 'Decimal to Octal, 10进制转8进制'
    model['image'] = '/image/cartoon-decimal-to-octal.png'
    return render_template(template_dir + 'template_decimal_to_octal_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/binary-to-decimal')
def binary_to_decimal():
    model = get_default_model()
    model['url'] = '/cn/binary-to-decimal'
    model['enUrl'] = '/binary-to-decimal'
    model['headerTitle'] = '2进制到10进制在线转换工具  - Coding.Tools'
    model['bodyTitle'] = '2进制到10进制在线转换工具'
    model['description'] = '这个在线2进制到10进制转换工具可帮助您将一个八进制数转换为十进制数.'
    model['keywords'] = 'Binary to Decimal, 2进制转10进制'
    model['image'] = '/image/cartoon-binary-to-decimal.png'
    return render_template(template_dir + 'template_binary_to_decimal_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/decimal-to-binary')
def decimal_to_binary():
    model = get_default_model()
    model['url'] = '/cn/decimal-to-binary'
    model['enUrl'] = '/decimal-to-binary'
    model['headerTitle'] = '10进制到2进制在线转换工具  - Coding.Tools'
    model['bodyTitle'] = '10进制到2进制在线转换工具'
    model['description'] = '这个在线10进制到2进制转换工具可帮助您将一个十进制数转换为二进制数.'
    model['keywords'] = 'Decimal to Binary, 10进制转2进制'
    model['image'] = '/image/cartoon-decimal-to-binary.png'
    return render_template(template_dir + 'template_decimal_to_binary_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/binary-to-hex')
def binary_to_hex():
    model = get_default_model()
    model['url'] = '/cn/binary-to-hex'
    model['enUrl'] = '/binary-to-hex'
    model['headerTitle'] = '2进制到16进制在线转换工具  - Coding.Tools'
    model['bodyTitle'] = '2进制到16进制在线转换工具'
    model['description'] = '这个在线2进制到16进制转换工具可帮助您将一个2进制数转换为16进制数.'
    model['keywords'] = 'Binary to Hex,2进制转16进制'
    model['image'] = '/image/20190308/cartoon_binary_to_hex.png'
    return render_template(template_dir + 'template_binary_to_hex_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/hex-to-binary')
def hex_to_binary():
    model = get_default_model()
    model['url'] = '/cn/hex-to-binary'
    model['enUrl'] = '/hex-to-binary'
    model['headerTitle'] = '16进制到2进制在线转换工具  - Coding.Tools'
    model['bodyTitle'] = '16进制到2进制在线转换工具'
    model['description'] = '这个在线16进制到2进制转换工具可帮助您将一个16进制数转换为2进制数.'
    model['keywords'] = 'Hex to Binary,16进制转2进制'
    model['image'] = '/image/20190308/cartoon_hex_to_binary.png'
    return render_template(template_dir + 'template_hex_to_binary_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/ascii-table')
def ascii_table():
    model = get_default_model()
    model['url'] = '/cn/ascii-table'
    model['enUrl'] = '/ascii-table'
    model['headerTitle'] = 'ASCII查询表  - Coding.Tools'
    model['bodyTitle'] = 'ASCII查询表'
    model['description'] = '完整的ASCII查询表(256位),包括ASCII控制字符,ASCII符号以及ASCII扩展字符.'
    model['keywords'] = 'ASCII表, ASCII扩展表'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_ascii_table_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/hex-to-ascii')
def hex_to_ascii():
    model = get_default_model()
    model['url'] = '/cn/hex-to-ascii'
    model['enUrl'] = '/hex-to-ascii'
    model['headerTitle'] = '16进制到ASCII字符串在线转换工具  - Coding.Tools'
    model['bodyTitle'] = '16进制到ASCII字符串在线转换工具'
    model['description'] = '这个在线16进制到ASCII字符串转换工具可帮助您将一个16进制数组转换为ASCII字符串.'
    model['keywords'] = 'Hex to ASCII, 16进制转ASCII'
    model['image'] = '/image/cartoon-hex-to-ascii.png'
    return render_template(template_dir + 'template_hex_to_ascii_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/ascii-to-hex')
def ascii_to_hex():
    model = get_default_model()
    model['url'] = '/cn/ascii-to-hex'
    model['enUrl'] = '/ascii-to-hex'
    model['headerTitle'] = 'ASCII字符串到16进制在线转换工具  - Coding.Tools'
    model['bodyTitle'] = 'ASCII字符串到16进制在线转换工具'
    model['description'] = '这个在线ASCII字符串到16进制转换工具可帮助您将一个ASCII字符串转换为16进制数组.'
    model['keywords'] = 'ASCII to Hex, ASCII转16进制'
    model['image'] = '/image/cartoon-ascii-to-hex.png'
    return render_template(template_dir + 'template_ascii_to_hex_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/binary-to-text')
def binary_to_text():
    model = get_default_model()
    model['url'] = '/cn/binary-to-text'
    model['enUrl'] = '/binary-to-text'
    model['headerTitle'] = '2进制到ASCII字符串在线转换工具  - Coding.Tools'
    model['bodyTitle'] = '2进制到ASCII字符串在线转换工具'
    model['description'] = '这个在线2进制到ASCII字符串转换工具可帮助您将一个2进制数组转换为ASCII字符串.'
    model['keywords'] = '16进制转字符串, binary to text'
    model['image'] = '/image/20190308/cartoon_binary_to_text.png'
    return render_template(template_dir + 'template_binary_to_text_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/text-to-binary')
def text_to_binary():
    model = get_default_model()
    model['url'] = '/cn/text-to-binary'
    model['enUrl'] = '/text-to-binary'
    model['headerTitle'] = 'ASCII字符串到2进制在线转换工具  - Coding.Tools'
    model['bodyTitle'] = 'ASCII字符串到2进制在线转换工具'
    model['description'] = '这个在线ASCII字符串到2进制转换工具可帮助您将一个ASCII字符串转换为2进制数组.'
    model['keywords'] = 'ASCII to binary, ASCII转2进制'
    model['image'] = '/image/20190308/cartoon_text_to_binary.png'
    return render_template(template_dir + 'template_text_to_binary_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/fraction-to-decimal')
def fraction_to_decimal():
    model = get_default_model()
    model['url'] = '/cn/fraction-to-decimal'
    model['enUrl'] = '/fraction-to-decimal'
    model['headerTitle'] = '分数到小数在线转换工具  - Coding.Tools'
    model['bodyTitle'] = '分数到小数在线转换工具'
    model['description'] = '这个在线分数到小数转换工具可帮助您将一个分数转换为小数.输入分子和分母,小数会显示在结果框中.'
    model['keywords'] = 'Fraction to Decimal, 分数转小数'
    model['image'] = '/image/cartoon-fraction-to-decimal.png'
    return render_template(template_dir + 'template_fraction_to_decimal_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/decimal-to-fraction')
def decimal_to_fraction():
    model = get_default_model()
    model['url'] = '/cn/decimal-to-fraction'
    model['enUrl'] = '/decimal-to-fraction'
    model['headerTitle'] = '小数到分数在线转换工具  - Coding.Tools'
    model['bodyTitle'] = '小数到分数在线转换工具'
    model['description'] = '这个在线小数到分数转换工具可帮助您将一个小数转换为分数.输入小数,分数会显示在结果框中.'
    model['keywords'] = 'Decimal to Fraction, 小数转分数'
    model['image'] = '/image/cartoon-decimal-to-fraction.png'
    return render_template(template_dir + 'template_decimal_to_fraction_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/percent-to-decimal')
def percent_to_decimal():
    model = get_default_model()
    model['url'] = '/cn/percent-to-decimal'
    model['enUrl'] = '/percent-to-decimal'
    model['headerTitle'] = '百分比到小数在线转换工具  - Coding.Tools'
    model['bodyTitle'] = '百分比到小数在线转换工具'
    model['description'] = '这个在线百分比到小数转换工具可帮助您将一个百分比数转换为小数.输入百分比数,小数会显示在结果框中.'
    model['keywords'] = 'Percent to Decimal, 百分比转小数'
    model['image'] = '/image/cartoon-percent-to-decimal.png'
    return render_template(template_dir + 'template_percent_to_decimal_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/decimal-to-percent')
def decimal_to_percent():
    model = get_default_model()
    model['url'] = '/cn/decimal-to-percent'
    model['enUrl'] = '/decimal-to-percent'
    model['headerTitle'] = '小数到百分比在线转换工具  - Coding.Tools'
    model['bodyTitle'] = '小数到百分比在线转换工具'
    model['description'] = '这个在线小数到百分比转换工具可帮助您将一个小数转换为百分比.输入小数,百分比会显示在结果框中.'
    model['keywords'] = 'Decimal to Percent, 小数转百分比'
    model['image'] = '/image/cartoon-decimal-to-percent.png'
    return render_template(template_dir + 'template_decimal_to_percent_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/percent-to-fraction')
def percent_to_fraction():
    model = get_default_model()
    model['url'] = '/cn/percent-to-fraction'
    model['enUrl'] = '/percent-to-fraction'
    model['headerTitle'] = '百分比到分数在线转换工具  - Coding.Tools'
    model['bodyTitle'] = '百分比到分数在线转换工具'
    model['description'] = '这个在线百分比到分数转换工具可帮助您将一个百分比数转换为分数.输入百分比,分数会显示在结果框中.'
    model['keywords'] = 'Percent to Fraction, 百分比转分数'
    model['image'] = '/image/cartoon-percent-to-fraction.png'
    return render_template(template_dir + 'template_percent_to_fraction_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/fraction-to-percent')
def fraction_to_percent():
    model = get_default_model()
    model['url'] = '/cn/fraction-to-percent'
    model['enUrl'] = '/fraction-to-percent'
    model['headerTitle'] = '分数到百分比在线转换工具  - Coding.Tools'
    model['bodyTitle'] = '分数到百分比在线转换工具'
    model['description'] = '这个在线分数到百分比转换工具可帮助您将一个分数转换为百分比.输入分子和分母,百分比会显示在结果框中.'
    model['keywords'] = 'Fraction to Percent, 分数转百分比'
    model['image'] = '/image/cartoon-fraction-to-percent.png'
    return render_template(template_dir + 'template_fraction_to_percent_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/hex-to-rgb')
def hex_to_rgb():
    model = get_default_model()
    model['url'] = '/cn/hex-to-rgb'
    model['enUrl'] = '/hex-to-rgb'
    model['headerTitle'] = 'Hex颜色到RGB颜色在线转换工具  - Coding.Tools'
    model['bodyTitle'] = 'Hex颜色到RGB颜色在线转换工具'
    model['description'] = '这个在线Hex颜色到RGB颜色转换工具可帮助您将一个Hex颜色转换为RGB颜色, 并实时测试您选择的颜色.'
    model['keywords'] = 'Hex to RGB, Hex颜色转RGB颜色'
    model['image'] = '/image/cartoon-hex-to-rgb.png'
    return render_template(template_dir + 'template_hex_to_rgb_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/rgb-to-hex')
def rgb_to_hex():
    model = get_default_model()
    model['url'] = '/cn/rgb-to-hex'
    model['enUrl'] = '/rgb-to-hex'
    model['headerTitle'] = 'RGB颜色到Hex颜色在线转换工具  - Coding.Tools'
    model['bodyTitle'] = 'RGB颜色到Hex颜色在线转换工具'
    model['description'] = '这个在线RGB颜色到Hex颜色转换工具可帮助您将一个RGB颜色转换为Hex颜色, 并实时测试您选择的颜色.'
    model['keywords'] = 'RGB to Hex, RGB颜色转Hex颜色'
    model['image'] = '/image/cartoon-rgb-to-hex.png'
    return render_template(template_dir + 'template_rgb_to_hex_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/hex-to-rgba')
def hex_to_rgba():
    model = get_default_model()
    model['url'] = '/cn/hex-to-rgba'
    model['enUrl'] = '/hex-to-rgba'
    model['headerTitle'] = 'Hex颜色到RGBA颜色在线转换工具  - Coding.Tools'
    model['bodyTitle'] = 'Hex颜色到RGBA颜色在线转换工具'
    model['description'] = '这个在线Hex颜色到RGBA颜色转换工具可帮助您将一个Hex颜色转换为RGBA颜色(包括透明度Opacity), 并实时测试您选择的颜色.'
    model['keywords'] = 'Hex to RGBA, Hex颜色转RGBA颜色'
    model['image'] = '/image/cartoon-hex-to-rgba.png'
    return render_template(template_dir + 'template_hex_to_rgba_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/rgba-to-hex')
def rgba_to_hex():
    model = get_default_model()
    model['url'] = '/cn/rgba-to-hex'
    model['enUrl'] = '/rgba-to-hex'
    model['headerTitle'] = 'RGBA颜色转Hex颜色在线转换工具  - Coding.Tools'
    model['bodyTitle'] = 'RGBA颜色转Hex颜色在线转换工具'
    model['description'] = '这个在线RGBA颜色转Hex颜色转换工具可帮助您将一个RGBA颜色(包括透明度Opacity)转换为Hex颜色, 并实时测试您选择的颜色.'
    model['keywords'] = 'RGBA to Hex, RGBA颜色转Hex颜色'
    model['image'] = '/image/cartoon-rgba-to-hex.png'
    return render_template(template_dir + 'template_rgba_to_hex_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/roman-numerals-chart')
def roman_numerals_chart():
    model = get_default_model()
    model['url'] = '/cn/roman-numerals-chart'
    model['enUrl'] = '/roman-numerals-chart'
    model['headerTitle'] = '罗马数字对照表 1-1000  - Coding.Tools'
    model['bodyTitle'] = '罗马数字对照表 1-1000'
    model['description'] = '从1到1000完整的罗马数字对照表.'
    model['keywords'] = 'Roman Numerals Chart, 罗马数字对照表'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_roman_numerals_chart_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/roman-numerals-to-numbers')
def roman_numerals_to_numbers():
    model = get_default_model()
    model['url'] = '/cn/roman-numerals-to-numbers'
    model['enUrl'] = '/roman-numerals-to-numbers'
    model['headerTitle'] = '罗马数字到阿拉伯数字在线转换工具  - Coding.Tools'
    model['bodyTitle'] = '罗马数字到阿拉伯数字在线转换工具'
    model['description'] = '这个在线罗马数字到阿拉伯数字转换工具可帮助您将一个罗马数字转换为阿拉伯数字. 输入罗马数字, 阿拉伯数字会显示在结果框中.'
    model['keywords'] = '罗马数字转阿拉伯数字'
    model['image'] = '/image/cartoon-roman-numerals-to-numbers.png'
    return render_template(template_dir + 'template_roman_numerals_to_numbers_cn.html', model=model)


@Web_HexToDecimal_blueprint.route('/cn/numbers-to-roman-numerals')
def numbers_to_roman_numerals():
    model = get_default_model()
    model['url'] = '/cn/numbers-to-roman-numerals'
    model['enUrl'] = '/numbers-to-roman-numerals'
    model['headerTitle'] = '阿拉伯数字到罗马数字在线转换工具  - Coding.Tools'
    model['bodyTitle'] = '阿拉伯数字到罗马数字在线转换工具'
    model['description'] = '这个在线阿拉伯数字到罗马数字转换工具可帮助您将一个阿拉伯数字转换为罗马数字. 输入阿拉伯数字, 罗马数字会显示在结果框中.'
    model['keywords'] = '阿拉伯数字转罗马数字'
    model['image'] = '/image/cartoon-numbers-to-roman-numerals.png'
    return render_template(template_dir + 'template_numbers_to_roman_numerals_cn.html', model=model)
