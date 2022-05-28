from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_PasswordsGenerator_blueprint = Blueprint('Web_PasswordsGenerator_blueprint_JP', __name__)
template_dir = 'PasswordsGenerator/jp/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'ja'
    return model


@Web_PasswordsGenerator_blueprint.route('/jp/md5', methods=['GET', 'POST'])
def md5():
    model = get_default_model()
    model['url'] = '/jp/md5'
    model['enUrl'] = "/md5"
    model['headerTitle'] = 'MD5暗号化オンラインツール  - Coding.Tools'
    model['bodyTitle'] = 'MD5暗号化オンラインツール'
    model['description'] = 'このMD5暗号化オンラインツールは、入力文字列を128ビットの固定MD5文字列に暗号化するのに役立ちます。'
    model['keywords'] = 'MD5、MD5暗号化'
    model['image'] = '/image/comic-md5.png'
    return render_template(template_dir + 'template_md5_jp.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/jp/sha1', methods=['GET', 'POST'])
def sha1():
    model = get_default_model()
    model['url'] = '/jp/sha1'
    model['enUrl'] = "/sha1"
    model['headerTitle'] = 'SHA1暗号化オンラインツール  - Coding.Tools'
    model['bodyTitle'] = 'SHA1暗号化オンラインツール'
    model['description'] = 'このSHA1暗号化オンラインツールは、入力文字列を固定の160ビットSHA1文字列に暗号化するのに役立ちます。'
    model['keywords'] = 'SHA1、SHA1暗号化'
    model['image'] = '/image/comic-sha1.png'
    return render_template(template_dir + 'template_sha1_jp.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/jp/sha224', methods=['GET', 'POST'])
def sha224():
    model = get_default_model()
    model['url'] = '/jp/sha224'
    model['enUrl'] = "/sha224"
    model['headerTitle'] = 'SHA224暗号化オンラインツール  - Coding.Tools'
    model['bodyTitle'] = 'SHA224暗号化オンラインツール'
    model['description'] = 'このSHA224暗号化オンラインツールは、入力文字列を固定の224ビットSHA224文字列に暗号化するのに役立ちます。'
    model['keywords'] = 'SHA224、SHA224暗号化'
    model['image'] = '/image/comic-sha224.png'
    return render_template(template_dir + 'template_sha224_jp.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/jp/sha256', methods=['GET', 'POST'])
def sha256():
    model = get_default_model()
    model['url'] = '/jp/sha256'
    model['enUrl'] = "/sha256"
    model['headerTitle'] = 'SHA256暗号化オンラインツール  - Coding.Tools'
    model['bodyTitle'] = 'SHA256暗号化オンラインツール'
    model['description'] = 'このSHA256暗号化オンラインツールは、入力文字列を固定の256ビットSHA256文字列に暗号化するのに役立ちます。'
    model['keywords'] = 'SHA256、SHA256暗号化'
    model['image'] = '/image/comic-sha256.png'
    return render_template(template_dir + 'template_sha256_jp.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/jp/sha384', methods=['GET', 'POST'])
def sha384():
    model = get_default_model()
    model['url'] = '/jp/sha384'
    model['enUrl'] = "/sha384"
    model['headerTitle'] = 'SHA384暗号化オンラインツール  - Coding.Tools'
    model['bodyTitle'] = 'SHA384暗号化オンラインツール'
    model['description'] = 'このSHA384暗号化オンラインツールを使用すると、入力文字列を固定の384ビットSHA384文字列に暗号化できます。'
    model['keywords'] = 'SHA384、SHA384暗号化'
    model['image'] = '/image/comic-sha384.png'
    return render_template(template_dir + 'template_sha384_jp.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/jp/sha512', methods=['GET', 'POST'])
def sha512():
    model = get_default_model()
    model['url'] = '/jp/sha512'
    model['enUrl'] = "/sha512"
    model['headerTitle'] = 'SHA512暗号化オンラインツール  - Coding.Tools'
    model['bodyTitle'] = 'SHA512暗号化オンラインツール'
    model['description'] = 'このSHA512暗号化オンラインツールは、入力文字列を固定の512ビットSHA512文字列に暗号化するのに役立ちます。'
    model['keywords'] = 'SHA512、SHA512暗号化'
    model['image'] = '/image/comic-sha512.png'
    return render_template(template_dir + 'template_sha512_jp.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/jp/base64-encode', methods=['GET', 'POST'])
def base64_encode():
    model = get_default_model()
    model['url'] = '/jp/base64-encode'
    model['enUrl'] = "/base64-encode"
    model['headerTitle'] = 'Base64エンコーディングオンラインツール  - Coding.Tools'
    model['bodyTitle'] = 'Base64エンコーディングオンラインツール'
    model['description'] = 'このオンラインBase64エンコーディングツールは、入力文字列をBase64エンコード文字列に変換するのに役立ちます。'
    model['keywords'] = 'Base64、base64オンラインコーディング'
    model['image'] = '/image/comic-base64-encode.png'
    return render_template(template_dir + 'template_base64_encode_jp.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/jp/base64-decode', methods=['GET', 'POST'])
def base64_decode():
    model = get_default_model()
    model['url'] = '/jp/base64-decode'
    model['enUrl'] = "/base64-decode"
    model['headerTitle'] = 'Base64オンラインデコードツール  - Coding.Tools'
    model['bodyTitle'] = 'Base64オンラインデコードツール'
    model['description'] = 'このオンラインBase64デコードツールは、Base64エンコードフォーマット文字列を通常のUTF-8文字列に変換するのに役立ちます。'
    model['keywords'] = 'Base64、base64オンラインデコード'
    model['image'] = '/image/comic-base64-decode.png'
    return render_template(template_dir + 'template_base64_decode_jp.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/jp/password-generator', methods=['GET', 'POST'])
def password_generator():
    model = get_default_model()
    model['url'] = '/jp/password-generator'
    model['enUrl'] = "/password-generator"
    model['headerTitle'] = 'オンラインランダムパスワード生成ツール  - Coding.Tools'
    model['bodyTitle'] = 'オンラインランダムパスワード生成ツール'
    model['description'] = 'このオンラインパスワード生成ツールを使用すると、ランダムで安全なパスワードを簡単に生成できます。'
    model['keywords'] = 'パスワード生成ツール、オンラインパスワード生成'
    model['image'] = '/image/comic-password-generator.png'
    return render_template(template_dir + 'template_password_generator_jp.html', model=model)
