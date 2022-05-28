from flask import Blueprint, render_template, request
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

logger = Logic_UTIL.get_logger(__name__)
Web_MyIpAddress_blueprint = Blueprint('Web_MyIpAddress_blueprint_IT', __name__)
template_dir = 'MyIpAddress/it/'

def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'it'
    return model

@Web_MyIpAddress_blueprint.route('/it/my-ip-address', methods=['GET', 'POST'])
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
        model['url'] = '/it/my-ip-address'
        model['enUrl'] = "/my-ip-address"
        model['headerTitle'] = 'Strumento di interrogazione online del mio indirizzo IP  - Coding.Tools'
        model['bodyTitle'] = 'Il mio strumento di ricerca online con indirizzo IP'
        model['description'] = 'Questo strumento per la ricerca degli indirizzi IP online può aiutarti a trovare il tuo indirizzo IP pubblico e le informazioni sulla posizione geografica per il tuo indirizzo IP, inclusi longitudine, latitudine e codice postale.'
        model['keywords'] = 'Il mio indirizzo IP, query di indirizzo IP, query di localizzazione IP'
        model['image'] = '/image/comic-my-ip-addresss.png'
        return render_template(template_dir + 'template_ip_address_it.html', model=model)


@Web_MyIpAddress_blueprint.route('/it/ping', methods=['GET', 'POST'])
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
        model['url'] = '/it/ping'
        model['enUrl'] = "/ping"
        model['headerTitle'] = 'Ping strumento di rilevamento online  - Coding.Tools'
        model['bodyTitle'] = 'Ping strumento di rilevamento online'
        model['description'] = 'Questo strumento ping online restituisce il risultato del ping dal server Linux.È possibile scegliere il numero di volte in cui eseguire il ping del nome del dominio e l\'intervallo di tempo tra due query ping.'
        model['keywords'] = 'Ping, ping rilevamento online'
        model['image'] = '/image/comic-ping.png'
        return render_template(template_dir + 'template_ping_it.html', model=model)


@Web_MyIpAddress_blueprint.route('/it/nslookup', methods=['GET', 'POST'])
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
        model['url'] = '/it/nslookup'
        model['enUrl'] = "/nslookup"
        model['headerTitle'] = 'Strumento di query online DNS  - Coding.Tools'
        model['bodyTitle'] = 'Strumento di query online DNS'
        model['description'] = 'Questo strumento di query DNS online restituisce i risultati delle query DNS da un server Linux.È possibile selezionare il tipo di query DNS (tipo A predefinito) e interrogare cinque server DNS pubblici (server DNS pubblico di Google predefinito).'
        model['keywords'] = 'Nslookup, query online DNS'
        model['image'] = '/image/comic-nslookup.png'
        return render_template(template_dir + 'template_nslookup_it.html', model=model)


@Web_MyIpAddress_blueprint.route('/it/traceroute', methods=['GET', 'POST'])
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
        model['url'] = '/it/traceroute'
        model['enUrl'] = "/traceroute"
        model['headerTitle'] = 'Strumento di monitoraggio online router  - Coding.Tools'
        model['bodyTitle'] = 'Strumento di monitoraggio online del router'
        model['description'] = 'Questo tracciante del router online restituisce i risultati del traceroute dal server Linux.È possibile scegliere tra tre diversi metodi di tracciamento (IMCP ECHO, TCP SYN, UDP) per il tracciamento del router.'
        model['keywords'] = 'Traceroute, tracciamento router'
        model['image'] = '/image/comic-traceroute.png'
        return render_template(template_dir + 'template_traceroute_it.html', model=model)


@Web_MyIpAddress_blueprint.route('/it/whois', methods=['GET', 'POST'])
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
        model['url'] = '/it/whois'
        model['enUrl'] = "/whois"
        model['headerTitle'] = 'Strumento di query di dominio online Whois  - Coding.Tools'
        model['bodyTitle'] = 'Strumento per la ricerca del nome di dominio online Whois'
        model['description'] = 'Questo strumento di query del dominio Whois in linea restituisce i risultati della query whois dal server Linux per ottenere le informazioni di contatto del proprietario del dominio, come il numero di telefono e l\'indirizzo email.'
        model['keywords'] = 'Whois, query Whois'
        model['image'] = '/image/comic-whois.png'
        return render_template(template_dir + 'template_whois_it.html', model=model)


@Web_MyIpAddress_blueprint.route('/it/port-checker', methods=['GET', 'POST'])
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
        model['url'] = '/it/port-checker'
        model['enUrl'] = "/port-checker"
        model['headerTitle'] = 'Port strumento di rilevamento online  - Coding.Tools'
        model['bodyTitle'] = 'Port strumento di rilevamento online'
        model['description'] = 'Questo strumento online di rilevamento online delle porte aperte può aiutarti a rilevare se un server è aperto su una porta specifica o se le impostazioni del port forwarding del server sono corrette.'
        model['keywords'] = 'Rilevazione della porta'
        model['image'] = '/image/comic-port-checker.png'
        return render_template(template_dir + 'template_port_checker_it.html', model=model)


@Web_MyIpAddress_blueprint.route('/it/url-encode', methods=['GET', 'POST'])
def url_encode():
    model = get_default_model()
    model['url'] = '/it/url-encode'
    model['enUrl'] = "/url-encode"
    model['headerTitle'] = 'Strumento di codifica URL online  - Coding.Tools'
    model['bodyTitle'] = 'Strumento di codifica degli URL online'
    model['description'] = 'Questo strumento di codifica degli URL online può aiutarti a convertire una stringa di input in una stringa di formato URL.'
    model['keywords'] = 'Codifica Url, codifica URL'
    model['image'] = '/image/comic-url-encode.png'
    return render_template(template_dir + 'template_url_encode_it.html', model=model)


@Web_MyIpAddress_blueprint.route('/it/url-decode', methods=['GET', 'POST'])
def url_decode():
    model = get_default_model()
    model['url'] = '/it/url-decode'
    model['enUrl'] = "/url-decode"
    model['headerTitle'] = 'Strumento online di decodifica dell\'URL  - Coding.Tools'
    model['bodyTitle'] = 'Strumento online di decodifica dell\'URL'
    model['description'] = 'Questo strumento di decodifica dell\'URL online può aiutarti a convertire una stringa di formato URL in una semplice stringa UTF-8.'
    model['keywords'] = 'Decodifica Url, decodifica URL'
    model['image'] = '/image/comic-url-decode.png'
    return render_template(template_dir + 'template_url_decode_it.html', model=model)
