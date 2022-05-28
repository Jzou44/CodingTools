from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_PasswordsGenerator_blueprint = Blueprint('Web_PasswordsGenerator_blueprint_PT', __name__)
template_dir = 'PasswordsGenerator/pt/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'pt'
    return model


@Web_PasswordsGenerator_blueprint.route('/pt/md5', methods=['GET', 'POST'])
def md5():
    model = get_default_model()
    model['url'] = '/pt/md5'
    model['enUrl'] = "/md5"
    model['headerTitle'] = 'Ferramenta on-line de criptografia MD5  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta on-line de criptografia MD5'
    model['description'] = 'Essa ferramenta on-line de criptografia MD5 ajuda a criptografar uma cadeia de entrada em uma cadeia MD5 fixa de 128 bits.'
    model['keywords'] = 'MD5, criptografia MD5'
    model['image'] = '/image/comic-md5.png'
    return render_template(template_dir + 'template_md5_pt.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/pt/sha1', methods=['GET', 'POST'])
def sha1():
    model = get_default_model()
    model['url'] = '/pt/sha1'
    model['enUrl'] = "/sha1"
    model['headerTitle'] = 'Ferramenta on-line de criptografia SHA1  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta on-line de criptografia SHA1'
    model['description'] = 'Essa ferramenta on-line de criptografia SHA1 ajuda a criptografar uma string de entrada em uma string SHA1 fixa de 160 bits.'
    model['keywords'] = 'SHA1, encriptação SHA1'
    model['image'] = '/image/comic-sha1.png'
    return render_template(template_dir + 'template_sha1_pt.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/pt/sha224', methods=['GET', 'POST'])
def sha224():
    model = get_default_model()
    model['url'] = '/pt/sha224'
    model['enUrl'] = "/sha224"
    model['headerTitle'] = 'Ferramenta on-line de criptografia SHA224  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta on-line de criptografia SHA224'
    model['description'] = 'Esta ferramenta on-line de criptografia SHA224 ajuda a criptografar uma string de entrada em uma string SHA224 fixa de 224 bits.'
    model['keywords'] = 'SHA224, criptografia SHA224'
    model['image'] = '/image/comic-sha224.png'
    return render_template(template_dir + 'template_sha224_pt.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/pt/sha256', methods=['GET', 'POST'])
def sha256():
    model = get_default_model()
    model['url'] = '/pt/sha256'
    model['enUrl'] = "/sha256"
    model['headerTitle'] = 'Ferramenta on-line de criptografia SHA256  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta on-line de criptografia SHA256'
    model['description'] = 'Esta ferramenta on-line de criptografia SHA256 ajuda a criptografar uma string de entrada em uma string SHA256 fixa de 256 bits.'
    model['keywords'] = 'SHA256, criptografia SHA256'
    model['image'] = '/image/comic-sha256.png'
    return render_template(template_dir + 'template_sha256_pt.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/pt/sha384', methods=['GET', 'POST'])
def sha384():
    model = get_default_model()
    model['url'] = '/pt/sha384'
    model['enUrl'] = "/sha384"
    model['headerTitle'] = 'Ferramenta on-line de criptografia SHA384  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta on-line de criptografia SHA384'
    model['description'] = 'Esta ferramenta on-line de criptografia SHA384 ajuda a criptografar uma string de entrada em uma string fixa SHA384 de 384 bits.'
    model['keywords'] = 'Criptografia SHA384, SHA384'
    model['image'] = '/image/comic-sha384.png'
    return render_template(template_dir + 'template_sha384_pt.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/pt/sha512', methods=['GET', 'POST'])
def sha512():
    model = get_default_model()
    model['url'] = '/pt/sha512'
    model['enUrl'] = "/sha512"
    model['headerTitle'] = 'Ferramenta on-line de criptografia SHA512  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta on-line de criptografia SHA512'
    model['description'] = 'Esta ferramenta on-line de criptografia SHA512 ajuda a criptografar uma string de entrada em uma string fixa SHA512 de 512 bits.'
    model['keywords'] = 'Encriptação SHA512, SHA512'
    model['image'] = '/image/comic-sha512.png'
    return render_template(template_dir + 'template_sha512_pt.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/pt/base64-encode', methods=['GET', 'POST'])
def base64_encode():
    model = get_default_model()
    model['url'] = '/pt/base64-encode'
    model['enUrl'] = "/base64-encode"
    model['headerTitle'] = 'Ferramenta on-line de codificação Base64  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta on-line de codificação Base64'
    model['description'] = 'Esta ferramenta de codificação on-line Base64 ajuda a converter uma string de entrada em uma string codificada em Base64.'
    model['keywords'] = 'Base64, codificação online de base64'
    model['image'] = '/image/comic-base64-encode.png'
    return render_template(template_dir + 'template_base64_encode_pt.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/pt/base64-decode', methods=['GET', 'POST'])
def base64_decode():
    model = get_default_model()
    model['url'] = '/pt/base64-decode'
    model['enUrl'] = "/base64-decode"
    model['headerTitle'] = 'Ferramenta de decodificação online Base64  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta de decodificação online Base64'
    model['description'] = 'Esta ferramenta on-line de decodificação Base64 pode ajudá-lo a converter uma string de formato codificada em Base64 em uma string UTF-8 normal.'
    model['keywords'] = 'Base64, decodificação online base64'
    model['image'] = '/image/comic-base64-decode.png'
    return render_template(template_dir + 'template_base64_decode_pt.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/pt/password-generator', methods=['GET', 'POST'])
def password_generator():
    model = get_default_model()
    model['url'] = '/pt/password-generator'
    model['enUrl'] = "/password-generator"
    model['headerTitle'] = 'Ferramenta de geração de senha aleatória online  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta de geração de senha aleatória online'
    model['description'] = 'Esta ferramenta de geração de senha on-line ajuda a gerar senhas seguras e aleatórias, gerando senhas diferentes para diferentes contas de sites.'
    model['keywords'] = 'Ferramenta de geração de senha, geração de senha online'
    model['image'] = '/image/comic-password-generator.png'
    return render_template(template_dir + 'template_password_generator_pt.html', model=model)
