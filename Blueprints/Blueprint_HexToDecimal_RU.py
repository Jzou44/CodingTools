from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_HexToDecimal_blueprint = Blueprint('Web_HexToDecimal_blueprint_RU', __name__)
template_dir = 'HexToDecimal/ru/'

def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'ru'
    return model

@Web_HexToDecimal_blueprint.route('/ru/hex-to-decimal')
def hex_to_decimal():
    model = get_default_model()
    model['url'] = '/ru/hex-to-decimal'
    model['enUrl'] = '/hex-to-decimal'
    model['headerTitle'] = 'Онлайн-конвертер шестнадцатеричного в десятичное  - Coding.Tools'
    model['bodyTitle'] = 'Онлайн-конвертер шестнадцатеричного в десятичное'
    model['description'] = 'Этот онлайн-инструмент преобразования шестнадцатеричного в десятичное поможет вам преобразовать шестнадцатеричное число в десятичное число.'
    model['keywords'] = 'От шестнадцатеричного до десятичного, от шестнадцатеричного до десятичного'
    model['image'] = '/image/cartoon-hex-to-decimal.png'
    return render_template(template_dir + 'template_hex_to_decimal_ru.html', model=model)


@Web_HexToDecimal_blueprint.route('/ru/decimal-to-hex')
def decimal_to_hex():
    model = get_default_model()
    model['url'] = '/ru/decimal-to-hex'
    model['enUrl'] = '/decimal-to-hex'
    model['headerTitle'] = 'Онлайн-конвертация десятичных в шестнадцатеричные  - Coding.Tools'
    model['bodyTitle'] = 'Онлайн-конвертация десятичных в шестнадцатеричные'
    model['description'] = 'Этот онлайн-инструмент для преобразования десятичных чисел в шестнадцатеричные помогает преобразовать десятичное число в шестнадцатеричное'
    model['keywords'] = 'Десятичное в шестнадцатеричное, десятичное в шестнадцатеричное'
    model['image'] = '/image/cartoon-decimal-to-hex.png'
    return render_template(template_dir + 'template_decimal_to_hex_ru.html', model=model)


@Web_HexToDecimal_blueprint.route('/ru/octal-to-decimal')
def octal_to_decimal():
    model = get_default_model()
    model['url'] = '/ru/octal-to-decimal'
    model['enUrl'] = '/octal-to-decimal'
    model['headerTitle'] = 'Преобразование из восьмеричного числа в десятичное онлайн  - Coding.Tools'
    model['bodyTitle'] = 'Восьмеричное в десятичное онлайн-инструмент конвертации'
    model['description'] = 'Этот онлайн-инструмент преобразования восьмеричного числа в десятичное поможет вам преобразовать восьмеричное число в десятичное число.'
    model['keywords'] = 'Восьмеричное в десятичное, восьмеричное в десятичное'
    model['image'] = '/image/octal_to_decimal.png'
    return render_template(template_dir + 'template_octal_to_decimal_ru.html', model=model)


@Web_HexToDecimal_blueprint.route('/ru/decimal-to-octal')
def decimal_to_octal():
    model = get_default_model()
    model['url'] = '/ru/decimal-to-octal'
    model['enUrl'] = '/decimal-to-octal'
    model['headerTitle'] = 'Онлайн-конвертер десятичных в восьмеричные  - Coding.Tools'
    model['bodyTitle'] = 'Десятичное в восьмеричное онлайн-конвертер'
    model['description'] = 'Этот онлайн-инструмент для преобразования десятичных чисел в восьмеричные поможет вам преобразовать десятичное число в восьмеричное число.'
    model['keywords'] = 'Десятичный в восьмеричный, десятичный в восьмеричный'
    model['image'] = '/image/cartoon-decimal-to-octal.png'
    return render_template(template_dir + 'template_decimal_to_octal_ru.html', model=model)


@Web_HexToDecimal_blueprint.route('/ru/binary-to-decimal')
def binary_to_decimal():
    model = get_default_model()
    model['url'] = '/ru/binary-to-decimal'
    model['enUrl'] = '/binary-to-decimal'
    model['headerTitle'] = 'Двоичный в десятичный онлайн-конвертер'
    model['bodyTitle'] = 'Двоичный в десятичный онлайн-инструмент для конвертации'
    model['description'] = 'Этот онлайн-инструмент преобразования двоичных данных в десятичные помогает преобразовать восьмеричное число в десятичное число.'
    model['keywords'] = 'Двоичные в десятичные, двоичные в десятичные'
    model['image'] = '/image/cartoon-decimal-to-binary.png'
    return render_template(template_dir + 'template_binary_to_decimal_ru.html', model=model)


@Web_HexToDecimal_blueprint.route('/ru/decimal-to-binary')
def decimal_to_binary():
    model = get_default_model()
    model['url'] = '/ru/decimal-to-binary'
    model['enUrl'] = '/decimal-to-binary'
    model['headerTitle'] = 'Десятичное в двоичное средство онлайн-конвертации  - Coding.Tools'
    model['bodyTitle'] = 'Десятичное в двоичное средство онлайн-конвертации'
    model['description'] = 'Этот онлайн-инструмент для преобразования десятичных чисел в двоичные поможет вам преобразовать десятичное число в двоичное число.'
    model['keywords'] = 'Десятичный в двоичный, десятичный в двоичный'
    model['image'] = '/image/cartoon-decimal-to-binary.png'
    return render_template(template_dir + 'template_decimal_to_binary_ru.html', model=model)


@Web_HexToDecimal_blueprint.route('/ru/ascii-table')
def ascii_table():
    model = get_default_model()
    model['url'] = '/ru/ascii-table'
    model['enUrl'] = '/ascii-table'
    model['headerTitle'] = 'Таблица поиска ASCII  - Coding.Tools'
    model['bodyTitle'] = 'Таблица поиска ASCII'
    model['description'] = 'Полная таблица поиска ASCII (256 бит), включая управляющие символы ASCII, символы ASCII и расширенные символы ASCII.'
    model['keywords'] = 'Таблица ASCII, таблица расширений ASCII'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_ascii_table_ru.html', model=model)


@Web_HexToDecimal_blueprint.route('/ru/hex-to-ascii')
def hex_to_ascii():
    model = get_default_model()
    model['url'] = '/ru/hex-to-ascii'
    model['enUrl'] = '/hex-to-ascii'
    model['headerTitle'] = 'Шестнадцатеричный в ASCII строку онлайн-инструмент для конвертации  - Coding.Tools'
    model['bodyTitle'] = 'Инструмент онлайн преобразования шестнадцатеричной строки в ASCII'
    model['description'] = 'Этот интерактивный инструмент преобразования шестнадцатеричной строки в ASCII помогает преобразовать шестнадцатеричный массив в строку ASCII'
    model['keywords'] = 'Шестнадцатеричный ASCII, шестнадцатеричный ASCII'
    model['image'] = '/image/cartoon-hex-to-ascii.png'
    return render_template(template_dir + 'template_hex_to_ascii_ru.html', model=model)


@Web_HexToDecimal_blueprint.route('/ru/ascii-to-hex')
def ascii_to_hex():
    model = get_default_model()
    model['url'] = '/ru/ascii-to-hex'
    model['enUrl'] = '/ascii-to-hex'
    model['headerTitle'] = 'ASCII строка в шестнадцатеричный инструмент онлайн-конвертации  - Coding.Tools'
    model['bodyTitle'] = 'ASCII-строка в шестнадцатеричный онлайн-инструмент для конвертации'
    model['description'] = 'Этот онлайн-инструмент для преобразования строки ASCII в шестнадцатеричный формат поможет вам преобразовать строку ASCII в шестнадцатеричный массив.'
    model['keywords'] = 'ASCII в шестнадцатеричный, ASCII в шестнадцатеричный'
    model['image'] = '/image/cartoon-ascii-to-hex.png'
    return render_template(template_dir + 'template_ascii_to_hex_ru.html', model=model)


@Web_HexToDecimal_blueprint.route('/ru/fraction-to-decimal')
def fraction_to_decimal():
    model = get_default_model()
    model['url'] = '/ru/fraction-to-decimal'
    model['enUrl'] = '/fraction-to-decimal'
    model['headerTitle'] = 'Счет в десятичный онлайн-инструмент конвертации  - Coding.Tools'
    model['bodyTitle'] = 'Счет в десятичном онлайн-инструмент конвертации'
    model['description'] = 'Этот онлайн-инструмент для преобразования счета в десятичную поможет вам преобразовать счет в десятичную форму. В поле результатов отображаются числитель и знаменатель.'
    model['keywords'] = 'Дробно-десятичный, дробно-десятичный'
    model['image'] = '/image/cartoon-fraction-to-decimal.png'
    return render_template(template_dir + 'template_fraction_to_decimal_ru.html', model=model)


@Web_HexToDecimal_blueprint.route('/ru/decimal-to-fraction')
def decimal_to_fraction():
    model = get_default_model()
    model['url'] = '/ru/decimal-to-fraction'
    model['enUrl'] = '/decimal-to-fraction'
    model['headerTitle'] = 'Десятичное число, чтобы забить онлайн инструмент конвертации  - Coding.Tools'
    model['bodyTitle'] = 'Десятичное число, чтобы выиграть онлайн инструмент преобразования'
    model['description'] = 'Этот интерактивный инструмент преобразования десятичной дроби в баллы поможет вам преобразовать десятичную дробь в дробную. Введите десятичную дробь, и результат будет отображаться в окне результатов.'
    model['keywords'] = 'Десятичное в дробное, дробное в дробное'
    model['image'] = '/image/cartoon-decimal-to-fraction.png'
    return render_template(template_dir + 'template_decimal_to_fraction_ru.html', model=model)


@Web_HexToDecimal_blueprint.route('/ru/percent-to-decimal')
def percent_to_decimal():
    model = get_default_model()
    model['url'] = '/ru/percent-to-decimal'
    model['enUrl'] = '/percent-to-decimal'
    model['headerTitle'] = 'Процент к десятичной онлайн конвертации  - Coding.Tools'
    model['bodyTitle'] = 'Процент к десятичной онлайн-конвертер'
    model['description'] = 'Этот онлайн-инструмент для перевода процентов в десятичные дроби поможет вам преобразовать процент в десятичную систему.'
    model['keywords'] = 'Процент к десятичной, процент к десятичной'
    model['image'] = '/image/cartoon-percent-to-decimal.png'
    return render_template(template_dir + 'template_percent_to_decimal_ru.html', model=model)


@Web_HexToDecimal_blueprint.route('/ru/decimal-to-percent')
def decimal_to_percent():
    model = get_default_model()
    model['url'] = '/ru/decimal-to-percent'
    model['enUrl'] = '/decimal-to-percent'
    model['headerTitle'] = 'Онлайн-инструмент для преобразования десятичных чисел в проценты  - Coding.Tools'
    model['bodyTitle'] = 'Десятичное в процентный инструмент онлайн конвертации'
    model['description'] = 'Этот онлайн-инструмент для преобразования десятичных чисел в процентные значения поможет вам преобразовать десятичные числа в процентные. Введите десятичное число, и процент будет отображаться в окне результатов.'
    model['keywords'] = 'Десятичное в проценты, дробное в процентах'
    model['image'] = '/image/cartoon-decimal-to-percent.png'
    return render_template(template_dir + 'template_decimal_to_percent_ru.html', model=model)


@Web_HexToDecimal_blueprint.route('/ru/percent-to-fraction')
def percent_to_fraction():
    model = get_default_model()
    model['url'] = '/ru/percent-to-fraction'
    model['enUrl'] = '/percent-to-fraction'
    model['headerTitle'] = 'Процент для оценки инструмента онлайн-конвертации  - Coding.Tools'
    model['bodyTitle'] = 'Процент для оценки инструмента онлайн-конвертации'
    model['description'] = 'Этот онлайн-инструмент для конвертации процентов в баллы поможет вам конвертировать проценты в баллы.Введите процент, и оценка будет отображаться в окне результатов.'
    model['keywords'] = 'Процент к доле, процент к доле'
    model['image'] = '/image/cartoon-percent-to-fraction.png'
    return render_template(template_dir + 'template_percent_to_fraction_ru.html', model=model)


@Web_HexToDecimal_blueprint.route('/ru/fraction-to-percent')
def fraction_to_percent():
    model = get_default_model()
    model['url'] = '/ru/fraction-to-percent'
    model['enUrl'] = '/fraction-to-percent'
    model['headerTitle'] = 'Оценка онлайн в процентах инструмент конвертации  - Coding.Tools'
    model['bodyTitle'] = 'Инструмент конвертации баллов в процент'
    model['description'] = 'Этот онлайн-инструмент для конвертации баллов в проценты поможет вам конвертировать баллы в проценты, введите числитель и знаменатель, и проценты будут отображены в окне результатов.'
    model['keywords'] = 'Фракция в процентах, дробный процент'
    model['image'] = '/image/cartoon-fraction-to-percent.png'
    return render_template(template_dir + 'template_fraction_to_percent_ru.html', model=model)


@Web_HexToDecimal_blueprint.route('/ru/hex-to-rgb')
def hex_to_rgb():
    model = get_default_model()
    model['url'] = '/ru/hex-to-rgb'
    model['enUrl'] = '/hex-to-rgb'
    model['headerTitle'] = 'Hex Color в RGB Color Онлайн инструмент для преобразования  - Coding.Tools'
    model['bodyTitle'] = 'Hex цвет в RGB цвет онлайн-инструмент преобразования'
    model['description'] = 'Этот онлайн-инструмент для преобразования шестнадцатеричного цвета в цвет RGB поможет вам преобразовать шестнадцатеричный цвет в цвет RGB и проверить выбранный цвет в режиме реального времени.'
    model['keywords'] = 'От шестнадцатеричного до RGB, От шестнадцатеричного до цветного RGB'
    model['image'] = '/image/cartoon-hex-to-rgb.png'
    return render_template(template_dir + 'template_hex_to_rgb_ru.html', model=model)


@Web_HexToDecimal_blueprint.route('/ru/rgb-to-hex')
def rgb_to_hex():
    model = get_default_model()
    model['url'] = '/ru/rgb-to-hex'
    model['enUrl'] = '/rgb-to-hex'
    model['headerTitle'] = 'RGB Color в Hex Color Онлайн инструмент для преобразования  - Coding.Tools'
    model['bodyTitle'] = 'RGB цвет в Hex цвет инструмент для онлайн-конвертации'
    model['description'] = 'Этот онлайн-инструмент преобразования цветов RGB в шестнадцатеричный цвет поможет вам преобразовать цвет RGB в шестнадцатеричный цвет и проверить выбранный цвет в режиме реального времени.'
    model['keywords'] = 'RGB в Hex, RGB цвет в Hex color'
    model['image'] = '/image/cartoon-rgb-to-hex.png'
    return render_template(template_dir + 'template_rgb_to_hex_ru.html', model=model)


@Web_HexToDecimal_blueprint.route('/ru/hex-to-rgba')
def hex_to_rgba():
    model = get_default_model()
    model['url'] = '/ru/hex-to-rgba'
    model['enUrl'] = '/hex-to-rgba'
    model['headerTitle'] = 'Hex Color в RGBA Color Онлайн инструмент преобразования  - Coding.Tools'
    model['bodyTitle'] = 'Инструмент для преобразования цвета из шестнадцатеричного цвета в RGBA'
    model['description'] = 'Этот онлайн-инструмент для преобразования цвета шестнадцатеричного цвета в RGBA поможет вам преобразовать шестнадцатеричный цвет в цвет RGBA (включая прозрачность и прозрачность) и протестировать выбранный цвет в режиме реального времени.'
    model['keywords'] = 'Шестнадцатеричный цвет к RGBA, шестнадцатеричный цвет к цвету RGBA'
    model['image'] = '/image/cartoon-hex-to-rgba.png'
    return render_template(template_dir + 'template_hex_to_rgba_ru.html', model=model)


@Web_HexToDecimal_blueprint.route('/ru/rgba-to-hex')
def rgba_to_hex():
    model = get_default_model()
    model['url'] = '/ru/rgba-to-hex'
    model['enUrl'] = '/rgba-to-hex'
    model['headerTitle'] = 'RGBA - инструмент для преобразования цветов в шестнадцатеричные цвета  - Coding.Tools'
    model['bodyTitle'] = 'RGBA цвет в Hex Color инструмент для онлайн-конвертации'
    model['description'] = 'Этот интерактивный инструмент преобразования цвета RGBA в шестнадцатеричный цвет помогает преобразовать цвет RGBA (включая прозрачность и непрозрачность) в шестнадцатеричный цвет и проверить выбранный цвет в режиме реального времени.'
    model['keywords'] = 'RGBA в Hex, RGBA в цвет Hex'
    model['image'] = '/image/cartoon-rgba-to-hex.png'
    return render_template(template_dir + 'template_rgba_to_hex_ru.html', model=model)


@Web_HexToDecimal_blueprint.route('/ru/roman-numerals-chart')
def roman_numerals_chart():
    model = get_default_model()
    model['url'] = '/ru/roman-numerals-chart'
    model['enUrl'] = '/roman-numerals-chart'
    model['headerTitle'] = 'Таблица римских цифр 1-1000  - Coding.Tools'
    model['bodyTitle'] = 'Сравнительная таблица римских цифр 1-1000'
    model['description'] = 'Полная таблица сравнения римских цифр от 1 до 1000.'
    model['keywords'] = 'Римские цифры Chart, Римские цифры'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_roman_numerals_chart_ru.html', model=model)


@Web_HexToDecimal_blueprint.route('/ru/roman-numerals-to-numbers')
def roman_numerals_to_numbers():
    model = get_default_model()
    model['url'] = '/ru/roman-numerals-to-numbers'
    model['enUrl'] = '/roman-numerals-to-numbers'
    model['headerTitle'] = 'Онлайн-конвертер римских цифр в арабские цифры  - Coding.Tools'
    model['bodyTitle'] = 'Цифровое онлайн-преобразование римских цифр в арабские'
    model['description'] = 'Этот интерактивный инструмент преобразования римских цифр в арабские цифры поможет вам преобразовать римские цифры в арабские цифры, введите римские цифры, и арабское число отобразится в окне результатов.'
    model['keywords'] = 'Римские цифры превращаются в арабские цифры'
    model['image'] = '/image/cartoon-roman-numerals-to-numbers.png'
    return render_template(template_dir + 'template_roman_numerals_to_numbers_ru.html', model=model)


@Web_HexToDecimal_blueprint.route('/ru/numbers-to-roman-numerals')
def numbers_to_roman_numerals():
    model = get_default_model()
    model['url'] = '/ru/numbers-to-roman-numerals'
    model['enUrl'] = '/numbers-to-roman-numerals'
    model['headerTitle'] = 'Арабский цифровой в римский цифровой онлайн-инструмент для преобразования  - Coding.Tools'
    model['bodyTitle'] = 'Арабский цифровой в римский цифровой онлайн-инструмент преобразования'
    model['description'] = 'Этот интерактивный инструмент преобразования арабских цифр в римские цифры поможет вам преобразовать арабские цифры в римские, введите арабское число, и римское число будет отображаться в окне результатов.'
    model['keywords'] = 'Арабские цифры превращаются в римские цифры'
    model['image'] = '/image/cartoon-numbers-to-roman-numerals.png'
    return render_template(template_dir + 'template_numbers_to_roman_numerals_ru.html', model=model)
