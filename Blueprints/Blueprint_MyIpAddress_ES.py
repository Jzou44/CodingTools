from flask import Blueprint, render_template, request
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

logger = Logic_UTIL.get_logger(__name__)
Web_MyIpAddress_blueprint = Blueprint('Web_MyIpAddress_blueprint_ES', __name__)
template_dir = 'MyIpAddress/es/'

def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'es'
    return model

@Web_MyIpAddress_blueprint.route('/es/my-ip-address', methods=['GET', 'POST'])
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
        model['url'] = '/es/my-ip-address'
        model['enUrl'] = "/my-ip-address"
        model['headerTitle'] = 'Herramienta de consulta en línea de mi dirección IP  - Coding.Tools'
        model['bodyTitle'] = 'Herramienta de consulta en línea de mi dirección IP'
        model['description'] = 'Esta herramienta de búsqueda de direcciones IP en línea puede ayudarlo a encontrar su dirección IP pública y la información de ubicación geográfica para su dirección IP, incluyendo longitud, latitud y código postal.'
        model['keywords'] = 'Mi dirección IP, consulta de dirección IP, consulta de ubicación IP'
        model['image'] = '/image/comic-my-ip-addresss.png'
        return render_template(template_dir + 'template_ip_address_es.html', model=model)


@Web_MyIpAddress_blueprint.route('/es/ping', methods=['GET', 'POST'])
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
        model['url'] = '/es/ping'
        model['enUrl'] = "/ping"
        model['headerTitle'] = 'Herramienta de detección de ping en línea - Codificación.Herramientas'
        model['bodyTitle'] = 'Herramienta de detección de ping en línea'
        model['description'] = 'Esta herramienta de ping en línea devuelve el resultado de ping del servidor de Linux. Puede elegir el número de veces para hacer ping al nombre de dominio y el intervalo de tiempo entre dos consultas de ping.'
        model['keywords'] = 'Ping, ping detección en línea'
        model['image'] = '/image/comic-ping.png'
        return render_template(template_dir + 'template_ping_es.html', model=model)


@Web_MyIpAddress_blueprint.route('/es/nslookup', methods=['GET', 'POST'])
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
        model['url'] = '/es/nslookup'
        model['enUrl'] = "/nslookup"
        model['headerTitle'] = 'Herramienta de consulta en línea de DNS  - Coding.Tools'
        model['bodyTitle'] = 'Herramienta de consulta en línea de DNS'
        model['description'] = 'Esta herramienta de consulta de DNS en línea devuelve los resultados de la consulta de DNS de un servidor Linux. Puede seleccionar el tipo de consulta de DNS (tipo predeterminado A) y consultar cinco servidores DNS públicos (servidor DNS público de Google predeterminado).'
        model['keywords'] = 'Nslookup, consulta de DNS en línea'
        model['image'] = '/image/comic-nslookup.png'
        return render_template(template_dir + 'template_nslookup_es.html', model=model)


@Web_MyIpAddress_blueprint.route('/es/traceroute', methods=['GET', 'POST'])
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
        model['url'] = '/es/traceroute'
        model['enUrl'] = "/traceroute"
        model['headerTitle'] = 'Herramienta de seguimiento de enrutador en línea - Codificación.Herramientas'
        model['bodyTitle'] = 'Herramienta de seguimiento de enrutador en línea'
        model['description'] = 'Este rastreador de enrutador en línea devuelve los resultados de traceroute desde el servidor Linux. Puede elegir entre tres métodos de seguimiento diferentes (IMCP ECHO, TCP SYN, UDP) para el seguimiento de enrutadores.'
        model['keywords'] = 'Traceroute, seguimiento de enrutador'
        model['image'] = '/image/comic-traceroute.png'
        return render_template(template_dir + 'template_traceroute_es.html', model=model)


@Web_MyIpAddress_blueprint.route('/es/whois', methods=['GET', 'POST'])
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
        model['url'] = '/es/whois'
        model['enUrl'] = "/whois"
        model['headerTitle'] = 'Herramienta de consulta de dominio en línea de Whois  - Coding.Tools'
        model['bodyTitle'] = 'Herramienta de consulta de nombres de dominio en línea Whois'
        model['description'] = 'Esta herramienta de consulta del dominio Whois en línea devuelve los resultados de la consulta whois del servidor Linux para obtener la información de contacto del propietario del dominio, como el número de teléfono y la dirección de correo electrónico.'
        model['keywords'] = 'Whois, consulta Whois'
        model['image'] = '/image/comic-whois.png'
        return render_template(template_dir + 'template_whois_es.html', model=model)


@Web_MyIpAddress_blueprint.route('/es/port-checker', methods=['GET', 'POST'])
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
        model['url'] = '/es/port-checker'
        model['enUrl'] = "/port-checker"
        model['headerTitle'] = 'Herramienta de detección de puertos en línea - Codificación.Herramientas'
        model['bodyTitle'] = 'Herramienta de detección de puerto en línea'
        model['description'] = 'Esta herramienta de detección en línea de puerto abierto en línea puede ayudarlo a detectar si algún servidor está abierto en un puerto específico o si la configuración de reenvío de puerto de su servidor es correcta.'
        model['keywords'] = 'Detección de puertos'
        model['image'] = '/image/comic-port-checker.png'
        return render_template(template_dir + 'template_port_checker_es.html', model=model)


@Web_MyIpAddress_blueprint.route('/es/url-encode', methods=['GET', 'POST'])
def url_encode():
    model = get_default_model()
    model['url'] = '/es/url-encode'
    model['enUrl'] = "/url-encode"
    model['headerTitle'] = 'Herramienta de codificación de URL en línea - Codificación.Herramientas'
    model['bodyTitle'] = 'Herramienta de codificación de URL en línea'
    model['description'] = 'Esta herramienta de codificación de URL en línea puede ayudarlo a convertir una cadena de entrada en una cadena de formato URL.'
    model['keywords'] = 'Codificación de URL, codificación de URL'
    model['image'] = '/image/comic-url-encode.png'
    return render_template(template_dir + 'template_url_encode_es.html', model=model)


@Web_MyIpAddress_blueprint.route('/es/url-decode', methods=['GET', 'POST'])
def url_decode():
    model = get_default_model()
    model['url'] = '/es/url-decode'
    model['enUrl'] = "/url-decode"
    model['headerTitle'] = 'Herramienta de decodificación de URL en línea  - Coding.Tools'
    model['bodyTitle'] = 'Herramienta de decodificación de URL en línea'
    model['description'] = 'Esta herramienta de decodificación de URL en línea puede ayudarlo a convertir una cadena de formato URL en una cadena UTF-8 simple.'
    model['keywords'] = 'Decodificación de url, decodificación de URL'
    model['image'] = '/image/comic-url-decode.png'
    return render_template(template_dir + 'template_url_decode_es.html', model=model)
