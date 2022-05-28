from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_PasswordsGenerator_blueprint = Blueprint('Web_PasswordsGenerator_blueprint_AR', __name__)
template_dir = 'PasswordsGenerator/ar/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'ar'
    return model


@Web_PasswordsGenerator_blueprint.route('/ar/md5', methods=['GET', 'POST'])
def md5():
    model = get_default_model()
    model['url'] = '/ar/md5'
    model['enUrl'] = "/md5"
    model['headerTitle'] = 'أداة تشفير MD5 عبر الإنترنت  - Coding.Tools'
    model['bodyTitle'] = 'تشفير MD5 على الإنترنت'
    model['description'] = 'تساعدك أداة التشفير عبر الإنترنت MD5 هذه على تشفير سلسلة إدخال في سلسلة MD5 ثابتة 128 بت.'
    model['keywords'] = 'MD5 ، تشفير MD5'
    model['image'] = '/image/comic-md5.png'
    return render_template(template_dir + 'template_md5_ar.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/ar/sha1', methods=['GET', 'POST'])
def sha1():
    model = get_default_model()
    model['url'] = '/ar/sha1'
    model['enUrl'] = "/sha1"
    model['headerTitle'] = 'SHA1 التشفير أداة على الإنترنت - الترميز. أدوات'
    model['bodyTitle'] = 'SHA1 التشفير أداة على الإنترنت'
    model['description'] = 'تساعدك أداة التشفير على الإنترنت SHA1 هذه على تشفير سلسلة إدخال في سلسلة SHA1 ثابتة 160 بت.'
    model['keywords'] = 'SHA1 ، تشفير SHA1'
    model['image'] = '/image/comic-sha1.png'
    return render_template(template_dir + 'template_sha1_ar.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/ar/sha224', methods=['GET', 'POST'])
def sha224():
    model = get_default_model()
    model['url'] = '/ar/sha224'
    model['enUrl'] = "/sha224"
    model['headerTitle'] = 'SHA224 أداة التشفير على الإنترنت - الترميز. أدوات'
    model['bodyTitle'] = 'SHA224 أداة التشفير على الانترنت'
    model['description'] = 'تساعدك أداة التشفير SHA224 هذه عبر الإنترنت على تشفير سلسلة إدخال في سلسلة SHA224 ثابتة تبلغ 224 بت.'
    model['keywords'] = 'SHA224 ، SHA224 التشفير'
    model['image'] = '/image/comic-sha224.png'
    return render_template(template_dir + 'template_sha224_ar.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/ar/sha256', methods=['GET', 'POST'])
def sha256():
    model = get_default_model()
    model['url'] = '/ar/sha256'
    model['enUrl'] = "/sha256"
    model['headerTitle'] = 'SHA256 أداة التشفير على الإنترنت - الترميز. أدوات'
    model['bodyTitle'] = 'SHA256 أداة التشفير على الإنترنت'
    model['description'] = 'تساعدك أداة التشفير على الإنترنت SHA256 هذه على تشفير سلسلة إدخال إلى سلسلة SHA256 256 بت.'
    model['keywords'] = 'SHA256 ، التشفير SHA256'
    model['image'] = '/image/comic-sha256.png'
    return render_template(template_dir + 'template_sha256_ar.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/ar/sha384', methods=['GET', 'POST'])
def sha384():
    model = get_default_model()
    model['url'] = '/ar/sha384'
    model['enUrl'] = "/sha384"
    model['headerTitle'] = 'SHA384 التشفير على الانترنت أداة - الترميز. أدوات'
    model['bodyTitle'] = 'SHA384 التشفير أداة على الانترنت'
    model['description'] = 'تساعدك أداة التشفير على الإنترنت SHA384 هذه على تشفير سلسلة إدخال في سلسلة SHA384 ثابتة ذات 384 بت.'
    model['keywords'] = 'SHA384 ، تشفير SHA384'
    model['image'] = '/image/comic-sha384.png'
    return render_template(template_dir + 'template_sha384_ar.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/ar/sha512', methods=['GET', 'POST'])
def sha512():
    model = get_default_model()
    model['url'] = '/ar/sha512'
    model['enUrl'] = "/sha512"
    model['headerTitle'] = 'SHA512 التشفير على الانترنت أداة - الترميز. أدوات'
    model['bodyTitle'] = 'SHA512 أداة التشفير على الانترنت'
    model['description'] = 'تساعدك أداة التشفير على الإنترنت SHA512 هذه على تشفير سلسلة إدخال إلى سلسلة SHA512 ذات 512-بت.'
    model['keywords'] = 'SHA512 ، التشفير SHA512'
    model['image'] = '/image/comic-sha512.png'
    return render_template(template_dir + 'template_sha512_ar.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/ar/base64-encode', methods=['GET', 'POST'])
def base64_encode():
    model = get_default_model()
    model['url'] = '/ar/base64-encode'
    model['enUrl'] = "/base64-encode"
    model['headerTitle'] = 'Base64 ترميز أداة على الإنترنت  - Coding.Tools'
    model['bodyTitle'] = 'Base64 ترميز أداة على الإنترنت'
    model['description'] = 'تساعدك أداة الترميز Base64 عبر الإنترنت على تحويل سلسلة إدخال إلى سلسلة مشفرة Base64.'
    model['keywords'] = 'Base64 ، base64 الترميز عبر الإنترنت'
    model['image'] = '/image/comic-base64-encode.png'
    return render_template(template_dir + 'template_base64_encode_ar.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/ar/base64-decode', methods=['GET', 'POST'])
def base64_decode():
    model = get_default_model()
    model['url'] = '/ar/base64-decode'
    model['enUrl'] = "/base64-decode"
    model['headerTitle'] = 'Base64 أداة فك التشفير عبر الإنترنت  - Coding.Tools'
    model['bodyTitle'] = 'Base64 أداة فك التشفير عبر الإنترنت'
    model['description'] = 'يمكن أن تساعدك أداة فك تشفير Base64 عبر الإنترنت على تحويل سلسلة تنسيق ترميز Base64 إلى سلسلة UTF-8 عادية.'
    model['keywords'] = 'Base64 ، base64 على الانترنت فك'
    model['image'] = '/image/comic-base64-decode.png'
    return render_template(template_dir + 'template_base64_decode_ar.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/ar/password-generator', methods=['GET', 'POST'])
def password_generator():
    model = get_default_model()
    model['url'] = '/ar/password-generator'
    model['enUrl'] = "/password-generator"
    model['headerTitle'] = 'أداة توليد كلمة مرور عشوائية عبر الإنترنت  - Coding.Tools'
    model['bodyTitle'] = 'أداة توليد كلمة مرور عشوائية عبر الإنترنت'
    model['description'] = 'تساعدك أداة إنشاء كلمة المرور عبر الإنترنت هذه في إنشاء كلمات مرور عشوائية وآمنة ، وإنشاء كلمات مرور مختلفة لحسابات مختلفة على الويب.'
    model['keywords'] = 'أداة توليد كلمة السر ، جيل كلمة السر على الانترنت'
    model['image'] = '/image/comic-password-generator.png'
    return render_template(template_dir + 'template_password_generator_ar.html', model=model)
