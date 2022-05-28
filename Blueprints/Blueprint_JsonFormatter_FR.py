from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_JsonFormatter_blueprint = Blueprint('Web_JsonFormatter_blueprint_FR', __name__)
template_dir = 'JsonFormatter/fr/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'fr'
    return model


@Web_JsonFormatter_blueprint.route('/fr/json-formatter', methods=['GET', 'POST'])
def json_formatter():
    model = get_default_model()
    model['url'] = '/fr/json-formatter'
    model['enUrl'] = '/json-formatter'
    model['headerTitle'] = 'Outil en ligne de formatage JSON  - Coding.Tools'
    model['bodyTitle'] = 'Outil en ligne de formatage JSON'
    model['description'] = 'Cet outil de formatage JSON en ligne peut vous aider à formater des chaînes JSON déroutantes en chaînes JSON lisibles.'
    model['keywords'] = 'Formateur Json, formatage JSON'
    model['image'] = '/image/comic-json-formatter.png'
    return render_template(template_dir + 'template_json_formatter_fr.html', model=model)


@Web_JsonFormatter_blueprint.route('/fr/json-minifier', methods=['GET', 'POST'])
def json_minifier():
    model = get_default_model()
    model['url'] = '/fr/json-minifier'
    model['enUrl'] = '/json-minifier'
    model['headerTitle'] = 'Outil en ligne de compression JSON  - Coding.Tools'
    model['bodyTitle'] = 'Outil en ligne de compression JSON'
    model['description'] = 'Cet outil en ligne de compression JSON vous aide à compresser les chaînes JSON d\'origine et à économiser de l\'espace pour un transfert plus rapide sur le réseau.'
    model['keywords'] = 'Json minifier, compression JSON'
    model['image'] = '/image/comic-json-minifier.png'
    return render_template(template_dir + 'template_json_minifier_fr.html', model=model)


@Web_JsonFormatter_blueprint.route('/fr/xml-formatter', methods=['GET', 'POST'])
def xml_formatter():
    model = get_default_model()
    model['url'] = '/fr/xml-formatter'
    model['enUrl'] = '/xml-formatter'
    model['headerTitle'] = 'Outil en ligne de formatage XML  - Coding.Tools'
    model['bodyTitle'] = 'Outil en ligne de formatage XML'
    model['description'] = 'Cet outil de formatage XML en ligne peut vous aider à formater des chaînes XML confuses en chaînes XML lisibles.'
    model['keywords'] = 'Formateur XML, formatage XML'
    model['image'] = '/image/comic-xml-formatter.png'
    return render_template(template_dir + 'template_xml_formatter_fr.html', model=model)


@Web_JsonFormatter_blueprint.route('/fr/xml-minifier', methods=['GET', 'POST'])
def xml_minifier():
    model = get_default_model()
    model['url'] = '/fr/xml-minifier'
    model['enUrl'] = '/xml-minifier'
    model['headerTitle'] = 'Outil en ligne de compression XML  - Coding.Tools'
    model['bodyTitle'] = 'Outil en ligne de compression XML'
    model['description'] = 'Cet outil en ligne de compression XML vous aide à compresser des chaînes XML brutes et à économiser de l\'espace pour un transfert plus rapide sur le réseau.'
    model['keywords'] = 'Minificateur Xml, compression XML'
    model['image'] = '/image/comic-xml-minifier.png'
    return render_template(template_dir + 'template_xml_minifier_fr.html', model=model)


@Web_JsonFormatter_blueprint.route('/fr/json-to-xml', methods=['GET', 'POST'])
def json_to_xml():
    model = get_default_model()
    model['url'] = '/fr/json-to-xml'
    model['enUrl'] = '/json-to-xml'
    model['headerTitle'] = 'Outil en ligne JSON to XML  - Coding.Tools'
    model['bodyTitle'] = 'Outil en ligne JSON to XML'
    model['description'] = 'Cet outil en ligne JSON to XML peut vous aider à convertir des chaînes de données au format JSON en chaînes de données au format XML.'
    model['keywords'] = 'Json à XML, JSON à XML'
    model['image'] = '/image/comic-json-to-xml.png'
    return render_template(template_dir + 'template_json_to_xml_fr.html', model=model)


@Web_JsonFormatter_blueprint.route('/fr/xml-to-json', methods=['GET', 'POST'])
def xml_to_json():
    model = get_default_model()
    model['url'] = '/fr/xml-to-json'
    model['enUrl'] = '/xml-to-json'
    model['headerTitle'] = 'Outil en ligne XML vers JSON  - Coding.Tools'
    model['bodyTitle'] = 'Outil en ligne XML to JSON'
    model['description'] = 'Cet outil en ligne XML vers JSON peut vous aider à convertir des chaînes de données au format XML en chaînes de données au format JSON.'
    model['keywords'] = 'XML à JSON, XML à JSON'
    model['image'] = '/image/comic-xml-to-json.png'
    return render_template(template_dir + 'template_xml_to_json_fr.html', model=model)


@Web_JsonFormatter_blueprint.route('/fr/html-beautifier', methods=['GET', 'POST'])
def html_beautifier():
    model = get_default_model()
    model['url'] = '/fr/html-beautifier'
    model['enUrl'] = '/html-beautifier'
    model['headerTitle'] = 'Outil en ligne de formatage HTML  - Coding.Tools'
    model['bodyTitle'] = 'Outil en ligne de formatage HTML'
    model['description'] = 'Cet outil de formatage HTML en ligne peut vous aider à formater des fichiers HTML prêtant à confusion en fichiers HTML lisibles.'
    model['keywords'] = 'Formateur HTML, embellisseur HTML, mise en forme HTML'
    model['image'] = '/image/comic-html-beautifier.png'
    return render_template(template_dir + 'template_html_beautifier_fr.html', model=model)


@Web_JsonFormatter_blueprint.route('/fr/html-minifier', methods=['GET', 'POST'])
def html_minifier():
    model = get_default_model()
    model['url'] = '/fr/html-minifier'
    model['enUrl'] = '/html-minifier'
    model['headerTitle'] = 'Outil en ligne de compression HTML  - Coding.Tools'
    model['bodyTitle'] = 'Outil en ligne de compression HTML'
    model['description'] = 'Cet outil en ligne de compression HTML vous aide à compresser vos fichiers HTML d\'origine, économisant ainsi de la place pour un transfert plus rapide sur le réseau.'
    model['keywords'] = 'Minificateur HTML, compression HTML'
    model['image'] = '/image/comic-html-minifier.png'
    return render_template(template_dir + 'template_html_minifier_fr.html', model=model)


@Web_JsonFormatter_blueprint.route('/fr/javascript-beautifier', methods=['GET', 'POST'])
def javascript_beautifier():
    model = get_default_model()
    model['url'] = '/fr/javascript-beautifier'
    model['enUrl'] = '/javascript-beautifier'
    model['headerTitle'] = 'Outil de mise en forme Javascript en ligne  - Coding.Tools'
    model['bodyTitle'] = 'Outil de mise en forme Javascript en ligne'
    model['description'] = 'Cet outil de formatage Javascript en ligne peut vous aider à formater des fichiers Javascript déroutants en fichiers javascript lisibles.'
    model['keywords'] = 'Formateur de Javascript, embellisseur de javascript, formatage de Javascript'
    model['image'] = '/image/comic-javascript-beautifier.png'
    return render_template(template_dir + 'template_javascript_beautifier_fr.html', model=model)


@Web_JsonFormatter_blueprint.route('/fr/javascript-minifier', methods=['GET', 'POST'])
def javascript_minifier():
    model = get_default_model()
    model['url'] = '/fr/javascript-minifier'
    model['enUrl'] = '/javascript-minifier'
    model['headerTitle'] = 'Outil en ligne de compression Javascript  - Coding.Tools'
    model['bodyTitle'] = 'Outil en ligne de compression Javascript'
    model['description'] = 'Cet outil en ligne de compression Javascript vous aide à compresser vos fichiers Javascript d\'origine, en économisant de l\'espace pour un transfert plus rapide sur le réseau.'
    model['keywords'] = 'Minifier Javascript, compression Javascript'
    model['image'] = '/image/comic-javascript-minifier.png'
    return render_template(template_dir + 'template_javascript_minifier_fr.html', model=model)


@Web_JsonFormatter_blueprint.route('/fr/css-beautifier', methods=['GET', 'POST'])
def css_beautifier():
    model = get_default_model()
    model['url'] = '/fr/css-beautifier'
    model['enUrl'] = '/css-beautifier'
    model['headerTitle'] = 'Outil en ligne de mise en forme CSS  - Coding.Tools'
    model['bodyTitle'] = 'Outil en ligne de formatage CSS'
    model['description'] = 'Cet outil de formatage CSS en ligne peut vous aider à formater des fichiers CSS confus en fichiers CSS lisibles.'
    model['keywords'] = 'Formateur CSS, esthétiseur CSS, formatage CSS'
    model['image'] = '/image/comic-css-beautifier.png'
    return render_template(template_dir + 'template_css_beautifier_fr.html', model=model)


@Web_JsonFormatter_blueprint.route('/fr/css-minifier', methods=['GET', 'POST'])
def css_minifier():
    model = get_default_model()
    model['url'] = '/fr/css-minifier'
    model['enUrl'] = '/css-minifier'
    model['headerTitle'] = 'Outil en ligne de compression CSS  - Coding.Tools'
    model['bodyTitle'] = 'Outil en ligne de compression CSS'
    model['description'] = 'Cet outil en ligne de compression CSS vous aide à compresser vos fichiers CSS d\'origine, en économisant de l\'espace pour un transfert plus rapide sur le réseau.'
    model['keywords'] = 'Css minifier, compression CSS'
    model['image'] = '/image/comic-css-minifier.png'
    return render_template(template_dir + 'template_css_minifier_fr.html', model=model)
