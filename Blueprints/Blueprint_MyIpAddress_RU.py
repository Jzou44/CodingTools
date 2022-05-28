from flask import Blueprint, render_template, request
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

logger = Logic_UTIL.get_logger(__name__)
Web_MyIpAddress_blueprint = Blueprint('Web_MyIpAddress_blueprint_RU', __name__)
template_dir = 'MyIpAddress/ru/'

def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'ru'
    return model

@Web_MyIpAddress_blueprint.route('/ru/my-ip-address', methods=['GET', 'POST'])
def home_page_handle_get():
    if request.method == 'POST':
        try:
            options = request.form
            ip_str = str(options['queryIp'])
            code2 = Logic_MyIpAddress.ip_geo_search(ip_str)
        except Exception as e:
            logger.error(str(e))
            code2 = 'Invalid Input Options'
        return code2
    else:
        model = get_default_model()
        # try:
        #     model['geolocation'] = Logic_MyIpAddress.ip_geo_search()
        # except Exception as e:
        #     logger.error(str(e))
        model['url'] = '/ru/my-ip-address'
        model['enUrl'] = "/my-ip-address"
        model['headerTitle'] = 'Мой IP-адрес онлайн-инструмент запросов  - Coding.Tools'
        model['bodyTitle'] = 'Мой IP-адрес онлайн-инструмент для запросов'
        model['description'] = 'Этот онлайн-инструмент поиска IP-адресов поможет вам найти ваш общедоступный IP-адрес и информацию о географическом местоположении для вашего IP-адреса, включая долготу, широту и почтовый индекс.'
        model['keywords'] = 'Мой IP-адрес, запрос IP-адреса, запрос IP-адреса'
        model['image'] = '/image/comic-my-ip-addresss.png'
        return render_template(template_dir + 'template_ip_address_ru.html', model=model)


@Web_MyIpAddress_blueprint.route('/ru/ping', methods=['GET', 'POST'])
def ping():
    if request.method == 'POST':
        try:
            options = request.form
            code2 = Logic_MyIpAddress.ping_command(options)
        except Exception as e:
            logger.error(str(e))
            code2 = 'Invalid Input Options'
        return code2
    else:
        model = get_default_model()
        model['url'] = '/ru/ping'
        model['enUrl'] = "/ping"
        model['headerTitle'] = 'Ping онлайн-инструмент обнаружения  - Coding.Tools'
        model['bodyTitle'] = 'Ping онлайн-инструмент обнаружения'
        model['description'] = 'Этот онлайн-инструмент ping возвращает результат ping с сервера Linux.Можно выбрать, сколько раз пинговать имя домена и интервал времени между двумя запросами ping.'
        model['keywords'] = 'Пинг, пинг онлайн обнаружения'
        model['image'] = '/image/comic-ping.png'
        return render_template(template_dir + 'template_ping_ru.html', model=model)


@Web_MyIpAddress_blueprint.route('/ru/nslookup', methods=['GET', 'POST'])
def nslookup():
    if request.method == 'POST':
        try:
            options = request.form
            code2 = Logic_MyIpAddress.nslookup_command(options)
        except Exception as e:
            logger.error(str(e))
            code2 = 'Invalid Input Options'
        return code2
    else:
        model = get_default_model()
        model['url'] = '/ru/nslookup'
        model['enUrl'] = "/nslookup"
        model['headerTitle'] = 'DNS онлайн-инструмент запросов  - Coding.Tools'
        model['bodyTitle'] = 'DNS онлайн-инструмент для запросов'
        model['description'] = 'Этот онлайн-инструмент DNS-запроса возвращает результаты DNS-запроса с сервера Linux.Вы можете выбрать тип DNS-запроса (тип A по умолчанию) и запросить любые пять общедоступных DNS-серверов (общедоступный DNS-сервер Google по умолчанию).'
        model['keywords'] = 'Nslookup, DNS онлайн-запрос'
        model['image'] = '/image/comic-nslookup.png'
        return render_template(template_dir + 'template_nslookup_ru.html', model=model)


@Web_MyIpAddress_blueprint.route('/ru/traceroute', methods=['GET', 'POST'])
def traceroute():
    if request.method == 'POST':
        try:
            options = request.form
            code2 = Logic_MyIpAddress.traceroute_command(options)
        except Exception as e:
            logger.error(str(e))
            code2 = 'Invalid Input Options'
        return code2
    else:
        model = get_default_model()
        model['url'] = '/ru/traceroute'
        model['enUrl'] = "/traceroute"
        model['headerTitle'] = 'Маршрутизатор онлайн-инструмент отслеживания  - Coding.Tools'
        model['bodyTitle'] = 'Маршрутизатор онлайн отслеживания'
        model['description'] = 'Этот онлайн-трассировщик маршрутизатора возвращает результаты трассировки с сервера Linux.Вы можете выбрать один из трех методов отслеживания (IMCP ECHO, TCP SYN, UDP) для отслеживания маршрутизатора.'
        model['keywords'] = 'Traceroute, отслеживание роутера'
        model['image'] = '/image/comic-traceroute.png'
        return render_template(template_dir + 'template_traceroute_ru.html', model=model)


@Web_MyIpAddress_blueprint.route('/ru/whois', methods=['GET', 'POST'])
def whois():
    if request.method == 'POST':
        try:
            options = request.form
            code2 = Logic_MyIpAddress.whois_command(options)
        except Exception as e:
            logger.error(str(e))
            code2 = 'Invalid Input Options'
        return code2
    else:
        model = get_default_model()
        model['url'] = '/ru/whois'
        model['enUrl'] = "/whois"
        model['headerTitle'] = 'Whois Online инструмент для запроса домена  - Coding.Tools'
        model['bodyTitle'] = 'Whois онлайн инструмент для запроса доменного имени'
        model['description'] = 'Этот онлайн-инструмент для запроса домена Whois возвращает результаты запроса whois с сервера Linux, чтобы получить контактную информацию владельца домена, такую как номер телефона и адрес электронной почты.'
        model['keywords'] = 'Whois, запрос Whois'
        model['image'] = '/image/comic-whois.png'
        return render_template(template_dir + 'template_whois_ru.html', model=model)


@Web_MyIpAddress_blueprint.route('/ru/port-checker', methods=['GET', 'POST'])
def port_checker():
    if request.method == 'POST':
        try:
            options = request.form
            code2 = Logic_MyIpAddress.port_checker(options)
        except Exception as e:
            logger.error(str(e))
            code2 = 'Invalid Input Options'
        return code2
    else:
        model = get_default_model()
        model['url'] = '/ru/port-checker'
        model['enUrl'] = "/port-checker"
        model['headerTitle'] = 'Порт онлайн-инструмент обнаружения  - Coding.Tools'
        model['bodyTitle'] = 'Порт онлайн-инструмент обнаружения'
        model['description'] = 'Этот онлайн-инструмент для обнаружения открытых портов онлайн может помочь вам определить, открыт ли какой-либо сервер для определенного порта или правильные параметры переадресации портов вашего сервера.'
        model['keywords'] = 'Обнаружение порта'
        model['image'] = '/image/comic-port-checker.png'
        return render_template(template_dir + 'template_port_checker_ru.html', model=model)


@Web_MyIpAddress_blueprint.route('/ru/url-encode', methods=['GET', 'POST'])
def url_encode():
    model = get_default_model()
    model['url'] = '/ru/url-encode'
    model['enUrl'] = "/url-encode"
    model['headerTitle'] = 'Инструмент для онлайн-кодирования URL  - Coding.Tools'
    model['bodyTitle'] = 'Онлайн-инструмент для кодирования URL'
    model['description'] = 'Этот онлайн-инструмент кодирования URL может помочь вам преобразовать входную строку в строку формата URL.'
    model['keywords'] = 'URL-кодирование, URL-кодирование'
    model['image'] = '/image/comic-url-encode.png'
    return render_template(template_dir + 'template_url_encode_ru.html', model=model)


@Web_MyIpAddress_blueprint.route('/ru/url-decode', methods=['GET', 'POST'])
def url_decode():
    model = get_default_model()
    model['url'] = '/ru/url-decode'
    model['enUrl'] = "/url-decode"
    model['headerTitle'] = 'Интернет-инструмент для декодирования URL  - Coding.Tools'
    model['bodyTitle'] = 'Интернет-инструмент для декодирования URL'
    model['description'] = 'Этот онлайн-инструмент для декодирования URL может помочь вам преобразовать строку формата URL в обычную строку UTF-8'
    model['keywords'] = 'Декодирование URL, декодирование URL'
    model['image'] = '/image/comic-url-decode.png'
    return render_template(template_dir + 'template_url_decode_ru.html', model=model)
