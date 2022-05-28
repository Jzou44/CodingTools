from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_JsonFormatter_blueprint = Blueprint('Web_JsonFormatter_blueprint_PT', __name__)
template_dir = 'JsonFormatter/pt/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'pt'
    return model


@Web_JsonFormatter_blueprint.route('/pt/json-formatter', methods=['GET', 'POST'])
def json_formatter():
    model = get_default_model()
    model['url'] = '/pt/json-formatter'
    model['enUrl'] = '/json-formatter'
    model['headerTitle'] = 'Ferramenta online de formatação JSON  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta online de formatação JSON'
    model['description'] = 'Essa ferramenta de formatação JSON on-line pode ajudar a formatar strings JSON confusas em strings JSON legíveis.'
    model['keywords'] = 'Formatador Json, formatação JSON'
    model['image'] = '/image/comic-json-formatter.png'
    return render_template(template_dir + 'template_json_formatter_pt.html', model=model)


@Web_JsonFormatter_blueprint.route('/pt/json-minifier', methods=['GET', 'POST'])
def json_minifier():
    model = get_default_model()
    model['url'] = '/pt/json-minifier'
    model['enUrl'] = '/json-minifier'
    model['headerTitle'] = 'Ferramenta on-line de compactação JSON  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta on-line de compactação JSON'
    model['description'] = 'Essa ferramenta on-line de compactação JSON ajuda a compactar as strings JSON originais, economizando espaço para uma transferência mais rápida pela rede.'
    model['keywords'] = 'Minimizador Json, compactação JSON'
    model['image'] = '/image/comic-json-minifier.png'
    return render_template(template_dir + 'template_json_minifier_pt.html', model=model)


@Web_JsonFormatter_blueprint.route('/pt/xml-formatter', methods=['GET', 'POST'])
def xml_formatter():
    model = get_default_model()
    model['url'] = '/pt/xml-formatter'
    model['enUrl'] = '/xml-formatter'
    model['headerTitle'] = 'Ferramenta Online de Formatação XML  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta on-line de formatação XML'
    model['description'] = 'Essa ferramenta de formatação XML on-line pode ajudar a formatar sequências XML confusas em cadeias XML legíveis.'
    model['keywords'] = 'Formatador XML, formatação XML'
    model['image'] = '/image/comic-xml-formatter.png'
    return render_template(template_dir + 'template_xml_formatter_pt.html', model=model)


@Web_JsonFormatter_blueprint.route('/pt/xml-minifier', methods=['GET', 'POST'])
def xml_minifier():
    model = get_default_model()
    model['url'] = '/pt/xml-minifier'
    model['enUrl'] = '/xml-minifier'
    model['headerTitle'] = 'Ferramenta on-line de compactação XML  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta on-line de compactação XML'
    model['description'] = 'Essa ferramenta on-line de compactação XML ajuda a compactar sequências XML brutas, economizando espaço para uma transferência mais rápida na rede.'
    model['keywords'] = 'Xml minifier, compressão XML'
    model['image'] = '/image/comic-xml-minifier.png'
    return render_template(template_dir + 'template_xml_minifier_pt.html', model=model)


@Web_JsonFormatter_blueprint.route('/pt/json-to-xml', methods=['GET', 'POST'])
def json_to_xml():
    model = get_default_model()
    model['url'] = '/pt/json-to-xml'
    model['enUrl'] = '/json-to-xml'
    model['headerTitle'] = 'Ferramenta online JSON para XML  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta on-line de JSON para XML'
    model['description'] = 'Essa ferramenta on-line JSON para XML pode ajudá-lo a converter sequências de dados no formato JSON em cadeias de dados no formato XML.'
    model['keywords'] = 'Json para xml, JSON para XML'
    model['image'] = '/image/comic-json-to-xml.png'
    return render_template(template_dir + 'template_json_to_xml_pt.html', model=model)


@Web_JsonFormatter_blueprint.route('/pt/xml-to-json', methods=['GET', 'POST'])
def xml_to_json():
    model = get_default_model()
    model['url'] = '/pt/xml-to-json'
    model['enUrl'] = '/xml-to-json'
    model['headerTitle'] = 'Ferramenta online XML para JSON  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta online XML para JSON'
    model['description'] = 'Essa ferramenta on-line XML para JSON pode ajudá-lo a converter sequências de dados no formato XML em sequências de dados no formato JSON.'
    model['keywords'] = 'XML para JSON, xml para json'
    model['image'] = '/image/comic-xml-to-json.png'
    return render_template(template_dir + 'template_xml_to_json_pt.html', model=model)


@Web_JsonFormatter_blueprint.route('/pt/html-beautifier', methods=['GET', 'POST'])
def html_beautifier():
    model = get_default_model()
    model['url'] = '/pt/html-beautifier'
    model['enUrl'] = '/html-beautifier'
    model['headerTitle'] = 'Ferramenta online de formatação HTML  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta on-line de formatação HTML'
    model['description'] = 'Esta ferramenta de formatação HTML on-line pode ajudá-lo a formatar arquivos HTML confusos em arquivos HTML legíveis.'
    model['keywords'] = 'Formatador HTML, embelezador html, formatação HTML'
    model['image'] = '/image/comic-html-beautifier.png'
    return render_template(template_dir + 'template_html_beautifier_pt.html', model=model)


@Web_JsonFormatter_blueprint.route('/pt/html-minifier', methods=['GET', 'POST'])
def html_minifier():
    model = get_default_model()
    model['url'] = '/pt/html-minifier'
    model['enUrl'] = '/html-minifier'
    model['headerTitle'] = 'Ferramenta on-line de compactação HTML  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta on-line de compactação HTML'
    model['description'] = 'Essa ferramenta on-line de compactação HTML ajuda a compactar seus arquivos HTML originais, economizando espaço para uma transferência mais rápida pela rede.'
    model['keywords'] = 'Minimizador HTML, compactação HTML'
    model['image'] = '/image/comic-html-minifier.png'
    return render_template(template_dir + 'template_html_minifier_pt.html', model=model)


@Web_JsonFormatter_blueprint.route('/pt/javascript-beautifier', methods=['GET', 'POST'])
def javascript_beautifier():
    model = get_default_model()
    model['url'] = '/pt/javascript-beautifier'
    model['enUrl'] = '/javascript-beautifier'
    model['headerTitle'] = 'Ferramenta on-line de formatação Javascript  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta online de formatação de Javascript'
    model['description'] = 'Esta ferramenta de formatação Javascript on-line pode ajudá-lo a formatar arquivos JavaScript confusos em arquivos JavaScript legíveis.'
    model['keywords'] = 'JavaScript formatter, javascript beautifier, formatação Javascript'
    model['image'] = '/image/comic-javascript-beautifier.png'
    return render_template(template_dir + 'template_javascript_beautifier_pt.html', model=model)


@Web_JsonFormatter_blueprint.route('/pt/javascript-minifier', methods=['GET', 'POST'])
def javascript_minifier():
    model = get_default_model()
    model['url'] = '/pt/javascript-minifier'
    model['enUrl'] = '/javascript-minifier'
    model['headerTitle'] = 'Ferramenta on-line de compressão Javascript  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta on-line de compressão Javascript'
    model['description'] = 'Essa ferramenta on-line de compactação Javascript ajuda a compactar seus arquivos Javascript originais, economizando espaço para uma transferência mais rápida pela rede.'
    model['keywords'] = 'Minifier Javascript, compressão Javascript'
    model['image'] = '/image/comic-javascript-minifier.png'
    return render_template(template_dir + 'template_javascript_minifier_pt.html', model=model)


@Web_JsonFormatter_blueprint.route('/pt/css-beautifier', methods=['GET', 'POST'])
def css_beautifier():
    model = get_default_model()
    model['url'] = '/pt/css-beautifier'
    model['enUrl'] = '/css-beautifier'
    model['headerTitle'] = 'Ferramenta Online de Formatação de CSS  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta on-line de formatação CSS'
    model['description'] = 'Esta ferramenta de formatação CSS on-line pode ajudá-lo a formatar arquivos CSS confusos em arquivos CSS legíveis.'
    model['keywords'] = 'Formatador Css, css beautifier, formatação CSS'
    model['image'] = '/image/comic-css-beautifier.png'
    return render_template(template_dir + 'template_css_beautifier_pt.html', model=model)


@Web_JsonFormatter_blueprint.route('/pt/css-minifier', methods=['GET', 'POST'])
def css_minifier():
    model = get_default_model()
    model['url'] = '/pt/css-minifier'
    model['enUrl'] = '/css-minifier'
    model['headerTitle'] = 'Ferramenta online de compressão CSS  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta online de compressão CSS'
    model['description'] = 'Essa ferramenta on-line de compactação CSS ajuda você a compactar seus arquivos CSS originais, economizando espaço para uma transferência mais rápida pela rede.'
    model['keywords'] = 'Css minifier, compressão CSS'
    model['image'] = '/image/comic-css-minifier.png'
    return render_template(template_dir + 'template_css_minifier_pt.html', model=model)
