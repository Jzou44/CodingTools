from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_JsonFormatter_blueprint = Blueprint('Web_JsonFormatter_blueprint_CN', __name__)
template_dir = 'JsonFormatter/cn/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'zh-Hans'
    return model


@Web_JsonFormatter_blueprint.route('/cn/json-formatter', methods=['GET', 'POST'])
def json_formatter():
    model = get_default_model()
    model['url'] = '/cn/json-formatter'
    model['enUrl'] = '/json-formatter'
    model['headerTitle'] = 'JSON格式化在线工具  - Coding.Tools'
    model['bodyTitle'] = 'JSON格式化在线工具'
    model['description'] = '这个在线JSON格式化工具可以帮助您将排列混乱的JSON字符串格式化为可读的JSON字符串.'
    model['keywords'] = 'json formatter, JSON格式化'
    model['image'] = '/image/comic-json-formatter.png'
    return render_template(template_dir + 'template_json_formatter_cn.html', model=model)


@Web_JsonFormatter_blueprint.route('/cn/json-minifier', methods=['GET', 'POST'])
def json_minifier():
    model = get_default_model()
    model['url'] = '/cn/json-minifier'
    model['enUrl'] = '/json-minifier'
    model['headerTitle'] = 'JSON压缩在线工具  - Coding.Tools'
    model['bodyTitle'] = 'JSON压缩在线工具'
    model['description'] = '这个JSON压缩在线工具可以帮助您压缩原始JSON字符串,可以节省空间,以便更快地在网络中传输.'
    model['keywords'] = 'json minifier, JSON压缩'
    model['image'] = '/image/comic-json-minifier.png'
    return render_template(template_dir + 'template_json_minifier_cn.html', model=model)


@Web_JsonFormatter_blueprint.route('/cn/xml-formatter', methods=['GET', 'POST'])
def xml_formatter():
    model = get_default_model()
    model['url'] = '/cn/xml-formatter'
    model['enUrl'] = '/xml-formatter'
    model['headerTitle'] = 'XML格式化在线工具  - Coding.Tools'
    model['bodyTitle'] = 'XML格式化在线工具'
    model['description'] = '这个在线XML格式化工具可以帮助您将排列混乱的XML字符串格式化为可读的XML字符串.'
    model['keywords'] = 'xml formatter, XML格式化'
    model['image'] = '/image/comic-xml-formatter.png'
    return render_template(template_dir + 'template_xml_formatter_cn.html', model=model)


@Web_JsonFormatter_blueprint.route('/cn/xml-minifier', methods=['GET', 'POST'])
def xml_minifier():
    model = get_default_model()
    model['url'] = '/cn/xml-minifier'
    model['enUrl'] = '/xml-minifier'
    model['headerTitle'] = 'XML压缩在线工具  - Coding.Tools'
    model['bodyTitle'] = 'XML压缩在线工具'
    model['description'] = '这个XML压缩在线工具可以帮助您压缩原始XML字符串,可以节省空间,以便更快地在网络中传输.'
    model['keywords'] = 'xml minifier, XML压缩'
    model['image'] = '/image/comic-xml-minifier.png'
    return render_template(template_dir + 'template_xml_minifier_cn.html', model=model)


@Web_JsonFormatter_blueprint.route('/cn/json-to-xml', methods=['GET', 'POST'])
def json_to_xml():
    model = get_default_model()
    model['url'] = '/cn/json-to-xml'
    model['enUrl'] = '/json-to-xml'
    model['headerTitle'] = 'JSON转XML在线工具  - Coding.Tools'
    model['bodyTitle'] = 'JSON转XML在线工具'
    model['description'] = '这个JSON转XML在线工具可以帮助您把JSON格式的数据字符串转换成XML格式的数据字符串.'
    model['keywords'] = 'json to xml, JSON转XML'
    model['image'] = '/image/comic-json-to-xml.png'
    return render_template(template_dir + 'template_json_to_xml_cn.html', model=model)


@Web_JsonFormatter_blueprint.route('/cn/xml-to-json', methods=['GET', 'POST'])
def xml_to_json():
    model = get_default_model()
    model['url'] = '/cn/xml-to-json'
    model['enUrl'] = '/xml-to-json'
    model['headerTitle'] = 'XML转JSON在线工具  - Coding.Tools'
    model['bodyTitle'] = 'XML转JSON在线工具'
    model['description'] = '这个XML转JSON在线工具可以帮助您把XML格式的数据字符串转换成JSON格式的数据字符串.'
    model['keywords'] = 'XML转JSON, xml to json'
    model['image'] = '/image/comic-xml-to-json.png'
    return render_template(template_dir + 'template_xml_to_json_cn.html', model=model)


@Web_JsonFormatter_blueprint.route('/cn/html-beautifier', methods=['GET', 'POST'])
def html_beautifier():
    model = get_default_model()
    model['url'] = '/cn/html-beautifier'
    model['enUrl'] = '/html-beautifier'
    model['headerTitle'] = 'HTML格式化在线工具  - Coding.Tools'
    model['bodyTitle'] = 'HTML格式化在线工具'
    model['description'] = '这个在线HTML格式化工具可以帮助您将排列混乱的HTML文件格式化为可读的HTML文件.'
    model['keywords'] = 'html formatter, html beautifier, HTML格式化'
    model['image'] = '/image/comic-html-beautifier.png'
    return render_template(template_dir + 'template_html_beautifier_cn.html', model=model)


@Web_JsonFormatter_blueprint.route('/cn/html-minifier', methods=['GET', 'POST'])
def html_minifier():
    model = get_default_model()
    model['url'] = '/cn/html-minifier'
    model['enUrl'] = '/html-minifier'
    model['headerTitle'] = 'HTML压缩在线工具  - Coding.Tools'
    model['bodyTitle'] = 'HTML压缩在线工具'
    model['description'] = '这个HTML压缩在线工具可以帮助您压缩原始HTML文件,可以节省空间,以便更快地在网络中传输.'
    model['keywords'] = 'html minifier, HTML压缩'
    model['image'] = '/image/comic-html-minifier.png'
    return render_template(template_dir + 'template_html_minifier_cn.html', model=model)


@Web_JsonFormatter_blueprint.route('/cn/javascript-beautifier', methods=['GET', 'POST'])
def javascript_beautifier():
    model = get_default_model()
    model['url'] = '/cn/javascript-beautifier'
    model['enUrl'] = '/javascript-beautifier'
    model['headerTitle'] = 'Javascript格式化在线工具  - Coding.Tools'
    model['bodyTitle'] = 'Javascript格式化在线工具'
    model['description'] = '这个在线Javascript格式化工具可以帮助您将排列混乱的Javascript文件格式化为可读的Javascript文件.'
    model['keywords'] = 'javascript formatter, javascript beautifier, Javascript格式化'
    model['image'] = '/image/comic-javascript-beautifier.png'
    return render_template(template_dir + 'template_javascript_beautifier_cn.html', model=model)


@Web_JsonFormatter_blueprint.route('/cn/javascript-minifier', methods=['GET', 'POST'])
def javascript_minifier():
    model = get_default_model()
    model['url'] = '/cn/javascript-minifier'
    model['enUrl'] = '/javascript-minifier'
    model['headerTitle'] = 'Javascript压缩在线工具  - Coding.Tools'
    model['bodyTitle'] = 'Javascript压缩在线工具'
    model['description'] = '这个Javascript压缩在线工具可以帮助您压缩原始Javascript文件,可以节省空间,以便更快地在网络中传输.'
    model['keywords'] = 'javascript minifier, Javascript压缩'
    model['image'] = '/image/comic-javascript-minifier.png'
    return render_template(template_dir + 'template_javascript_minifier_cn.html', model=model)


@Web_JsonFormatter_blueprint.route('/cn/css-beautifier', methods=['GET', 'POST'])
def css_beautifier():
    model = get_default_model()
    model['url'] = '/cn/css-beautifier'
    model['enUrl'] = '/css-beautifier'
    model['headerTitle'] = 'CSS格式化在线工具  - Coding.Tools'
    model['bodyTitle'] = 'CSS格式化在线工具'
    model['description'] = '这个在线CSS格式化工具可以帮助您将排列混乱的CSS文件格式化为可读的CSS文件.'
    model['keywords'] = 'css formatter, css beautifier, CSS格式化'
    model['image'] = '/image/comic-css-beautifier.png'
    return render_template(template_dir + 'template_css_beautifier_cn.html', model=model)


@Web_JsonFormatter_blueprint.route('/cn/css-minifier', methods=['GET', 'POST'])
def css_minifier():
    model = get_default_model()
    model['url'] = '/cn/css-minifier'
    model['enUrl'] = '/css-minifier'
    model['headerTitle'] = 'CSS压缩在线工具  - Coding.Tools'
    model['bodyTitle'] = 'CSS压缩在线工具'
    model['description'] = '这个CSS压缩在线工具可以帮助您压缩原始CSS文件,可以节省空间,以便更快地在网络中传输.'
    model['keywords'] = 'css minifier, CSS压缩'
    model['image'] = '/image/comic-css-minifier.png'
    return render_template(template_dir + 'template_css_minifier_cn.html', model=model)


@Web_JsonFormatter_blueprint.route('/cn/sql-formatter', methods=['GET', 'POST'])
def sql_formatter():
    model = get_default_model()
    model['url'] = '/cn/sql-formatter'
    model['enUrl'] = '/sql-formatter'
    model['headerTitle'] = 'SQL格式化在线工具  - Coding.Tools'
    model['bodyTitle'] = 'SQL格式化在线工具'
    model['description'] = '这个在线SQL格式化工具可以帮助您将排列混乱的SQL字符串格式化为可读的SQL格式.'
    model['keywords'] = 'sql formatter, SQL格式化'
    model['image'] = '/image/20190308/cartoon_sql_formatter.png'
    return render_template(template_dir + 'template_sql_formatter_cn.html', model=model)


@Web_JsonFormatter_blueprint.route('/cn/sql-minifier', methods=['GET', 'POST'])
def sql_minifier():
    model = get_default_model()
    model['url'] = '/cn/sql-minifier'
    model['enUrl'] = '/sql-minifier'
    model['headerTitle'] = 'SQL压缩在线工具  - Coding.Tools'
    model['bodyTitle'] = 'SQL压缩在线工具'
    model['description'] = '这个SQL压缩在线工具可以帮助您压缩原始SQL字符串,可以节省您的IDE空间.'
    model['keywords'] = 'sql minifier, SQL压缩'
    model['image'] = '/image/20190308/cartoon_sql_minifier.png'
    return render_template(template_dir + 'template_sql_minifier_cn.html', model=model)
