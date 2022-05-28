from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_PasswordsGenerator_blueprint = Blueprint('Web_PasswordsGenerator_blueprint_FR', __name__)
template_dir = 'PasswordsGenerator/fr/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'fr'
    return model


@Web_PasswordsGenerator_blueprint.route('/fr/md5', methods=['GET', 'POST'])
def md5():
    model = get_default_model()
    model['url'] = '/fr/md5'
    model['enUrl'] = "/md5"
    model['headerTitle'] = 'Outil en ligne de chiffrement MD5  - Coding.Tools'
    model['bodyTitle'] = 'Outil en ligne de chiffrement MD5'
    model['description'] = 'Cet outil en ligne de chiffrement MD5 vous aide à chiffrer une chaîne d\'entrée en une chaîne MD5 fixe de 128 bits.'
    model['keywords'] = 'MD5, cryptage MD5'
    model['image'] = '/image/comic-md5.png'
    return render_template(template_dir + 'template_md5_fr.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/fr/sha1', methods=['GET', 'POST'])
def sha1():
    model = get_default_model()
    model['url'] = '/fr/sha1'
    model['enUrl'] = "/sha1"
    model['headerTitle'] = 'Outil en ligne de chiffrement SHA1  - Coding.Tools'
    model['bodyTitle'] = 'Outil en ligne de chiffrement SHA1'
    model['description'] = 'Cet outil en ligne de chiffrement SHA1 vous aide à chiffrer une chaîne d\'entrée en une chaîne SHA1 fixe de 160 bits.'
    model['keywords'] = 'SHA1, SHA1 cryptage'
    model['image'] = '/image/comic-sha1.png'
    return render_template(template_dir + 'template_sha1_fr.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/fr/sha224', methods=['GET', 'POST'])
def sha224():
    model = get_default_model()
    model['url'] = '/fr/sha224'
    model['enUrl'] = "/sha224"
    model['headerTitle'] = 'Outil en ligne de chiffrement SHA224  - Coding.Tools'
    model['bodyTitle'] = 'Outil en ligne de chiffrement SHA224'
    model['description'] = 'Cet outil en ligne SHA224 Encryption vous aide à chiffrer une chaîne d\'entrée en une chaîne SHA224 fixe de 224 bits.'
    model['keywords'] = 'SHA224, SHA224 cryptage'
    model['image'] = '/image/comic-sha224.png'
    return render_template(template_dir + 'template_sha224_fr.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/fr/sha256', methods=['GET', 'POST'])
def sha256():
    model = get_default_model()
    model['url'] = '/fr/sha256'
    model['enUrl'] = "/sha256"
    model['headerTitle'] = 'Outil en ligne de chiffrement SHA256  - Coding.Tools'
    model['bodyTitle'] = 'Outil en ligne de chiffrement SHA256'
    model['description'] = 'Cet outil en ligne de chiffrement SHA256 vous aide à chiffrer une chaîne d\'entrée en chaîne SHA256 fixe de 256 bits.'
    model['keywords'] = 'SHA256, SHA256 cryptage'
    model['image'] = '/image/comic-sha256.png'
    return render_template(template_dir + 'template_sha256_fr.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/fr/sha384', methods=['GET', 'POST'])
def sha384():
    model = get_default_model()
    model['url'] = '/fr/sha384'
    model['enUrl'] = "/sha384"
    model['headerTitle'] = 'Outil en ligne de chiffrement SHA384  - Coding.Tools'
    model['bodyTitle'] = 'Outil en ligne de chiffrement SHA384'
    model['description'] = 'Cet outil en ligne de chiffrement SHA384 vous aide à chiffrer une chaîne d\'entrée en une chaîne SHA384 fixe de 384 bits.'
    model['keywords'] = 'SHA384, SHA384 cryptage'
    model['image'] = '/image/comic-sha384.png'
    return render_template(template_dir + 'template_sha384_fr.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/fr/sha512', methods=['GET', 'POST'])
def sha512():
    model = get_default_model()
    model['url'] = '/fr/sha512'
    model['enUrl'] = "/sha512"
    model['headerTitle'] = 'Outil en ligne SHA512 Encryption - Outils de codage'
    model['bodyTitle'] = 'Outil en ligne de chiffrement SHA512'
    model['description'] = 'Cet outil en ligne de chiffrement SHA512 vous aide à chiffrer une chaîne d\'entrée en une chaîne SHA512 fixe de 512 bits.'
    model['keywords'] = 'SHA512, SHA512 cryptage'
    model['image'] = '/image/comic-sha512.png'
    return render_template(template_dir + 'template_sha512_fr.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/fr/base64-encode', methods=['GET', 'POST'])
def base64_encode():
    model = get_default_model()
    model['url'] = '/fr/base64-encode'
    model['enUrl'] = "/base64-encode"
    model['headerTitle'] = 'Outil en ligne d\'encodage Base64  - Coding.Tools'
    model['bodyTitle'] = 'Outil en ligne d\'encodage Base64'
    model['description'] = 'Cet outil d\'encodage Base64 en ligne vous aide à convertir une chaîne d\'entrée en une chaîne encodée en Base64.'
    model['keywords'] = 'Base64, codage en ligne base64'
    model['image'] = '/image/comic-base64-encode.png'
    return render_template(template_dir + 'template_base64_encode_fr.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/fr/base64-decode', methods=['GET', 'POST'])
def base64_decode():
    model = get_default_model()
    model['url'] = '/fr/base64-decode'
    model['enUrl'] = "/base64-decode"
    model['headerTitle'] = 'Outil de décodage en ligne Base64  - Coding.Tools'
    model['bodyTitle'] = 'Outil de décodage en ligne Base64'
    model['description'] = 'Cet outil de décodage Base64 en ligne peut vous aider à convertir une chaîne au format encodé en Base64 en chaîne UTF-8 normale.'
    model['keywords'] = 'Base64, base64 décodage en ligne'
    model['image'] = '/image/comic-base64-decode.png'
    return render_template(template_dir + 'template_base64_decode_fr.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/fr/password-generator', methods=['GET', 'POST'])
def password_generator():
    model = get_default_model()
    model['url'] = '/fr/password-generator'
    model['enUrl'] = "/password-generator"
    model['headerTitle'] = 'Outil de génération de mot de passe aléatoire en ligne  - Coding.Tools'
    model['bodyTitle'] = 'Outil de génération de mot de passe aléatoire en ligne'
    model['description'] = 'Cet outil de génération de mots de passe en ligne vous aide à générer des mots de passe aléatoires et sécurisés.'
    model['keywords'] = 'Outil de génération de mot de passe, génération de mot de passe en ligne'
    model['image'] = '/image/comic-password-generator.png'
    return render_template(template_dir + 'template_password_generator_fr.html', model=model)
