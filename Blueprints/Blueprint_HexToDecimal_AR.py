from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_HexToDecimal_blueprint = Blueprint('Web_HexToDecimal_blueprint_AR', __name__)
template_dir = 'HexToDecimal/ar/'

def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'ar'
    return model

@Web_HexToDecimal_blueprint.route('/ar/hex-to-decimal')
def hex_to_decimal():
    model = get_default_model()
    model['url'] = '/ar/hex-to-decimal'
    model['enUrl'] = '/hex-to-decimal'
    model['headerTitle'] = 'سداسي عشري إلى عشري أداة التحويل عبر الإنترنت - الترميز. أدوات'
    model['bodyTitle'] = 'سداسي عشري إلى أداة التحويل عبر الإنترنت العشرية'
    model['description'] = 'تساعدك أداة التحويل الست عشري إلى عشري على الإنترنت في تحويل رقم سداسي عشري إلى رقم عشري.'
    model['keywords'] = 'عشري إلى عشري ، سداسي عشري إلى عشري'
    model['image'] = '/image/cartoon-hex-to-decimal.png'
    return render_template(template_dir + 'template_hex_to_decimal_ar.html', model=model)


@Web_HexToDecimal_blueprint.route('/ar/decimal-to-hex')
def decimal_to_hex():
    model = get_default_model()
    model['url'] = '/ar/decimal-to-hex'
    model['enUrl'] = '/decimal-to-hex'
    model['headerTitle'] = 'عشري إلى أداة التحويل عبر الإنترنت ست عشري - الترميز. أدوات'
    model['bodyTitle'] = 'عشري إلى أداة تحويل عبر الإنترنت ست عشري'
    model['description'] = 'تساعدك هذه الأداة العشرية إلى أداة تحويل عشري على الإنترنت في تحويل رقم عشري إلى رقم سداسي عشري.'
    model['keywords'] = 'عشري إلى Hex ، عشري إلى سداسي عشري'
    model['image'] = '/image/cartoon-decimal-to-hex.png'
    return render_template(template_dir + 'template_decimal_to_hex_ar.html', model=model)


@Web_HexToDecimal_blueprint.route('/ar/octal-to-decimal')
def octal_to_decimal():
    model = get_default_model()
    model['url'] = '/ar/octal-to-decimal'
    model['enUrl'] = '/octal-to-decimal'
    model['headerTitle'] = 'Octal to Decimal Online Conversion Tool  - Coding.Tools'
    model['bodyTitle'] = 'ثماني إلى عشري أداة تحويل عبر الإنترنت'
    model['description'] = 'تساعدك أداة التحويل العشرية الثماني هذه على تحويل رقم ثماني إلى رقم عشري.'
    model['keywords'] = 'من ثماني إلى عشري ، ثماني إلى عشري'
    model['image'] = '/image/octal_to_decimal.png'
    return render_template(template_dir + 'template_octal_to_decimal_ar.html', model=model)


@Web_HexToDecimal_blueprint.route('/ar/decimal-to-octal')
def decimal_to_octal():
    model = get_default_model()
    model['url'] = '/ar/decimal-to-octal'
    model['enUrl'] = '/decimal-to-octal'
    model['headerTitle'] = 'من عشري إلى Octal أداة التحويل عبر الإنترنت - الترميز. أدوات'
    model['bodyTitle'] = 'عشري إلى أداة تحويل عبر الإنترنت ثماني'
    model['description'] = 'تساعدك هذه الأداة العشرية على الإنترنت لتحويلها إلى تحويل رقم عشري إلى رقم ثماني.'
    model['keywords'] = 'عشري إلى ثماني ، عشري إلى ثماني'
    model['image'] = '/image/cartoon-decimal-to-octal.png'
    return render_template(template_dir + 'template_decimal_to_octal_ar.html', model=model)


@Web_HexToDecimal_blueprint.route('/ar/binary-to-decimal')
def binary_to_decimal():
    model = get_default_model()
    model['url'] = '/ar/binary-to-decimal'
    model['enUrl'] = '/binary-to-decimal'
    model['headerTitle'] = 'ثنائي إلى عشري أداة التحويل عبر الإنترنت  - Coding.Tools'
    model['bodyTitle'] = 'ثنائي إلى عشري أداة التحويل عبر الإنترنت'
    model['description'] = 'تساعدك أداة التحويل الثنائية إلى عشري على تحويل رقم ثماني إلى رقم عشري.'
    model['keywords'] = 'ثنائي إلى عشري ، ثنائي إلى عشري'
    model['image'] = '/image/cartoon-decimal-to-binary.png'
    return render_template(template_dir + 'template_binary_to_decimal_ar.html', model=model)


@Web_HexToDecimal_blueprint.route('/ar/decimal-to-binary')
def decimal_to_binary():
    model = get_default_model()
    model['url'] = '/ar/decimal-to-binary'
    model['enUrl'] = '/decimal-to-binary'
    model['headerTitle'] = 'عشري إلى ثنائي أداة التحويل عبر الإنترنت  - Coding.Tools'
    model['bodyTitle'] = 'عشري إلى ثنائي أداة التحويل عبر الإنترنت'
    model['description'] = 'تساعدك هذه الأداة العشرية لتحويل الإنترنت الثنائية على تحويل رقم عشري إلى رقم ثنائي.'
    model['keywords'] = 'عشري إلى ثنائي ، عشري إلى ثنائي'
    model['image'] = '/image/cartoon-decimal-to-binary.png'
    return render_template(template_dir + 'template_decimal_to_binary_ar.html', model=model)


@Web_HexToDecimal_blueprint.route('/ar/ascii-table')
def ascii_table():
    model = get_default_model()
    model['url'] = '/ar/ascii-table'
    model['enUrl'] = '/ascii-table'
    model['headerTitle'] = 'جدول بحث ASCII  - Coding.Tools'
    model['bodyTitle'] = 'جدول بحث ASCII'
    model['description'] = 'إكمال جدول بحث ASCII (256 بت) ، بما في ذلك أحرف تحكم ASCII ورموز ASCII والحروف الموسعة ASCII.'
    model['keywords'] = 'جدول ASCII ، جدول تمديد ASCII'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_ascii_table_ar.html', model=model)


@Web_HexToDecimal_blueprint.route('/ar/hex-to-ascii')
def hex_to_ascii():
    model = get_default_model()
    model['url'] = '/ar/hex-to-ascii'
    model['enUrl'] = '/hex-to-ascii'
    model['headerTitle'] = 'سداسي عشري إلى ASCII سلسلة أداة التحويل عبر الإنترنت  - Coding.Tools'
    model['bodyTitle'] = 'سداسي عشري إلى ASCII سلسلة أداة التحويل عبر الإنترنت'
    model['description'] = 'تساعدك هذه أداة تحويل سلسلة ASCII عبر الإنترنت إلى تحويل صفيف سداسي عشري إلى سلسلة ASCII.'
    model['keywords'] = 'عرافة إلى ASCII ، عرافة إلى ASCII'
    model['image'] = '/image/cartoon-hex-to-ascii.png'
    return render_template(template_dir + 'template_hex_to_ascii_ar.html', model=model)


@Web_HexToDecimal_blueprint.route('/ar/ascii-to-hex')
def ascii_to_hex():
    model = get_default_model()
    model['url'] = '/ar/ascii-to-hex'
    model['enUrl'] = '/ascii-to-hex'
    model['headerTitle'] = 'سلسلة ASCII إلى أداة تحويل عبر الإنترنت ست عشري  - Coding.Tools'
    model['bodyTitle'] = 'سلسلة ASCII إلى أداة تحويل عبر الإنترنت ست عشري'
    model['description'] = 'يساعدك هذا سلسلة ASCII عبر الإنترنت إلى أداة تحويل سداسي عشرية تحويل سلسلة ASCII إلى صفيف سداسي عشري.'
    model['keywords'] = 'ASCII إلى Hex ، ASCII إلى ست عشري'
    model['image'] = '/image/cartoon-ascii-to-hex.png'
    return render_template(template_dir + 'template_ascii_to_hex_ar.html', model=model)


@Web_HexToDecimal_blueprint.route('/ar/fraction-to-decimal')
def fraction_to_decimal():
    model = get_default_model()
    model['url'] = '/ar/fraction-to-decimal'
    model['enUrl'] = '/fraction-to-decimal'
    model['headerTitle'] = 'يسجل لأداة التحويل على الإنترنت العشري  - Coding.Tools'
    model['bodyTitle'] = 'يسجل لأداة التحويل عبر الإنترنت العشري'
    model['description'] = 'تساعدك هذه النتيجة عبر الإنترنت إلى أداة التحويل العشرية في تحويل علامة إلى رقم عشري ، حيث يتم عرض البسط والمقام في مربع النتائج.'
    model['keywords'] = 'جزء إلى عشري ، كسري إلى عشري'
    model['image'] = '/image/cartoon-fraction-to-decimal.png'
    return render_template(template_dir + 'template_fraction_to_decimal_ar.html', model=model)


@Web_HexToDecimal_blueprint.route('/ar/decimal-to-fraction')
def decimal_to_fraction():
    model = get_default_model()
    model['url'] = '/ar/decimal-to-fraction'
    model['enUrl'] = '/decimal-to-fraction'
    model['headerTitle'] = 'عشري لتسجيل أداة التحويل عبر الإنترنت  - Coding.Tools'
    model['bodyTitle'] = 'عشري لتسجيل أداة تحويل عبر الإنترنت'
    model['description'] = 'تساعدك أداة التحويل العشرية هذه عبر الإنترنت في تحويل علامة عشرية إلى درجة ، أدخل الرقم العشري وستظهر النتيجة في مربع النتائج.'
    model['keywords'] = 'عشري إلى كسر ، كسري إلى كسر'
    model['image'] = '/image/cartoon-decimal-to-fraction.png'
    return render_template(template_dir + 'template_decimal_to_fraction_ar.html', model=model)


@Web_HexToDecimal_blueprint.route('/ar/percent-to-decimal')
def percent_to_decimal():
    model = get_default_model()
    model['url'] = '/ar/percent-to-decimal'
    model['enUrl'] = '/percent-to-decimal'
    model['headerTitle'] = 'النسبة المئوية لأداة التحويل عبر الإنترنت العشرية  - Coding.Tools'
    model['bodyTitle'] = 'النسبة المئوية لأداة التحويل عبر الإنترنت العشرية'
    model['description'] = 'تساعدك هذه النسبة المئوية عبر الإنترنت إلى أداة التحويل العشرية في تحويل النسبة المئوية إلى رقم عشري. أدخل النسبة المئوية وستظهر العلامة العشرية في مربع النتائج.'
    model['keywords'] = 'النسبة المئوية إلى القيمة العشرية ، النسبة المئوية إلى العلامة العشرية'
    model['image'] = '/image/cartoon-percent-to-decimal.png'
    return render_template(template_dir + 'template_percent_to_decimal_ar.html', model=model)


@Web_HexToDecimal_blueprint.route('/ar/decimal-to-percent')
def decimal_to_percent():
    model = get_default_model()
    model['url'] = '/ar/decimal-to-percent'
    model['enUrl'] = '/decimal-to-percent'
    model['headerTitle'] = 'العشرية إلى نسبة أداة التحويل عبر الإنترنت  - Coding.Tools'
    model['bodyTitle'] = 'العشرية إلى نسبة أداة التحويل عبر الإنترنت'
    model['description'] = 'تساعدك هذه الأداة العشرية إلى النسبة المئوية للتحويل عبر الإنترنت في تحويل عشري إلى نسبة مئوية. أدخل العلامة العشرية وسيتم عرض النسبة المئوية في مربع النتائج.'
    model['keywords'] = 'العشري إلى النسبة المئوية ، والكسر إلى النسبة المئوية'
    model['image'] = '/image/cartoon-decimal-to-percent.png'
    return render_template(template_dir + 'template_decimal_to_percent_ar.html', model=model)


@Web_HexToDecimal_blueprint.route('/ar/percent-to-fraction')
def percent_to_fraction():
    model = get_default_model()
    model['url'] = '/ar/percent-to-fraction'
    model['enUrl'] = '/percent-to-fraction'
    model['headerTitle'] = 'النسبة المئوية لتسجيل أداة التحويل عبر الإنترنت  - Coding.Tools'
    model['bodyTitle'] = 'النسبة المئوية لتسجيل أداة التحويل عبر الإنترنت'
    model['description'] = 'تساعدك هذه النسبة المئوية عبر الإنترنت لتحويل أداة التحويل على تحويل نسبة إلى درجة. أدخل النسبة المئوية وسيتم عرض النتيجة في مربع النتائج.'
    model['keywords'] = 'النسبة المئوية إلى الكسر ، النسبة المئوية إلى الكسر'
    model['image'] = '/image/cartoon-percent-to-fraction.png'
    return render_template(template_dir + 'template_percent_to_fraction_ar.html', model=model)


@Web_HexToDecimal_blueprint.route('/ar/fraction-to-percent')
def fraction_to_percent():
    model = get_default_model()
    model['url'] = '/ar/fraction-to-percent'
    model['enUrl'] = '/fraction-to-percent'
    model['headerTitle'] = 'يسجل النسبة المئوية لأداة التحويل عبر الإنترنت  - Coding.Tools'
    model['bodyTitle'] = 'يسجل النسبة المئوية لأداة التحويل عبر الإنترنت'
    model['description'] = 'تساعدك هذه النتيجة عبر الإنترنت إلى أداة تحويل النسبة المئوية في تحويل علامة إلى نسبة مئوية ، ثم إدخال البسط والمقام وسيتم عرض النسبة المئوية في مربع النتائج.'
    model['keywords'] = 'جزء إلى نسبة مئوية ، نسبة مئوية'
    model['image'] = '/image/cartoon-fraction-to-percent.png'
    return render_template(template_dir + 'template_fraction_to_percent_ar.html', model=model)


@Web_HexToDecimal_blueprint.route('/ar/hex-to-rgb')
def hex_to_rgb():
    model = get_default_model()
    model['url'] = '/ar/hex-to-rgb'
    model['enUrl'] = '/hex-to-rgb'
    model['headerTitle'] = 'هيكس لون إلى RGB لون أداة التحويل عبر الإنترنت  - Coding.Tools'
    model['bodyTitle'] = 'Hex لون إلى RGB لون أداة التحويل عبر الإنترنت'
    model['description'] = 'يساعدك هذا التحويل عبر الإنترنت من HEX إلى RGB على تحويل لون Hex إلى لون RGB واختبار لونك المختار في الوقت الحقيقي.'
    model['keywords'] = 'من Hex إلى RGB ، لون Hex إلى لون RGB'
    model['image'] = '/image/cartoon-hex-to-rgb.png'
    return render_template(template_dir + 'template_hex_to_rgb_ar.html', model=model)


@Web_HexToDecimal_blueprint.route('/ar/rgb-to-hex')
def rgb_to_hex():
    model = get_default_model()
    model['url'] = '/ar/rgb-to-hex'
    model['enUrl'] = '/rgb-to-hex'
    model['headerTitle'] = 'RGB لون لتحرير الهيكس على الانترنت أداة  - Coding.Tools'
    model['bodyTitle'] = 'لون RGB إلى أداة تحويل لون Hex على الإنترنت'
    model['description'] = 'يساعدك لون RGB هذا على الإنترنت إلى أداة تحويل اللون Hex على تحويل لون RGB إلى لون Hex واختبار لونك المختار في الوقت الحقيقي.'
    model['keywords'] = 'RGB إلى Hex ، لون RGB إلى Hex'
    model['image'] = '/image/cartoon-rgb-to-hex.png'
    return render_template(template_dir + 'template_rgb_to_hex_ar.html', model=model)


@Web_HexToDecimal_blueprint.route('/ar/hex-to-rgba')
def hex_to_rgba():
    model = get_default_model()
    model['url'] = '/ar/hex-to-rgba'
    model['enUrl'] = '/hex-to-rgba'
    model['headerTitle'] = 'هيكس لون إلى RGBA تحويل اون لاين أداة  - Coding.Tools'
    model['bodyTitle'] = 'HEX لون إلى RGBA أداة تحويل لون على الإنترنت'
    model['description'] = 'يساعدك لون التحويل من HEX هذا على اللون إلى RGBA على تحويل لون Hex إلى لون RGBA (بما في ذلك شفافية الشفافية) واختبار اللون الذي اخترته في الوقت الحقيقي.'
    model['keywords'] = 'من Hex إلى RGBA ، لون Hex إلى لون RGBA'
    model['image'] = '/image/cartoon-hex-to-rgba.png'
    return render_template(template_dir + 'template_hex_to_rgba_ar.html', model=model)


@Web_HexToDecimal_blueprint.route('/ar/rgba-to-hex')
def rgba_to_hex():
    model = get_default_model()
    model['url'] = '/ar/rgba-to-hex'
    model['enUrl'] = '/rgba-to-hex'
    model['headerTitle'] = 'لون RGBA إلى أداة تحويل لون Hex على الإنترنت  - Coding.Tools'
    model['bodyTitle'] = 'لون RGBA إلى أداة تحويل لون Hex على الإنترنت'
    model['description'] = 'يساعدك لون RGBA هذا على الإنترنت إلى أداة تحويل اللون Hex على تحويل لون RGBA (بما في ذلك شفافية الشفافية) إلى اللون السداسي واختبار لونك المختار في الوقت الحقيقي.'
    model['keywords'] = 'RGBA إلى Hex ، لون RGBA إلى Hex'
    model['image'] = '/image/cartoon-rgba-to-hex.png'
    return render_template(template_dir + 'template_rgba_to_hex_ar.html', model=model)


@Web_HexToDecimal_blueprint.route('/ar/roman-numerals-chart')
def roman_numerals_chart():
    model = get_default_model()
    model['url'] = '/ar/roman-numerals-chart'
    model['enUrl'] = '/roman-numerals-chart'
    model['headerTitle'] = 'الجدول الأرقام الرومانية 1-1000 - الترميز. أدوات'
    model['bodyTitle'] = 'الرومانية مقارنة جدول الأرقام 1-1000'
    model['description'] = 'جدول مقارنة رقمي روماني كامل من 1 إلى 1000.'
    model['keywords'] = 'أرقام رومانية ، أرقام رومانية'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_roman_numerals_chart_ar.html', model=model)


@Web_HexToDecimal_blueprint.route('/ar/roman-numerals-to-numbers')
def roman_numerals_to_numbers():
    model = get_default_model()
    model['url'] = '/ar/roman-numerals-to-numbers'
    model['enUrl'] = '/roman-numerals-to-numbers'
    model['headerTitle'] = 'الأرقام الرومانية إلى الأرقام العربية أداة التحويل عبر الإنترنت  - Coding.Tools'
    model['bodyTitle'] = 'الأرقام الرومانية إلى أداة التحويل الرقمي عبر الإنترنت'
    model['description'] = 'تساعدك هذه الأرقام الرومانية على الإنترنت على أداة تحويل الأرقام العربية على تحويل الأرقام الرومانية إلى الأرقام العربية أدخل الرقم الروماني وسيتم عرض الرقم العربي في مربع النتائج.'
    model['keywords'] = 'تتحول الأرقام الرومانية إلى الأرقام العربية'
    model['image'] = '/image/cartoon-roman-numerals-to-numbers.png'
    return render_template(template_dir + 'template_roman_numerals_to_numbers_ar.html', model=model)


@Web_HexToDecimal_blueprint.route('/ar/numbers-to-roman-numerals')
def numbers_to_roman_numerals():
    model = get_default_model()
    model['url'] = '/ar/numbers-to-roman-numerals'
    model['enUrl'] = '/numbers-to-roman-numerals'
    model['headerTitle'] = 'العربية الرقمية إلى الرومانية الرقمية على الإنترنت أداة التحويل - الترميز. أدوات'
    model['bodyTitle'] = 'العربية الرقمية إلى الرومانية الرقمية على الإنترنت أداة التحويل'
    model['description'] = 'تساعدك هذه الأرقام العربية عبر الإنترنت على أداة تحويل الأرقام الرومانية على تحويل الأرقام العربية إلى الأرقام الرومانية ، أدخل الرقم العربي وسيتم عرض الأرقام الرومانية في مربع النتائج.'
    model['keywords'] = 'الأرقام العربية تتحول إلى الأرقام الرومانية'
    model['image'] = '/image/cartoon-numbers-to-roman-numerals.png'
    return render_template(template_dir + 'template_numbers_to_roman_numerals_ar.html', model=model)
