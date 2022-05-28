from flask import Blueprint, render_template, request
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress
import traceback

logger = Logic_UTIL.get_logger(__name__)
Web_MyIpAddress_blueprint = Blueprint('Web_MyIpAddress_blueprint', __name__)
template_dir = 'MyIpAddress/en/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'en'
    return model


@Web_MyIpAddress_blueprint.route('/my-ip-address', methods=['GET', 'POST'])
def my_ip_address():
    if request.method == 'POST':
        try:
            options = request.form
            print(options)
            ip_str = str(options['queryIp'])
            print(ip_str)
            code2 = Logic_MyIpAddress.ip_geo_search(ip_str)
        except Exception as e:
            traceback.print_exc()
            logger.error(str(e))
            code2 = 'Invalid Input Options'
        return code2
    else:
        model = get_default_model()
        # try:
        #     model['geolocation'] = Logic_MyIpAddress.ip_geo_search()
        # except Exception as e:
        #     logger.error(str(e))
        model['url'] = '/my-ip-address'
        model['enUrl'] = "/my-ip-address"
        model['headerTitle'] = 'My IP Address Online Tool  - Coding.Tools'
        model['bodyTitle'] = 'My IP Address Online Tool'
        model['description'] = 'This online my ip address location tool helps you to find your public IP address, with IP geographical information include longitude, latitude and zip code.'
        model['keywords'] = 'my ip address, ip location, ip geographical'
        model['image'] = '/image/comic-my-ip-addresss.png'
        return render_template(template_dir + 'template_ip_address.html', model=model)


@Web_MyIpAddress_blueprint.route('/ping', methods=['GET', 'POST'])
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
        model['url'] = '/ping'
        model['enUrl'] = "/ping"
        model['headerTitle'] = 'Ping Online Tool  - Coding.Tools'
        model['bodyTitle'] = 'Ping Online Tool'
        model['description'] = 'This online ping tool return ping result from Linux server. You can choose how much time to ping a domain name, and the interval between two ping query.'
        model['keywords'] = 'ping, ping tool, online ping, ping online'
        model['image'] = '/image/comic-ping.png'
        return render_template(template_dir + 'template_ping.html', model=model)


@Web_MyIpAddress_blueprint.route('/nslookup', methods=['GET', 'POST'])
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
        model['url'] = '/nslookup'
        model['enUrl'] = "/nslookup"
        model['headerTitle'] = 'Nslookup Online Tool  - Coding.Tools'
        model['bodyTitle'] = 'Nslookup Online Tool'
        model['description'] = 'This online nslookup tool return dns lookup result from Linux server. You can choose the DNS query type (default type ALL), and query any five public DNS servers (default google public DNS server).'
        model['keywords'] = 'nslookup, nslookup tool, online nslookup, dns lookup'
        model['image'] = '/image/comic-nslookup.png'
        return render_template(template_dir + 'template_nslookup.html', model=model)


@Web_MyIpAddress_blueprint.route('/traceroute', methods=['GET', 'POST'])
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
        model['url'] = '/traceroute'
        model['enUrl'] = "/traceroute"
        model['headerTitle'] = 'Traceroute Online Tool  - Coding.Tools'
        model['bodyTitle'] = 'Traceroute Online Tool'
        model['description'] = 'This online traceroute tool return traceroute result from Linux server. You can choose from three different technics (IMCP ECHO package, TCP SYN package, UDP package) to do the traceroute query.'
        model['keywords'] = 'traceroute, traceroute tool, traceroute command, traceroute online'
        model['image'] = '/image/comic-traceroute.png'
        return render_template(template_dir + 'template_traceroute.html', model=model)


@Web_MyIpAddress_blueprint.route('/whois', methods=['GET', 'POST'])
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
        model['url'] = '/whois'
        model['enUrl'] = "/whois"
        model['headerTitle'] = 'Whois Online Tool  - Coding.Tools'
        model['bodyTitle'] = 'Whois Online Tool'
        model['description'] = 'This online whois tool return whois result from Linux server, get domain owner\'s contact information such as phone number and email address.'
        model['keywords'] = 'whois, whois tool, whois command, whois online'
        model['image'] = '/image/comic-whois.png'
        return render_template(template_dir + 'template_whois.html', model=model)


@Web_MyIpAddress_blueprint.route('/port-checker', methods=['GET', 'POST'])
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
        model['url'] = '/port-checker'
        model['enUrl'] = "/port-checker"
        model['headerTitle'] = 'Open Port Checker Online Tool  - Coding.Tools'
        model['bodyTitle'] = 'Open Port Checker Online Tool'
        model['description'] = 'The open port check tool can help you to find out whether a web server is open to external Internet on a specific port, or find out whether your server\'s port forwarding rules are setup correctly.'
        model['keywords'] = 'Port Checker, port scan, Port Checker Online, open port checker'
        model['image'] = '/image/comic-port-checker.png'
        return render_template(template_dir + 'template_port_checker.html', model=model)


@Web_MyIpAddress_blueprint.route('/url-encode', methods=['GET', 'POST'])
def url_encode():
    model = get_default_model()
    model['url'] = '/url-encode'
    model['enUrl'] = "/url-encode"
    model['headerTitle'] = 'URL Encode Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'URL Encode Online Tool'
    model['description'] = 'This online url encode tool helps you to convert one input string into a url format String.'
    model['keywords'] = 'url encode, url encode tool, url encode online'
    model['image'] = '/image/comic-url-encode.png'
    return render_template(template_dir + 'template_url_encode.html', model=model)


@Web_MyIpAddress_blueprint.route('/url-decode', methods=['GET', 'POST'])
def url_decode():
    model = get_default_model()
    model['url'] = '/url-decode'
    model['enUrl'] = "/url-decode"
    model['headerTitle'] = 'URL Decode Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'URL Decode Online Tool'
    model['description'] = 'This online url decode tool helps you to convert one url format String into a regular string.'
    model['keywords'] = 'url decode, url decode tool, url decode online'
    model['image'] = '/image/comic-url-decode.png'
    return render_template(template_dir + 'template_url_decode.html', model=model)
