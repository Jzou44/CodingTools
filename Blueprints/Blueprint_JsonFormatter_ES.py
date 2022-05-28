from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_JsonFormatter_blueprint = Blueprint('Web_JsonFormatter_blueprint_ES', __name__)
template_dir = 'JsonFormatter/es/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'es'
    return model


@Web_JsonFormatter_blueprint.route('/es/json-formatter', methods=['GET', 'POST'])
def json_formatter():
    model = get_default_model()
    model['url'] = '/es/json-formatter'
    model['enUrl'] = '/json-formatter'
    model['headerTitle'] = 'Herramienta en línea para formatear JSON  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta en línea de formato JSON'
    model['description'] = 'Esta herramienta de formato JSON en línea puede ayudarlo a formatear cadenas JSON confusas en cadenas JSON legibles.'
    model['keywords'] = 'Formateador Json, formateo JSON'
    model['image'] = '/image/comic-json-formatter.png'
    return render_template(template_dir + 'template_json_formatter_es.html', model=model)


@Web_JsonFormatter_blueprint.route('/es/json-minifier', methods=['GET', 'POST'])
def json_minifier():
    model = get_default_model()
    model['url'] = '/es/json-minifier'
    model['enUrl'] = '/json-minifier'
    model['headerTitle'] = 'Herramienta de compresión en línea JSON - Codificación.Herramientas'
    model['bodyTitle'] = 'Herramienta de compresión en línea JSON'
    model['description'] = 'Esta herramienta en línea de compresión JSON lo ayuda a comprimir las cadenas JSON originales, ahorrando espacio para una transferencia más rápida a través de la red.'
    model['keywords'] = 'Json minifier, compresión JSON'
    model['image'] = '/image/comic-json-minifier.png'
    return render_template(template_dir + 'template_json_minifier_es.html', model=model)


@Web_JsonFormatter_blueprint.route('/es/xml-formatter', methods=['GET', 'POST'])
def xml_formatter():
    model = get_default_model()
    model['url'] = '/es/xml-formatter'
    model['enUrl'] = '/xml-formatter'
    model['headerTitle'] = 'Herramienta de formato XML en línea - Codificación.Herramientas'
    model['bodyTitle'] = 'Herramienta de formato XML en línea'
    model['description'] = 'Esta herramienta de formato XML en línea puede ayudarlo a formatear cadenas XML confusas en cadenas XML legibles.'
    model['keywords'] = 'Formateador xml, formato XML'
    model['image'] = '/image/comic-xml-formatter.png'
    return render_template(template_dir + 'template_xml_formatter_es.html', model=model)


@Web_JsonFormatter_blueprint.route('/es/xml-minifier', methods=['GET', 'POST'])
def xml_minifier():
    model = get_default_model()
    model['url'] = '/es/xml-minifier'
    model['enUrl'] = '/xml-minifier'
    model['headerTitle'] = 'Herramienta de compresión XML en línea - Codificación.Herramientas'
    model['bodyTitle'] = 'Herramienta de compresión XML en línea'
    model['description'] = 'Esta herramienta en línea de compresión XML lo ayuda a comprimir cadenas XML sin procesar, ahorrando espacio para una transferencia más rápida en la red.'
    model['keywords'] = 'Minifier xml, compresión XML'
    model['image'] = '/image/comic-xml-minifier.png'
    return render_template(template_dir + 'template_xml_minifier_es.html', model=model)


@Web_JsonFormatter_blueprint.route('/es/json-to-xml', methods=['GET', 'POST'])
def json_to_xml():
    model = get_default_model()
    model['url'] = '/es/json-to-xml'
    model['enUrl'] = '/json-to-xml'
    model['headerTitle'] = 'Herramienta en línea de JSON a XML  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta en línea de JSON a XML'
    model['description'] = 'Esta herramienta en línea de JSON a XML puede ayudarlo a convertir cadenas de datos en formato JSON en cadenas de datos en formato XML.'
    model['keywords'] = 'Json a xml, JSON a XML'
    model['image'] = '/image/comic-json-to-xml.png'
    return render_template(template_dir + 'template_json_to_xml_es.html', model=model)


@Web_JsonFormatter_blueprint.route('/es/xml-to-json', methods=['GET', 'POST'])
def xml_to_json():
    model = get_default_model()
    model['url'] = '/es/xml-to-json'
    model['enUrl'] = '/xml-to-json'
    model['headerTitle'] = 'Herramienta en línea de XML a JSON  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta en línea de XML a JSON'
    model['description'] = 'Esta herramienta en línea de XML a JSON puede ayudarlo a convertir cadenas de datos en formato XML en cadenas de datos en formato JSON.'
    model['keywords'] = 'XML a JSON, xml a json'
    model['image'] = '/image/comic-xml-to-json.png'
    return render_template(template_dir + 'template_xml_to_json_es.html', model=model)


@Web_JsonFormatter_blueprint.route('/es/html-beautifier', methods=['GET', 'POST'])
def html_beautifier():
    model = get_default_model()
    model['url'] = '/es/html-beautifier'
    model['enUrl'] = '/html-beautifier'
    model['headerTitle'] = 'Herramienta de formato HTML en línea - Codificación.Herramientas'
    model['bodyTitle'] = 'Herramienta de formato HTML en línea'
    model['description'] = 'Esta herramienta de formato HTML en línea puede ayudarlo a formatear archivos HTML confusos en archivos HTML legibles.'
    model['keywords'] = 'Formateador HTML, embellecedor HTML, formato HTML'
    model['image'] = '/image/comic-html-beautifier.png'
    return render_template(template_dir + 'template_html_beautifier_es.html', model=model)


@Web_JsonFormatter_blueprint.route('/es/html-minifier', methods=['GET', 'POST'])
def html_minifier():
    model = get_default_model()
    model['url'] = '/es/html-minifier'
    model['enUrl'] = '/html-minifier'
    model['headerTitle'] = 'Herramienta de compresión HTML en línea - Codificación.Herramientas'
    model['bodyTitle'] = 'Herramienta de compresión HTML en línea'
    model['description'] = 'Esta herramienta en línea de compresión HTML lo ayuda a comprimir sus archivos HTML originales, ahorrando espacio para una transferencia más rápida a través de la red.'
    model['keywords'] = 'Minificador de HTML, compresión HTML'
    model['image'] = '/image/comic-html-minifier.png'
    return render_template(template_dir + 'template_html_minifier_es.html', model=model)


@Web_JsonFormatter_blueprint.route('/es/javascript-beautifier', methods=['GET', 'POST'])
def javascript_beautifier():
    model = get_default_model()
    model['url'] = '/es/javascript-beautifier'
    model['enUrl'] = '/javascript-beautifier'
    model['headerTitle'] = 'Herramienta de formateo de Javascript en línea  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta de formateo de Javascript en línea'
    model['description'] = 'Esta herramienta de formato Javascript en línea puede ayudarlo a formatear archivos Javascript confusos en archivos Javascript legibles.'
    model['keywords'] = 'Formateador de Javascript, embellecedor de JavaScript, formato de Javascript'
    model['image'] = '/image/comic-javascript-beautifier.png'
    return render_template(template_dir + 'template_javascript_beautifier_es.html', model=model)


@Web_JsonFormatter_blueprint.route('/es/javascript-minifier', methods=['GET', 'POST'])
def javascript_minifier():
    model = get_default_model()
    model['url'] = '/es/javascript-minifier'
    model['enUrl'] = '/javascript-minifier'
    model['headerTitle'] = 'Herramienta de compresión de Javascript en línea  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta de compresión de Javascript en línea'
    model['description'] = 'Esta herramienta en línea de compresión Javascript lo ayuda a comprimir sus archivos Javascript originales, ahorrando espacio para una transferencia más rápida a través de la red.'
    model['keywords'] = 'Javascript minificador, compresión Javascript'
    model['image'] = '/image/comic-javascript-minifier.png'
    return render_template(template_dir + 'template_javascript_minifier_es.html', model=model)


@Web_JsonFormatter_blueprint.route('/es/css-beautifier', methods=['GET', 'POST'])
def css_beautifier():
    model = get_default_model()
    model['url'] = '/es/css-beautifier'
    model['enUrl'] = '/css-beautifier'
    model['headerTitle'] = 'Herramienta de formato CSS en línea - Codificación.Herramientas'
    model['bodyTitle'] = 'Herramienta de formato CSS en línea'
    model['description'] = 'Esta herramienta de formato CSS en línea puede ayudarlo a formatear archivos CSS confusos en archivos CSS legibles.'
    model['keywords'] = 'Formateador CSS, embellecedor CSS, formato CSS'
    model['image'] = '/image/comic-css-beautifier.png'
    return render_template(template_dir + 'template_css_beautifier_es.html', model=model)


@Web_JsonFormatter_blueprint.route('/es/css-minifier', methods=['GET', 'POST'])
def css_minifier():
    model = get_default_model()
    model['url'] = '/es/css-minifier'
    model['enUrl'] = '/css-minifier'
    model['headerTitle'] = 'Herramienta de compresión de CSS en línea  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta de compresión de CSS en línea'
    model['description'] = 'Esta herramienta en línea de compresión CSS le ayuda a comprimir sus archivos CSS originales, ahorrando espacio para una transferencia más rápida a través de la red.'
    model['keywords'] = 'Minificador CSS, compresión CSS'
    model['image'] = '/image/comic-css-minifier.png'
    return render_template(template_dir + 'template_css_minifier_es.html', model=model)
