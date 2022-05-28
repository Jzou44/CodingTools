from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_JsonFormatter_blueprint = Blueprint('Web_JsonFormatter_blueprint', __name__)
template_dir = 'JsonFormatter/en/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'en'
    return model


@Web_JsonFormatter_blueprint.route('/json-formatter', methods=['GET', 'POST'])
def json_formatter():
    model = get_default_model()
    model['url'] = '/json-formatter'
    model['enUrl'] = '/json-formatter'
    model['headerTitle'] = 'JSON Formatter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'JSON Formatter Online Tool'
    model['description'] = 'This online json formatter tool helps you to format raw JSON string so it can easily be read by human being.'
    model['keywords'] = 'json formatter, json beautifier, json pretty printer'
    model['image'] = '/image/comic-json-formatter.png'
    return render_template(template_dir + 'template_json_formatter.html', model=model)


@Web_JsonFormatter_blueprint.route('/json-minifier', methods=['GET', 'POST'])
def json_minifier():
    model = get_default_model()
    model['url'] = '/json-minifier'
    model['enUrl'] = '/json-minifier'
    model['headerTitle'] = 'JSON Minifier Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'JSON Minifier Online Tool'
    model['description'] = 'This online json minifier tool helps you to minify raw JSON string to save space to transmit faster cross Internet.'
    model['keywords'] = 'json minifier, json minify, json compress'
    model['image'] = '/image/comic-json-minifier.png'
    return render_template(template_dir + 'template_json_minifier.html', model=model)


@Web_JsonFormatter_blueprint.route('/xml-formatter', methods=['GET', 'POST'])
def xml_formatter():
    model = get_default_model()
    model['url'] = '/xml-formatter'
    model['enUrl'] = '/xml-formatter'
    model['headerTitle'] = 'XML Formatter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'XML Formatter Online Tool'
    model['description'] = 'This online xml formatter tool helps you to format raw XML string so it can easily be read by human being.'
    model['keywords'] = 'xml formatter, xml beautifier, xml pretty printer'
    model['image'] = '/image/comic-xml-formatter.png'
    return render_template(template_dir + 'template_xml_formatter.html', model=model)


@Web_JsonFormatter_blueprint.route('/xml-minifier', methods=['GET', 'POST'])
def xml_minifier():
    model = get_default_model()
    model['url'] = '/xml-minifier'
    model['enUrl'] = '/xml-minifier'
    model['headerTitle'] = 'XML Minifier Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'XML Minifier Online Tool'
    model['description'] = 'This online xml minifier tool helps you to minify raw XML string to save space to transmit faster cross Internet.'
    model['keywords'] = 'xml minifier, xml minify, xml compress'
    model['image'] = '/image/comic-xml-minifier.png'
    return render_template(template_dir + 'template_xml_minifier.html', model=model)


@Web_JsonFormatter_blueprint.route('/json-to-xml', methods=['GET', 'POST'])
def json_to_xml():
    model = get_default_model()
    model['url'] = '/json-to-xml'
    model['enUrl'] = '/json-to-xml'
    model['headerTitle'] = 'JSON to XML Converter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'JSON to XML Converter Online Tool'
    model['description'] = 'This online json to xml converter tool helps you to convert raw json format string to xml format string.'
    model['keywords'] = 'json to xml, json to xml converter, json convert xml'
    model['image'] = '/image/comic-json-to-xml.png'
    return render_template(template_dir + 'template_json_to_xml.html', model=model)


@Web_JsonFormatter_blueprint.route('/xml-to-json', methods=['GET', 'POST'])
def xml_to_json():
    model = get_default_model()
    model['url'] = '/xml-to-json'
    model['enUrl'] = '/xml-to-json'
    model['headerTitle'] = 'XML to JSON Converter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'XML to JSON Converter Online Tool'
    model['description'] = 'This online xml to json converter tool helps you to convert raw xml format string to json format string.'
    model['keywords'] = 'xml to json, xml to json converter, xml convert json'
    model['image'] = '/image/comic-xml-to-json.png'
    return render_template(template_dir + 'template_xml_to_json.html', model=model)


@Web_JsonFormatter_blueprint.route('/html-beautifier', methods=['GET', 'POST'])
def html_beautifier():
    model = get_default_model()
    model['url'] = '/html-beautifier'
    model['enUrl'] = '/html-beautifier'
    model['headerTitle'] = 'HTML Beautifier Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'HTML Beautifier Online Tool'
    model['description'] = 'This online html beautifier tool helps you to format raw HTML file so it can easily be read by human being.'
    model['keywords'] = 'html formatter, html beautifier, html pretty printer'
    model['image'] = '/image/comic-html-beautifier.png'
    return render_template(template_dir + 'template_html_beautifier.html', model=model)


@Web_JsonFormatter_blueprint.route('/html-minifier', methods=['GET', 'POST'])
def html_minifier():
    model = get_default_model()
    model['url'] = '/html-minifier'
    model['enUrl'] = '/html-minifier'
    model['headerTitle'] = 'HTML Minifier Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'HTML Minifier Online Tool'
    model['description'] = 'This online html minifier tool helps you to minify raw HTML file to save space to transmit faster cross Internet.'
    model['keywords'] = 'html minifier, html minify, html compress'
    model['image'] = '/image/comic-html-minifier.png'
    return render_template(template_dir + 'template_html_minifier.html', model=model)


@Web_JsonFormatter_blueprint.route('/javascript-beautifier', methods=['GET', 'POST'])
def javascript_beautifier():
    model = get_default_model()
    model['url'] = '/javascript-beautifier'
    model['enUrl'] = '/javascript-beautifier'
    model['headerTitle'] = 'Javascript Beautifier Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Javascript Beautifier Online Tool'
    model['description'] = 'This online javascript beautifier tool helps you to format raw Javascript string so it can easily be read by human being.'
    model['keywords'] = 'javascript formatter, javascript beautifier, javascript pretty printer'
    model['image'] = '/image/comic-javascript-beautifier.png'
    return render_template(template_dir + 'template_javascript_beautifier.html', model=model)


@Web_JsonFormatter_blueprint.route('/javascript-minifier', methods=['GET', 'POST'])
def javascript_minifier():
    model = get_default_model()
    model['url'] = '/javascript-minifier'
    model['enUrl'] = '/javascript-minifier'
    model['headerTitle'] = 'Javascript Minifier Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Javascript Minifier Online Tool'
    model['description'] = 'This online javascript minifier tool helps you to minify raw Javascript string to save space to transmit faster cross Internet.'
    model['keywords'] = 'javascript minifier, javascript minify, javascript compress'
    model['image'] = '/image/comic-javascript-minifier.png'
    return render_template(template_dir + 'template_javascript_minifier.html', model=model)


@Web_JsonFormatter_blueprint.route('/css-beautifier', methods=['GET', 'POST'])
def css_beautifier():
    model = get_default_model()
    model['url'] = '/css-beautifier'
    model['enUrl'] = '/css-beautifier'
    model['headerTitle'] = 'CSS Beautifier Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'CSS Beautifier Online Tool'
    model['description'] = 'This online css beautifier tool helps you to format raw css string so it can easily be read by human being.'
    model['keywords'] = 'css formatter, css beautifier, css pretty printer'
    model['image'] = '/image/comic-css-beautifier.png'
    return render_template(template_dir + 'template_css_beautifier.html', model=model)


@Web_JsonFormatter_blueprint.route('/css-minifier', methods=['GET', 'POST'])
def css_minifier():
    model = get_default_model()
    model['url'] = '/css-minifier'
    model['enUrl'] = '/css-minifier'
    model['headerTitle'] = 'CSS Minifier Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'CSS Minifier Online Tool'
    model['description'] = 'This online css minifier tool helps you to minify raw css string to save space to transmit faster cross Internet.'
    model['keywords'] = 'css minifier, css minify, css compress'
    model['image'] = '/image/comic-css-minifier.png'
    return render_template(template_dir + 'template_css_minifier.html', model=model)


@Web_JsonFormatter_blueprint.route('/sql-formatter', methods=['GET', 'POST'])
def sql_formatter():
    model = get_default_model()
    model['url'] = '/sql-formatter'
    model['enUrl'] = '/sql-formatter'
    model['headerTitle'] = 'SQL Formatter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'SQL Formatter Online Tool'
    model['description'] = 'This online sql formatter tool helps you to format ugly indented sql string so it can easily be read by human being.'
    model['keywords'] = 'sql formatter, sql beautifier'
    model['image'] = '/image/20190308/cartoon_sql_formatter.png'
    return render_template(template_dir + 'template_sql_formatter.html', model=model)


@Web_JsonFormatter_blueprint.route('/sql-minifier', methods=['GET', 'POST'])
def sql_minifier():
    model = get_default_model()
    model['url'] = '/sql-minifier'
    model['enUrl'] = '/sql-minifier'
    model['headerTitle'] = 'SQL Minifier Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'SQL Minifier Online Tool'
    model['description'] = 'This online sql minifier tool helps you to minify sql string to save space in your IDE.'
    model['keywords'] = 'sql minifier, sql minify, sql compress'
    model['image'] = '/image/20190308/cartoon_sql_minifier.png'
    return render_template(template_dir + 'template_sql_minifier.html', model=model)
