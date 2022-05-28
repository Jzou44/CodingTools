from flask import Blueprint, render_template, request
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

logger = Logic_UTIL.get_logger(__name__)
Web_MyIpAddress_blueprint = Blueprint('Web_MyIpAddress_blueprint_CN', __name__)
template_dir = 'MyIpAddress/cn/'

def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'zh-Hans'
    return model

@Web_MyIpAddress_blueprint.route('/cn/my-ip-address', methods=['GET', 'POST'])
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
        model['url'] = '/cn/my-ip-address'
        model['enUrl'] = "/my-ip-address"
        model['headerTitle'] = '我的IP地址在线查询工具  - Coding.Tools'
        model['bodyTitle'] = '我的IP地址在线查询工具'
        model['description'] = '这个在线IP地址查询工具可以帮助您查询您的公共IP地址, 以及您IP地址的地理位置信息, 包括经度,纬度和邮政编码.'
        model['keywords'] = '我的IP地址, IP地址查询, IP地理位置查询'
        model['image'] = '/image/comic-my-ip-addresss.png'
        return render_template(template_dir + 'template_ip_address_cn.html', model=model)


@Web_MyIpAddress_blueprint.route('/cn/ping', methods=['GET', 'POST'])
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
        model['url'] = '/cn/ping'
        model['enUrl'] = "/ping"
        model['headerTitle'] = 'Ping在线检测工具  - Coding.Tools'
        model['bodyTitle'] = 'Ping在线检测工具'
        model['description'] = '这个在线ping工具从Linux服务器返回ping结果. 您可以选择ping域名的次数,以及两次ping查询之间的时间间隔.'
        model['keywords'] = 'ping, ping在线检测'
        model['image'] = '/image/comic-ping.png'
        return render_template(template_dir + 'template_ping_cn.html', model=model)


@Web_MyIpAddress_blueprint.route('/cn/nslookup', methods=['GET', 'POST'])
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
        model['url'] = '/cn/nslookup'
        model['enUrl'] = "/nslookup"
        model['headerTitle'] = 'DNS在线查询工具  - Coding.Tools'
        model['bodyTitle'] = 'DNS在线查询工具'
        model['description'] = '这个在线DNS查询工具从Linux服务器返回DNS查询结果.您可以选择DNS查询类型(默认类型A),并查询任何五个公共DNS服务器(默认谷歌公共DNS服务器).'
        model['keywords'] = 'nslookup, DNS在线查询'
        model['image'] = '/image/comic-nslookup.png'
        return render_template(template_dir + 'template_nslookup_cn.html', model=model)


@Web_MyIpAddress_blueprint.route('/cn/traceroute', methods=['GET', 'POST'])
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
        model['url'] = '/cn/traceroute'
        model['enUrl'] = "/traceroute"
        model['headerTitle'] = '路由器在线追踪工具  - Coding.Tools'
        model['bodyTitle'] = '路由器在线追踪工具'
        model['description'] = '这个在线路由器追踪工具从Linux服务器返回traceroute结果. 您可以选择三种不同的追踪方法(IMCP ECHO包,TCP SYN包,UDP包)来进行路由器追踪.'
        model['keywords'] = 'traceroute, 路由器追踪'
        model['image'] = '/image/comic-traceroute.png'
        return render_template(template_dir + 'template_traceroute_cn.html', model=model)


@Web_MyIpAddress_blueprint.route('/cn/whois', methods=['GET', 'POST'])
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
        model['url'] = '/cn/whois'
        model['enUrl'] = "/whois"
        model['headerTitle'] = 'Whois在线域名查询工具  - Coding.Tools'
        model['bodyTitle'] = 'Whois在线域名查询工具'
        model['description'] = '这个在线Whois域名查询工具返回来自Linux服务器的whois查询结果,获取域名所有者的联系方式,如电话号码和电子邮件地址.'
        model['keywords'] = 'whois, Whois查询'
        model['image'] = '/image/comic-whois.png'
        return render_template(template_dir + 'template_whois_cn.html', model=model)


@Web_MyIpAddress_blueprint.route('/cn/port-checker', methods=['GET', 'POST'])
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
        model['url'] = '/cn/port-checker'
        model['enUrl'] = "/port-checker"
        model['headerTitle'] = '端口在线检测工具  - Coding.Tools'
        model['bodyTitle'] = '端口在线检测工具'
        model['description'] = '这个在线开放端口在线检测工具可以帮助您检测任何服务器是否在特定端口开放, 也可以检测您的服务器端口转发设置是否正确.'
        model['keywords'] = '端口检测'
        model['image'] = '/image/comic-port-checker.png'
        return render_template(template_dir + 'template_port_checker_cn.html', model=model)


@Web_MyIpAddress_blueprint.route('/cn/url-encode', methods=['GET', 'POST'])
def url_encode():
    model = get_default_model()
    model['url'] = '/cn/url-encode'
    model['enUrl'] = "/url-encode"
    model['headerTitle'] = 'URL编码在线工具  - Coding.Tools'
    model['bodyTitle'] = 'URL编码在线工具'
    model['description'] = '这个在线URL编码工具可以帮助您将一个输入字符串转换为URL格式字符串.'
    model['keywords'] = 'url encode, URL编码'
    model['image'] = '/image/comic-url-encode.png'
    return render_template(template_dir + 'template_url_encode_cn.html', model=model)


@Web_MyIpAddress_blueprint.route('/cn/url-decode', methods=['GET', 'POST'])
def url_decode():
    model = get_default_model()
    model['url'] = '/cn/url-decode'
    model['enUrl'] = "/url-decode"
    model['headerTitle'] = 'URL解码在线工具  - Coding.Tools'
    model['bodyTitle'] = 'URL解码在线工具'
    model['description'] = '这个在线URL解码工具可以帮助您将一个URL格式字符串转换成一个普通UTF-8字符串.'
    model['keywords'] = 'url decode, URL解码'
    model['image'] = '/image/comic-url-decode.png'
    return render_template(template_dir + 'template_url_decode_cn.html', model=model)
