from flask import Blueprint, render_template, request
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

logger = Logic_UTIL.get_logger(__name__)
Web_MyIpAddress_blueprint = Blueprint('Web_MyIpAddress_blueprint_DE', __name__)
template_dir = 'MyIpAddress/de/'

def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'de'
    return model

@Web_MyIpAddress_blueprint.route('/de/my-ip-address', methods=['GET', 'POST'])
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
        model['url'] = '/de/my-ip-address'
        model['enUrl'] = "/my-ip-address"
        model['headerTitle'] = 'Online-Abfrage-Tool für meine IP-Adresse  - Coding.Tools'
        model['bodyTitle'] = 'Online-Abfrage-Tool für meine IP-Adresse'
        model['description'] = 'Mit diesem Online-Tool zum Suchen von IP-Adressen können Sie Ihre öffentliche IP-Adresse und geografische Standortinformationen für Ihre IP-Adresse finden, einschließlich Längengrad, Breitengrad und Postleitzahl.'
        model['keywords'] = 'Meine IP-Adresse, IP-Adressabfrage, IP-Standortabfrage'
        model['image'] = '/image/comic-my-ip-addresss.png'
        return render_template(template_dir + 'template_ip_address_de.html', model=model)


@Web_MyIpAddress_blueprint.route('/de/ping', methods=['GET', 'POST'])
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
        model['url'] = '/de/ping'
        model['enUrl'] = "/ping"
        model['headerTitle'] = 'Ping-Online-Erkennungstool  - Coding.Tools'
        model['bodyTitle'] = 'Ping-Online-Erkennungstool'
        model['description'] = 'Dieses Online-Ping-Tool gibt das Ping-Ergebnis vom Linux-Server zurück. Sie können auswählen, wie oft der Domain-Name gepingt werden soll, sowie das Zeitintervall zwischen zwei Ping-Abfragen.'
        model['keywords'] = 'Ping, Ping-Onlineerkennung'
        model['image'] = '/image/comic-ping.png'
        return render_template(template_dir + 'template_ping_de.html', model=model)


@Web_MyIpAddress_blueprint.route('/de/nslookup', methods=['GET', 'POST'])
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
        model['url'] = '/de/nslookup'
        model['enUrl'] = "/nslookup"
        model['headerTitle'] = 'DNS-Online-Abfrage-Tool  - Coding.Tools'
        model['bodyTitle'] = 'DNS-Online-Abfrage-Tool'
        model['description'] = 'Dieses Online-DNS-Abfragetool gibt DNS-Abfrageergebnisse von einem Linux-Server zurück. Sie können den DNS-Abfragetyp auswählen (Standardtyp A) und fünf beliebige öffentliche DNS-Server (Standard-Google-öffentlicher DNS-Server) abfragen.'
        model['keywords'] = 'Nslookup, DNS-Online-Abfrage'
        model['image'] = '/image/comic-nslookup.png'
        return render_template(template_dir + 'template_nslookup_de.html', model=model)


@Web_MyIpAddress_blueprint.route('/de/traceroute', methods=['GET', 'POST'])
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
        model['url'] = '/de/traceroute'
        model['enUrl'] = "/traceroute"
        model['headerTitle'] = 'Online-Tracking-Tool für Router  - Coding.Tools'
        model['bodyTitle'] = 'Online-Tracking-Tool für Router'
        model['description'] = 'Dieser Online-Tracer-Tracer liefert die Traceroute-Ergebnisse vom Linux-Server. Sie können aus drei verschiedenen Tracking-Methoden (IMCP ECHO, TCP SYN, UDP) für die Routerverfolgung auswählen.'
        model['keywords'] = 'Traceroute, Routerverfolgung'
        model['image'] = '/image/comic-traceroute.png'
        return render_template(template_dir + 'template_traceroute_de.html', model=model)


@Web_MyIpAddress_blueprint.route('/de/whois', methods=['GET', 'POST'])
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
        model['url'] = '/de/whois'
        model['enUrl'] = "/whois"
        model['headerTitle'] = 'Whois Online Domain Abfrage-Tool  - Coding.Tools'
        model['bodyTitle'] = 'Whois Online-Abfrage für Domainnamen'
        model['description'] = 'Dieses Online-Abfrage-Tool für Whois-Domänen gibt die whois-Abfrageergebnisse vom Linux-Server zurück, um die Kontaktinformationen des Domäneninhabers abzurufen, z. B. Telefonnummer und E-Mail-Adresse.'
        model['keywords'] = 'Whois, Whois-Abfrage'
        model['image'] = '/image/comic-whois.png'
        return render_template(template_dir + 'template_whois_de.html', model=model)


@Web_MyIpAddress_blueprint.route('/de/port-checker', methods=['GET', 'POST'])
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
        model['url'] = '/de/port-checker'
        model['enUrl'] = "/port-checker"
        model['headerTitle'] = 'Port-Online-Erkennungstool  - Coding.Tools'
        model['bodyTitle'] = 'Port Online-Erkennungstool'
        model['description'] = 'Mit diesem Online-Erkennungstool für online geöffnete Ports können Sie feststellen, ob an einem bestimmten Port ein Server geöffnet ist oder ob die Einstellungen für die Server-Port-Weiterleitung korrekt sind.'
        model['keywords'] = 'Porterkennung'
        model['image'] = '/image/comic-port-checker.png'
        return render_template(template_dir + 'template_port_checker_de.html', model=model)


@Web_MyIpAddress_blueprint.route('/de/url-encode', methods=['GET', 'POST'])
def url_encode():
    model = get_default_model()
    model['url'] = '/de/url-encode'
    model['enUrl'] = "/url-encode"
    model['headerTitle'] = 'Online-Tool zur URL-Kodierung  - Coding.Tools'
    model['bodyTitle'] = 'Online-Tool zur URL-Kodierung'
    model['description'] = 'Mit diesem Online-URL-Codierungsprogramm können Sie eine Eingabezeichenfolge in eine URL-Formatzeichenfolge konvertieren.'
    model['keywords'] = 'URL-Kodierung, URL-Kodierung'
    model['image'] = '/image/comic-url-encode.png'
    return render_template(template_dir + 'template_url_encode_de.html', model=model)


@Web_MyIpAddress_blueprint.route('/de/url-decode', methods=['GET', 'POST'])
def url_decode():
    model = get_default_model()
    model['url'] = '/de/url-decode'
    model['enUrl'] = "/url-decode"
    model['headerTitle'] = 'Online-Tool zur URL-Dekodierung  - Coding.Tools'
    model['bodyTitle'] = 'Online-Tool zur URL-Dekodierung'
    model['description'] = 'Mit diesem Online-Tool zum Dekodieren von URLs können Sie eine URL-Formatzeichenfolge in eine einfache UTF-8-Zeichenfolge konvertieren.'
    model['keywords'] = 'URL-Dekodierung, URL-Dekodierung'
    model['image'] = '/image/comic-url-decode.png'
    return render_template(template_dir + 'template_url_decode_de.html', model=model)
