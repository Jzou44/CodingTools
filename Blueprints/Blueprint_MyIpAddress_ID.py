from flask import Blueprint, render_template, request
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

logger = Logic_UTIL.get_logger(__name__)
Web_MyIpAddress_blueprint = Blueprint('Web_MyIpAddress_blueprint_ID', __name__)
template_dir = 'MyIpAddress/id/'

def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'id'
    return model

@Web_MyIpAddress_blueprint.route('/id/my-ip-address', methods=['GET', 'POST'])
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
        model['url'] = '/id/my-ip-address'
        model['enUrl'] = "/my-ip-address"
        model['headerTitle'] = 'Alat kueri online alamat IP saya  - Coding.Tools'
        model['bodyTitle'] = 'Alat kueri online alamat IP saya'
        model['description'] = 'Alat pencarian alamat IP online ini dapat membantu Anda menemukan alamat IP publik dan informasi lokasi geografis untuk alamat IP Anda, termasuk bujur, lintang dan kode pos.'
        model['keywords'] = 'Alamat IP saya, permintaan alamat IP, permintaan lokasi IP'
        model['image'] = '/image/comic-my-ip-addresss.png'
        return render_template(template_dir + 'template_ip_address_id.html', model=model)


@Web_MyIpAddress_blueprint.route('/id/ping', methods=['GET', 'POST'])
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
        model['url'] = '/id/ping'
        model['enUrl'] = "/ping"
        model['headerTitle'] = 'Ping alat deteksi online  - Coding.Tools'
        model['bodyTitle'] = 'Ping alat deteksi online'
        model['description'] = 'Alat ping online ini mengembalikan hasil ping dari server Linux. Anda dapat memilih berapa kali untuk melakukan ping nama domain dan interval waktu antara dua permintaan ping.'
        model['keywords'] = 'Ping, ping deteksi online'
        model['image'] = '/image/comic-ping.png'
        return render_template(template_dir + 'template_ping_id.html', model=model)


@Web_MyIpAddress_blueprint.route('/id/nslookup', methods=['GET', 'POST'])
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
        model['url'] = '/id/nslookup'
        model['enUrl'] = "/nslookup"
        model['headerTitle'] = 'Alat kueri online DNS  - Coding.Tools'
        model['bodyTitle'] = 'Alat query DNS online'
        model['description'] = 'Alat kueri DNS daring ini mengembalikan hasil kueri DNS dari server Linux. Anda dapat memilih jenis kueri DNS (tipe default A) dan meminta lima server DNS publik (default server DNS publik Google).'
        model['keywords'] = 'Nslookup, permintaan DNS online'
        model['image'] = '/image/comic-nslookup.png'
        return render_template(template_dir + 'template_nslookup_id.html', model=model)


@Web_MyIpAddress_blueprint.route('/id/traceroute', methods=['GET', 'POST'])
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
        model['url'] = '/id/traceroute'
        model['enUrl'] = "/traceroute"
        model['headerTitle'] = 'Router alat pelacakan online  - Coding.Tools'
        model['bodyTitle'] = 'Router alat pelacakan online'
        model['description'] = 'Pelacak router online ini mengembalikan hasil traceroute dari server Linux. Anda dapat memilih dari tiga metode pelacakan yang berbeda (IMCP ECHO, TCP SYN, UDP) untuk pelacakan router.'
        model['keywords'] = 'Traceroute, pelacakan router'
        model['image'] = '/image/comic-traceroute.png'
        return render_template(template_dir + 'template_traceroute_id.html', model=model)


@Web_MyIpAddress_blueprint.route('/id/whois', methods=['GET', 'POST'])
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
        model['url'] = '/id/whois'
        model['enUrl'] = "/whois"
        model['headerTitle'] = 'Whois Alat Kueri Domain Online  - Coding.Tools'
        model['bodyTitle'] = 'Whois alat permintaan nama domain online'
        model['description'] = 'Alat permintaan domain Whois online ini mengembalikan hasil permintaan whois dari server Linux untuk mendapatkan informasi kontak dari pemilik domain, seperti nomor telepon dan alamat email.'
        model['keywords'] = 'Whois, Whois query'
        model['image'] = '/image/comic-whois.png'
        return render_template(template_dir + 'template_whois_id.html', model=model)


@Web_MyIpAddress_blueprint.route('/id/port-checker', methods=['GET', 'POST'])
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
        model['url'] = '/id/port-checker'
        model['enUrl'] = "/port-checker"
        model['headerTitle'] = 'Alat deteksi online port  - Coding.Tools'
        model['bodyTitle'] = 'Alat deteksi port online'
        model['description'] = 'Alat deteksi online port terbuka online ini dapat membantu Anda mendeteksi apakah ada server yang terbuka pada port tertentu atau jika pengaturan penerusan port server Anda sudah benar.'
        model['keywords'] = 'Deteksi port'
        model['image'] = '/image/comic-port-checker.png'
        return render_template(template_dir + 'template_port_checker_id.html', model=model)


@Web_MyIpAddress_blueprint.route('/id/url-encode', methods=['GET', 'POST'])
def url_encode():
    model = get_default_model()
    model['url'] = '/id/url-encode'
    model['enUrl'] = "/url-encode"
    model['headerTitle'] = 'Alat Pengodean URL Online  - Coding.Tools'
    model['bodyTitle'] = 'Alat penyandian URL online'
    model['description'] = 'Alat pengkodean URL online ini dapat membantu Anda mengonversi string input ke string format URL.'
    model['keywords'] = 'Penyandian URL, penyandian URL'
    model['image'] = '/image/comic-url-encode.png'
    return render_template(template_dir + 'template_url_encode_id.html', model=model)


@Web_MyIpAddress_blueprint.route('/id/url-decode', methods=['GET', 'POST'])
def url_decode():
    model = get_default_model()
    model['url'] = '/id/url-decode'
    model['enUrl'] = "/url-decode"
    model['headerTitle'] = 'Alat decoding URL online  - Coding.Tools'
    model['bodyTitle'] = 'Alat decoding URL online'
    model['description'] = 'Alat decoding URL online ini dapat membantu Anda mengubah string format URL menjadi string UTF-8 biasa.'
    model['keywords'] = 'Decode url, decoding URL'
    model['image'] = '/image/comic-url-decode.png'
    return render_template(template_dir + 'template_url_decode_id.html', model=model)
