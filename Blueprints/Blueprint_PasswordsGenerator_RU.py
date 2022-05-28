from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_PasswordsGenerator_blueprint = Blueprint('Web_PasswordsGenerator_blueprint_RU', __name__)
template_dir = 'PasswordsGenerator/ru/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'ru'
    return model


@Web_PasswordsGenerator_blueprint.route('/ru/md5', methods=['GET', 'POST'])
def md5():
    model = get_default_model()
    model['url'] = '/ru/md5'
    model['enUrl'] = "/md5"
    model['headerTitle'] = 'MD5 онлайн-инструмент шифрования  - Coding.Tools'
    model['bodyTitle'] = 'MD5 шифрование онлайн инструмент'
    model['description'] = 'Этот онлайн-инструмент шифрования MD5 поможет вам зашифровать входную строку в фиксированную 128-битную строку MD5.'
    model['keywords'] = 'MD5, MD5 шифрование'
    model['image'] = '/image/comic-md5.png'
    return render_template(template_dir + 'template_md5_ru.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/ru/sha1', methods=['GET', 'POST'])
def sha1():
    model = get_default_model()
    model['url'] = '/ru/sha1'
    model['enUrl'] = "/sha1"
    model['headerTitle'] = 'Инструмент шифрования SHA1 онлайн  - Coding.Tools'
    model['bodyTitle'] = 'SHA1 онлайн-инструмент шифрования'
    model['description'] = 'Этот онлайн-инструмент шифрования SHA1 поможет вам зашифровать входную строку в фиксированную 160-битную строку SHA1.'
    model['keywords'] = 'SHA1, SHA1 шифрование'
    model['image'] = '/image/comic-sha1.png'
    return render_template(template_dir + 'template_sha1_ru.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/ru/sha224', methods=['GET', 'POST'])
def sha224():
    model = get_default_model()
    model['url'] = '/ru/sha224'
    model['enUrl'] = "/sha224"
    model['headerTitle'] = 'Инструмент шифрования SHA224 онлайн  - Coding.Tools'
    model['bodyTitle'] = 'SHA224 онлайн-инструмент шифрования'
    model['description'] = 'Этот онлайн-инструмент шифрования SHA224 помогает зашифровать входную строку в фиксированную 224-битную строку SHA224.'
    model['keywords'] = 'SHA224, шифрование SHA224'
    model['image'] = '/image/comic-sha224.png'
    return render_template(template_dir + 'template_sha224_ru.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/ru/sha256', methods=['GET', 'POST'])
def sha256():
    model = get_default_model()
    model['url'] = '/ru/sha256'
    model['enUrl'] = "/sha256"
    model['headerTitle'] = 'SHA256 онлайн инструмент шифрования  - Coding.Tools'
    model['bodyTitle'] = 'SHA256 онлайн инструмент шифрования'
    model['description'] = 'Этот онлайн-инструмент шифрования SHA256 помогает зашифровать входную строку в фиксированную 256-битную строку SHA256.'
    model['keywords'] = 'SHA256, шифрование SHA256'
    model['image'] = '/image/comic-sha256.png'
    return render_template(template_dir + 'template_sha256_ru.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/ru/sha384', methods=['GET', 'POST'])
def sha384():
    model = get_default_model()
    model['url'] = '/ru/sha384'
    model['enUrl'] = "/sha384"
    model['headerTitle'] = 'SHA384 онлайн-инструмент шифрования  - Coding.Tools'
    model['bodyTitle'] = 'SHA384 онлайн-инструмент шифрования'
    model['description'] = 'Этот онлайн-инструмент шифрования SHA384 помогает зашифровать входную строку в фиксированную 384-битную строку SHA384'
    model['keywords'] = 'SHA384, шифрование SHA384'
    model['image'] = '/image/comic-sha384.png'
    return render_template(template_dir + 'template_sha384_ru.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/ru/sha512', methods=['GET', 'POST'])
def sha512():
    model = get_default_model()
    model['url'] = '/ru/sha512'
    model['enUrl'] = "/sha512"
    model['headerTitle'] = 'Инструмент шифрования SHA512 онлайн  - Coding.Tools'
    model['bodyTitle'] = 'SHA512 онлайн-инструмент шифрования'
    model['description'] = 'Этот онлайн-инструмент шифрования SHA512 поможет вам зашифровать входную строку в фиксированную 512-битную строку SHA512.'
    model['keywords'] = 'SHA512, шифрование SHA512'
    model['image'] = '/image/comic-sha512.png'
    return render_template(template_dir + 'template_sha512_ru.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/ru/base64-encode', methods=['GET', 'POST'])
def base64_encode():
    model = get_default_model()
    model['url'] = '/ru/base64-encode'
    model['enUrl'] = "/base64-encode"
    model['headerTitle'] = 'Онлайн инструмент для кодирования Base64  - Coding.Tools'
    model['bodyTitle'] = 'Онлайн-инструмент для кодирования Base64'
    model['description'] = 'Этот интерактивный инструмент кодирования Base64 помогает преобразовать входную строку в строку в кодировке Base64.'
    model['keywords'] = 'Base64, base64 онлайн-кодирование'
    model['image'] = '/image/comic-base64-encode.png'
    return render_template(template_dir + 'template_base64_encode_ru.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/ru/base64-decode', methods=['GET', 'POST'])
def base64_decode():
    model = get_default_model()
    model['url'] = '/ru/base64-decode'
    model['enUrl'] = "/base64-decode"
    model['headerTitle'] = 'Base64 онлайн инструмент для декодирования  - Coding.Tools'
    model['bodyTitle'] = 'Base64 онлайн инструмент для декодирования'
    model['description'] = 'Этот интерактивный инструмент декодирования Base64 может помочь вам преобразовать строку формата в кодировке Base64 в обычную строку UTF-8.'
    model['keywords'] = 'Base64, base64 онлайн декодирование'
    model['image'] = '/image/comic-base64-decode.png'
    return render_template(template_dir + 'template_base64_decode_ru.html', model=model)


@Web_PasswordsGenerator_blueprint.route('/ru/password-generator', methods=['GET', 'POST'])
def password_generator():
    model = get_default_model()
    model['url'] = '/ru/password-generator'
    model['enUrl'] = "/password-generator"
    model['headerTitle'] = 'Онлайн инструмент для генерации случайных паролей  - Coding.Tools'
    model['bodyTitle'] = 'Онлайн инструмент для генерации случайных паролей'
    model['description'] = 'Этот онлайн-инструмент для генерации паролей помогает вам генерировать случайные и надежные пароли.Создайте разные пароли для разных учетных записей веб-сайтов.'
    model['keywords'] = 'Инструмент генерации паролей, онлайн генерация паролей'
    model['image'] = '/image/comic-password-generator.png'
    return render_template(template_dir + 'template_password_generator_ru.html', model=model)
