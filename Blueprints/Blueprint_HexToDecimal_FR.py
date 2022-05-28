from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_HexToDecimal_blueprint = Blueprint('Web_HexToDecimal_blueprint_FR', __name__)
template_dir = 'HexToDecimal/fr/'

def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'fr'
    return model

@Web_HexToDecimal_blueprint.route('/fr/hex-to-decimal')
def hex_to_decimal():
    model = get_default_model()
    model['url'] = '/fr/hex-to-decimal'
    model['enUrl'] = '/hex-to-decimal'
    model['headerTitle'] = 'Outil de conversion en ligne hexadécimale à décimale  - Coding.Tools'
    model['bodyTitle'] = 'Outil de conversion en ligne hexadécimal à décimal'
    model['description'] = 'Cet outil de conversion hexadécimal en décimal en ligne vous aide à convertir un nombre hexadécimal en un nombre décimal.'
    model['keywords'] = 'Hex à décimal, hexadécimal à décimal'
    model['image'] = '/image/cartoon-hex-to-decimal.png'
    return render_template(template_dir + 'template_hex_to_decimal_fr.html', model=model)


@Web_HexToDecimal_blueprint.route('/fr/decimal-to-hex')
def decimal_to_hex():
    model = get_default_model()
    model['url'] = '/fr/decimal-to-hex'
    model['enUrl'] = '/decimal-to-hex'
    model['headerTitle'] = 'Outil de conversion en ligne décimale à hexadécimale  - Coding.Tools'
    model['bodyTitle'] = 'Outil de conversion en ligne décimale à hexadécimale'
    model['description'] = 'Cet outil de conversion décimal en hexadécimal en ligne vous aide à convertir un nombre décimal en un nombre hexadécimal.'
    model['keywords'] = 'Décimal à hexadécimal, décimal à hexadécimal'
    model['image'] = '/image/cartoon-decimal-to-hex.png'
    return render_template(template_dir + 'template_decimal_to_hex_fr.html', model=model)


@Web_HexToDecimal_blueprint.route('/fr/octal-to-decimal')
def octal_to_decimal():
    model = get_default_model()
    model['url'] = '/fr/octal-to-decimal'
    model['enUrl'] = '/octal-to-decimal'
    model['headerTitle'] = 'Outil de conversion en ligne octal à décimal  - Coding.Tools'
    model['bodyTitle'] = 'Outil de conversion en ligne octal à décimal'
    model['description'] = 'Cet outil de conversion octal en décimal en ligne vous aide à convertir un nombre octal en un nombre décimal.'
    model['keywords'] = 'Octal à décimal, octal à décimal'
    model['image'] = '/image/octal_to_decimal.png'
    return render_template(template_dir + 'template_octal_to_decimal_fr.html', model=model)


@Web_HexToDecimal_blueprint.route('/fr/decimal-to-octal')
def decimal_to_octal():
    model = get_default_model()
    model['url'] = '/fr/decimal-to-octal'
    model['enUrl'] = '/decimal-to-octal'
    model['headerTitle'] = 'Outil de conversion en ligne décimal à octal  - Coding.Tools'
    model['bodyTitle'] = 'Outil de conversion en ligne décimal à octal'
    model['description'] = 'Cet outil de conversion décimal en octal en ligne vous aide à convertir un nombre décimal en un nombre octal.'
    model['keywords'] = 'Décimal à octal, décimal à octal'
    model['image'] = '/image/cartoon-decimal-to-octal.png'
    return render_template(template_dir + 'template_decimal_to_octal_fr.html', model=model)


@Web_HexToDecimal_blueprint.route('/fr/binary-to-decimal')
def binary_to_decimal():
    model = get_default_model()
    model['url'] = '/fr/binary-to-decimal'
    model['enUrl'] = '/binary-to-decimal'
    model['headerTitle'] = 'Outil de conversion en ligne binaire à décimal  - Coding.Tools'
    model['bodyTitle'] = 'Outil de conversion en ligne binaire à décimal'
    model['description'] = 'Cet outil de conversion binaire en décimal en ligne vous aide à convertir un nombre octal en un nombre décimal.'
    model['keywords'] = 'Binaire à décimal, binaire à décimal'
    model['image'] = '/image/cartoon-decimal-to-binary.png'
    return render_template(template_dir + 'template_binary_to_decimal_fr.html', model=model)


@Web_HexToDecimal_blueprint.route('/fr/decimal-to-binary')
def decimal_to_binary():
    model = get_default_model()
    model['url'] = '/fr/decimal-to-binary'
    model['enUrl'] = '/decimal-to-binary'
    model['headerTitle'] = 'Outil de conversion en ligne décimal en binaire  - Coding.Tools'
    model['bodyTitle'] = 'Outil de conversion en ligne décimal en binaire'
    model['description'] = 'Cet outil de conversion décimal en binaire en ligne vous aide à convertir un nombre décimal en un nombre binaire.'
    model['keywords'] = 'Décimal à binaire, décimal à binaire'
    model['image'] = '/image/cartoon-decimal-to-binary.png'
    return render_template(template_dir + 'template_decimal_to_binary_fr.html', model=model)


@Web_HexToDecimal_blueprint.route('/fr/ascii-table')
def ascii_table():
    model = get_default_model()
    model['url'] = '/fr/ascii-table'
    model['enUrl'] = '/ascii-table'
    model['headerTitle'] = 'Table de consultation ASCII  - Coding.Tools'
    model['bodyTitle'] = 'Table de consultation ASCII'
    model['description'] = 'Table de consultation ASCII complète (256 bits), y compris les caractères de contrôle ASCII, les symboles ASCII et les caractères étendus ASCII.'
    model['keywords'] = 'Table ASCII, table d\'extension ASCII'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_ascii_table_fr.html', model=model)


@Web_HexToDecimal_blueprint.route('/fr/hex-to-ascii')
def hex_to_ascii():
    model = get_default_model()
    model['url'] = '/fr/hex-to-ascii'
    model['enUrl'] = '/hex-to-ascii'
    model['headerTitle'] = 'Outil de conversion en ligne de chaîne hexadécimale à chaîne ASCII  - Coding.Tools'
    model['bodyTitle'] = 'Outil de conversion en ligne de chaîne hexadécimale à chaîne ASCII'
    model['description'] = 'Cet outil de conversion de chaîne hexadécimale en chaîne ASCII en ligne vous aide à convertir un tableau hexadécimal en chaîne ASCII.'
    model['keywords'] = 'Hex en ASCII, hex en ASCII'
    model['image'] = '/image/cartoon-hex-to-ascii.png'
    return render_template(template_dir + 'template_hex_to_ascii_fr.html', model=model)


@Web_HexToDecimal_blueprint.route('/fr/ascii-to-hex')
def ascii_to_hex():
    model = get_default_model()
    model['url'] = '/fr/ascii-to-hex'
    model['enUrl'] = '/ascii-to-hex'
    model['headerTitle'] = 'Chaîne ASCII en outil de conversion en ligne hexadécimale  - Coding.Tools'
    model['bodyTitle'] = 'Chaîne ASCII en outil de conversion en ligne hexadécimal'
    model['description'] = 'Cet outil de conversion de chaîne en hexa ASCII en ligne vous aide à convertir une chaîne ASCII en tableau hexadécimal.'
    model['keywords'] = 'ASCII en hexadécimal, ASCII en hexadécimal'
    model['image'] = '/image/cartoon-ascii-to-hex.png'
    return render_template(template_dir + 'template_ascii_to_hex_fr.html', model=model)


@Web_HexToDecimal_blueprint.route('/fr/fraction-to-decimal')
def fraction_to_decimal():
    model = get_default_model()
    model['url'] = '/fr/fraction-to-decimal'
    model['enUrl'] = '/fraction-to-decimal'
    model['headerTitle'] = 'Score en décimal outil de conversion en ligne  - Coding.Tools'
    model['bodyTitle'] = 'Score en décimal outil de conversion en ligne'
    model['description'] = 'Cet outil de conversion score en décimal en ligne vous aide à convertir un score en décimal.Le numérateur et le dénominateur en entrée sont affichés dans la zone de résultat.'
    model['keywords'] = 'Fraction à décimale, fraction à décimale'
    model['image'] = '/image/cartoon-fraction-to-decimal.png'
    return render_template(template_dir + 'template_fraction_to_decimal_fr.html', model=model)


@Web_HexToDecimal_blueprint.route('/fr/decimal-to-fraction')
def decimal_to_fraction():
    model = get_default_model()
    model['url'] = '/fr/decimal-to-fraction'
    model['enUrl'] = '/decimal-to-fraction'
    model['headerTitle'] = 'Outil de conversion en ligne décimal pour marquer  - Coding.Tools'
    model['bodyTitle'] = 'Décimal pour marquer un outil de conversion en ligne'
    model['description'] = 'Cet outil de conversion de score en nombre décimal en ligne vous aide à convertir un nombre décimal en score.'
    model['keywords'] = 'Décimal à la fraction, fractionnaire à la fraction'
    model['image'] = '/image/cartoon-decimal-to-fraction.png'
    return render_template(template_dir + 'template_decimal_to_fraction_fr.html', model=model)


@Web_HexToDecimal_blueprint.route('/fr/percent-to-decimal')
def percent_to_decimal():
    model = get_default_model()
    model['url'] = '/fr/percent-to-decimal'
    model['enUrl'] = '/percent-to-decimal'
    model['headerTitle'] = 'Outil de conversion en ligne en pourcentage à décimal  - Coding.Tools'
    model['bodyTitle'] = 'Outil de conversion en ligne en pourcentage à décimal'
    model['description'] = 'Cet outil de conversion de pourcentage en nombre décimal en ligne vous aide à convertir un pourcentage en nombre décimal. Entrez un pourcentage et le nombre décimal apparaît dans la zone de résultats.'
    model['keywords'] = 'Décimal à décimal, pourcentage à décimal'
    model['image'] = '/image/cartoon-percent-to-decimal.png'
    return render_template(template_dir + 'template_percent_to_decimal_fr.html', model=model)


@Web_HexToDecimal_blueprint.route('/fr/decimal-to-percent')
def decimal_to_percent():
    model = get_default_model()
    model['url'] = '/fr/decimal-to-percent'
    model['enUrl'] = '/decimal-to-percent'
    model['headerTitle'] = 'Outil de conversion en ligne décimal à pourcentage  - Coding.Tools'
    model['bodyTitle'] = 'Outil de conversion en ligne décimal à pourcentage'
    model['description'] = 'Cet outil de conversion décimal en pourcentage en ligne vous aide à convertir une décimale en un pourcentage. Entrez la décimale et le pourcentage sera affiché dans la zone de résultats.'
    model['keywords'] = 'Décimal à%, fraction à pourcentage'
    model['image'] = '/image/cartoon-decimal-to-percent.png'
    return render_template(template_dir + 'template_decimal_to_percent_fr.html', model=model)


@Web_HexToDecimal_blueprint.route('/fr/percent-to-fraction')
def percent_to_fraction():
    model = get_default_model()
    model['url'] = '/fr/percent-to-fraction'
    model['enUrl'] = '/percent-to-fraction'
    model['headerTitle'] = 'Percentage to Score Outil de conversion en ligne  - Coding.Tools'
    model['bodyTitle'] = 'Pourcentage de score outil de conversion en ligne'
    model['description'] = 'Cet outil en ligne de conversion de pourcentage en score vous aide à convertir un pourcentage en score.'
    model['keywords'] = 'Pourcentage à fraction, Pourcentage à fraction'
    model['image'] = '/image/cartoon-percent-to-fraction.png'
    return render_template(template_dir + 'template_percent_to_fraction_fr.html', model=model)


@Web_HexToDecimal_blueprint.route('/fr/fraction-to-percent')
def fraction_to_percent():
    model = get_default_model()
    model['url'] = '/fr/fraction-to-percent'
    model['enUrl'] = '/fraction-to-percent'
    model['headerTitle'] = 'Score en pourcentage outil de conversion en ligne  - Coding.Tools'
    model['bodyTitle'] = 'Score en pourcentage outil de conversion en ligne'
    model['description'] = 'Cet outil de conversion de score en pourcentage en ligne vous aide à convertir un score en pourcentage en saisissant le numérateur et le dénominateur et le pourcentage s\'affiche dans la zone des résultats.'
    model['keywords'] = 'Fraction à pourcentage, pourcentage fractionnaire'
    model['image'] = '/image/cartoon-fraction-to-percent.png'
    return render_template(template_dir + 'template_fraction_to_percent_fr.html', model=model)


@Web_HexToDecimal_blueprint.route('/fr/hex-to-rgb')
def hex_to_rgb():
    model = get_default_model()
    model['url'] = '/fr/hex-to-rgb'
    model['enUrl'] = '/hex-to-rgb'
    model['headerTitle'] = 'Outil de conversion en ligne des couleurs Hex en RVB  - Coding.Tools'
    model['bodyTitle'] = 'Outil de conversion en ligne de couleur hexagonale à couleur RVB'
    model['description'] = 'Cet outil de conversion de couleur Hex en RVB en ligne vous permet de convertir une couleur Hex en couleur RVB et de tester la couleur de votre choix en temps réel.'
    model['keywords'] = 'Hex en RVB, couleur Hex en RVB'
    model['image'] = '/image/cartoon-hex-to-rgb.png'
    return render_template(template_dir + 'template_hex_to_rgb_fr.html', model=model)


@Web_HexToDecimal_blueprint.route('/fr/rgb-to-hex')
def rgb_to_hex():
    model = get_default_model()
    model['url'] = '/fr/rgb-to-hex'
    model['enUrl'] = '/rgb-to-hex'
    model['headerTitle'] = 'Outil de conversion en ligne des couleurs RVB en couleurs hexagonales  - Coding.Tools'
    model['bodyTitle'] = 'Outil de conversion en ligne de couleurs RVB en couleurs hexagonales'
    model['description'] = 'Cet outil de conversion de couleur RVB en hexagone en ligne vous permet de convertir une couleur RVB en une couleur hexagonale et de tester la couleur de votre choix en temps réel.'
    model['keywords'] = 'RVB à Hex, couleur RVB à Hex'
    model['image'] = '/image/cartoon-rgb-to-hex.png'
    return render_template(template_dir + 'template_rgb_to_hex_fr.html', model=model)


@Web_HexToDecimal_blueprint.route('/fr/hex-to-rgba')
def hex_to_rgba():
    model = get_default_model()
    model['url'] = '/fr/hex-to-rgba'
    model['enUrl'] = '/hex-to-rgba'
    model['headerTitle'] = 'Outil de conversion en ligne des couleurs Hex à RGBA  - Coding.Tools'
    model['bodyTitle'] = 'Outil de conversion en ligne de couleur hexagonale à couleur RGBA'
    model['description'] = 'Cet outil de conversion de couleurs Hex en ligne RGBA en ligne vous permet de convertir une couleur Hex en une couleur RGBA (y compris Opacité des transparences) et de tester la couleur de votre choix en temps réel.'
    model['keywords'] = 'Hex à RGBA, couleur Hex à RGBA'
    model['image'] = '/image/cartoon-hex-to-rgba.png'
    return render_template(template_dir + 'template_hex_to_rgba_fr.html', model=model)


@Web_HexToDecimal_blueprint.route('/fr/rgba-to-hex')
def rgba_to_hex():
    model = get_default_model()
    model['url'] = '/fr/rgba-to-hex'
    model['enUrl'] = '/rgba-to-hex'
    model['headerTitle'] = 'Convertisseur en ligne de couleurs RGBA en couleurs Hex  - Coding.Tools'
    model['bodyTitle'] = 'Convertisseur en ligne de couleur RGBA en couleur hexagonale'
    model['description'] = 'Cet outil de conversion de couleur RGBA en couleur hexagonale en ligne vous aide à convertir une couleur RGBA (y compris l\'opacité des transparences) en couleur hexadécimale et à tester la couleur de votre choix en temps réel.'
    model['keywords'] = 'RGBA à Hex, couleur RGBA à Hex'
    model['image'] = '/image/cartoon-rgba-to-hex.png'
    return render_template(template_dir + 'template_rgba_to_hex_fr.html', model=model)


@Web_HexToDecimal_blueprint.route('/fr/roman-numerals-chart')
def roman_numerals_chart():
    model = get_default_model()
    model['url'] = '/fr/roman-numerals-chart'
    model['enUrl'] = '/roman-numerals-chart'
    model['headerTitle'] = 'Tableau des chiffres romains 1-1000 - Codage.Outils'
    model['bodyTitle'] = 'Tableau comparatif des chiffres romains 1-1000'
    model['description'] = 'Un tableau de comparaison complet des chiffres romains de 1 à 1000.'
    model['keywords'] = 'Tableau des chiffres romains, chiffres romains'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_roman_numerals_chart_fr.html', model=model)


@Web_HexToDecimal_blueprint.route('/fr/roman-numerals-to-numbers')
def roman_numerals_to_numbers():
    model = get_default_model()
    model['url'] = '/fr/roman-numerals-to-numbers'
    model['enUrl'] = '/roman-numerals-to-numbers'
    model['headerTitle'] = 'Outil de conversion en ligne de chiffres romains en chiffres arabes  - Coding.Tools'
    model['bodyTitle'] = 'Convertisseur numérique en ligne de chiffres romains en arabe'
    model['description'] = 'Cet outil de conversion de chiffres romains en chiffres arabes en ligne vous aide à convertir un chiffre romain en un chiffre arabe.'
    model['keywords'] = 'Les chiffres romains se tournent vers les chiffres arabes'
    model['image'] = '/image/cartoon-roman-numerals-to-numbers.png'
    return render_template(template_dir + 'template_roman_numerals_to_numbers_fr.html', model=model)


@Web_HexToDecimal_blueprint.route('/fr/numbers-to-roman-numerals')
def numbers_to_roman_numerals():
    model = get_default_model()
    model['url'] = '/fr/numbers-to-roman-numerals'
    model['enUrl'] = '/numbers-to-roman-numerals'
    model['headerTitle'] = 'Outil de conversion en ligne numérique arabe en numérique  - Coding.Tools'
    model['bodyTitle'] = 'Outil de conversion en ligne numérique arabe en numérique'
    model['description'] = 'Cet outil de conversion de chiffres arabes en chiffres romains en ligne vous aide à convertir un chiffre arabe en un chiffre romain.'
    model['keywords'] = 'Les chiffres arabes se transforment en chiffres romains'
    model['image'] = '/image/cartoon-numbers-to-roman-numerals.png'
    return render_template(template_dir + 'template_numbers_to_roman_numerals_fr.html', model=model)
