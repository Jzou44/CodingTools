from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_PasswordsGenerator_blueprint = Blueprint('Web_PasswordsGenerator_blueprint_ES', __name__)
template_dir = 'PasswordsGenerator/es/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'es'
    return model


@Web_PasswordsGenerator_blueprint.route('/es/md5', methods=['GET', 'POST'])
def md5():
    model = get_default_model()
    model['url'] = '/es/md5'
    model['enUrl'] = "/md5"
    model['headerTitle'] = 'Herramienta de cifrado en línea MD5  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta de cifrado MD5 en línea'
    model['description'] = 'Esta herramienta en línea de encriptación MD5 lo ayuda a encriptar una cadena de entrada en una cadena MD5 fija de 128 bits.'
    model['keywords'] = 'MD5, cifrado MD5'
    model['image'] = '/image/comic-md5.png'
    return render_template(template_dir + 'template_md5_es.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/es/sha1', methods=['GET', 'POST'])
def sha1():
    model = get_default_model()
    model['url'] = '/es/sha1'
    model['enUrl'] = "/sha1"
    model['headerTitle'] = 'Herramienta en línea de cifrado SHA1  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta de cifrado en línea SHA1'
    model['description'] = 'Esta herramienta en línea de encriptación SHA1 lo ayuda a encriptar una cadena de entrada en una cadena SHA1 fija de 160 bits.'
    model['keywords'] = 'SHA1, SHA1 cifrado'
    model['image'] = '/image/comic-sha1.png'
    return render_template(template_dir + 'template_sha1_es.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/es/sha224', methods=['GET', 'POST'])
def sha224():
    model = get_default_model()
    model['url'] = '/es/sha224'
    model['enUrl'] = "/sha224"
    model['headerTitle'] = 'Herramienta en línea de encriptación SHA224  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta de cifrado en línea SHA224'
    model['description'] = 'Esta herramienta en línea de cifrado SHA224 lo ayuda a cifrar una cadena de entrada en una cadena SHA224 de 224 bits fija.'
    model['keywords'] = 'SHA224, cifrado SHA224'
    model['image'] = '/image/comic-sha224.png'
    return render_template(template_dir + 'template_sha224_es.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/es/sha256', methods=['GET', 'POST'])
def sha256():
    model = get_default_model()
    model['url'] = '/es/sha256'
    model['enUrl'] = "/sha256"
    model['headerTitle'] = 'Herramienta en línea de cifrado SHA256  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta en línea de cifrado SHA256'
    model['description'] = 'Esta herramienta en línea de encriptación SHA256 lo ayuda a cifrar una cadena de entrada en una cadena SHA256 fija de 256 bits.'
    model['keywords'] = 'SHA256, cifrado SHA256'
    model['image'] = '/image/comic-sha256.png'
    return render_template(template_dir + 'template_sha256_es.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/es/sha384', methods=['GET', 'POST'])
def sha384():
    model = get_default_model()
    model['url'] = '/es/sha384'
    model['enUrl'] = "/sha384"
    model['headerTitle'] = 'Herramienta en línea de cifrado SHA384  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta de cifrado en línea SHA384'
    model['description'] = 'Esta herramienta en línea de encriptación SHA384 lo ayuda a cifrar una cadena de entrada en una cadena SHA384 de 384 bits fija.'
    model['keywords'] = 'SHA384, cifrado SHA384'
    model['image'] = '/image/comic-sha384.png'
    return render_template(template_dir + 'template_sha384_es.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/es/sha512', methods=['GET', 'POST'])
def sha512():
    model = get_default_model()
    model['url'] = '/es/sha512'
    model['enUrl'] = "/sha512"
    model['headerTitle'] = 'Herramienta en línea de cifrado SHA512  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta de cifrado en línea SHA512'
    model['description'] = 'Esta herramienta en línea de encriptación SHA512 lo ayuda a cifrar una cadena de entrada en una cadena SHA512 de 512 bits fija.'
    model['keywords'] = 'SHA512, cifrado SHA512'
    model['image'] = '/image/comic-sha512.png'
    return render_template(template_dir + 'template_sha512_es.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/es/base64-encode', methods=['GET', 'POST'])
def base64_encode():
    model = get_default_model()
    model['url'] = '/es/base64-encode'
    model['enUrl'] = "/base64-encode"
    model['headerTitle'] = 'Herramienta en línea de codificación Base64  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta en línea de codificación Base64'
    model['description'] = 'Esta herramienta de codificación Base64 en línea le ayuda a convertir una cadena de entrada en una cadena codificada Base64.'
    model['keywords'] = 'Base64, base64 codificación en línea'
    model['image'] = '/image/comic-base64-encode.png'
    return render_template(template_dir + 'template_base64_encode_es.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/es/base64-decode', methods=['GET', 'POST'])
def base64_decode():
    model = get_default_model()
    model['url'] = '/es/base64-decode'
    model['enUrl'] = "/base64-decode"
    model['headerTitle'] = 'Herramienta de decodificación en línea Base64  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta de decodificación en línea Base64'
    model['description'] = 'Esta herramienta de decodificación en línea Base64 puede ayudarlo a convertir una cadena de formato codificado en Base64 en una cadena UTF-8 normal.'
    model['keywords'] = 'Base64, decodificación en línea base64'
    model['image'] = '/image/comic-base64-decode.png'
    return render_template(template_dir + 'template_base64_decode_es.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/es/password-generator', methods=['GET', 'POST'])
def password_generator():
    model = get_default_model()
    model['url'] = '/es/password-generator'
    model['enUrl'] = "/password-generator"
    model['headerTitle'] = 'Herramienta de generación de contraseña aleatoria en línea  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta de generación de contraseña aleatoria en línea'
    model['description'] = 'Esta herramienta de generación de contraseñas en línea lo ayuda a generar contraseñas seguras y aleatorias. Genere diferentes contraseñas para diferentes cuentas de sitios web.'
    model['keywords'] = 'Herramienta de generación de contraseñas, generación de contraseñas en línea.'
    model['image'] = '/image/comic-password-generator.png'
    return render_template(template_dir + 'template_password_generator_es.html', model=model)
