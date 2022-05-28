from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_JsonFormatter_blueprint = Blueprint('Web_JsonFormatter_blueprint_TW', __name__)
template_dir = 'JsonFormatter/tw/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'zh-Hant'
    return model


@Web_JsonFormatter_blueprint.route('/tw/json-formatter', methods=['GET', 'POST'])
def json_formatter():
    model = get_default_model()
    model['url'] = '/tw/json-formatter'
    model['enUrl'] = '/json-formatter'
    model['headerTitle'] = 'JSON格式化在線工具 - Coding.Tools'
    model['bodyTitle'] = 'JSON格式化在線工具'
    model['description'] = '這個在線JSON格式化工具可以幫助您將排列混亂的JSON字符串格式化為可讀的JSON字符串.'
    model['keywords'] = 'json formatter, JSON格式化'
    model['image'] = '/image/comic-json-formatter.png'
    return render_template(template_dir + 'template_json_formatter_tw.html', model=model)


@Web_JsonFormatter_blueprint.route('/tw/json-minifier', methods=['GET', 'POST'])
def json_minifier():
    model = get_default_model()
    model['url'] = '/tw/json-minifier'
    model['enUrl'] = '/json-minifier'
    model['headerTitle'] = 'JSON壓縮在線工具 - Coding.Tools'
    model['bodyTitle'] = 'JSON壓縮在線工具'
    model['description'] = '這個JSON壓縮在線工具可以幫助您壓縮原始JSON字符串,可以節省空間,以便更快地在網絡中傳輸.'
    model['keywords'] = 'json minifier, JSON壓縮'
    model['image'] = '/image/comic-json-minifier.png'
    return render_template(template_dir + 'template_json_minifier_tw.html', model=model)


@Web_JsonFormatter_blueprint.route('/tw/xml-formatter', methods=['GET', 'POST'])
def xml_formatter():
    model = get_default_model()
    model['url'] = '/tw/xml-formatter'
    model['enUrl'] = '/xml-formatter'
    model['headerTitle'] = 'XML格式化在線工具 - Coding.Tools'
    model['bodyTitle'] = 'XML格式化在線工具'
    model['description'] = '這個在線XML格式化工具可以幫助您將排列混亂的XML字符串格式化為可讀的XML字符串.'
    model['keywords'] = 'xml formatter, XML格式化'
    model['image'] = '/image/comic-xml-formatter.png'
    return render_template(template_dir + 'template_xml_formatter_tw.html', model=model)


@Web_JsonFormatter_blueprint.route('/tw/xml-minifier', methods=['GET', 'POST'])
def xml_minifier():
    model = get_default_model()
    model['url'] = '/tw/xml-minifier'
    model['enUrl'] = '/xml-minifier'
    model['headerTitle'] = 'XML壓縮在線工具 - Coding.Tools'
    model['bodyTitle'] = 'XML壓縮在線工具'
    model['description'] = '這個XML壓縮在線工具可以幫助您壓縮原始XML字符串,可以節省空間,以便更快地在網絡中傳輸.'
    model['keywords'] = 'xml minifier, XML壓縮'
    model['image'] = '/image/comic-xml-minifier.png'
    return render_template(template_dir + 'template_xml_minifier_tw.html', model=model)


@Web_JsonFormatter_blueprint.route('/tw/json-to-xml', methods=['GET', 'POST'])
def json_to_xml():
    model = get_default_model()
    model['url'] = '/tw/json-to-xml'
    model['enUrl'] = '/json-to-xml'
    model['headerTitle'] = 'JSON轉XML在線工具 - Coding.Tools'
    model['bodyTitle'] = 'JSON轉XML在線工具'
    model['description'] = '這個JSON轉XML在線工具可以幫助您把JSON格式的數據字符串轉換成XML格式的數據字符串.'
    model['keywords'] = 'json to xml, JSON轉XML'
    model['image'] = '/image/comic-json-to-xml.png'
    return render_template(template_dir + 'template_json_to_xml_tw.html', model=model)


@Web_JsonFormatter_blueprint.route('/tw/xml-to-json', methods=['GET', 'POST'])
def xml_to_json():
    model = get_default_model()
    model['url'] = '/tw/xml-to-json'
    model['enUrl'] = '/xml-to-json'
    model['headerTitle'] = 'XML轉JSON在線工具 - Coding.Tools'
    model['bodyTitle'] = 'XML轉JSON在線工具'
    model['description'] = '這個XML轉JSON在線工具可以幫助您把XML格式的數據字符串轉換成JSON格式的數據字符串.'
    model['keywords'] = 'XML轉JSON, xml to json'
    model['image'] = '/image/comic-xml-to-json.png'
    return render_template(template_dir + 'template_xml_to_json_tw.html', model=model)


@Web_JsonFormatter_blueprint.route('/tw/html-beautifier', methods=['GET', 'POST'])
def html_beautifier():
    model = get_default_model()
    model['url'] = '/tw/html-beautifier'
    model['enUrl'] = '/html-beautifier'
    model['headerTitle'] = 'HTML格式化在線工具 - Coding.Tools'
    model['bodyTitle'] = 'HTML格式化在線工具'
    model['description'] = '這個在線HTML格式化工具可以幫助您將排列混亂的HTML文件格式化為可讀的HTML文件.'
    model['keywords'] = 'html formatter, html beautifier, HTML格式化'
    model['image'] = '/image/comic-html-beautifier.png'
    return render_template(template_dir + 'template_html_beautifier_tw.html', model=model)


@Web_JsonFormatter_blueprint.route('/tw/html-minifier', methods=['GET', 'POST'])
def html_minifier():
    model = get_default_model()
    model['url'] = '/tw/html-minifier'
    model['enUrl'] = '/html-minifier'
    model['headerTitle'] = 'HTML壓縮在線工具 - Coding.Tools'
    model['bodyTitle'] = 'HTML壓縮在線工具'
    model['description'] = '這個HTML壓縮在線工具可以幫助您壓縮原始HTML文件,可以節省空間,以便更快地在網絡中傳輸.'
    model['keywords'] = 'html minifier, HTML壓縮'
    model['image'] = '/image/comic-html-minifier.png'
    return render_template(template_dir + 'template_html_minifier_tw.html', model=model)


@Web_JsonFormatter_blueprint.route('/tw/javascript-beautifier', methods=['GET', 'POST'])
def javascript_beautifier():
    model = get_default_model()
    model['url'] = '/tw/javascript-beautifier'
    model['enUrl'] = '/javascript-beautifier'
    model['headerTitle'] = 'Javascript格式化在線工具 - Coding.Tools'
    model['bodyTitle'] = 'Javascript格式化在線工具'
    model['description'] = '這個在線Javascript格式化工具可以幫助您將排列混亂的Javascript文件格式化為可讀的Javascript文件.'
    model['keywords'] = 'javascript formatter, javascript beautifier, Javascript格式化'
    model['image'] = '/image/comic-javascript-beautifier.png'
    return render_template(template_dir + 'template_javascript_beautifier_tw.html', model=model)


@Web_JsonFormatter_blueprint.route('/tw/javascript-minifier', methods=['GET', 'POST'])
def javascript_minifier():
    model = get_default_model()
    model['url'] = '/tw/javascript-minifier'
    model['enUrl'] = '/javascript-minifier'
    model['headerTitle'] = 'Javascript壓縮在線工具 - Coding.Tools'
    model['bodyTitle'] = 'Javascript壓縮在線工具'
    model['description'] = '這個Javascript壓縮在線工具可以幫助您壓縮原始Javascript文件,可以節省空間,以便更快地在網絡中傳輸.'
    model['keywords'] = 'javascript minifier, Javascript壓縮'
    model['image'] = '/image/comic-javascript-minifier.png'
    return render_template(template_dir + 'template_javascript_minifier_tw.html', model=model)


@Web_JsonFormatter_blueprint.route('/tw/css-beautifier', methods=['GET', 'POST'])
def css_beautifier():
    model = get_default_model()
    model['url'] = '/tw/css-beautifier'
    model['enUrl'] = '/css-beautifier'
    model['headerTitle'] = 'CSS格式化在線工具 - Coding.Tools'
    model['bodyTitle'] = 'CSS格式化在線工具'
    model['description'] = '這個在線CSS格式化工具可以幫助您將排列混亂的CSS文件格式化為可讀的CSS文件.'
    model['keywords'] = 'css formatter, css beautifier, CSS格式化'
    model['image'] = '/image/comic-css-beautifier.png'
    return render_template(template_dir + 'template_css_beautifier_tw.html', model=model)


@Web_JsonFormatter_blueprint.route('/tw/css-minifier', methods=['GET', 'POST'])
def css_minifier():
    model = get_default_model()
    model['url'] = '/tw/css-minifier'
    model['enUrl'] = '/css-minifier'
    model['headerTitle'] = 'CSS壓縮在線工具 - Coding.Tools'
    model['bodyTitle'] = 'CSS壓縮在線工具'
    model['description'] = '這個CSS壓縮在線工具可以幫助您壓縮原始CSS文件,可以節省空間,以便更快地在網絡中傳輸.'
    model['keywords'] = 'css minifier, CSS壓縮'
    model['image'] = '/image/comic-css-minifier.png'
    return render_template(template_dir + 'template_css_minifier_tw.html', model=model)


@Web_JsonFormatter_blueprint.route('/tw/sql-formatter', methods=['GET', 'POST'])
def sql_formatter():
    model = get_default_model()
    model['url'] = '/tw/sql-formatter'
    model['enUrl'] = '/sql-formatter'
    model['headerTitle'] = 'SQL格式化在線工具  - Coding.Tools'
    model['bodyTitle'] = 'SQL格式化在線工具'
    model['description'] = '這個在線SQL格式化工具可以幫助您將排列混亂的SQL字符串格式化為可讀的SQL格式.'
    model['keywords'] = 'sql formatter, SQL格式化'
    model['image'] = '/image/20190308/cartoon_sql_formatter.png'
    return render_template(template_dir + 'template_sql_formatter_tw.html', model=model)


@Web_JsonFormatter_blueprint.route('/tw/sql-minifier', methods=['GET', 'POST'])
def sql_minifier():
    model = get_default_model()
    model['url'] = '/tw/sql-minifier'
    model['enUrl'] = '/sql-minifier'
    model['headerTitle'] = 'SQL壓縮在線工具  - Coding.Tools'
    model['bodyTitle'] = 'SQL壓縮在線工具'
    model['description'] = '這個SQL壓縮在線工具可以幫助您壓縮原始SQL字符串,可以節省您的IDE空間.'
    model['keywords'] = 'sql minifier, SQL壓縮'
    model['image'] = '/image/20190308/cartoon_sql_minifier.png'
    return render_template(template_dir + 'template_sql_minifier_tw.html', model=model)
