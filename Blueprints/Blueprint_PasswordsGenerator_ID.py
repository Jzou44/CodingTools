from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_PasswordsGenerator_blueprint = Blueprint('Web_PasswordsGenerator_blueprint_ID', __name__)
template_dir = 'PasswordsGenerator/id/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'id'
    return model


@Web_PasswordsGenerator_blueprint.route('/id/md5', methods=['GET', 'POST'])
def md5():
    model = get_default_model()
    model['url'] = '/id/md5'
    model['enUrl'] = "/md5"
    model['headerTitle'] = 'Alat online enkripsi MD5  - Coding.Tools'
    model['bodyTitle'] = 'Alat online enkripsi MD5'
    model['description'] = 'Alat online enkripsi MD5 ini membantu Anda mengenkripsi string input ke string MD5 128-bit yang tetap.'
    model['keywords'] = 'Enkripsi MD5, MD5'
    model['image'] = '/image/comic-md5.png'
    return render_template(template_dir + 'template_md5_id.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/id/sha1', methods=['GET', 'POST'])
def sha1():
    model = get_default_model()
    model['url'] = '/id/sha1'
    model['enUrl'] = "/sha1"
    model['headerTitle'] = 'Alat online enkripsi SHA1  - Coding.Tools'
    model['bodyTitle'] = 'Alat enkripsi online SHA1'
    model['description'] = 'Alat online enkripsi SHA1 ini membantu Anda mengenkripsi string input ke string SHA1 160-bit yang tetap.'
    model['keywords'] = 'SHA1, enkripsi SHA1'
    model['image'] = '/image/comic-sha1.png'
    return render_template(template_dir + 'template_sha1_id.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/id/sha224', methods=['GET', 'POST'])
def sha224():
    model = get_default_model()
    model['url'] = '/id/sha224'
    model['enUrl'] = "/sha224"
    model['headerTitle'] = 'Alat online enkripsi SHA224  - Coding.Tools'
    model['bodyTitle'] = 'Alat enkripsi online SHA224'
    model['description'] = 'Alat online Enkripsi SHA224 ini membantu Anda mengenkripsi string input menjadi string SHA224 224-bit yang tetap.'
    model['keywords'] = 'SHA224, enkripsi SHA224'
    model['image'] = '/image/comic-sha224.png'
    return render_template(template_dir + 'template_sha224_id.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/id/sha256', methods=['GET', 'POST'])
def sha256():
    model = get_default_model()
    model['url'] = '/id/sha256'
    model['enUrl'] = "/sha256"
    model['headerTitle'] = 'Alat online enkripsi SHA256  - Coding.Tools'
    model['bodyTitle'] = 'Alat enkripsi online SHA256'
    model['description'] = 'Alat online enkripsi SHA256 ini membantu Anda mengenkripsi string input ke string SHA256 256-bit yang tetap.'
    model['keywords'] = 'SHA256, enkripsi SHA256'
    model['image'] = '/image/comic-sha256.png'
    return render_template(template_dir + 'template_sha256_id.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/id/sha384', methods=['GET', 'POST'])
def sha384():
    model = get_default_model()
    model['url'] = '/id/sha384'
    model['enUrl'] = "/sha384"
    model['headerTitle'] = 'Alat online enkripsi SHA384  - Coding.Tools'
    model['bodyTitle'] = 'Alat enkripsi online SHA384'
    model['description'] = 'Alat online enkripsi SHA384 ini membantu Anda mengenkripsi string input ke string SHA384 384 bit yang tetap.'
    model['keywords'] = 'SHA384, enkripsi SHA384'
    model['image'] = '/image/comic-sha384.png'
    return render_template(template_dir + 'template_sha384_id.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/id/sha512', methods=['GET', 'POST'])
def sha512():
    model = get_default_model()
    model['url'] = '/id/sha512'
    model['enUrl'] = "/sha512"
    model['headerTitle'] = 'Alat Online Enkripsi SHA512  - Coding.Tools'
    model['bodyTitle'] = 'Alat enkripsi online SHA512'
    model['description'] = 'Alat online enkripsi SHA512 ini membantu Anda mengenkripsi string input ke string SHA512 512-bit yang tetap.'
    model['keywords'] = 'SHA512, enkripsi SHA512'
    model['image'] = '/image/comic-sha512.png'
    return render_template(template_dir + 'template_sha512_id.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/id/base64-encode', methods=['GET', 'POST'])
def base64_encode():
    model = get_default_model()
    model['url'] = '/id/base64-encode'
    model['enUrl'] = "/base64-encode"
    model['headerTitle'] = 'Alat encoding online Base64  - Coding.Tools'
    model['bodyTitle'] = 'Alat encoding online base64'
    model['description'] = 'Alat pengkodean Base64 online ini membantu Anda mengubah string input menjadi string yang dikodekan Base64.'
    model['keywords'] = 'Base64, base64 pengkodean online'
    model['image'] = '/image/comic-base64-encode.png'
    return render_template(template_dir + 'template_base64_encode_id.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/id/base64-decode', methods=['GET', 'POST'])
def base64_decode():
    model = get_default_model()
    model['url'] = '/id/base64-decode'
    model['enUrl'] = "/base64-decode"
    model['headerTitle'] = 'Alat decoding online Base64  - Coding.Tools'
    model['bodyTitle'] = 'Alat decoding online Base64'
    model['description'] = 'Alat decoding Base64 online ini dapat membantu Anda mengubah string format yang disandikan Base64 menjadi string UTF-8 yang normal.'
    model['keywords'] = 'Base64, base64 decoding online'
    model['image'] = '/image/comic-base64-decode.png'
    return render_template(template_dir + 'template_base64_decode_id.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/id/password-generator', methods=['GET', 'POST'])
def password_generator():
    model = get_default_model()
    model['url'] = '/id/password-generator'
    model['enUrl'] = "/password-generator"
    model['headerTitle'] = 'Alat pembuatan kata sandi online acak  - Coding.Tools'
    model['bodyTitle'] = 'Alat pembuatan kata sandi acak online'
    model['description'] = 'Alat penghasil kata sandi online ini membantu Anda menghasilkan kata sandi acak dan aman. Menghasilkan kata sandi yang berbeda untuk akun situs web yang berbeda.'
    model['keywords'] = 'Alat pembuatan kata sandi, pembuatan kata sandi online'
    model['image'] = '/image/comic-password-generator.png'
    return render_template(template_dir + 'template_password_generator_id.html', model=model)
