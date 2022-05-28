from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_HexToDecimal_blueprint = Blueprint('Web_HexToDecimal_blueprint_KR', __name__)
template_dir = 'HexToDecimal/kr/'

def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'ko'
    return model

@Web_HexToDecimal_blueprint.route('/kr/hex-to-decimal')
def hex_to_decimal():
    model = get_default_model()
    model['url'] = '/kr/hex-to-decimal'
    model['enUrl'] = '/hex-to-decimal'
    model['headerTitle'] = '16 진수 - 10 진수 온라인 변환 도구  - Coding.Tools'
    model['bodyTitle'] = '16 진수 - 십진수 온라인 변환 도구'
    model['description'] = '십진수 변환 도구에 대한 온라인 16 진수는 16 진수를 10 진수로 변환하는 데 유용합니다.'
    model['keywords'] = '16 진수에서 10 진수, 16 진수에서 10 진수'
    model['image'] = '/image/cartoon-hex-to-decimal.png'
    return render_template(template_dir + 'template_hex_to_decimal_kr.html', model=model)


@Web_HexToDecimal_blueprint.route('/kr/decimal-to-hex')
def decimal_to_hex():
    model = get_default_model()
    model['url'] = '/kr/decimal-to-hex'
    model['enUrl'] = '/decimal-to-hex'
    model['headerTitle'] = '십진수에서 16 진수로의 온라인 변환 도구  - Coding.Tools'
    model['bodyTitle'] = '10 진수에서 16 진수로의 온라인 변환 도구'
    model['description'] = '이 온라인 10 진수 - 16 진수 변환 도구는 10 진수를 16 진수로 변환하는 데 유용합니다.'
    model['keywords'] = '10 진수 - 16 진수, 10 진수 - 16 진수'
    model['image'] = '/image/cartoon-decimal-to-hex.png'
    return render_template(template_dir + 'template_decimal_to_hex_kr.html', model=model)


@Web_HexToDecimal_blueprint.route('/kr/octal-to-decimal')
def octal_to_decimal():
    model = get_default_model()
    model['url'] = '/kr/octal-to-decimal'
    model['enUrl'] = '/octal-to-decimal'
    model['headerTitle'] = '10 진 - 십진수 온라인 변환 도구  - Coding.Tools'
    model['bodyTitle'] = '10 진수에서 10 진수로의 온라인 변환 도구'
    model['description'] = '이 온라인 8 진수 - 10 진수 변환 도구는 8 진수를 10 진수로 변환하는 데 유용합니다.'
    model['keywords'] = '8 진수를 10 진수로, 8 진수를 10 진수로'
    model['image'] = '/image/octal_to_decimal.png'
    return render_template(template_dir + 'template_octal_to_decimal_kr.html', model=model)


@Web_HexToDecimal_blueprint.route('/kr/decimal-to-octal')
def decimal_to_octal():
    model = get_default_model()
    model['url'] = '/kr/decimal-to-octal'
    model['enUrl'] = '/decimal-to-octal'
    model['headerTitle'] = '십진법에서 8 진수 온라인 변환 도구  - Coding.Tools'
    model['bodyTitle'] = '10 진수 - 8 진수 온라인 변환 도구'
    model['description'] = '이 온라인 10 진수 - 8 진 변환 도구는 10 진수를 8 진수로 변환하는 데 유용합니다.'
    model['keywords'] = '10 진수를 8 진수로, 10 진수를 8 진수로'
    model['image'] = '/image/cartoon-decimal-to-octal.png'
    return render_template(template_dir + 'template_decimal_to_octal_kr.html', model=model)


@Web_HexToDecimal_blueprint.route('/kr/binary-to-decimal')
def binary_to_decimal():
    model = get_default_model()
    model['url'] = '/kr/binary-to-decimal'
    model['enUrl'] = '/binary-to-decimal'
    model['headerTitle'] = '십진수 온라인 변환 도구에서 이진법  - Coding.Tools'
    model['bodyTitle'] = '2 진 - 십진수 온라인 변환 도구'
    model['description'] = '이 온라인 2 진 - 10 진수 변환 도구는 8 진수를 10 진수로 변환하는 데 유용합니다.'
    model['keywords'] = '2 진수에서 10 진수로, 2 진수에서 10 진수로'
    model['image'] = '/image/cartoon-decimal-to-binary.png'
    return render_template(template_dir + 'template_binary_to_decimal_kr.html', model=model)


@Web_HexToDecimal_blueprint.route('/kr/decimal-to-binary')
def decimal_to_binary():
    model = get_default_model()
    model['url'] = '/kr/decimal-to-binary'
    model['enUrl'] = '/decimal-to-binary'
    model['headerTitle'] = '십진법에서 이진 온라인 변환 도구  - Coding.Tools'
    model['bodyTitle'] = '10 진수 - 2 진 온라인 변환 도구'
    model['description'] = '이 온라인 10 진수 - 2 진 변환 도구는 10 진수를 2 진수로 변환하는 데 유용합니다.'
    model['keywords'] = '십진수 바이너리, 십진수 바이너리'
    model['image'] = '/image/cartoon-decimal-to-binary.png'
    return render_template(template_dir + 'template_decimal_to_binary_kr.html', model=model)


@Web_HexToDecimal_blueprint.route('/kr/ascii-table')
def ascii_table():
    model = get_default_model()
    model['url'] = '/kr/ascii-table'
    model['enUrl'] = '/ascii-table'
    model['headerTitle'] = 'ASCII 조회 테이블  - Coding.Tools'
    model['bodyTitle'] = 'ASCII 조회 테이블'
    model['description'] = 'ASCII 제어 문자, ASCII 기호 및 ASCII 확장 문자를 포함하여 완전한 ASCII 조회 표 (256 비트).'
    model['keywords'] = 'ASCII 테이블, ASCII 확장 테이블'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_ascii_table_kr.html', model=model)


@Web_HexToDecimal_blueprint.route('/kr/hex-to-ascii')
def hex_to_ascii():
    model = get_default_model()
    model['url'] = '/kr/hex-to-ascii'
    model['enUrl'] = '/hex-to-ascii'
    model['headerTitle'] = 'ASCII 문자열 온라인 변환 도구에 16 진수  - Coding.Tools'
    model['bodyTitle'] = 'ASCII 문자열 온라인 변환 도구에 대한 16 진수'
    model['description'] = '이 온라인 16 진수 - ASCII 문자열 변환 도구는 16 진수 배열을 ASCII 문자열로 변환하는 데 유용합니다.'
    model['keywords'] = '16 진수로 ASCII, 16 진수에서 ASCII로'
    model['image'] = '/image/cartoon-hex-to-ascii.png'
    return render_template(template_dir + 'template_hex_to_ascii_kr.html', model=model)


@Web_HexToDecimal_blueprint.route('/kr/ascii-to-hex')
def ascii_to_hex():
    model = get_default_model()
    model['url'] = '/kr/ascii-to-hex'
    model['enUrl'] = '/ascii-to-hex'
    model['headerTitle'] = 'ASCII 문자열 - 16 진수 온라인 변환 도구  - Coding.Tools'
    model['bodyTitle'] = 'ASCII 문자열 - 16 진수 온라인 변환 도구'
    model['description'] = '이 온라인 ASCII 16 진수 - 16 진 변환 도구는 ASCII. 자열을 16 진수 배열로 변환하는 데 유용합니다.'
    model['keywords'] = 'ASCII에서 16 진수, ASCII에서 16 진수'
    model['image'] = '/image/cartoon-ascii-to-hex.png'
    return render_template(template_dir + 'template_ascii_to_hex_kr.html', model=model)


@Web_HexToDecimal_blueprint.route('/kr/fraction-to-decimal')
def fraction_to_decimal():
    model = get_default_model()
    model['url'] = '/kr/fraction-to-decimal'
    model['enUrl'] = '/fraction-to-decimal'
    model['headerTitle'] = '십진수 온라인 변환 도구 점수  - Coding.Tools'
    model['bodyTitle'] = '소수점 온라인 변환 도구 점수'
    model['description'] = '십진 변환 도구에이 온라인 점수는 점수를 십진수로 변환하는 데 도움이됩니다. 입력 분자와 분모는 결과 상자에 표시됩니다.'
    model['keywords'] = '십진수까지의 소수점, 소수점 이하 자릿수'
    model['image'] = '/image/cartoon-fraction-to-decimal.png'
    return render_template(template_dir + 'template_fraction_to_decimal_kr.html', model=model)


@Web_HexToDecimal_blueprint.route('/kr/decimal-to-fraction')
def decimal_to_fraction():
    model = get_default_model()
    model['url'] = '/kr/decimal-to-fraction'
    model['enUrl'] = '/decimal-to-fraction'
    model['headerTitle'] = '십진법 온라인 점수 계산 도구  - Coding.Tools'
    model['bodyTitle'] = '10 진수 - 점수 온라인 변환 도구'
    model['description'] = '이 온라인 10 진수 - 점수 변환 도구는 소수점을 점수로 변환하는 데 도움이됩니다. 소수점을 입력하면 점수가 결과 상자에 표시됩니다.'
    model['keywords'] = '십진법에서 분수까지, 분수에서 분수까지'
    model['image'] = '/image/cartoon-decimal-to-fraction.png'
    return render_template(template_dir + 'template_decimal_to_fraction_kr.html', model=model)


@Web_HexToDecimal_blueprint.route('/kr/percent-to-decimal')
def percent_to_decimal():
    model = get_default_model()
    model['url'] = '/kr/percent-to-decimal'
    model['enUrl'] = '/percent-to-decimal'
    model['headerTitle'] = '10 진수 온라인 변환 도구 백분율  - Coding.Tools'
    model['bodyTitle'] = '10 진수 온라인 변환 도구 백분율'
    model['description'] = '십진수 변환 도구에 대한 온라인 백분율은 백분율을 십진수로 변환하는 데 도움이됩니다. 백분율을 입력하면 십진수가 결과 상자에 나타납니다.'
    model['keywords'] = '십진수 백분율, 십진수 백분율'
    model['image'] = '/image/cartoon-percent-to-decimal.png'
    return render_template(template_dir + 'template_percent_to_decimal_kr.html', model=model)


@Web_HexToDecimal_blueprint.route('/kr/decimal-to-percent')
def decimal_to_percent():
    model = get_default_model()
    model['url'] = '/kr/decimal-to-percent'
    model['enUrl'] = '/decimal-to-percent'
    model['headerTitle'] = '십진수에서 백분율로의 온라인 변환 도구  - Coding.Tools'
    model['bodyTitle'] = '10 진수에서 백분율로의 온라인 변환 도구'
    model['description'] = '이 온라인 10 진수 - 백분율 변환 도구를 사용하면 십진수를 백분율로 변환하는 데 도움이됩니다. 십진수를 입력하면 백분율이 결과 상자에 표시됩니다.'
    model['keywords'] = '십진수에서 백분율, 백분율에서 백분율'
    model['image'] = '/image/cartoon-decimal-to-percent.png'
    return render_template(template_dir + 'template_decimal_to_percent_kr.html', model=model)


@Web_HexToDecimal_blueprint.route('/kr/percent-to-fraction')
def percent_to_fraction():
    model = get_default_model()
    model['url'] = '/kr/percent-to-fraction'
    model['enUrl'] = '/percent-to-fraction'
    model['headerTitle'] = '점수 온라인 전환 도구  - Coding.Tools'
    model['bodyTitle'] = '온라인 전환 도구 점수 백분율'
    model['description'] = '이 온라인 백분율 점수 변환 도구는 백분율을 점수로 변환하는 데 도움이됩니다. 백분율을 입력하면 점수가 결과 상자에 표시됩니다.'
    model['keywords'] = '분율 대비 백분율'
    model['image'] = '/image/cartoon-percent-to-fraction.png'
    return render_template(template_dir + 'template_percent_to_fraction_kr.html', model=model)


@Web_HexToDecimal_blueprint.route('/kr/fraction-to-percent')
def fraction_to_percent():
    model = get_default_model()
    model['url'] = '/kr/fraction-to-percent'
    model['enUrl'] = '/fraction-to-percent'
    model['headerTitle'] = '점수 - 온라인 변환 도구  - Coding.Tools'
    model['bodyTitle'] = '점수 변환 온라인 전환 도구'
    model['description'] = '이 온라인 점수 대 백분율 변환 도구를 사용하면 점수를 백분율로 변환하는 데 도움이됩니다. 분자와 분모를 입력하면 백분율이 결과 상자에 표시됩니다.'
    model['keywords'] = '분율에서 백분율, 분율'
    model['image'] = '/image/cartoon-fraction-to-percent.png'
    return render_template(template_dir + 'template_fraction_to_percent_kr.html', model=model)


@Web_HexToDecimal_blueprint.route('/kr/hex-to-rgb')
def hex_to_rgb():
    model = get_default_model()
    model['url'] = '/kr/hex-to-rgb'
    model['enUrl'] = '/hex-to-rgb'
    model['headerTitle'] = '16 진수 색상 - RGB 색상 온라인 변환 도구  - Coding.Tools'
    model['bodyTitle'] = '16 진수 색상 - RGB 색상 온라인 변환 도구'
    model['description'] = '이 온라인 16 진수 - RGB RGB 변환 도구를 사용하면 16 진수 색상을 RGB 색상으로 변환하고 선택한 색상을 실시간으로 테스트 할 수 있습니다.'
    model['keywords'] = 'Hex ~ RGB, Hex 색 ~ RGB 색'
    model['image'] = '/image/cartoon-hex-to-rgb.png'
    return render_template(template_dir + 'template_hex_to_rgb_kr.html', model=model)


@Web_HexToDecimal_blueprint.route('/kr/rgb-to-hex')
def rgb_to_hex():
    model = get_default_model()
    model['url'] = '/kr/rgb-to-hex'
    model['enUrl'] = '/rgb-to-hex'
    model['headerTitle'] = 'RGB 색상 - 16 진수 색상 온라인 변환 도구  - Coding.Tools'
    model['bodyTitle'] = 'RGB 색상 - 16 진수 색상 온라인 변환 도구'
    model['description'] = '이 온라인 RGB 색상 - 16 진수 색상 변환 도구를 사용하면 RGB 색상을 16 진수 색상으로 변환하고 선택한 색상을 실시간으로 테스트 할 수 있습니다.'
    model['keywords'] = 'RGB에서 Hex로, RGB에서 Hex로'
    model['image'] = '/image/cartoon-rgb-to-hex.png'
    return render_template(template_dir + 'template_rgb_to_hex_kr.html', model=model)


@Web_HexToDecimal_blueprint.route('/kr/hex-to-rgba')
def hex_to_rgba():
    model = get_default_model()
    model['url'] = '/kr/hex-to-rgba'
    model['enUrl'] = '/hex-to-rgba'
    model['headerTitle'] = 'Hex 컬러에서 RGBA 컬러 온라인 변환 도구  - Coding.Tools'
    model['bodyTitle'] = 'RGBA 컬러 온라인 변환 도구에 대한 16 진수 색상'
    model['description'] = '이 온라인 16 진수 - RGBA 색상 변환 도구를 사용하면 16 진수 색상을 RGBA 색상 (투명도 불투명도 포함)으로 변환하고 선택한 색상을 실시간으로 테스트 할 수 있습니다.'
    model['keywords'] = 'Hex ~ RGBA, Hex 색 ~ RGBA 색'
    model['image'] = '/image/cartoon-hex-to-rgba.png'
    return render_template(template_dir + 'template_hex_to_rgba_kr.html', model=model)


@Web_HexToDecimal_blueprint.route('/kr/rgba-to-hex')
def rgba_to_hex():
    model = get_default_model()
    model['url'] = '/kr/rgba-to-hex'
    model['enUrl'] = '/rgba-to-hex'
    model['headerTitle'] = 'RGBA 컬러에서 16 진수 컬러 온라인 변환 도구  - Coding.Tools'
    model['bodyTitle'] = 'RGBA 색상 - 16 진수 색상 온라인 변환 도구'
    model['description'] = '이 온라인 RGBA 색상 - 16 진수 색상 변환 도구를 사용하면 RGBA 색상 (투명도 불투명도 포함)을 16 진수 색상으로 변환하고 선택한 색상을 실시간으로 테스트 할 수 있습니다.'
    model['keywords'] = 'RGBA에서 Hex로, RGBA에서 Hex로'
    model['image'] = '/image/cartoon-rgba-to-hex.png'
    return render_template(template_dir + 'template_rgba_to_hex_kr.html', model=model)


@Web_HexToDecimal_blueprint.route('/kr/roman-numerals-chart')
def roman_numerals_chart():
    model = get_default_model()
    model['url'] = '/kr/roman-numerals-chart'
    model['enUrl'] = '/roman-numerals-chart'
    model['headerTitle'] = '로마 숫자 표 1-1000 - 코딩. 도구'
    model['bodyTitle'] = '로마 숫자 비교표 1-1000'
    model['description'] = '1에서 1000 사이의 완전한 로마 숫자 비교표.'
    model['keywords'] = '로마 숫자 차트, 로마 숫자'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_roman_numerals_chart_kr.html', model=model)


@Web_HexToDecimal_blueprint.route('/kr/roman-numerals-to-numbers')
def roman_numerals_to_numbers():
    model = get_default_model()
    model['url'] = '/kr/roman-numerals-to-numbers'
    model['enUrl'] = '/roman-numerals-to-numbers'
    model['headerTitle'] = '로마 숫자를 아라비아 숫자로 변환하는 온라인 변환 도구  - Coding.Tools'
    model['bodyTitle'] = '로마 숫자에서 아랍어 디지털 온라인 변환 도구'
    model['description'] = '이 온라인 로마 숫자와 아라비아 숫자 변환 도구를 사용하면 로마 숫자를 아라비아 숫자로 변환 할 수 있습니다. 로마 숫자를 입력하면 아랍어 숫자가 결과 상자에 표시됩니다.'
    model['keywords'] = '로마 숫자는 아라비아 숫자로 바뀝니다.'
    model['image'] = '/image/cartoon-roman-numerals-to-numbers.png'
    return render_template(template_dir + 'template_roman_numerals_to_numbers_kr.html', model=model)


@Web_HexToDecimal_blueprint.route('/kr/numbers-to-roman-numerals')
def numbers_to_roman_numerals():
    model = get_default_model()
    model['url'] = '/kr/numbers-to-roman-numerals'
    model['enUrl'] = '/numbers-to-roman-numerals'
    model['headerTitle'] = '아랍어 디지털에서 로마 온라인 디지털 전환 도구  - Coding.Tools'
    model['bodyTitle'] = '아랍어 디지털 to 로마 디지털 온라인 변환 도구'
    model['description'] = '이 온라인 아라비아 숫자 - 로마 숫자 변환 도구를 사용하면 아라비아 숫자를 로마 숫자로 변환 할 수 있습니다. 아라비아 숫자를 입력하면 로마 숫자가 결과 상자에 표시됩니다.'
    model['keywords'] = '아라비아 숫자는 로마 숫자로 바뀝니다.'
    model['image'] = '/image/cartoon-numbers-to-roman-numerals.png'
    return render_template(template_dir + 'template_numbers_to_roman_numerals_kr.html', model=model)
