from flask import Blueprint, render_template, request
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

logger = Logic_UTIL.get_logger(__name__)
Web_MyIpAddress_blueprint = Blueprint('Web_MyIpAddress_blueprint_PT', __name__)
template_dir = 'MyIpAddress/pt/'

def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'pt'
    return model

@Web_MyIpAddress_blueprint.route('/pt/my-ip-address', methods=['GET', 'POST'])
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
        model['url'] = '/pt/my-ip-address'
        model['enUrl'] = "/my-ip-address"
        model['headerTitle'] = 'Minha ferramenta de consulta online de endereços IP  - Coding.Tools'
        model['bodyTitle'] = 'Minha ferramenta de consulta on-line de endereço IP'
        model['description'] = 'Essa ferramenta de pesquisa de endereço IP on-line pode ajudar você a encontrar seu endereço IP público e informações de localização geográfica para seu endereço IP, incluindo longitude, latitude e código postal.'
        model['keywords'] = 'Meu endereço IP, consulta de endereço IP, consulta de localização IP'
        model['image'] = '/image/comic-my-ip-addresss.png'
        return render_template(template_dir + 'template_ip_address_pt.html', model=model)


@Web_MyIpAddress_blueprint.route('/pt/ping', methods=['GET', 'POST'])
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
        model['url'] = '/pt/ping'
        model['enUrl'] = "/ping"
        model['headerTitle'] = 'Ferramenta de detecção on-line de ping  - Coding.Tools'
        model['bodyTitle'] = 'Ferramenta de detecção on-line de ping'
        model['description'] = 'Esta ferramenta de ping on-line retorna o resultado do ping do servidor Linux.Você pode escolher o número de vezes para pingar o nome de domínio e o intervalo de tempo entre duas consultas de ping.'
        model['keywords'] = 'Ping, detecção on-line de ping'
        model['image'] = '/image/comic-ping.png'
        return render_template(template_dir + 'template_ping_pt.html', model=model)


@Web_MyIpAddress_blueprint.route('/pt/nslookup', methods=['GET', 'POST'])
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
        model['url'] = '/pt/nslookup'
        model['enUrl'] = "/nslookup"
        model['headerTitle'] = 'Ferramenta de consulta on-line de DNS  - Coding.Tools'
        model['bodyTitle'] = 'Ferramenta de consulta on-line de DNS'
        model['description'] = 'Essa ferramenta de consulta DNS online retorna os resultados da consulta DNS de um servidor Linux.Você pode selecionar o tipo de consulta DNS (tipo padrão A) e consultar os cinco servidores DNS públicos (servidor DNS público padrão do Google).'
        model['keywords'] = 'Nslookup, consulta on-line de DNS'
        model['image'] = '/image/comic-nslookup.png'
        return render_template(template_dir + 'template_nslookup_pt.html', model=model)


@Web_MyIpAddress_blueprint.route('/pt/traceroute', methods=['GET', 'POST'])
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
        model['url'] = '/pt/traceroute'
        model['enUrl'] = "/traceroute"
        model['headerTitle'] = 'Ferramenta de rastreamento on-line do roteador  - Coding.Tools'
        model['bodyTitle'] = 'Ferramenta de rastreamento on-line do roteador'
        model['description'] = 'Este rastreador de roteador on-line retorna os resultados do traceroute do servidor Linux.Você pode escolher entre três métodos de rastreamento diferentes (IMCP ECHO, TCP SYN, UDP) para rastreamento de roteador.'
        model['keywords'] = 'Traceroute, rastreamento de roteador'
        model['image'] = '/image/comic-traceroute.png'
        return render_template(template_dir + 'template_traceroute_pt.html', model=model)


@Web_MyIpAddress_blueprint.route('/pt/whois', methods=['GET', 'POST'])
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
        model['url'] = '/pt/whois'
        model['enUrl'] = "/whois"
        model['headerTitle'] = 'Ferramenta de consulta de domínio Whois Online  - Coding.Tools'
        model['bodyTitle'] = 'Ferramenta de consulta de nome de domínio online Whois'
        model['description'] = 'Essa ferramenta de consulta de domínio Whois on-line retorna os resultados da consulta whois do servidor Linux para obter as informações de contato do proprietário do domínio, como número de telefone e endereço de email.'
        model['keywords'] = 'Whois, consulta Whois'
        model['image'] = '/image/comic-whois.png'
        return render_template(template_dir + 'template_whois_pt.html', model=model)


@Web_MyIpAddress_blueprint.route('/pt/port-checker', methods=['GET', 'POST'])
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
        model['url'] = '/pt/port-checker'
        model['enUrl'] = "/port-checker"
        model['headerTitle'] = 'Ferramenta de deteção online de portas  - Coding.Tools'
        model['bodyTitle'] = 'Ferramenta de detecção online de portas'
        model['description'] = 'Essa ferramenta online de detecção de portas abertas pode ajudá-lo a detectar se algum servidor está aberto em uma porta específica ou se as configurações de encaminhamento de porta do servidor estão corretas.'
        model['keywords'] = 'Detecção de porta'
        model['image'] = '/image/comic-port-checker.png'
        return render_template(template_dir + 'template_port_checker_pt.html', model=model)


@Web_MyIpAddress_blueprint.route('/pt/url-encode', methods=['GET', 'POST'])
def url_encode():
    model = get_default_model()
    model['url'] = '/pt/url-encode'
    model['enUrl'] = "/url-encode"
    model['headerTitle'] = 'Ferramenta online de codificação de URL  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta on-line de codificação de URL'
    model['description'] = 'Essa ferramenta de codificação de URL on-line pode ajudá-lo a converter uma string de entrada em uma string de formato de URL.'
    model['keywords'] = 'Codificação URL, codificação URL'
    model['image'] = '/image/comic-url-encode.png'
    return render_template(template_dir + 'template_url_encode_pt.html', model=model)


@Web_MyIpAddress_blueprint.route('/pt/url-decode', methods=['GET', 'POST'])
def url_decode():
    model = get_default_model()
    model['url'] = '/pt/url-decode'
    model['enUrl'] = "/url-decode"
    model['headerTitle'] = 'Ferramenta on-line de decodificação de URL  - Coding.Tools'
    model['bodyTitle'] = 'Ferramenta on-line de decodificação de URL'
    model['description'] = 'Essa ferramenta de decodificação de URL on-line pode ajudá-lo a converter uma string de formato de URL em uma string UTF-8 simples.'
    model['keywords'] = 'Decodificação de URL, decodificação de URL'
    model['image'] = '/image/comic-url-decode.png'
    return render_template(template_dir + 'template_url_decode_pt.html', model=model)
