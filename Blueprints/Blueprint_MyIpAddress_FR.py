from flask import Blueprint, render_template, request
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

logger = Logic_UTIL.get_logger(__name__)
Web_MyIpAddress_blueprint = Blueprint('Web_MyIpAddress_blueprint_FR', __name__)
template_dir = 'MyIpAddress/fr/'

def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'fr'
    return model

@Web_MyIpAddress_blueprint.route('/fr/my-ip-address', methods=['GET', 'POST'])
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
        model['url'] = '/fr/my-ip-address'
        model['enUrl'] = "/my-ip-address"
        model['headerTitle'] = 'Outil de recherche en ligne Mon adresse IP  - Coding.Tools'
        model['bodyTitle'] = 'Mon outil de recherche en ligne d\'adresse IP'
        model['description'] = 'Cet outil de recherche d\'adresse IP en ligne peut vous aider à trouver votre adresse IP publique et les informations de localisation géographique de votre adresse IP, notamment la longitude, la latitude et le code postal.'
        model['keywords'] = 'Mon adresse IP, requête d\'adresse IP, requête d\'emplacement IP'
        model['image'] = '/image/comic-my-ip-addresss.png'
        return render_template(template_dir + 'template_ip_address_fr.html', model=model)


@Web_MyIpAddress_blueprint.route('/fr/ping', methods=['GET', 'POST'])
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
        model['url'] = '/fr/ping'
        model['enUrl'] = "/ping"
        model['headerTitle'] = 'Outil de détection en ligne Ping  - Coding.Tools'
        model['bodyTitle'] = 'Outil de détection en ligne Ping'
        model['description'] = 'Cet outil de ping en ligne renvoie le résultat du ping sur le serveur Linux.Vous pouvez choisir le nombre de ping sur le nom de domaine et l\'intervalle de temps entre deux requêtes ping.'
        model['keywords'] = 'Ping, détection de ping en ligne'
        model['image'] = '/image/comic-ping.png'
        return render_template(template_dir + 'template_ping_fr.html', model=model)


@Web_MyIpAddress_blueprint.route('/fr/nslookup', methods=['GET', 'POST'])
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
        model['url'] = '/fr/nslookup'
        model['enUrl'] = "/nslookup"
        model['headerTitle'] = 'Outil de requête en ligne DNS  - Coding.Tools'
        model['bodyTitle'] = 'Outil de requête en ligne DNS'
        model['description'] = 'Cet outil de requête DNS en ligne renvoie les résultats d\'une requête DNS à partir d\'un serveur Linux.Vous pouvez sélectionner le type de requête DNS (type par défaut A) et interroger cinq serveurs DNS publics (serveur DNS public par défaut de Google).'
        model['keywords'] = 'Nslookup, requête DNS en ligne'
        model['image'] = '/image/comic-nslookup.png'
        return render_template(template_dir + 'template_nslookup_fr.html', model=model)


@Web_MyIpAddress_blueprint.route('/fr/traceroute', methods=['GET', 'POST'])
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
        model['url'] = '/fr/traceroute'
        model['enUrl'] = "/traceroute"
        model['headerTitle'] = 'Outil de suivi en ligne de routeur  - Coding.Tools'
        model['bodyTitle'] = 'Outil de suivi en ligne de routeur'
        model['description'] = 'Ce traceur de routeur en ligne renvoie les résultats de traceroute du serveur Linux.Vous pouvez choisir parmi trois méthodes de suivi différentes (IMCP ECHO, TCP SYN, UDP) pour le suivi de routeur.'
        model['keywords'] = 'Traceroute, suivi de routeur'
        model['image'] = '/image/comic-traceroute.png'
        return render_template(template_dir + 'template_traceroute_fr.html', model=model)


@Web_MyIpAddress_blueprint.route('/fr/whois', methods=['GET', 'POST'])
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
        model['url'] = '/fr/whois'
        model['enUrl'] = "/whois"
        model['headerTitle'] = 'Whois Online Domain Query Tool - Outils de codage'
        model['bodyTitle'] = 'Whois outil de recherche de nom de domaine en ligne'
        model['description'] = 'Cet outil de requête de domaine Whois en ligne renvoie les résultats de la requête whois du serveur Linux pour obtenir les informations de contact du propriétaire du domaine, telles que le numéro de téléphone et l\'adresse électronique.'
        model['keywords'] = 'Whois, requête Whois'
        model['image'] = '/image/comic-whois.png'
        return render_template(template_dir + 'template_whois_fr.html', model=model)


@Web_MyIpAddress_blueprint.route('/fr/port-checker', methods=['GET', 'POST'])
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
        model['url'] = '/fr/port-checker'
        model['enUrl'] = "/port-checker"
        model['headerTitle'] = 'Outil de détection en ligne de port  - Coding.Tools'
        model['bodyTitle'] = 'Outil de détection de port en ligne'
        model['description'] = 'Cet outil de détection en ligne de port ouvert en ligne peut vous aider à détecter si un serveur est ouvert sur un port spécifique ou si les paramètres de redirection de port de votre serveur sont corrects.'
        model['keywords'] = 'Détection de port'
        model['image'] = '/image/comic-port-checker.png'
        return render_template(template_dir + 'template_port_checker_fr.html', model=model)


@Web_MyIpAddress_blueprint.route('/fr/url-encode', methods=['GET', 'POST'])
def url_encode():
    model = get_default_model()
    model['url'] = '/fr/url-encode'
    model['enUrl'] = "/url-encode"
    model['headerTitle'] = 'Outil en ligne de codage d\'URL  - Coding.Tools'
    model['bodyTitle'] = 'Outil en ligne de codage d\'URL'
    model['description'] = 'Cet outil de codage d\'URL en ligne peut vous aider à convertir une chaîne d\'entrée en une chaîne de format d\'URL.'
    model['keywords'] = 'Url encode, encodage d\'URL'
    model['image'] = '/image/comic-url-encode.png'
    return render_template(template_dir + 'template_url_encode_fr.html', model=model)


@Web_MyIpAddress_blueprint.route('/fr/url-decode', methods=['GET', 'POST'])
def url_decode():
    model = get_default_model()
    model['url'] = '/fr/url-decode'
    model['enUrl'] = "/url-decode"
    model['headerTitle'] = 'Outil en ligne de décodage d\'URL  - Coding.Tools'
    model['bodyTitle'] = 'Outil en ligne de décodage d\'URL'
    model['description'] = 'Cet outil de décodage d\'URL en ligne peut vous aider à convertir une chaîne de format d\'URL en chaîne UTF-8 en clair.'
    model['keywords'] = 'Décodage d\'URL, décodage d\'URL'
    model['image'] = '/image/comic-url-decode.png'
    return render_template(template_dir + 'template_url_decode_fr.html', model=model)
