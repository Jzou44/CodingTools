from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_JsonFormatter_blueprint = Blueprint('Web_JsonFormatter_blueprint_RU', __name__)
template_dir = 'JsonFormatter/ru/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'ru'
    return model


@Web_JsonFormatter_blueprint.route('/ru/json-formatter', methods=['GET', 'POST'])
def json_formatter():
    model = get_default_model()
    model['url'] = '/ru/json-formatter'
    model['enUrl'] = '/json-formatter'
    model['headerTitle'] = 'JSON форматирование онлайн инструмент  - Coding.Tools'
    model['bodyTitle'] = 'JSON форматирование онлайн инструмент'
    model['description'] = 'Этот онлайн-инструмент форматирования JSON может помочь вам отформатировать запутанные строки JSON в читаемые строки JSON.'
    model['keywords'] = 'JSON форматер, JSON форматирование'
    model['image'] = '/image/comic-json-formatter.png'
    return render_template(template_dir + 'template_json_formatter_ru.html', model=model)


@Web_JsonFormatter_blueprint.route('/ru/json-minifier', methods=['GET', 'POST'])
def json_minifier():
    model = get_default_model()
    model['url'] = '/ru/json-minifier'
    model['enUrl'] = '/json-minifier'
    model['headerTitle'] = 'JSON сжатие онлайн инструмент  - Coding.Tools'
    model['bodyTitle'] = 'JSON сжатие онлайн инструмент'
    model['description'] = 'Этот онлайн-инструмент сжатия JSON поможет вам сжать исходные строки JSON, сэкономив место для более быстрой передачи по сети.'
    model['keywords'] = 'JSON Minifier, JSON сжатие'
    model['image'] = '/image/comic-json-minifier.png'
    return render_template(template_dir + 'template_json_minifier_ru.html', model=model)


@Web_JsonFormatter_blueprint.route('/ru/xml-formatter', methods=['GET', 'POST'])
def xml_formatter():
    model = get_default_model()
    model['url'] = '/ru/xml-formatter'
    model['enUrl'] = '/xml-formatter'
    model['headerTitle'] = 'XML форматирование онлайн инструмент  - Coding.Tools'
    model['bodyTitle'] = 'XML форматирование онлайн инструмент'
    model['description'] = 'Этот онлайн-инструмент форматирования XML может помочь вам отформатировать запутанные строки XML в удобочитаемые строки XML.'
    model['keywords'] = 'Форматирование XML, форматирование XML'
    model['image'] = '/image/comic-xml-formatter.png'
    return render_template(template_dir + 'template_xml_formatter_ru.html', model=model)


@Web_JsonFormatter_blueprint.route('/ru/xml-minifier', methods=['GET', 'POST'])
def xml_minifier():
    model = get_default_model()
    model['url'] = '/ru/xml-minifier'
    model['enUrl'] = '/xml-minifier'
    model['headerTitle'] = 'Онлайн-инструмент для сжатия XML  - Coding.Tools'
    model['bodyTitle'] = 'XML инструмент сжатия онлайн'
    model['description'] = 'Этот онлайн-инструмент для сжатия XML помогает вам сжимать необработанные строки XML, экономя место для быстрой передачи по сети.'
    model['keywords'] = 'Xml minifier, сжатие XML'
    model['image'] = '/image/comic-xml-minifier.png'
    return render_template(template_dir + 'template_xml_minifier_ru.html', model=model)


@Web_JsonFormatter_blueprint.route('/ru/json-to-xml', methods=['GET', 'POST'])
def json_to_xml():
    model = get_default_model()
    model['url'] = '/ru/json-to-xml'
    model['enUrl'] = '/json-to-xml'
    model['headerTitle'] = 'Онлайн инструмент JSON to XML  - Coding.Tools'
    model['bodyTitle'] = 'JSON в XML онлайн инструмент'
    model['description'] = 'Этот онлайн-инструмент JSON to XML может помочь вам преобразовать строки данных в формате JSON в строки данных в формате XML.'
    model['keywords'] = 'JSON в XML, JSON в XML'
    model['image'] = '/image/comic-json-to-xml.png'
    return render_template(template_dir + 'template_json_to_xml_ru.html', model=model)


@Web_JsonFormatter_blueprint.route('/ru/xml-to-json', methods=['GET', 'POST'])
def xml_to_json():
    model = get_default_model()
    model['url'] = '/ru/xml-to-json'
    model['enUrl'] = '/xml-to-json'
    model['headerTitle'] = 'XML для JSON онлайн-инструмент  - Coding.Tools'
    model['bodyTitle'] = 'XML в JSON онлайн инструмент'
    model['description'] = 'Этот онлайн-инструмент XML в JSON может помочь вам преобразовать строки данных в формате XML в строки данных в формате JSON.'
    model['keywords'] = 'XML в JSON, XML в JSON'
    model['image'] = '/image/comic-xml-to-json.png'
    return render_template(template_dir + 'template_xml_to_json_ru.html', model=model)


@Web_JsonFormatter_blueprint.route('/ru/html-beautifier', methods=['GET', 'POST'])
def html_beautifier():
    model = get_default_model()
    model['url'] = '/ru/html-beautifier'
    model['enUrl'] = '/html-beautifier'
    model['headerTitle'] = 'Онлайн инструмент для форматирования HTML  - Coding.Tools'
    model['bodyTitle'] = 'HTML форматирование онлайн инструмент'
    model['description'] = 'Этот онлайн-инструмент форматирования HTML может помочь вам отформатировать запутанные HTML-файлы в удобочитаемые HTML-файлы.'
    model['keywords'] = 'HTML-форматер, HTML-формат, HTML-форматирование'
    model['image'] = '/image/comic-html-beautifier.png'
    return render_template(template_dir + 'template_html_beautifier_ru.html', model=model)


@Web_JsonFormatter_blueprint.route('/ru/html-minifier', methods=['GET', 'POST'])
def html_minifier():
    model = get_default_model()
    model['url'] = '/ru/html-minifier'
    model['enUrl'] = '/html-minifier'
    model['headerTitle'] = 'Онлайн-инструмент для сжатия HTML  - Coding.Tools'
    model['bodyTitle'] = 'HTML сжатие онлайн инструмент'
    model['description'] = 'Этот онлайн-инструмент сжатия HTML поможет вам сжать исходные файлы HTML, сэкономив место для более быстрой передачи по сети.'
    model['keywords'] = 'Html minifier, сжатие HTML'
    model['image'] = '/image/comic-html-minifier.png'
    return render_template(template_dir + 'template_html_minifier_ru.html', model=model)


@Web_JsonFormatter_blueprint.route('/ru/javascript-beautifier', methods=['GET', 'POST'])
def javascript_beautifier():
    model = get_default_model()
    model['url'] = '/ru/javascript-beautifier'
    model['enUrl'] = '/javascript-beautifier'
    model['headerTitle'] = 'Онлайн инструмент для форматирования Javascript  - Coding.Tools'
    model['bodyTitle'] = 'Онлайн инструмент для форматирования Javascript'
    model['description'] = 'Этот онлайн-инструмент форматирования Javascript может помочь вам отформатировать запутанные файлы Javascript в читаемые файлы Javascript.'
    model['keywords'] = 'Javascript форматер, Javascript Beautifier, Javascript форматирование'
    model['image'] = '/image/comic-javascript-beautifier.png'
    return render_template(template_dir + 'template_javascript_beautifier_ru.html', model=model)


@Web_JsonFormatter_blueprint.route('/ru/javascript-minifier', methods=['GET', 'POST'])
def javascript_minifier():
    model = get_default_model()
    model['url'] = '/ru/javascript-minifier'
    model['enUrl'] = '/javascript-minifier'
    model['headerTitle'] = 'Онлайн-инструмент для сжатия Javascript  - Coding.Tools'
    model['bodyTitle'] = 'Онлайн-инструмент для сжатия Javascript'
    model['description'] = 'Этот онлайн-инструмент сжатия Javascript поможет вам сжать исходные файлы Javascript, сэкономив место для более быстрой передачи по сети.'
    model['keywords'] = 'Javascript minifier, сжатие JavaScript'
    model['image'] = '/image/comic-javascript-minifier.png'
    return render_template(template_dir + 'template_javascript_minifier_ru.html', model=model)


@Web_JsonFormatter_blueprint.route('/ru/css-beautifier', methods=['GET', 'POST'])
def css_beautifier():
    model = get_default_model()
    model['url'] = '/ru/css-beautifier'
    model['enUrl'] = '/css-beautifier'
    model['headerTitle'] = 'CSS инструмент форматирования онлайн  - Coding.Tools'
    model['bodyTitle'] = 'CSS форматирование онлайн инструмент'
    model['description'] = 'Этот онлайн-инструмент форматирования CSS может помочь вам отформатировать запутанные CSS-файлы в удобочитаемые CSS-файлы.'
    model['keywords'] = 'Форматирование css, css beautifier, форматирование CSS'
    model['image'] = '/image/comic-css-beautifier.png'
    return render_template(template_dir + 'template_css_beautifier_ru.html', model=model)


@Web_JsonFormatter_blueprint.route('/ru/css-minifier', methods=['GET', 'POST'])
def css_minifier():
    model = get_default_model()
    model['url'] = '/ru/css-minifier'
    model['enUrl'] = '/css-minifier'
    model['headerTitle'] = 'CSS инструмент сжатия онлайн  - Coding.Tools'
    model['bodyTitle'] = 'CSS инструмент сжатия онлайн'
    model['description'] = 'Этот онлайн-инструмент для сжатия CSS поможет вам сжать исходные файлы CSS, сэкономив место для более быстрой передачи по сети.'
    model['keywords'] = 'CSS Minifier, CSS сжатие'
    model['image'] = '/image/comic-css-minifier.png'
    return render_template(template_dir + 'template_css_minifier_ru.html', model=model)
