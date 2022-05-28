from flask import Blueprint, render_template, request
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

logger = Logic_UTIL.get_logger(__name__)
Web_MyIpAddress_blueprint = Blueprint('Web_MyIpAddress_blueprint_TW', __name__)
template_dir = 'MyIpAddress/tw/'

def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'zh-Hant'
    return model

@Web_MyIpAddress_blueprint.route('/tw/my-ip-address', methods=['GET', 'POST'])
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
        model['url'] = '/tw/my-ip-address'
        model['enUrl'] = "/my-ip-address"
        model['headerTitle'] = '我的IP地址在線查詢工具 - Coding.Tools'
        model['bodyTitle'] = '我的IP地址在線查詢工具'
        model['description'] = '這個在線IP地址查詢工具可以幫助您查詢您的公共IP地址, 以及您IP地址的地理位置信息, 包括經度,緯度和郵政編碼.'
        model['keywords'] = '我的IP地址, IP地址查詢, IP地理位置查詢'
        model['image'] = '/image/comic-my-ip-addresss.png'
        return render_template(template_dir + 'template_ip_address_tw.html', model=model)


@Web_MyIpAddress_blueprint.route('/tw/ping', methods=['GET', 'POST'])
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
        model['url'] = '/tw/ping'
        model['enUrl'] = "/ping"
        model['headerTitle'] = 'Ping在線檢測工具 - Coding.Tools'
        model['bodyTitle'] = 'Ping在線檢測工具'
        model['description'] = '這個在線ping工具從Linux服務器返回ping結果. 您可以選擇ping域名的次數,以及兩次ping查詢之間的時間間隔.'
        model['keywords'] = 'ping, ping在線檢測'
        model['image'] = '/image/comic-ping.png'
        return render_template(template_dir + 'template_ping_tw.html', model=model)


@Web_MyIpAddress_blueprint.route('/tw/nslookup', methods=['GET', 'POST'])
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
        model['url'] = '/tw/nslookup'
        model['enUrl'] = "/nslookup"
        model['headerTitle'] = 'DNS在線查詢工具 - Coding.Tools'
        model['bodyTitle'] = 'DNS在線查詢工具'
        model['description'] = '這個在線DNS查詢工具從Linux服務器返回DNS查詢結果.您可以選擇DNS查詢類型(默認類型A),並查詢任何五個公共DNS服務器(默認谷歌公共DNS服務器).'
        model['keywords'] = 'nslookup, DNS在線查詢'
        model['image'] = '/image/comic-nslookup.png'
        return render_template(template_dir + 'template_nslookup_tw.html', model=model)


@Web_MyIpAddress_blueprint.route('/tw/traceroute', methods=['GET', 'POST'])
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
        model['url'] = '/tw/traceroute'
        model['enUrl'] = "/traceroute"
        model['headerTitle'] = '路由器在線追踪工具 - Coding.Tools'
        model['bodyTitle'] = '路由器在線追踪工具'
        model['description'] = '這個在線路由器追踪工具從Linux服務器返回traceroute結果. 您可以選擇三種不同的追踪方法(IMCP ECHO包,TCP SYN包,UDP包)來進行路由器追踪.'
        model['keywords'] = 'traceroute, 路由器追踪'
        model['image'] = '/image/comic-traceroute.png'
        return render_template(template_dir + 'template_traceroute_tw.html', model=model)


@Web_MyIpAddress_blueprint.route('/tw/whois', methods=['GET', 'POST'])
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
        model['url'] = '/tw/whois'
        model['enUrl'] = "/whois"
        model['headerTitle'] = 'Whois在線域名查詢工具 - Coding.Tools'
        model['bodyTitle'] = 'Whois在線域名查詢工具'
        model['description'] = '這個在線Whois域名查詢工具返回來自Linux服務器的whois查詢結果,獲取域名所有者的聯繫方式,如電話號碼和電子郵件地址.'
        model['keywords'] = 'whois, Whois查詢'
        model['image'] = '/image/comic-whois.png'
        return render_template(template_dir + 'template_whois_tw.html', model=model)


@Web_MyIpAddress_blueprint.route('/tw/port-checker', methods=['GET', 'POST'])
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
        model['url'] = '/tw/port-checker'
        model['enUrl'] = "/port-checker"
        model['headerTitle'] = '端口在線檢測工具 - Coding.Tools'
        model['bodyTitle'] = '端口在線檢測工具'
        model['description'] = '這個在線開放端口在線檢測工具可以幫助您檢測任何服務器是否在特定端口開放, 也可以檢測您的服務器端口轉發設置是否正確.'
        model['keywords'] = '端口檢測'
        model['image'] = '/image/comic-port-checker.png'
        return render_template(template_dir + 'template_port_checker_tw.html', model=model)


@Web_MyIpAddress_blueprint.route('/tw/url-encode', methods=['GET', 'POST'])
def url_encode():
    model = get_default_model()
    model['url'] = '/tw/url-encode'
    model['enUrl'] = "/url-encode"
    model['headerTitle'] = 'URL編碼在線工具 - Coding.Tools'
    model['bodyTitle'] = 'URL編碼在線工具'
    model['description'] = '這個在線URL編碼工具可以幫助您將一個輸入字符串轉換為URL格式字符串.'
    model['keywords'] = 'url encode, URL編碼'
    model['image'] = '/image/comic-url-encode.png'
    return render_template(template_dir + 'template_url_encode_tw.html', model=model)


@Web_MyIpAddress_blueprint.route('/tw/url-decode', methods=['GET', 'POST'])
def url_decode():
    model = get_default_model()
    model['url'] = '/tw/url-decode'
    model['enUrl'] = "/url-decode"
    model['headerTitle'] = 'URL解碼在線工具 - Coding.Tools'
    model['bodyTitle'] = 'URL解碼在線工具'
    model['description'] = '這個在線URL解碼工具可以幫助您將一個URL格式字符串轉換成一個普通UTF-8字符串.'
    model['keywords'] = 'url decode, URL解碼'
    model['image'] = '/image/comic-url-decode.png'
    return render_template(template_dir + 'template_url_decode_tw.html', model=model)
