from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_JsonFormatter_blueprint = Blueprint('Web_JsonFormatter_blueprint_JP', __name__)
template_dir = 'JsonFormatter/jp/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'ja'
    return model


@Web_JsonFormatter_blueprint.route('/jp/json-formatter', methods=['GET', 'POST'])
def json_formatter():
    model = get_default_model()
    model['url'] = '/jp/json-formatter'
    model['enUrl'] = '/json-formatter'
    model['headerTitle'] = 'JSONフォーマット化オンラインツール  - Coding.Tools'
    model['bodyTitle'] = 'JSONフォーマットオンラインツール'
    model['description'] = 'このオンラインJSONフォーマット設定ツールは、混乱しやすいJSONストリングを読み取り可能なJSONストリングにフォーマット設定するのに役立ちます。'
    model['keywords'] = 'Jsonフォーマッタ、JSONフォーマット'
    model['image'] = '/image/comic-json-formatter.png'
    return render_template(template_dir + 'template_json_formatter_jp.html', model=model)


@Web_JsonFormatter_blueprint.route('/jp/json-minifier', methods=['GET', 'POST'])
def json_minifier():
    model = get_default_model()
    model['url'] = '/jp/json-minifier'
    model['enUrl'] = '/json-minifier'
    model['headerTitle'] = 'JSON圧縮オンラインツール  - Coding.Tools'
    model['bodyTitle'] = 'JSON圧縮オンラインツール'
    model['description'] = 'このJSON圧縮オンラインツールを使用すると、元のJSON文字列を圧縮し、ネットワークを介した転送を高速化するためのスペースを節約できます。'
    model['keywords'] = 'Jsonミニファイア、JSON圧縮'
    model['image'] = '/image/comic-json-minifier.png'
    return render_template(template_dir + 'template_json_minifier_jp.html', model=model)


@Web_JsonFormatter_blueprint.route('/jp/xml-formatter', methods=['GET', 'POST'])
def xml_formatter():
    model = get_default_model()
    model['url'] = '/jp/xml-formatter'
    model['enUrl'] = '/xml-formatter'
    model['headerTitle'] = 'XMLフォーマットオンラインツール  - Coding.Tools'
    model['bodyTitle'] = 'XMLフォーマットオンラインツール'
    model['description'] = 'このオンラインXMLフォーマット化ツールは、混乱しやすいXMLストリングを読みやすいXMLストリングにフォーマットするのに役立ちます。'
    model['keywords'] = 'XMLフォーマッター、XMLフォーマット'
    model['image'] = '/image/comic-xml-formatter.png'
    return render_template(template_dir + 'template_xml_formatter_jp.html', model=model)


@Web_JsonFormatter_blueprint.route('/jp/xml-minifier', methods=['GET', 'POST'])
def xml_minifier():
    model = get_default_model()
    model['url'] = '/jp/xml-minifier'
    model['enUrl'] = '/xml-minifier'
    model['headerTitle'] = 'XML圧縮オンラインツール  - Coding.Tools'
    model['bodyTitle'] = 'XML圧縮オンラインツール'
    model['description'] = 'このXML圧縮オンラインツールを使用すると、生のXML文字列を圧縮し、ネットワークを介した転送を高速化するためのスペースを節約できます。'
    model['keywords'] = 'XMLミニファイア、XML圧縮'
    model['image'] = '/image/comic-xml-minifier.png'
    return render_template(template_dir + 'template_xml_minifier_jp.html', model=model)


@Web_JsonFormatter_blueprint.route('/jp/json-to-xml', methods=['GET', 'POST'])
def json_to_xml():
    model = get_default_model()
    model['url'] = '/jp/json-to-xml'
    model['enUrl'] = '/json-to-xml'
    model['headerTitle'] = 'JSON to XMLオンラインツール  - Coding.Tools'
    model['bodyTitle'] = 'JSON to XMLオンラインツール'
    model['description'] = 'このJSON to XMLオンラインツールは、JSON形式のデータ文字列をXML形式のデータ文字列に変換するのに役立ちます。'
    model['keywords'] = 'Jsonからxmlへ、JSONからXMLへ'
    model['image'] = '/image/comic-json-to-xml.png'
    return render_template(template_dir + 'template_json_to_xml_jp.html', model=model)


@Web_JsonFormatter_blueprint.route('/jp/xml-to-json', methods=['GET', 'POST'])
def xml_to_json():
    model = get_default_model()
    model['url'] = '/jp/xml-to-json'
    model['enUrl'] = '/xml-to-json'
    model['headerTitle'] = 'XMLからJSONへのオンラインツール  - Coding.Tools'
    model['bodyTitle'] = 'XML to JSONオンラインツール'
    model['description'] = 'このXML to JSONオンラインツールは、XML形式のデータ文字列をJSON形式のデータ文字列に変換するのに役立ちます。'
    model['keywords'] = 'XMLからJSONへ、xmlからjsonへ'
    model['image'] = '/image/comic-xml-to-json.png'
    return render_template(template_dir + 'template_xml_to_json_jp.html', model=model)


@Web_JsonFormatter_blueprint.route('/jp/html-beautifier', methods=['GET', 'POST'])
def html_beautifier():
    model = get_default_model()
    model['url'] = '/jp/html-beautifier'
    model['enUrl'] = '/html-beautifier'
    model['headerTitle'] = 'HTMLフォーマットオンラインツール  - Coding.Tools'
    model['bodyTitle'] = 'HTMLフォーマットオンラインツール'
    model['description'] = 'このオンラインHTMLフォーマットツールを使用すると、わかりにくいHTMLファイルを読みやすいHTMLファイルにフォーマットできます。'
    model['keywords'] = 'HTMLフォーマッタ、HTML美化、HTMLフォーマット'
    model['image'] = '/image/comic-html-beautifier.png'
    return render_template(template_dir + 'template_html_beautifier_jp.html', model=model)


@Web_JsonFormatter_blueprint.route('/jp/html-minifier', methods=['GET', 'POST'])
def html_minifier():
    model = get_default_model()
    model['url'] = '/jp/html-minifier'
    model['enUrl'] = '/html-minifier'
    model['headerTitle'] = 'HTML圧縮オンラインツール  - Coding.Tools'
    model['bodyTitle'] = 'HTML圧縮オンラインツール'
    model['description'] = 'このHTML圧縮オンラインツールを使用すると、オリジナルのHTMLファイルを圧縮して、ネットワーク経由での転送速度を上げるためのスペースを節約できます。'
    model['keywords'] = 'HTMLミニファイア、HTML圧縮'
    model['image'] = '/image/comic-html-minifier.png'
    return render_template(template_dir + 'template_html_minifier_jp.html', model=model)


@Web_JsonFormatter_blueprint.route('/jp/javascript-beautifier', methods=['GET', 'POST'])
def javascript_beautifier():
    model = get_default_model()
    model['url'] = '/jp/javascript-beautifier'
    model['enUrl'] = '/javascript-beautifier'
    model['headerTitle'] = 'Javascriptフォーマットオンラインツール  - Coding.Tools'
    model['bodyTitle'] = 'Javascriptフォーマットオンラインツール'
    model['description'] = 'このオンラインJavascriptフォーマットツールを使用すると、わかりにくいJavascriptファイルを読みやすいJavascriptファイルにフォーマットできます。'
    model['keywords'] = 'Javascriptフォーマッタ、Javascriptビューア、Javascriptフォーマット'
    model['image'] = '/image/comic-javascript-beautifier.png'
    return render_template(template_dir + 'template_javascript_beautifier_jp.html', model=model)


@Web_JsonFormatter_blueprint.route('/jp/javascript-minifier', methods=['GET', 'POST'])
def javascript_minifier():
    model = get_default_model()
    model['url'] = '/jp/javascript-minifier'
    model['enUrl'] = '/javascript-minifier'
    model['headerTitle'] = 'Javascript圧縮オンラインツール  - Coding.Tools'
    model['bodyTitle'] = 'Javascript圧縮オンラインツール'
    model['description'] = 'このJavascript圧縮オンラインツールを使用すると、オリジナルのJavascriptファイルを圧縮し、ネットワークを介した転送を高速化するためのスペースを節約できます。'
    model['keywords'] = 'Javascript minifier、Javascriptの圧縮'
    model['image'] = '/image/comic-javascript-minifier.png'
    return render_template(template_dir + 'template_javascript_minifier_jp.html', model=model)


@Web_JsonFormatter_blueprint.route('/jp/css-beautifier', methods=['GET', 'POST'])
def css_beautifier():
    model = get_default_model()
    model['url'] = '/jp/css-beautifier'
    model['enUrl'] = '/css-beautifier'
    model['headerTitle'] = 'CSSフォーマットオンラインツール  - Coding.Tools'
    model['bodyTitle'] = 'CSSフォーマットオンラインツール'
    model['description'] = 'このオンラインCSSフォーマットツールは、わかりにくいCSSファイルを読みやすいCSSファイルにフォーマットするのに役立ちます。'
    model['keywords'] = 'CSSフォーマッタ、CSS美化、CSSフォーマット'
    model['image'] = '/image/comic-css-beautifier.png'
    return render_template(template_dir + 'template_css_beautifier_jp.html', model=model)


@Web_JsonFormatter_blueprint.route('/jp/css-minifier', methods=['GET', 'POST'])
def css_minifier():
    model = get_default_model()
    model['url'] = '/jp/css-minifier'
    model['enUrl'] = '/css-minifier'
    model['headerTitle'] = 'CSS圧縮オンラインツール  - Coding.Tools'
    model['bodyTitle'] = 'CSS圧縮オンラインツール'
    model['description'] = 'このCSS圧縮オンラインツールを使用すると、元のCSSファイルを圧縮して、ネットワーク経由での転送速度を上げるためのスペースを節約できます。'
    model['keywords'] = 'CSSミニファイア、CSS圧縮'
    model['image'] = '/image/comic-css-minifier.png'
    return render_template(template_dir + 'template_css_minifier_jp.html', model=model)
