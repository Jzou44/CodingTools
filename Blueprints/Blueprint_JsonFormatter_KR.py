from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_JsonFormatter_blueprint = Blueprint('Web_JsonFormatter_blueprint_KR', __name__)
template_dir = 'JsonFormatter/kr/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'ko'
    return model


@Web_JsonFormatter_blueprint.route('/kr/json-formatter', methods=['GET', 'POST'])
def json_formatter():
    model = get_default_model()
    model['url'] = '/kr/json-formatter'
    model['enUrl'] = '/json-formatter'
    model['headerTitle'] = 'JSON 서식 온라인 도구  - Coding.Tools'
    model['bodyTitle'] = 'JSON 서식 온라인 도구'
    model['description'] = '이 온라인 JSON 형식 도구는 혼동을 유발하는 JSON 문자열을 읽을 수있는 JSON 문자열로 포맷하는 데 도움을줍니다.'
    model['keywords'] = 'Json 포맷터, JSON 포맷팅'
    model['image'] = '/image/comic-json-formatter.png'
    return render_template(template_dir + 'template_json_formatter_kr.html', model=model)


@Web_JsonFormatter_blueprint.route('/kr/json-minifier', methods=['GET', 'POST'])
def json_minifier():
    model = get_default_model()
    model['url'] = '/kr/json-minifier'
    model['enUrl'] = '/json-minifier'
    model['headerTitle'] = 'JSON 압축 온라인 도구  - Coding.Tools'
    model['bodyTitle'] = 'JSON 압축 온라인 도구'
    model['description'] = '이 JSON 압축 온라인 도구는 원래 JSON 문자열을 압축하여 네트워크를 통해 더 빠른 전송을위한 공간을 절약합니다.'
    model['keywords'] = 'JSON 압축기, JSON 압축기'
    model['image'] = '/image/comic-json-minifier.png'
    return render_template(template_dir + 'template_json_minifier_kr.html', model=model)


@Web_JsonFormatter_blueprint.route('/kr/xml-formatter', methods=['GET', 'POST'])
def xml_formatter():
    model = get_default_model()
    model['url'] = '/kr/xml-formatter'
    model['enUrl'] = '/xml-formatter'
    model['headerTitle'] = 'XML 서식 지정 온라인 도구  - Coding.Tools'
    model['bodyTitle'] = 'XML 서식 지정 온라인 도구'
    model['description'] = '이 온라인 XML 서식 도구는 복잡한 XML 문자열을 읽을 수있는 XML 문자열로 포맷하는 데 도움을줍니다.'
    model['keywords'] = 'XML 포맷터, XML 형식'
    model['image'] = '/image/comic-xml-formatter.png'
    return render_template(template_dir + 'template_xml_formatter_kr.html', model=model)


@Web_JsonFormatter_blueprint.route('/kr/xml-minifier', methods=['GET', 'POST'])
def xml_minifier():
    model = get_default_model()
    model['url'] = '/kr/xml-minifier'
    model['enUrl'] = '/xml-minifier'
    model['headerTitle'] = 'XML 압축 온라인 도구  - Coding.Tools'
    model['bodyTitle'] = 'XML 압축 온라인 도구'
    model['description'] = '이 XML 압축 온라인 도구는 원시 XML 문자열을 압축하여 네트워크를 통해보다 빠른 전송을위한 공간을 절약합니다.'
    model['keywords'] = 'XML 압축기, XML 압축'
    model['image'] = '/image/comic-xml-minifier.png'
    return render_template(template_dir + 'template_xml_minifier_kr.html', model=model)


@Web_JsonFormatter_blueprint.route('/kr/json-to-xml', methods=['GET', 'POST'])
def json_to_xml():
    model = get_default_model()
    model['url'] = '/kr/json-to-xml'
    model['enUrl'] = '/json-to-xml'
    model['headerTitle'] = 'JSON에서 XML 온라인 도구로  - Coding.Tools'
    model['bodyTitle'] = 'JSON에서 XML 온라인 도구로'
    model['description'] = '이 JSON to XML 온라인 도구는 JSON 형식의 데이터 문자열을 XML 형식의 데이터 문자열로 변환하는 데 도움을줍니다.'
    model['keywords'] = 'Json에서 XML로, JSON에서 XML로'
    model['image'] = '/image/comic-json-to-xml.png'
    return render_template(template_dir + 'template_json_to_xml_kr.html', model=model)


@Web_JsonFormatter_blueprint.route('/kr/xml-to-json', methods=['GET', 'POST'])
def xml_to_json():
    model = get_default_model()
    model['url'] = '/kr/xml-to-json'
    model['enUrl'] = '/xml-to-json'
    model['headerTitle'] = 'XML에서 JSON 온라인 도구로  - Coding.Tools'
    model['bodyTitle'] = 'XML에서 JSON 온라인 도구로'
    model['description'] = '이 XML to JSON 온라인 도구는 XML 형식의 데이터 문자열을 JSON 형식의 데이터 문자열로 변환하는 데 유용합니다.'
    model['keywords'] = 'XML을 JSON으로, XML을 json으로'
    model['image'] = '/image/comic-xml-to-json.png'
    return render_template(template_dir + 'template_xml_to_json_kr.html', model=model)


@Web_JsonFormatter_blueprint.route('/kr/html-beautifier', methods=['GET', 'POST'])
def html_beautifier():
    model = get_default_model()
    model['url'] = '/kr/html-beautifier'
    model['enUrl'] = '/html-beautifier'
    model['headerTitle'] = 'HTML 서식 온라인 도구  - Coding.Tools'
    model['bodyTitle'] = 'HTML 서식 온라인 도구'
    model['description'] = '이 온라인 HTML 서식 도구는 혼란스러운 HTML 파일을 읽을 수있는 HTML 파일로 포맷하는 데 도움을줍니다.'
    model['keywords'] = 'HTML 포맷터, html 미인, HTML 형식'
    model['image'] = '/image/comic-html-beautifier.png'
    return render_template(template_dir + 'template_html_beautifier_kr.html', model=model)


@Web_JsonFormatter_blueprint.route('/kr/html-minifier', methods=['GET', 'POST'])
def html_minifier():
    model = get_default_model()
    model['url'] = '/kr/html-minifier'
    model['enUrl'] = '/html-minifier'
    model['headerTitle'] = 'HTML 압축 온라인 도구  - Coding.Tools'
    model['bodyTitle'] = 'HTML 압축 온라인 도구'
    model['description'] = '이 HTML 압축 온라인 도구는 원본 HTML 파일을 압축하여 네트워크를 통해보다 빠른 전송을위한 공간을 절약합니다.'
    model['keywords'] = 'HTML 축소 기, HTML 압축'
    model['image'] = '/image/comic-html-minifier.png'
    return render_template(template_dir + 'template_html_minifier_kr.html', model=model)


@Web_JsonFormatter_blueprint.route('/kr/javascript-beautifier', methods=['GET', 'POST'])
def javascript_beautifier():
    model = get_default_model()
    model['url'] = '/kr/javascript-beautifier'
    model['enUrl'] = '/javascript-beautifier'
    model['headerTitle'] = '자바 스크립트 온라인 서식 지정 도구  - Coding.Tools'
    model['bodyTitle'] = 'Javascript 서식 온라인 도구'
    model['description'] = '이 온라인 Javascript 서식 도구는 혼동스러운 Javascript 파일을 읽을 수있는 Javascript 파일로 형식화하는 데 도움을 줄 수 있습니다.'
    model['keywords'] = '자바 스크립트 포맷터, 자바 스크립트 미화, 자바 스크립트 포맷'
    model['image'] = '/image/comic-javascript-beautifier.png'
    return render_template(template_dir + 'template_javascript_beautifier_kr.html', model=model)


@Web_JsonFormatter_blueprint.route('/kr/javascript-minifier', methods=['GET', 'POST'])
def javascript_minifier():
    model = get_default_model()
    model['url'] = '/kr/javascript-minifier'
    model['enUrl'] = '/javascript-minifier'
    model['headerTitle'] = '자바 스크립트 압축 온라인 도구  - Coding.Tools'
    model['bodyTitle'] = '자바 스크립트 압축 온라인 도구'
    model['description'] = '이 Javascript 압축 온라인 도구는 원본 Javascript 파일을 압축하여 네트워크를 통해보다 빠른 전송을위한 공간을 절약합니다.'
    model['keywords'] = 'Javascript 축소 자, Javascript 압축'
    model['image'] = '/image/comic-javascript-minifier.png'
    return render_template(template_dir + 'template_javascript_minifier_kr.html', model=model)


@Web_JsonFormatter_blueprint.route('/kr/css-beautifier', methods=['GET', 'POST'])
def css_beautifier():
    model = get_default_model()
    model['url'] = '/kr/css-beautifier'
    model['enUrl'] = '/css-beautifier'
    model['headerTitle'] = 'CSS 도구 온라인 서식 지정  - Coding.Tools'
    model['bodyTitle'] = 'CSS 서식 온라인 도구'
    model['description'] = '이 온라인 CSS 서식 도구는 혼동스러운 CSS 파일을 읽을 수있는 CSS 파일로 포맷하는 데 도움을줍니다.'
    model['keywords'] = 'CSS 포매터, CSS 미화, CSS 포맷'
    model['image'] = '/image/comic-css-beautifier.png'
    return render_template(template_dir + 'template_css_beautifier_kr.html', model=model)


@Web_JsonFormatter_blueprint.route('/kr/css-minifier', methods=['GET', 'POST'])
def css_minifier():
    model = get_default_model()
    model['url'] = '/kr/css-minifier'
    model['enUrl'] = '/css-minifier'
    model['headerTitle'] = 'CSS 압축 온라인 도구  - Coding.Tools'
    model['bodyTitle'] = 'CSS 압축 온라인 도구'
    model['description'] = '이 CSS 압축 온라인 도구는 원본 CSS 파일을 압축하여 네트워크를 통해보다 빠르게 전송할 수있는 공간을 절약합니다.'
    model['keywords'] = 'CSS 축소 기, CSS 압축'
    model['image'] = '/image/comic-css-minifier.png'
    return render_template(template_dir + 'template_css_minifier_kr.html', model=model)
