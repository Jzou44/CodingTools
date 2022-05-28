from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_PasswordsGenerator_blueprint = Blueprint('Web_PasswordsGenerator_blueprint_DE', __name__)
template_dir = 'PasswordsGenerator/de/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'de'
    return model


@Web_PasswordsGenerator_blueprint.route('/de/md5', methods=['GET', 'POST'])
def md5():
    model = get_default_model()
    model['url'] = '/de/md5'
    model['enUrl'] = "/md5"
    model['headerTitle'] = 'MD5-Verschlüsselungs-Online-Tool  - Coding.Tools'
    model['bodyTitle'] = 'MD5-Verschlüsselungs-Online-Tool'
    model['description'] = 'Mit diesem Online-Tool zur MD5-Verschlüsselung können Sie eine Eingabezeichenfolge in eine feste 128-Bit-MD5-Zeichenfolge verschlüsseln.'
    model['keywords'] = 'MD5, MD5-Verschlüsselung'
    model['image'] = '/image/comic-md5.png'
    return render_template(template_dir + 'template_md5_de.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/de/sha1', methods=['GET', 'POST'])
def sha1():
    model = get_default_model()
    model['url'] = '/de/sha1'
    model['enUrl'] = "/sha1"
    model['headerTitle'] = 'SHA1-Verschlüsselungs-Online-Tool  - Coding.Tools'
    model['bodyTitle'] = 'SHA1-Verschlüsselungs-Online-Tool'
    model['description'] = 'Dieses Online-Tool zur SHA1-Verschlüsselung unterstützt Sie beim Verschlüsseln einer Eingabezeichenfolge in eine feste 160-Bit-SHA1-Zeichenfolge.'
    model['keywords'] = 'SHA1, SHA1-Verschlüsselung'
    model['image'] = '/image/comic-sha1.png'
    return render_template(template_dir + 'template_sha1_de.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/de/sha224', methods=['GET', 'POST'])
def sha224():
    model = get_default_model()
    model['url'] = '/de/sha224'
    model['enUrl'] = "/sha224"
    model['headerTitle'] = 'SHA224 Online-Verschlüsselungstool  - Coding.Tools'
    model['bodyTitle'] = 'SHA224-Verschlüsselungs-Online-Tool'
    model['description'] = 'Dieses Online-Tool für die SHA224-Verschlüsselung unterstützt Sie beim Verschlüsseln einer Eingabezeichenfolge in einer festen 224-Bit-SHA224-Zeichenfolge.'
    model['keywords'] = 'SHA224, SHA224-Verschlüsselung'
    model['image'] = '/image/comic-sha224.png'
    return render_template(template_dir + 'template_sha224_de.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/de/sha256', methods=['GET', 'POST'])
def sha256():
    model = get_default_model()
    model['url'] = '/de/sha256'
    model['enUrl'] = "/sha256"
    model['headerTitle'] = 'SHA256 Online-Verschlüsselungstool  - Coding.Tools'
    model['bodyTitle'] = 'SHA256-Verschlüsselungs-Online-Tool'
    model['description'] = 'Dieses Online-Tool zur SHA256-Verschlüsselung hilft Ihnen, eine Eingabezeichenfolge in einer festen 256-Bit-SHA256-Zeichenfolge zu verschlüsseln.'
    model['keywords'] = 'SHA256, SHA256-Verschlüsselung'
    model['image'] = '/image/comic-sha256.png'
    return render_template(template_dir + 'template_sha256_de.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/de/sha384', methods=['GET', 'POST'])
def sha384():
    model = get_default_model()
    model['url'] = '/de/sha384'
    model['enUrl'] = "/sha384"
    model['headerTitle'] = 'SHA384 Online-Verschlüsselungstool  - Coding.Tools'
    model['bodyTitle'] = 'SHA384-Verschlüsselungs-Online-Tool'
    model['description'] = 'Dieses Online-Tool zur SHA384-Verschlüsselung unterstützt Sie beim Verschlüsseln einer Eingabezeichenfolge in eine feste 384-Bit-SHA384-Zeichenfolge.'
    model['keywords'] = 'SHA384, SHA384-Verschlüsselung'
    model['image'] = '/image/comic-sha384.png'
    return render_template(template_dir + 'template_sha384_de.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/de/sha512', methods=['GET', 'POST'])
def sha512():
    model = get_default_model()
    model['url'] = '/de/sha512'
    model['enUrl'] = "/sha512"
    model['headerTitle'] = 'SHA512 Online-Tool zur Verschlüsselung  - Coding.Tools'
    model['bodyTitle'] = 'SHA512 Online-Verschlüsselungstool'
    model['description'] = 'Dieses Online-Tool zur SHA512-Verschlüsselung unterstützt Sie beim Verschlüsseln einer Eingabezeichenfolge in einer festen 512-Bit-SHA512-Zeichenfolge.'
    model['keywords'] = 'SHA512, SHA512-Verschlüsselung'
    model['image'] = '/image/comic-sha512.png'
    return render_template(template_dir + 'template_sha512_de.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/de/base64-encode', methods=['GET', 'POST'])
def base64_encode():
    model = get_default_model()
    model['url'] = '/de/base64-encode'
    model['enUrl'] = "/base64-encode"
    model['headerTitle'] = 'Base64-Codierungs-Online-Tool  - Coding.Tools'
    model['bodyTitle'] = 'Base64-Kodierungs-Online-Tool'
    model['description'] = 'Dieses Online-Base64-Codierungstool hilft Ihnen, eine Eingabezeichenfolge in eine Base64-codierte Zeichenfolge zu konvertieren.'
    model['keywords'] = 'Base64, base64 Online-Codierung'
    model['image'] = '/image/comic-base64-encode.png'
    return render_template(template_dir + 'template_base64_encode_de.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/de/base64-decode', methods=['GET', 'POST'])
def base64_decode():
    model = get_default_model()
    model['url'] = '/de/base64-decode'
    model['enUrl'] = "/base64-decode"
    model['headerTitle'] = 'Online-Dekodierungstool Base64  - Coding.Tools'
    model['bodyTitle'] = 'Base64 Online-Dekodierungstool'
    model['description'] = 'Mit diesem Online-Base64-Dekodierungstool können Sie eine Base64-kodierte Formatzeichenfolge in eine normale UTF-8-Zeichenfolge konvertieren.'
    model['keywords'] = 'Base64, base64 Online-Dekodierung'
    model['image'] = '/image/comic-base64-decode.png'
    return render_template(template_dir + 'template_base64_decode_de.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/de/password-generator', methods=['GET', 'POST'])
def password_generator():
    model = get_default_model()
    model['url'] = '/de/password-generator'
    model['enUrl'] = "/password-generator"
    model['headerTitle'] = 'Online-Tool zur Erzeugung zufälliger Passwörter  - Coding.Tools'
    model['bodyTitle'] = 'Online-Tool zur Erzeugung zufälliger Passwörter'
    model['description'] = 'Mit diesem Online-Passworterstellungs-Tool können Sie zufällige, sichere Passwörter erstellen und unterschiedliche Passwörter für verschiedene Website-Konten erstellen.'
    model['keywords'] = 'Tool zur Passwortgenerierung, Online-Passwortgenerierung'
    model['image'] = '/image/comic-password-generator.png'
    return render_template(template_dir + 'template_password_generator_de.html', model=model)
