from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_PasswordsGenerator_blueprint = Blueprint('Web_PasswordsGenerator_blueprint_KR', __name__)
template_dir = 'PasswordsGenerator/kr/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'ko'
    return model


@Web_PasswordsGenerator_blueprint.route('/kr/md5', methods=['GET', 'POST'])
def md5():
    model = get_default_model()
    model['url'] = '/kr/md5'
    model['enUrl'] = "/md5"
    model['headerTitle'] = 'MD5 암호화 온라인 도구  - Coding.Tools'
    model['bodyTitle'] = 'MD5 암호화 온라인 도구'
    model['description'] = '이 MD5 암호화 온라인 도구는 입력 문자열을 고정 된 128 비트 MD5 문자열로 암호화하는 데 유용합니다.'
    model['keywords'] = 'MD5, MD5 암호화'
    model['image'] = '/image/comic-md5.png'
    return render_template(template_dir + 'template_md5_kr.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/kr/sha1', methods=['GET', 'POST'])
def sha1():
    model = get_default_model()
    model['url'] = '/kr/sha1'
    model['enUrl'] = "/sha1"
    model['headerTitle'] = 'SHA1 암호화 온라인 도구  - Coding.Tools'
    model['bodyTitle'] = 'SHA1 암호화 온라인 도구'
    model['description'] = '이 SHA1 암호화 온라인 도구는 입력 문자열을 고정 160 비트 SHA1 문자열로 암호화하는 데 도움이됩니다.'
    model['keywords'] = 'SHA1, SHA1 암호화'
    model['image'] = '/image/comic-sha1.png'
    return render_template(template_dir + 'template_sha1_kr.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/kr/sha224', methods=['GET', 'POST'])
def sha224():
    model = get_default_model()
    model['url'] = '/kr/sha224'
    model['enUrl'] = "/sha224"
    model['headerTitle'] = 'SHA224 암호화 온라인 도구  - Coding.Tools'
    model['bodyTitle'] = 'SHA224 암호화 온라인 도구'
    model['description'] = '이 SHA224 암호화 온라인 도구는 입력 문자열을 고정 된 224 비트 SHA224 문자열로 암호화하는 데 도움이됩니다.'
    model['keywords'] = 'SHA224, SHA224 암호화'
    model['image'] = '/image/comic-sha224.png'
    return render_template(template_dir + 'template_sha224_kr.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/kr/sha256', methods=['GET', 'POST'])
def sha256():
    model = get_default_model()
    model['url'] = '/kr/sha256'
    model['enUrl'] = "/sha256"
    model['headerTitle'] = 'SHA256 암호화 온라인 도구  - Coding.Tools'
    model['bodyTitle'] = 'SHA256 암호화 온라인 도구'
    model['description'] = '이 SHA256 암호화 온라인 도구는 입력 문자열을 고정 된 256 비트 SHA256 문자열로 암호화하는 데 도움이됩니다.'
    model['keywords'] = 'SHA256, SHA256 암호화'
    model['image'] = '/image/comic-sha256.png'
    return render_template(template_dir + 'template_sha256_kr.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/kr/sha384', methods=['GET', 'POST'])
def sha384():
    model = get_default_model()
    model['url'] = '/kr/sha384'
    model['enUrl'] = "/sha384"
    model['headerTitle'] = 'SHA384 암호화 온라인 도구  - Coding.Tools'
    model['bodyTitle'] = 'SHA384 암호화 온라인 도구'
    model['description'] = '이 SHA384 암호화 온라인 도구는 입력 문자열을 고정 된 384 비트 SHA384 문자열로 암호화하는 데 도움이됩니다.'
    model['keywords'] = 'SHA384, SHA384 암호화'
    model['image'] = '/image/comic-sha384.png'
    return render_template(template_dir + 'template_sha384_kr.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/kr/sha512', methods=['GET', 'POST'])
def sha512():
    model = get_default_model()
    model['url'] = '/kr/sha512'
    model['enUrl'] = "/sha512"
    model['headerTitle'] = 'SHA512 암호화 온라인 도구  - Coding.Tools'
    model['bodyTitle'] = 'SHA512 암호화 온라인 도구'
    model['description'] = '이 SHA512 암호화 온라인 도구는 입력 문자열을 고정 된 512 비트 SHA512 문자열로 암호화하는 데 유용합니다.'
    model['keywords'] = 'SHA512, SHA512 암호화'
    model['image'] = '/image/comic-sha512.png'
    return render_template(template_dir + 'template_sha512_kr.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/kr/base64-encode', methods=['GET', 'POST'])
def base64_encode():
    model = get_default_model()
    model['url'] = '/kr/base64-encode'
    model['enUrl'] = "/base64-encode"
    model['headerTitle'] = 'Base64 인코딩 온라인 도구  - Coding.Tools'
    model['bodyTitle'] = 'Base64 인코딩 온라인 도구'
    model['description'] = '이 온라인 Base64 인코딩 도구는 입력 문자열을 Base64 인코딩 문자열로 변환하는 데 유용합니다.'
    model['keywords'] = 'Base64, base64 온라인 코딩'
    model['image'] = '/image/comic-base64-encode.png'
    return render_template(template_dir + 'template_base64_encode_kr.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/kr/base64-decode', methods=['GET', 'POST'])
def base64_decode():
    model = get_default_model()
    model['url'] = '/kr/base64-decode'
    model['enUrl'] = "/base64-decode"
    model['headerTitle'] = 'Base64 온라인 디코딩 도구  - Coding.Tools'
    model['bodyTitle'] = 'Base64 온라인 디코딩 도구'
    model['description'] = '이 온라인 Base64 디코딩 도구는 Base64 인코딩 형식 문자열을 일반적인 UTF-8 문자열로 변환하는 데 도움을줍니다.'
    model['keywords'] = 'Base64, base64 온라인 디코딩'
    model['image'] = '/image/comic-base64-decode.png'
    return render_template(template_dir + 'template_base64_decode_kr.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/kr/password-generator', methods=['GET', 'POST'])
def password_generator():
    model = get_default_model()
    model['url'] = '/kr/password-generator'
    model['enUrl'] = "/password-generator"
    model['headerTitle'] = '온라인 임의 암호 생성 도구  - Coding.Tools'
    model['bodyTitle'] = '온라인 임의 암호 생성 도구'
    model['description'] = '이 온라인 암호 생성 도구는 임의의 안전한 암호를 생성하는 데 도움이됩니다. 다른 웹 사이트 계정에 대해 다른 암호를 생성하십시오.'
    model['keywords'] = '암호 생성 도구, 온라인 암호 생성'
    model['image'] = '/image/comic-password-generator.png'
    return render_template(template_dir + 'template_password_generator_kr.html', model=model)
