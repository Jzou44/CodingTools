from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_PasswordsGenerator_blueprint = Blueprint('Web_PasswordsGenerator_blueprint', __name__)
template_dir = 'PasswordsGenerator/en/'

def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'en'
    return model

@Web_PasswordsGenerator_blueprint.route('/md5', methods=['GET', 'POST'])
def md5():
    model = get_default_model()
    model['url'] = '/md5'
    model['enUrl'] = "/md5"
    model['headerTitle'] = 'MD5 Hash Generator Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'MD5 Hash Generator Online Tool'
    model['description'] = 'This online MD5 Hash Generator tool helps you to encrypt one input string into a fixed 128 bits MD5 String.'
    model['keywords'] = 'MD5, MD5 Encrypt, MD5 Online, MD5 Generator'
    model['image'] = '/image/comic-md5.png'
    return render_template(template_dir + 'template_md5.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/sha1', methods=['GET', 'POST'])
def sha1():
    model = get_default_model()
    model['url'] = '/sha1'
    model['enUrl'] = "/sha1"
    model['headerTitle'] = 'SHA1 Hash Generator Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'SHA1 Hash Generator Online Tool'
    model['description'] = 'This online SHA1 Hash Generator tool helps you to encrypt one input string into a fixed 160 bits SHA1 String.'
    model['keywords'] = 'SHA1, SHA1 Encrypt, SHA1 Online, SHA1 Generator'
    model['image'] = '/image/comic-sha1.png'
    return render_template(template_dir + 'template_sha1.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/sha224', methods=['GET', 'POST'])
def sha224():
    model = get_default_model()
    model['url'] = '/sha224'
    model['enUrl'] = "/sha224"
    model['headerTitle'] = 'SHA224 Hash Generator Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'SHA224 Hash Generator Online Tool'
    model['description'] = 'This online SHA224 Hash Generator tool helps you to encrypt one input string into a fixed 224 bits SHA224 String.'
    model['keywords'] = 'SHA224, SHA224 Encrypt, SHA224 Online, SHA224 Generator'
    model['image'] = '/image/comic-sha224.png'
    return render_template(template_dir + 'template_sha224.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/sha256', methods=['GET', 'POST'])
def sha256():
    model = get_default_model()
    model['url'] = '/sha256'
    model['enUrl'] = "/sha256"
    model['headerTitle'] = 'SHA256 Hash Generator Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'SHA256 Hash Generator Online Tool'
    model['description'] = 'This online SHA256 Hash Generator tool helps you to encrypt one input string into a fixed 256 bits SHA256 String.'
    model['keywords'] = 'SHA256, SHA256 Encrypt, SHA256 Online, SHA256 Generator'
    model['image'] = '/image/comic-sha256.png'
    return render_template(template_dir + 'template_sha256.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/sha384', methods=['GET', 'POST'])
def sha384():
    model = get_default_model()
    model['url'] = '/sha384'
    model['enUrl'] = "/sha384"
    model['headerTitle'] = 'SHA384 Hash Generator Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'SHA384 Hash Generator Online Tool'
    model['description'] = 'This online SHA384 Hash Generator tool helps you to encrypt one input string into a fixed 384 bits SHA384 String.'
    model['keywords'] = 'SHA384, SHA384 Encrypt, SHA384 Online, SHA384 Generator'
    model['image'] = '/image/comic-sha384.png'
    return render_template(template_dir + 'template_sha384.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/sha512', methods=['GET', 'POST'])
def sha512():
    model = get_default_model()
    model['url'] = '/sha512'
    model['enUrl'] = "/sha512"
    model['headerTitle'] = 'SHA512 Hash Generator Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'SHA512 Hash Generator Online Tool'
    model['description'] = 'This online SHA512 Hash Generator tool helps you to encrypt one input string into a fixed 512 bits SHA512 String.'
    model['keywords'] = 'SHA512, SHA512 Encrypt, SHA512 Online, SHA512 Generator'
    model['image'] = '/image/comic-sha512.png'
    return render_template(template_dir + 'template_sha512.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/base64-encode', methods=['GET', 'POST'])
def base64_encode():
    model = get_default_model()
    model['url'] = '/base64-encode'
    model['enUrl'] = "/base64-encode"
    model['headerTitle'] = 'Base64 Encode Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Base64 Encode Online Tool'
    model['description'] = 'This online base64 encode tool helps you to convert one input string into a base64 format String.'
    model['keywords'] = 'base64, base64 encode, base64 encoder'
    model['image'] = '/image/comic-base64-encode.png'
    return render_template(template_dir + 'template_base64_encode.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/base64-decode', methods=['GET', 'POST'])
def base64_decode():
    model = get_default_model()
    model['url'] = '/base64-decode'
    model['enUrl'] = "/base64-decode"
    model['headerTitle'] = 'Base64 Decode Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Base64 Decode Online Tool'
    model['description'] = 'This online base64 decode tool helps you to convert a base64 format String into a raw string.'
    model['keywords'] = 'base64, base64 decode, base64 decoder'
    model['image'] = '/image/comic-base64-decode.png'
    return render_template(template_dir + 'template_base64_decode.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/password-generator', methods=['GET', 'POST'])
def password_generator():
    model = get_default_model()
    model['url'] = '/password-generator'
    model['enUrl'] = "/password-generator"
    model['headerTitle'] = 'Password Generator Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Password Generator Online Tool'
    model['description'] = 'This online password generator tool helps you to generate secure random password, secure your privacy by creating different password for each website.'
    model['keywords'] = 'password generator, secure password generator, random password generator'
    model['image'] = '/image/comic-password-generator.png'
    return render_template(template_dir + 'template_password_generator.html', model=model)
