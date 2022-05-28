from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_PasswordsGenerator_blueprint = Blueprint('Web_PasswordsGenerator_blueprint_IT', __name__)
template_dir = 'PasswordsGenerator/it/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'it'
    return model


@Web_PasswordsGenerator_blueprint.route('/it/md5', methods=['GET', 'POST'])
def md5():
    model = get_default_model()
    model['url'] = '/it/md5'
    model['enUrl'] = "/md5"
    model['headerTitle'] = 'Strumento online di crittografia MD5  - Coding.Tools'
    model['bodyTitle'] = 'Strumento online di crittografia MD5'
    model['description'] = 'Questo strumento online di crittografia MD5 consente di crittografare una stringa di input in una stringa MD5 fissa a 128 bit.'
    model['keywords'] = 'MD5, crittografia MD5'
    model['image'] = '/image/comic-md5.png'
    return render_template(template_dir + 'template_md5_it.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/it/sha1', methods=['GET', 'POST'])
def sha1():
    model = get_default_model()
    model['url'] = '/it/sha1'
    model['enUrl'] = "/sha1"
    model['headerTitle'] = 'Strumento online di crittografia SHA1  - Coding.Tools'
    model['bodyTitle'] = 'Strumento online di crittografia SHA1'
    model['description'] = 'Questo strumento online di crittografia SHA1 consente di crittografare una stringa di input in una stringa SHA1 fissa a 160 bit.'
    model['keywords'] = 'Crittografia SHA1, SHA1'
    model['image'] = '/image/comic-sha1.png'
    return render_template(template_dir + 'template_sha1_it.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/it/sha224', methods=['GET', 'POST'])
def sha224():
    model = get_default_model()
    model['url'] = '/it/sha224'
    model['enUrl'] = "/sha224"
    model['headerTitle'] = 'Strumento online di crittografia SHA224  - Coding.Tools'
    model['bodyTitle'] = 'Strumento online di crittografia SHA224'
    model['description'] = 'Questo strumento online di crittografia SHA224 consente di crittografare una stringa di input in una stringa SHA224 fissa a 224 bit.'
    model['keywords'] = 'Crittografia SHA224, SHA224'
    model['image'] = '/image/comic-sha224.png'
    return render_template(template_dir + 'template_sha224_it.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/it/sha256', methods=['GET', 'POST'])
def sha256():
    model = get_default_model()
    model['url'] = '/it/sha256'
    model['enUrl'] = "/sha256"
    model['headerTitle'] = 'Strumento online di crittografia SHA256  - Coding.Tools'
    model['bodyTitle'] = 'Strumento online di crittografia SHA256'
    model['description'] = 'Questo strumento online di crittografia SHA256 consente di crittografare una stringa di input in una stringa SHA256 fissa a 256 bit.'
    model['keywords'] = 'Crittografia SHA256, SHA256'
    model['image'] = '/image/comic-sha256.png'
    return render_template(template_dir + 'template_sha256_it.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/it/sha384', methods=['GET', 'POST'])
def sha384():
    model = get_default_model()
    model['url'] = '/it/sha384'
    model['enUrl'] = "/sha384"
    model['headerTitle'] = 'Strumento online di crittografia SHA384  - Coding.Tools'
    model['bodyTitle'] = 'Strumento online di crittografia SHA384'
    model['description'] = 'Questo strumento online di crittografia SHA384 consente di crittografare una stringa di input in una stringa SHA384 fissa a 384 bit.'
    model['keywords'] = 'Crittografia SHA384, SHA384'
    model['image'] = '/image/comic-sha384.png'
    return render_template(template_dir + 'template_sha384_it.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/it/sha512', methods=['GET', 'POST'])
def sha512():
    model = get_default_model()
    model['url'] = '/it/sha512'
    model['enUrl'] = "/sha512"
    model['headerTitle'] = 'Strumento online di crittografia SHA512  - Coding.Tools'
    model['bodyTitle'] = 'Strumento online di crittografia SHA512'
    model['description'] = 'Questo strumento online di crittografia SHA512 consente di crittografare una stringa di input in una stringa SHA512 fissa a 512 bit.'
    model['keywords'] = 'Crittografia SHA512, SHA512'
    model['image'] = '/image/comic-sha512.png'
    return render_template(template_dir + 'template_sha512_it.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/it/base64-encode', methods=['GET', 'POST'])
def base64_encode():
    model = get_default_model()
    model['url'] = '/it/base64-encode'
    model['enUrl'] = "/base64-encode"
    model['headerTitle'] = 'Strumento online di codifica Base64  - Coding.Tools'
    model['bodyTitle'] = 'Strumento online di codifica Base64'
    model['description'] = 'Questo strumento di codifica Base64 online consente di convertire una stringa di input in una stringa codificata Base64.'
    model['keywords'] = 'Base64, codifica online base64'
    model['image'] = '/image/comic-base64-encode.png'
    return render_template(template_dir + 'template_base64_encode_it.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/it/base64-decode', methods=['GET', 'POST'])
def base64_decode():
    model = get_default_model()
    model['url'] = '/it/base64-decode'
    model['enUrl'] = "/base64-decode"
    model['headerTitle'] = 'Strumento di decodifica online Base64  - Coding.Tools'
    model['bodyTitle'] = 'Strumento di decodifica online Base64'
    model['description'] = 'Questo strumento di decodifica Base64 online può aiutarti a convertire una stringa di formato codificata Base64 in una normale stringa UTF-8.'
    model['keywords'] = 'Base64, decodifica online base64'
    model['image'] = '/image/comic-base64-decode.png'
    return render_template(template_dir + 'template_base64_decode_it.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/it/password-generator', methods=['GET', 'POST'])
def password_generator():
    model = get_default_model()
    model['url'] = '/it/password-generator'
    model['enUrl'] = "/password-generator"
    model['headerTitle'] = 'Strumento di generazione di password casuali online  - Coding.Tools'
    model['bodyTitle'] = 'Strumento di generazione di password casuali online'
    model['description'] = 'Questo strumento di generazione di password online ti aiuta a generare password casuali e sicure. Genera password diverse per account di siti web diversi.'
    model['keywords'] = 'Strumento per la generazione di password, generazione di password online'
    model['image'] = '/image/comic-password-generator.png'
    return render_template(template_dir + 'template_password_generator_it.html', model=model)
