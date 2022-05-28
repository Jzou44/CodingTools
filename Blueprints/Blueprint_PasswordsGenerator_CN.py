from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_PasswordsGenerator_blueprint = Blueprint('Web_PasswordsGenerator_blueprint_CN', __name__)
template_dir = 'PasswordsGenerator/cn/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'zh-Hans'
    return model


@Web_PasswordsGenerator_blueprint.route('/cn/md5', methods=['GET', 'POST'])
def md5():
    model = get_default_model()
    model['url'] = '/cn/md5'
    model['enUrl'] = "/md5"
    model['headerTitle'] = 'MD5加密在线工具  - Coding.Tools'
    model['bodyTitle'] = 'MD5加密在线工具'
    model['description'] = '这个MD5加密在线工具可以帮助您将一个输入字符串加密为固定的128位MD5字符串.'
    model['keywords'] = 'MD5, MD5加密'
    model['image'] = '/image/comic-md5.png'
    return render_template(template_dir + 'template_md5_cn.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/cn/sha1', methods=['GET', 'POST'])
def sha1():
    model = get_default_model()
    model['url'] = '/cn/sha1'
    model['enUrl'] = "/sha1"
    model['headerTitle'] = 'SHA1加密在线工具  - Coding.Tools'
    model['bodyTitle'] = 'SHA1加密在线工具'
    model['description'] = '这个SHA1加密在线工具可以帮助您将一个输入字符串加密为固定的160位SHA1字符串.'
    model['keywords'] = 'SHA1, SHA1加密'
    model['image'] = '/image/comic-sha1.png'
    return render_template(template_dir + 'template_sha1_cn.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/cn/sha224', methods=['GET', 'POST'])
def sha224():
    model = get_default_model()
    model['url'] = '/cn/sha224'
    model['enUrl'] = "/sha224"
    model['headerTitle'] = 'SHA224加密在线工具  - Coding.Tools'
    model['bodyTitle'] = 'SHA224加密在线工具'
    model['description'] = '这个SHA224加密在线工具可以帮助您将一个输入字符串加密为固定的224位SHA224字符串.'
    model['keywords'] = 'SHA224, SHA224加密'
    model['image'] = '/image/comic-sha224.png'
    return render_template(template_dir + 'template_sha224_cn.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/cn/sha256', methods=['GET', 'POST'])
def sha256():
    model = get_default_model()
    model['url'] = '/cn/sha256'
    model['enUrl'] = "/sha256"
    model['headerTitle'] = 'SHA256加密在线工具  - Coding.Tools'
    model['bodyTitle'] = 'SHA256加密在线工具'
    model['description'] = '这个SHA256加密在线工具可以帮助您将一个输入字符串加密为固定的256位SHA256字符串.'
    model['keywords'] = 'SHA256, SHA256加密'
    model['image'] = '/image/comic-sha256.png'
    return render_template(template_dir + 'template_sha256_cn.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/cn/sha384', methods=['GET', 'POST'])
def sha384():
    model = get_default_model()
    model['url'] = '/cn/sha384'
    model['enUrl'] = "/sha384"
    model['headerTitle'] = 'SHA384加密在线工具  - Coding.Tools'
    model['bodyTitle'] = 'SHA384加密在线工具'
    model['description'] = '这个SHA384加密在线工具可以帮助您将一个输入字符串加密为固定的384位SHA384字符串.'
    model['keywords'] = 'SHA384, SHA384加密'
    model['image'] = '/image/comic-sha384.png'
    return render_template(template_dir + 'template_sha384_cn.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/cn/sha512', methods=['GET', 'POST'])
def sha512():
    model = get_default_model()
    model['url'] = '/cn/sha512'
    model['enUrl'] = "/sha512"
    model['headerTitle'] = 'SHA512加密在线工具  - Coding.Tools'
    model['bodyTitle'] = 'SHA512加密在线工具'
    model['description'] = '这个SHA512加密在线工具可以帮助您将一个输入字符串加密为固定的512位SHA512字符串.'
    model['keywords'] = 'SHA512, SHA512加密'
    model['image'] = '/image/comic-sha512.png'
    return render_template(template_dir + 'template_sha512_cn.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/cn/base64-encode', methods=['GET', 'POST'])
def base64_encode():
    model = get_default_model()
    model['url'] = '/cn/base64-encode'
    model['enUrl'] = "/base64-encode"
    model['headerTitle'] = 'Base64编码在线工具  - Coding.Tools'
    model['bodyTitle'] = 'Base64编码在线工具'
    model['description'] = '这个在线Base64编码工具可以帮助您将一个输入字符串转换成Base64编码格式的字符串.'
    model['keywords'] = 'base64, base64在线编码'
    model['image'] = '/image/comic-base64-encode.png'
    return render_template(template_dir + 'template_base64_encode_cn.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/cn/base64-decode', methods=['GET', 'POST'])
def base64_decode():
    model = get_default_model()
    model['url'] = '/cn/base64-decode'
    model['enUrl'] = "/base64-decode"
    model['headerTitle'] = 'Base64在线解码工具  - Coding.Tools'
    model['bodyTitle'] = 'Base64在线解码工具'
    model['description'] = '这个在线Base64解码工具可以帮助您将一个Base64编码格式字符串转换成普通UTF-8字符串.'
    model['keywords'] = 'base64, base64在线解码'
    model['image'] = '/image/comic-base64-decode.png'
    return render_template(template_dir + 'template_base64_decode_cn.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/cn/password-generator', methods=['GET', 'POST'])
def password_generator():
    model = get_default_model()
    model['url'] = '/cn/password-generator'
    model['enUrl'] = "/password-generator"
    model['headerTitle'] = '在线随机密码生成工具  - Coding.Tools'
    model['bodyTitle'] = '在线随机密码生成工具'
    model['description'] = '这个在线密码生成工具帮助您生成随机,安全的密码. 为您不同的网站账号生成不同的密码.'
    model['keywords'] = '密码生成工具, 在线密码生成'
    model['image'] = '/image/comic-password-generator.png'
    return render_template(template_dir + 'template_password_generator_cn.html', model=model)
