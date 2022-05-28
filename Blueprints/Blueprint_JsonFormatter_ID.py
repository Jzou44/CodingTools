from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_JsonFormatter_blueprint = Blueprint('Web_JsonFormatter_blueprint_ID', __name__)
template_dir = 'JsonFormatter/id/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'id'
    return model


@Web_JsonFormatter_blueprint.route('/id/json-formatter', methods=['GET', 'POST'])
def json_formatter():
    model = get_default_model()
    model['url'] = '/id/json-formatter'
    model['enUrl'] = '/json-formatter'
    model['headerTitle'] = 'Alat pemformatan online JSON  - Coding.Tools'
    model['bodyTitle'] = 'Alat format online JSON'
    model['description'] = 'Alat pemformatan JSON online ini dapat membantu Anda memformat string JSON yang membingungkan menjadi string JSON yang dapat dibaca.'
    model['keywords'] = 'Pemformat Json, pemformatan JSON'
    model['image'] = '/image/comic-json-formatter.png'
    return render_template(template_dir + 'template_json_formatter_id.html', model=model)


@Web_JsonFormatter_blueprint.route('/id/json-minifier', methods=['GET', 'POST'])
def json_minifier():
    model = get_default_model()
    model['url'] = '/id/json-minifier'
    model['enUrl'] = '/json-minifier'
    model['headerTitle'] = 'Alat online kompresi JSON  - Coding.Tools'
    model['bodyTitle'] = 'Alat online kompresi JSON'
    model['description'] = 'Alat online kompresi JSON ini membantu Anda mengompresi string JSON asli, menghemat ruang untuk transfer lebih cepat melalui jaringan.'
    model['keywords'] = 'Json minifier, kompresi JSON'
    model['image'] = '/image/comic-json-minifier.png'
    return render_template(template_dir + 'template_json_minifier_id.html', model=model)


@Web_JsonFormatter_blueprint.route('/id/xml-formatter', methods=['GET', 'POST'])
def xml_formatter():
    model = get_default_model()
    model['url'] = '/id/xml-formatter'
    model['enUrl'] = '/xml-formatter'
    model['headerTitle'] = 'Alat Online Format XML  - Coding.Tools'
    model['bodyTitle'] = 'Alat format online XML'
    model['description'] = 'Alat pemformatan XML online ini dapat membantu Anda memformat string XML yang membingungkan menjadi string XML yang dapat dibaca.'
    model['keywords'] = 'Pemformat xml, pemformatan XML'
    model['image'] = '/image/comic-xml-formatter.png'
    return render_template(template_dir + 'template_xml_formatter_id.html', model=model)


@Web_JsonFormatter_blueprint.route('/id/xml-minifier', methods=['GET', 'POST'])
def xml_minifier():
    model = get_default_model()
    model['url'] = '/id/xml-minifier'
    model['enUrl'] = '/xml-minifier'
    model['headerTitle'] = 'Alat kompresi online XML  - Coding.Tools'
    model['bodyTitle'] = 'Alat online kompresi XML'
    model['description'] = 'Alat online kompresi XML ini membantu Anda mengompresi string XML mentah, menghemat ruang untuk transfer lebih cepat melalui jaringan.'
    model['keywords'] = 'Pengubah xml, kompresi XML'
    model['image'] = '/image/comic-xml-minifier.png'
    return render_template(template_dir + 'template_xml_minifier_id.html', model=model)


@Web_JsonFormatter_blueprint.route('/id/json-to-xml', methods=['GET', 'POST'])
def json_to_xml():
    model = get_default_model()
    model['url'] = '/id/json-to-xml'
    model['enUrl'] = '/json-to-xml'
    model['headerTitle'] = 'Alat JSON ke XML online  - Coding.Tools'
    model['bodyTitle'] = 'JSON ke alat XML online'
    model['description'] = 'Alat JSON ke XML online ini dapat membantu Anda mengubah string data dalam format JSON menjadi string data dalam format XML.'
    model['keywords'] = 'Json ke xml, JSON ke XML'
    model['image'] = '/image/comic-json-to-xml.png'
    return render_template(template_dir + 'template_json_to_xml_id.html', model=model)


@Web_JsonFormatter_blueprint.route('/id/xml-to-json', methods=['GET', 'POST'])
def xml_to_json():
    model = get_default_model()
    model['url'] = '/id/xml-to-json'
    model['enUrl'] = '/xml-to-json'
    model['headerTitle'] = 'Alat XML to JSON online  - Coding.Tools'
    model['bodyTitle'] = 'Alat XML to JSON online'
    model['description'] = 'Alat online XML ke JSON ini dapat membantu Anda mengubah string data dalam format XML menjadi string data dalam format JSON.'
    model['keywords'] = 'XML ke JSON, xml ke json'
    model['image'] = '/image/comic-xml-to-json.png'
    return render_template(template_dir + 'template_xml_to_json_id.html', model=model)


@Web_JsonFormatter_blueprint.route('/id/html-beautifier', methods=['GET', 'POST'])
def html_beautifier():
    model = get_default_model()
    model['url'] = '/id/html-beautifier'
    model['enUrl'] = '/html-beautifier'
    model['headerTitle'] = 'Alat pemformatan online HTML  - Coding.Tools'
    model['bodyTitle'] = 'Alat pemformatan online HTML'
    model['description'] = 'Alat pemformatan HTML online ini dapat membantu Anda memformat file HTML yang membingungkan menjadi file HTML yang dapat dibaca.'
    model['keywords'] = 'Pemformat html, html beautifier, pemformatan HTML'
    model['image'] = '/image/comic-html-beautifier.png'
    return render_template(template_dir + 'template_html_beautifier_id.html', model=model)


@Web_JsonFormatter_blueprint.route('/id/html-minifier', methods=['GET', 'POST'])
def html_minifier():
    model = get_default_model()
    model['url'] = '/id/html-minifier'
    model['enUrl'] = '/html-minifier'
    model['headerTitle'] = 'Alat kompresi online HTML  - Coding.Tools'
    model['bodyTitle'] = 'Alat online kompresi HTML'
    model['description'] = 'Alat online kompresi HTML ini membantu Anda mengompres file HTML asli Anda, menghemat ruang untuk transfer lebih cepat melalui jaringan.'
    model['keywords'] = 'Pengubah html, kompresi HTML'
    model['image'] = '/image/comic-html-minifier.png'
    return render_template(template_dir + 'template_html_minifier_id.html', model=model)


@Web_JsonFormatter_blueprint.route('/id/javascript-beautifier', methods=['GET', 'POST'])
def javascript_beautifier():
    model = get_default_model()
    model['url'] = '/id/javascript-beautifier'
    model['enUrl'] = '/javascript-beautifier'
    model['headerTitle'] = 'Alat online format Javascript  - Coding.Tools'
    model['bodyTitle'] = 'Alat online pemformatan Javascript'
    model['description'] = 'Alat pemformatan Javascript online ini dapat membantu Anda memformat file Javascript yang membingungkan menjadi file Javascript yang dapat dibaca.'
    model['keywords'] = 'Formatter Javascript, penambah javascript, pemformatan Javascript'
    model['image'] = '/image/comic-javascript-beautifier.png'
    return render_template(template_dir + 'template_javascript_beautifier_id.html', model=model)


@Web_JsonFormatter_blueprint.route('/id/javascript-minifier', methods=['GET', 'POST'])
def javascript_minifier():
    model = get_default_model()
    model['url'] = '/id/javascript-minifier'
    model['enUrl'] = '/javascript-minifier'
    model['headerTitle'] = 'Alat online kompresi Javascript  - Coding.Tools'
    model['bodyTitle'] = 'Alat online kompresi Javascript'
    model['description'] = 'Alat online kompresi Javascript ini membantu Anda mengompres file Javascript asli Anda, menghemat ruang untuk transfer lebih cepat melalui jaringan.'
    model['keywords'] = 'Pengubah Javascript, kompresi Javascript'
    model['image'] = '/image/comic-javascript-minifier.png'
    return render_template(template_dir + 'template_javascript_minifier_id.html', model=model)


@Web_JsonFormatter_blueprint.route('/id/css-beautifier', methods=['GET', 'POST'])
def css_beautifier():
    model = get_default_model()
    model['url'] = '/id/css-beautifier'
    model['enUrl'] = '/css-beautifier'
    model['headerTitle'] = 'Alat Online Pemformatan CSS  - Coding.Tools'
    model['bodyTitle'] = 'Alat pemformatan online CSS'
    model['description'] = 'Alat pemformatan CSS online ini dapat membantu Anda memformat file CSS yang membingungkan menjadi file CSS yang dapat dibaca.'
    model['keywords'] = 'Css formatter, css beautifier, pemformatan CSS'
    model['image'] = '/image/comic-css-beautifier.png'
    return render_template(template_dir + 'template_css_beautifier_id.html', model=model)


@Web_JsonFormatter_blueprint.route('/id/css-minifier', methods=['GET', 'POST'])
def css_minifier():
    model = get_default_model()
    model['url'] = '/id/css-minifier'
    model['enUrl'] = '/css-minifier'
    model['headerTitle'] = 'Alat online kompresi CSS  - Coding.Tools'
    model['bodyTitle'] = 'Alat online kompresi CSS'
    model['description'] = 'Alat online kompresi CSS ini membantu Anda mengompres file CSS asli Anda, menghemat ruang untuk transfer lebih cepat melalui jaringan.'
    model['keywords'] = 'Pengukur css, kompresi CSS'
    model['image'] = '/image/comic-css-minifier.png'
    return render_template(template_dir + 'template_css_minifier_id.html', model=model)
