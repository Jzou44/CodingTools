from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_JsonFormatter_blueprint = Blueprint('Web_JsonFormatter_blueprint_IT', __name__)
template_dir = 'JsonFormatter/it/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'it'
    return model


@Web_JsonFormatter_blueprint.route('/it/json-formatter', methods=['GET', 'POST'])
def json_formatter():
    model = get_default_model()
    model['url'] = '/it/json-formatter'
    model['enUrl'] = '/json-formatter'
    model['headerTitle'] = 'Strumento online di formattazione JSON  - Coding.Tools'
    model['bodyTitle'] = 'Strumento di formattazione JSON online'
    model['description'] = 'Questo strumento di formattazione JSON online può aiutarti a formattare stringhe JSON confuse in stringhe JSON leggibili.'
    model['keywords'] = 'Formattatore JSON, formattazione JSON'
    model['image'] = '/image/comic-json-formatter.png'
    return render_template(template_dir + 'template_json_formatter_it.html', model=model)


@Web_JsonFormatter_blueprint.route('/it/json-minifier', methods=['GET', 'POST'])
def json_minifier():
    model = get_default_model()
    model['url'] = '/it/json-minifier'
    model['enUrl'] = '/json-minifier'
    model['headerTitle'] = 'Strumento di compressione online JSON  - Coding.Tools'
    model['bodyTitle'] = 'Strumento di compressione online JSON'
    model['description'] = 'Questo strumento online di compressione JSON ti aiuta a comprimere le stringhe JSON originali, risparmiando spazio per un trasferimento più rapido sulla rete.'
    model['keywords'] = 'Minificatore Json, compressione JSON'
    model['image'] = '/image/comic-json-minifier.png'
    return render_template(template_dir + 'template_json_minifier_it.html', model=model)


@Web_JsonFormatter_blueprint.route('/it/xml-formatter', methods=['GET', 'POST'])
def xml_formatter():
    model = get_default_model()
    model['url'] = '/it/xml-formatter'
    model['enUrl'] = '/xml-formatter'
    model['headerTitle'] = 'Strumento online di formattazione XML  - Coding.Tools'
    model['bodyTitle'] = 'Strumento online di formattazione XML'
    model['description'] = 'Questo strumento di formattazione XML online può aiutarti a formattare stringhe XML confusionarie in stringhe XML leggibili.'
    model['keywords'] = 'Formattatore Xml, formattazione XML'
    model['image'] = '/image/comic-xml-formatter.png'
    return render_template(template_dir + 'template_xml_formatter_it.html', model=model)


@Web_JsonFormatter_blueprint.route('/it/xml-minifier', methods=['GET', 'POST'])
def xml_minifier():
    model = get_default_model()
    model['url'] = '/it/xml-minifier'
    model['enUrl'] = '/xml-minifier'
    model['headerTitle'] = 'Strumento online per la compressione XML  - Coding.Tools'
    model['bodyTitle'] = 'Strumento online di compressione XML'
    model['description'] = 'Questo strumento online di compressione XML ti aiuta a comprimere stringhe XML primarie, risparmiando spazio per un trasferimento più rapido sulla rete.'
    model['keywords'] = 'Minificatore Xml, compressione XML'
    model['image'] = '/image/comic-xml-minifier.png'
    return render_template(template_dir + 'template_xml_minifier_it.html', model=model)


@Web_JsonFormatter_blueprint.route('/it/json-to-xml', methods=['GET', 'POST'])
def json_to_xml():
    model = get_default_model()
    model['url'] = '/it/json-to-xml'
    model['enUrl'] = '/json-to-xml'
    model['headerTitle'] = 'Strumento online da JSON a XML  - Coding.Tools'
    model['bodyTitle'] = 'Strumento online da JSON a XML'
    model['description'] = 'Questo strumento online da JSON a XML può aiutarti a convertire stringhe di dati in formato JSON in stringhe di dati in formato XML.'
    model['keywords'] = 'Da JSON a XML, da JSON a XML'
    model['image'] = '/image/comic-json-to-xml.png'
    return render_template(template_dir + 'template_json_to_xml_it.html', model=model)


@Web_JsonFormatter_blueprint.route('/it/xml-to-json', methods=['GET', 'POST'])
def xml_to_json():
    model = get_default_model()
    model['url'] = '/it/xml-to-json'
    model['enUrl'] = '/xml-to-json'
    model['headerTitle'] = 'Strumento online da XML a JSON  - Coding.Tools'
    model['bodyTitle'] = 'Strumento online da XML a JSON'
    model['description'] = 'Questo strumento online XML to JSON può aiutarti a convertire stringhe di dati in formato XML in stringhe di dati in formato JSON.'
    model['keywords'] = 'Da XML a JSON, da XML a JSON'
    model['image'] = '/image/comic-xml-to-json.png'
    return render_template(template_dir + 'template_xml_to_json_it.html', model=model)


@Web_JsonFormatter_blueprint.route('/it/html-beautifier', methods=['GET', 'POST'])
def html_beautifier():
    model = get_default_model()
    model['url'] = '/it/html-beautifier'
    model['enUrl'] = '/html-beautifier'
    model['headerTitle'] = 'Strumento online di formattazione HTML  - Coding.Tools'
    model['bodyTitle'] = 'Strumento online di formattazione HTML'
    model['description'] = 'Questo strumento di formattazione HTML online può aiutarti a formattare file HTML confusi in file HTML leggibili.'
    model['keywords'] = 'Formattatore HTML, beautifier html, formattazione HTML'
    model['image'] = '/image/comic-html-beautifier.png'
    return render_template(template_dir + 'template_html_beautifier_it.html', model=model)


@Web_JsonFormatter_blueprint.route('/it/html-minifier', methods=['GET', 'POST'])
def html_minifier():
    model = get_default_model()
    model['url'] = '/it/html-minifier'
    model['enUrl'] = '/html-minifier'
    model['headerTitle'] = 'Strumento online di compressione HTML  - Coding.Tools'
    model['bodyTitle'] = 'Strumento online di compressione HTML'
    model['description'] = 'Questo strumento online di compressione HTML ti aiuta a comprimere i file HTML originali, risparmiando spazio per un trasferimento più rapido sulla rete.'
    model['keywords'] = 'Minificatore Html, compressione HTML'
    model['image'] = '/image/comic-html-minifier.png'
    return render_template(template_dir + 'template_html_minifier_it.html', model=model)


@Web_JsonFormatter_blueprint.route('/it/javascript-beautifier', methods=['GET', 'POST'])
def javascript_beautifier():
    model = get_default_model()
    model['url'] = '/it/javascript-beautifier'
    model['enUrl'] = '/javascript-beautifier'
    model['headerTitle'] = 'Strumento di formattazione Javascript online  - Coding.Tools'
    model['bodyTitle'] = 'Strumento di formattazione Javascript online'
    model['description'] = 'Questo strumento di formattazione Javascript online può aiutarti a formattare file Javascript confusi in file Javascript leggibili.'
    model['keywords'] = 'JavaScript formattatore, abbellitore javascript, formattazione Javascript'
    model['image'] = '/image/comic-javascript-beautifier.png'
    return render_template(template_dir + 'template_javascript_beautifier_it.html', model=model)


@Web_JsonFormatter_blueprint.route('/it/javascript-minifier', methods=['GET', 'POST'])
def javascript_minifier():
    model = get_default_model()
    model['url'] = '/it/javascript-minifier'
    model['enUrl'] = '/javascript-minifier'
    model['headerTitle'] = 'Strumento online di compressione Javascript  - Coding.Tools'
    model['bodyTitle'] = 'Strumento online di compressione Javascript'
    model['description'] = 'Questo strumento online di compressione Javascript ti aiuta a comprimere i tuoi file Javascript originali, risparmiando spazio per un trasferimento più veloce sulla rete.'
    model['keywords'] = 'Minificatore Javascript, compressione Javascript'
    model['image'] = '/image/comic-javascript-minifier.png'
    return render_template(template_dir + 'template_javascript_minifier_it.html', model=model)


@Web_JsonFormatter_blueprint.route('/it/css-beautifier', methods=['GET', 'POST'])
def css_beautifier():
    model = get_default_model()
    model['url'] = '/it/css-beautifier'
    model['enUrl'] = '/css-beautifier'
    model['headerTitle'] = 'Strumento online di formattazione CSS  - Coding.Tools'
    model['bodyTitle'] = 'Strumento di formattazione CSS online'
    model['description'] = 'Questo strumento di formattazione CSS online può aiutarti a formattare file CSS confusi in file CSS leggibili.'
    model['keywords'] = 'Formatterizzatore Css, abbellimento css, formattazione CSS'
    model['image'] = '/image/comic-css-beautifier.png'
    return render_template(template_dir + 'template_css_beautifier_it.html', model=model)


@Web_JsonFormatter_blueprint.route('/it/css-minifier', methods=['GET', 'POST'])
def css_minifier():
    model = get_default_model()
    model['url'] = '/it/css-minifier'
    model['enUrl'] = '/css-minifier'
    model['headerTitle'] = 'Strumento online di compressione CSS  - Coding.Tools'
    model['bodyTitle'] = 'Strumento online di compressione CSS'
    model['description'] = 'Questo strumento online di compressione CSS ti aiuta a comprimere i tuoi file CSS originali, risparmiando spazio per un trasferimento più veloce sulla rete.'
    model['keywords'] = 'Minificatore Css, compressione CSS'
    model['image'] = '/image/comic-css-minifier.png'
    return render_template(template_dir + 'template_css_minifier_it.html', model=model)
