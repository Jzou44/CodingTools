from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_JsonFormatter_blueprint = Blueprint('Web_JsonFormatter_blueprint_AR', __name__)
template_dir = 'JsonFormatter/ar/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'ar'
    return model


@Web_JsonFormatter_blueprint.route('/ar/json-formatter', methods=['GET', 'POST'])
def json_formatter():
    model = get_default_model()
    model['url'] = '/ar/json-formatter'
    model['enUrl'] = '/json-formatter'
    model['headerTitle'] = 'JSON تنسيق أداة عبر الإنترنت  - Coding.Tools'
    model['bodyTitle'] = 'JSON تنسيق أداة على الإنترنت'
    model['description'] = 'يمكن لأداة تنسيق JSON عبر الإنترنت مساعدتك على تنسيق مربعات JSON المربكة في سلاسل JSON القابلة للقراءة.'
    model['keywords'] = 'منسق Json ، تنسيق JSON'
    model['image'] = '/image/comic-json-formatter.png'
    return render_template(template_dir + 'template_json_formatter_ar.html', model=model)


@Web_JsonFormatter_blueprint.route('/ar/json-minifier', methods=['GET', 'POST'])
def json_minifier():
    model = get_default_model()
    model['url'] = '/ar/json-minifier'
    model['enUrl'] = '/json-minifier'
    model['headerTitle'] = 'أداة ضغط JSON على الإنترنت  - Coding.Tools'
    model['bodyTitle'] = 'ضغط JSON أداة على الانترنت'
    model['description'] = 'تساعدك أداة ضغط JSON على الإنترنت على ضغط سلاسل JSON الأصلية ، مما يوفر مساحة لنقل أسرع عبر الشبكة.'
    model['keywords'] = 'Json minifier ، JSON compression'
    model['image'] = '/image/comic-json-minifier.png'
    return render_template(template_dir + 'template_json_minifier_ar.html', model=model)


@Web_JsonFormatter_blueprint.route('/ar/xml-formatter', methods=['GET', 'POST'])
def xml_formatter():
    model = get_default_model()
    model['url'] = '/ar/xml-formatter'
    model['enUrl'] = '/xml-formatter'
    model['headerTitle'] = 'أداة تنسيق XML عبر الإنترنت  - Coding.Tools'
    model['bodyTitle'] = 'XML تنسيق أداة عبر الإنترنت'
    model['description'] = 'يمكن لأداة تنسيق XML عبر الإنترنت هذه أن تساعدك على تنسيق سلاسل XML المربكة في سلاسل XML القابلة للقراءة.'
    model['keywords'] = 'منسق Xml ، تنسيق XML'
    model['image'] = '/image/comic-xml-formatter.png'
    return render_template(template_dir + 'template_xml_formatter_ar.html', model=model)


@Web_JsonFormatter_blueprint.route('/ar/xml-minifier', methods=['GET', 'POST'])
def xml_minifier():
    model = get_default_model()
    model['url'] = '/ar/xml-minifier'
    model['enUrl'] = '/xml-minifier'
    model['headerTitle'] = 'أداة ضغط XML عبر الإنترنت  - Coding.Tools'
    model['bodyTitle'] = 'أداة ضغط XML عبر الإنترنت'
    model['description'] = 'تساعدك أداة ضغط XML المتوفرة عبر الإنترنت على ضغط سلاسل XML الأولية ، مما يوفر مساحة لنقل أسرع عبر الشبكة.'
    model['keywords'] = 'Xml minifier ، وضغط XML'
    model['image'] = '/image/comic-xml-minifier.png'
    return render_template(template_dir + 'template_xml_minifier_ar.html', model=model)


@Web_JsonFormatter_blueprint.route('/ar/json-to-xml', methods=['GET', 'POST'])
def json_to_xml():
    model = get_default_model()
    model['url'] = '/ar/json-to-xml'
    model['enUrl'] = '/json-to-xml'
    model['headerTitle'] = 'JSON to XML online tool  - Coding.Tools'
    model['bodyTitle'] = 'JSON إلى أداة XML عبر الإنترنت'
    model['description'] = 'يمكن أن تساعدك أداة JSON to XML عبر الإنترنت على تحويل سلاسل البيانات بتنسيق JSON إلى سلاسل بيانات بتنسيق XML.'
    model['keywords'] = 'Json to xml، JSON to XML'
    model['image'] = '/image/comic-json-to-xml.png'
    return render_template(template_dir + 'template_json_to_xml_ar.html', model=model)


@Web_JsonFormatter_blueprint.route('/ar/xml-to-json', methods=['GET', 'POST'])
def xml_to_json():
    model = get_default_model()
    model['url'] = '/ar/xml-to-json'
    model['enUrl'] = '/xml-to-json'
    model['headerTitle'] = 'XML to JSON online tool  - Coding.Tools'
    model['bodyTitle'] = 'XML to JSON online tool'
    model['description'] = 'يمكن أن تساعدك أداة XML إلى JSON عبر الإنترنت في تحويل سلاسل البيانات بتنسيق XML إلى سلاسل بيانات بتنسيق JSON.'
    model['keywords'] = 'XML إلى JSON ، xml to json'
    model['image'] = '/image/comic-xml-to-json.png'
    return render_template(template_dir + 'template_xml_to_json_ar.html', model=model)


@Web_JsonFormatter_blueprint.route('/ar/html-beautifier', methods=['GET', 'POST'])
def html_beautifier():
    model = get_default_model()
    model['url'] = '/ar/html-beautifier'
    model['enUrl'] = '/html-beautifier'
    model['headerTitle'] = 'HTML تنسيق أداة عبر الإنترنت  - Coding.Tools'
    model['bodyTitle'] = 'HTML تنسيق أداة على الإنترنت'
    model['description'] = 'يمكن لأداة تنسيق HTML عبر الإنترنت هذه أن تساعدك على تنسيق ملفات HTML المربكة في ملفات HTML القابلة للقراءة.'
    model['keywords'] = 'هتمل المنسق ، أتش تي أم أل تجميل ، تنسيق HTML'
    model['image'] = '/image/comic-html-beautifier.png'
    return render_template(template_dir + 'template_html_beautifier_ar.html', model=model)


@Web_JsonFormatter_blueprint.route('/ar/html-minifier', methods=['GET', 'POST'])
def html_minifier():
    model = get_default_model()
    model['url'] = '/ar/html-minifier'
    model['enUrl'] = '/html-minifier'
    model['headerTitle'] = 'أداة ضغط HTML عبر الإنترنت  - Coding.Tools'
    model['bodyTitle'] = 'أداة ضغط HTML عبر الإنترنت'
    model['description'] = 'تساعدك أداة ضغط HTML عبر الإنترنت هذه في ضغط ملفات HTML الأصلية ، مما يوفر مساحة لنقل أسرع عبر الشبكة.'
    model['keywords'] = 'Html minifier ، ضغط HTML'
    model['image'] = '/image/comic-html-minifier.png'
    return render_template(template_dir + 'template_html_minifier_ar.html', model=model)


@Web_JsonFormatter_blueprint.route('/ar/javascript-beautifier', methods=['GET', 'POST'])
def javascript_beautifier():
    model = get_default_model()
    model['url'] = '/ar/javascript-beautifier'
    model['enUrl'] = '/javascript-beautifier'
    model['headerTitle'] = 'Javascript تنسيق أداة عبر الإنترنت  - Coding.Tools'
    model['bodyTitle'] = 'جافا سكريبت تنسيق أداة على الإنترنت'
    model['description'] = 'يمكن لأداة تنسيق جافا سكريبت عبر الإنترنت مساعدتك على تنسيق ملفات جافا سكريبت المشوشة في ملفات جافا سكريبت قابلة للقراءة.'
    model['keywords'] = 'تنسيق Javascript ، javascript beautifier ، تنسيق جافا سكريبت'
    model['image'] = '/image/comic-javascript-beautifier.png'
    return render_template(template_dir + 'template_javascript_beautifier_ar.html', model=model)


@Web_JsonFormatter_blueprint.route('/ar/javascript-minifier', methods=['GET', 'POST'])
def javascript_minifier():
    model = get_default_model()
    model['url'] = '/ar/javascript-minifier'
    model['enUrl'] = '/javascript-minifier'
    model['headerTitle'] = 'أداة ضغط على الإنترنت من Javascript  - Coding.Tools'
    model['bodyTitle'] = 'أداة ضغط على الإنترنت من Javascript'
    model['description'] = 'تساعدك أداة الضغط على الجافاسكريبت على الإنترنت في ضغط ملفات Javascript الأصلية ، مما يوفر مساحة لنقل أسرع عبر الشبكة.'
    model['keywords'] = 'منبه جافا سكريبت ، ضغط جافا سكريبت'
    model['image'] = '/image/comic-javascript-minifier.png'
    return render_template(template_dir + 'template_javascript_minifier_ar.html', model=model)


@Web_JsonFormatter_blueprint.route('/ar/css-beautifier', methods=['GET', 'POST'])
def css_beautifier():
    model = get_default_model()
    model['url'] = '/ar/css-beautifier'
    model['enUrl'] = '/css-beautifier'
    model['headerTitle'] = 'أداة تنسيق CSS عبر الإنترنت  - Coding.Tools'
    model['bodyTitle'] = 'CSS تنسيق أداة على الإنترنت'
    model['description'] = 'يمكن لأداة تنسيق CSS الموجودة على الإنترنت مساعدتك على تنسيق خلط ملفات CSS في ملفات CSS القابلة للقراءة.'
    model['keywords'] = 'Css المنسق ، CSS المغلف ، تنسيق CSS'
    model['image'] = '/image/comic-css-beautifier.png'
    return render_template(template_dir + 'template_css_beautifier_ar.html', model=model)


@Web_JsonFormatter_blueprint.route('/ar/css-minifier', methods=['GET', 'POST'])
def css_minifier():
    model = get_default_model()
    model['url'] = '/ar/css-minifier'
    model['enUrl'] = '/css-minifier'
    model['headerTitle'] = 'أداة ضغط CSS عبر الإنترنت  - Coding.Tools'
    model['bodyTitle'] = 'أداة ضغط CSS على الإنترنت'
    model['description'] = 'تساعدك أداة ضغط CSS الموجودة على الإنترنت على ضغط ملفات CSS الأصلية ، مما يوفر مساحة لنقل أسرع عبر الشبكة.'
    model['keywords'] = 'Css minifier ، ضغط CSS'
    model['image'] = '/image/comic-css-minifier.png'
    return render_template(template_dir + 'template_css_minifier_ar.html', model=model)
