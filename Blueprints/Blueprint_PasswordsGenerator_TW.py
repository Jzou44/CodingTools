from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_PasswordsGenerator_blueprint = Blueprint('Web_PasswordsGenerator_blueprint_TW', __name__)
template_dir = 'PasswordsGenerator/tw/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'zh-Hant'
    return model


@Web_PasswordsGenerator_blueprint.route('/tw/md5', methods=['GET', 'POST'])
def md5():
    model = get_default_model()
    model['url'] = '/tw/md5'
    model['enUrl'] = "/md5"
    model['headerTitle'] = 'MD5加密在線工具 - Coding.Tools'
    model['bodyTitle'] = 'MD5加密在線工具'
    model['description'] = '這個MD5加密在線工具可以幫助您將一個輸入字符串加密為固定的128位MD5字符串.'
    model['keywords'] = 'MD5, MD5加密'
    model['image'] = '/image/comic-md5.png'
    return render_template(template_dir + 'template_md5_tw.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/tw/sha1', methods=['GET', 'POST'])
def sha1():
    model = get_default_model()
    model['url'] = '/tw/sha1'
    model['enUrl'] = "/sha1"
    model['headerTitle'] = 'SHA1加密在線工具 - Coding.Tools'
    model['bodyTitle'] = 'SHA1加密在線工具'
    model['description'] = '這個SHA1加密在線工具可以幫助您將一個輸入字符串加密為固定的160位SHA1字符串.'
    model['keywords'] = 'SHA1, SHA1加密'
    model['image'] = '/image/comic-sha1.png'
    return render_template(template_dir + 'template_sha1_tw.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/tw/sha224', methods=['GET', 'POST'])
def sha224():
    model = get_default_model()
    model['url'] = '/tw/sha224'
    model['enUrl'] = "/sha224"
    model['headerTitle'] = 'SHA224加密在線工具 - Coding.Tools'
    model['bodyTitle'] = 'SHA224加密在線工具'
    model['description'] = '這個SHA224加密在線工具可以幫助您將一個輸入字符串加密為固定的224位SHA224字符串.'
    model['keywords'] = 'SHA224, SHA224加密'
    model['image'] = '/image/comic-sha224.png'
    return render_template(template_dir + 'template_sha224_tw.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/tw/sha256', methods=['GET', 'POST'])
def sha256():
    model = get_default_model()
    model['url'] = '/tw/sha256'
    model['enUrl'] = "/sha256"
    model['headerTitle'] = 'SHA256加密在線工具 - Coding.Tools'
    model['bodyTitle'] = 'SHA256加密在線工具'
    model['description'] = '這個SHA256加密在線工具可以幫助您將一個輸入字符串加密為固定的256位SHA256字符串.'
    model['keywords'] = 'SHA256, SHA256加密'
    model['image'] = '/image/comic-sha256.png'
    return render_template(template_dir + 'template_sha256_tw.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/tw/sha384', methods=['GET', 'POST'])
def sha384():
    model = get_default_model()
    model['url'] = '/tw/sha384'
    model['enUrl'] = "/sha384"
    model['headerTitle'] = 'SHA384加密在線工具 - Coding.Tools'
    model['bodyTitle'] = 'SHA384加密在線工具'
    model['description'] = '這個SHA384加密在線工具可以幫助您將一個輸入字符串加密為固定的384位SHA384字符串.'
    model['keywords'] = 'SHA384, SHA384加密'
    model['image'] = '/image/comic-sha384.png'
    return render_template(template_dir + 'template_sha384_tw.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/tw/sha512', methods=['GET', 'POST'])
def sha512():
    model = get_default_model()
    model['url'] = '/tw/sha512'
    model['enUrl'] = "/sha512"
    model['headerTitle'] = 'SHA512加密在線工具 - Coding.Tools'
    model['bodyTitle'] = 'SHA512加密在線工具'
    model['description'] = '這個SHA512加密在線工具可以幫助您將一個輸入字符串加密為固定的512位SHA512字符串.'
    model['keywords'] = 'SHA512, SHA512加密'
    model['image'] = '/image/comic-sha512.png'
    return render_template(template_dir + 'template_sha512_tw.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/tw/base64-encode', methods=['GET', 'POST'])
def base64_encode():
    model = get_default_model()
    model['url'] = '/tw/base64-encode'
    model['enUrl'] = "/base64-encode"
    model['headerTitle'] = 'Base64編碼在線工具 - Coding.Tools'
    model['bodyTitle'] = 'Base64編碼在線工具'
    model['description'] = '這個在線Base64編碼工具可以幫助您將一個輸入字符串轉換成Base64編碼格式的字符串.'
    model['keywords'] = 'base64, base64在線編碼'
    model['image'] = '/image/comic-base64-encode.png'
    return render_template(template_dir + 'template_base64_encode_tw.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/tw/base64-decode', methods=['GET', 'POST'])
def base64_decode():
    model = get_default_model()
    model['url'] = '/tw/base64-decode'
    model['enUrl'] = "/base64-decode"
    model['headerTitle'] = 'Base64在線解碼工具 - Coding.Tools'
    model['bodyTitle'] = 'Base64在線解碼工具'
    model['description'] = '這個在線Base64解碼工具可以幫助您將一個Base64編碼格式字符串轉換成普通UTF-8字符串.'
    model['keywords'] = 'base64, base64在線解碼'
    model['image'] = '/image/comic-base64-decode.png'
    return render_template(template_dir + 'template_base64_decode_tw.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/tw/password-generator', methods=['GET', 'POST'])
def password_generator():
    model = get_default_model()
    model['url'] = '/tw/password-generator'
    model['enUrl'] = "/password-generator"
    model['headerTitle'] = '在線隨機密碼生成工具 - Coding.Tools'
    model['bodyTitle'] = '在線隨機密碼生成工具'
    model['description'] = '這個在線密碼生成工具幫助您生成隨機,安全的密碼. 為您不同的網站賬號生成不同的密碼.'
    model['keywords'] = '密碼生成工具, 在線密碼生成'
    model['image'] = '/image/comic-password-generator.png'
    return render_template(template_dir + 'template_password_generator_tw.html', model=model)
