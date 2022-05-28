from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_JsonFormatter_blueprint = Blueprint('Web_JsonFormatter_blueprint_DE', __name__)
template_dir = 'JsonFormatter/de/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'de'
    return model


@Web_JsonFormatter_blueprint.route('/de/json-formatter', methods=['GET', 'POST'])
def json_formatter():
    model = get_default_model()
    model['url'] = '/de/json-formatter'
    model['enUrl'] = '/json-formatter'
    model['headerTitle'] = 'JSON-Formatierungs-Online-Tool  - Coding.Tools'
    model['bodyTitle'] = 'JSON-Formatierungs-Online-Tool'
    model['description'] = 'Mit diesem Online-JSON-Formatierungswerkzeug können Sie verwirrende JSON-Zeichenfolgen in lesbare JSON-Zeichenfolgen formatieren.'
    model['keywords'] = 'Json-Formatierer, JSON-Formatierung'
    model['image'] = '/image/comic-json-formatter.png'
    return render_template(template_dir + 'template_json_formatter_de.html', model=model)


@Web_JsonFormatter_blueprint.route('/de/json-minifier', methods=['GET', 'POST'])
def json_minifier():
    model = get_default_model()
    model['url'] = '/de/json-minifier'
    model['enUrl'] = '/json-minifier'
    model['headerTitle'] = 'JSON-Komprimierungs-Online-Tool  - Coding.Tools'
    model['bodyTitle'] = 'JSON-Komprimierungs-Online-Tool'
    model['description'] = 'Mit diesem Online-Tool zur JSON-Komprimierung können Sie die ursprünglichen JSON-Zeichenfolgen komprimieren, um Platz für eine schnellere Übertragung über das Netzwerk zu sparen.'
    model['keywords'] = 'Json Minifier, JSON-Komprimierung'
    model['image'] = '/image/comic-json-minifier.png'
    return render_template(template_dir + 'template_json_minifier_de.html', model=model)


@Web_JsonFormatter_blueprint.route('/de/xml-formatter', methods=['GET', 'POST'])
def xml_formatter():
    model = get_default_model()
    model['url'] = '/de/xml-formatter'
    model['enUrl'] = '/xml-formatter'
    model['headerTitle'] = 'XML-Formatierungs-Online-Tool  - Coding.Tools'
    model['bodyTitle'] = 'Online-Tool zur XML-Formatierung'
    model['description'] = 'Mit diesem Online-XML-Formatierungswerkzeug können Sie verwirrende XML-Zeichenfolgen in lesbare XML-Zeichenfolgen formatieren.'
    model['keywords'] = 'XML-Formatierer, XML-Formatierung'
    model['image'] = '/image/comic-xml-formatter.png'
    return render_template(template_dir + 'template_xml_formatter_de.html', model=model)


@Web_JsonFormatter_blueprint.route('/de/xml-minifier', methods=['GET', 'POST'])
def xml_minifier():
    model = get_default_model()
    model['url'] = '/de/xml-minifier'
    model['enUrl'] = '/xml-minifier'
    model['headerTitle'] = 'XML-Komprimierungs-Online-Tool  - Coding.Tools'
    model['bodyTitle'] = 'XML-Komprimierungs-Online-Tool'
    model['description'] = 'Mit diesem Online-Tool zur XML-Komprimierung können Sie rohe XML-Zeichenfolgen komprimieren, um Platz zu sparen und die Übertragung über das Netzwerk zu beschleunigen.'
    model['keywords'] = 'XML-Minifier, XML-Komprimierung'
    model['image'] = '/image/comic-xml-minifier.png'
    return render_template(template_dir + 'template_xml_minifier_de.html', model=model)


@Web_JsonFormatter_blueprint.route('/de/json-to-xml', methods=['GET', 'POST'])
def json_to_xml():
    model = get_default_model()
    model['url'] = '/de/json-to-xml'
    model['enUrl'] = '/json-to-xml'
    model['headerTitle'] = 'JSON-zu-XML-Online-Tool  - Coding.Tools'
    model['bodyTitle'] = 'JSON zu XML Online-Tool'
    model['description'] = 'Dieses JSON-zu-XML-Online-Tool kann Ihnen beim Konvertieren von Datenzeichenfolgen im JSON-Format in Datenzeichenfolgen im XML-Format helfen.'
    model['keywords'] = 'Json in XML, JSON in XML'
    model['image'] = '/image/comic-json-to-xml.png'
    return render_template(template_dir + 'template_json_to_xml_de.html', model=model)


@Web_JsonFormatter_blueprint.route('/de/xml-to-json', methods=['GET', 'POST'])
def xml_to_json():
    model = get_default_model()
    model['url'] = '/de/xml-to-json'
    model['enUrl'] = '/xml-to-json'
    model['headerTitle'] = 'XML zu JSON Online-Tool  - Coding.Tools'
    model['bodyTitle'] = 'XML zu JSON Online-Tool'
    model['description'] = 'Mit diesem Online-Tool für XML in JSON können Sie Datenzeichenfolgen im XML-Format in Datenzeichenfolgen im JSON-Format konvertieren.'
    model['keywords'] = 'XML zu JSON, XML zu Json'
    model['image'] = '/image/comic-xml-to-json.png'
    return render_template(template_dir + 'template_xml_to_json_de.html', model=model)


@Web_JsonFormatter_blueprint.route('/de/html-beautifier', methods=['GET', 'POST'])
def html_beautifier():
    model = get_default_model()
    model['url'] = '/de/html-beautifier'
    model['enUrl'] = '/html-beautifier'
    model['headerTitle'] = 'Online-Tool zur HTML-Formatierung  - Coding.Tools'
    model['bodyTitle'] = 'Online-Tool zur HTML-Formatierung'
    model['description'] = 'Mit diesem Online-HTML-Formatierungswerkzeug können Sie verwirrende HTML-Dateien in lesbare HTML-Dateien formatieren.'
    model['keywords'] = 'HTML-Formatierer, HTML-Beautifier, HTML-Formatierung'
    model['image'] = '/image/comic-html-beautifier.png'
    return render_template(template_dir + 'template_html_beautifier_de.html', model=model)


@Web_JsonFormatter_blueprint.route('/de/html-minifier', methods=['GET', 'POST'])
def html_minifier():
    model = get_default_model()
    model['url'] = '/de/html-minifier'
    model['enUrl'] = '/html-minifier'
    model['headerTitle'] = 'Online-Tool zur HTML-Komprimierung  - Coding.Tools'
    model['bodyTitle'] = 'Online-Tool zur HTML-Komprimierung'
    model['description'] = 'Mit diesem Online-Tool zur HTML-Komprimierung können Sie Ihre ursprünglichen HTML-Dateien komprimieren, um Platz für eine schnellere Übertragung über das Netzwerk zu sparen.'
    model['keywords'] = 'HTML-Minifier, HTML-Komprimierung'
    model['image'] = '/image/comic-html-minifier.png'
    return render_template(template_dir + 'template_html_minifier_de.html', model=model)


@Web_JsonFormatter_blueprint.route('/de/javascript-beautifier', methods=['GET', 'POST'])
def javascript_beautifier():
    model = get_default_model()
    model['url'] = '/de/javascript-beautifier'
    model['enUrl'] = '/javascript-beautifier'
    model['headerTitle'] = 'Javascript-Formatierungs-Online-Tool  - Coding.Tools'
    model['bodyTitle'] = 'Javascript-Formatierungs-Online-Tool'
    model['description'] = 'Mit diesem Online-Formatierungswerkzeug für Javascript können Sie verwirrende Javascript-Dateien in lesbare Javascript-Dateien formatieren.'
    model['keywords'] = 'Javascript-Formatierer, Javascript-Beautifier, Javascript-Formatierung'
    model['image'] = '/image/comic-javascript-beautifier.png'
    return render_template(template_dir + 'template_javascript_beautifier_de.html', model=model)


@Web_JsonFormatter_blueprint.route('/de/javascript-minifier', methods=['GET', 'POST'])
def javascript_minifier():
    model = get_default_model()
    model['url'] = '/de/javascript-minifier'
    model['enUrl'] = '/javascript-minifier'
    model['headerTitle'] = 'Javascript-Komprimierungs-Online-Tool  - Coding.Tools'
    model['bodyTitle'] = 'Javascript-Komprimierungs-Online-Tool'
    model['description'] = 'Mit diesem Online-Tool zur Javascript-Komprimierung können Sie Ihre ursprünglichen Javascript-Dateien komprimieren, um Platz für eine schnellere Übertragung über das Netzwerk zu sparen.'
    model['keywords'] = 'Javascript Minifier, Javascript-Komprimierung'
    model['image'] = '/image/comic-javascript-minifier.png'
    return render_template(template_dir + 'template_javascript_minifier_de.html', model=model)


@Web_JsonFormatter_blueprint.route('/de/css-beautifier', methods=['GET', 'POST'])
def css_beautifier():
    model = get_default_model()
    model['url'] = '/de/css-beautifier'
    model['enUrl'] = '/css-beautifier'
    model['headerTitle'] = 'CSS-Formatierungs-Online-Tool  - Coding.Tools'
    model['bodyTitle'] = 'Online-Tool zur CSS-Formatierung'
    model['description'] = 'Mit diesem Online-Tool zur CSS-Formatierung können Sie verwirrende CSS-Dateien in lesbare CSS-Dateien formatieren.'
    model['keywords'] = 'CSS-Formatierer, CSS-Beautifier, CSS-Formatierung'
    model['image'] = '/image/comic-css-beautifier.png'
    return render_template(template_dir + 'template_css_beautifier_de.html', model=model)


@Web_JsonFormatter_blueprint.route('/de/css-minifier', methods=['GET', 'POST'])
def css_minifier():
    model = get_default_model()
    model['url'] = '/de/css-minifier'
    model['enUrl'] = '/css-minifier'
    model['headerTitle'] = 'Online-Tool zur CSS-Komprimierung  - Coding.Tools'
    model['bodyTitle'] = 'Online-Tool zur CSS-Komprimierung'
    model['description'] = 'Mit diesem Online-Tool zur CSS-Komprimierung können Sie Ihre ursprünglichen CSS-Dateien komprimieren, um Platz für eine schnellere Übertragung über das Netzwerk zu sparen.'
    model['keywords'] = 'CSS-Minifier, CSS-Komprimierung'
    model['image'] = '/image/comic-css-minifier.png'
    return render_template(template_dir + 'template_css_minifier_de.html', model=model)
