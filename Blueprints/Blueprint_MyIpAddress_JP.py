from flask import Blueprint, render_template, request
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

logger = Logic_UTIL.get_logger(__name__)
Web_MyIpAddress_blueprint = Blueprint('Web_MyIpAddress_blueprint_JP', __name__)
template_dir = 'MyIpAddress/jp/'

def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'ja'
    return model

@Web_MyIpAddress_blueprint.route('/jp/my-ip-address', methods=['GET', 'POST'])
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
        model['url'] = '/jp/my-ip-address'
        model['enUrl'] = "/my-ip-address"
        model['headerTitle'] = '私のIPアドレスオンラインクエリツール  - Coding.Tools'
        model['bodyTitle'] = '私のIPアドレスオンラインクエリツール'
        model['description'] = 'このオンラインIPアドレス検索ツールを使用すると、あなたのパブリックIPアドレスと、そのIPアドレスの経度、緯度、郵便番号などの地理的な位置情報を見つけることができます。'
        model['keywords'] = '私のIPアドレス、IPアドレスクエリ、IPロケーションクエリ'
        model['image'] = '/image/comic-my-ip-addresss.png'
        return render_template(template_dir + 'template_ip_address_jp.html', model=model)


@Web_MyIpAddress_blueprint.route('/jp/ping', methods=['GET', 'POST'])
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
        model['url'] = '/jp/ping'
        model['enUrl'] = "/ping"
        model['headerTitle'] = 'Pingオンライン検出ツール  - Coding.Tools'
        model['bodyTitle'] = 'pingオンライン検出ツール'
        model['description'] = 'このオンラインpingツールは、Linuxサーバーからpingの結果を返すもので、ドメイン名をpingする回数と2つのpingクエリの間隔を選択できます。'
        model['keywords'] = 'ping、pingオンライン検出'
        model['image'] = '/image/comic-ping.png'
        return render_template(template_dir + 'template_ping_jp.html', model=model)


@Web_MyIpAddress_blueprint.route('/jp/nslookup', methods=['GET', 'POST'])
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
        model['url'] = '/jp/nslookup'
        model['enUrl'] = "/nslookup"
        model['headerTitle'] = 'DNSオンラインクエリツール  - Coding.Tools'
        model['bodyTitle'] = 'DNSオンラインクエリツール'
        model['description'] = 'このオンラインDNSクエリツールは、LinuxサーバーからDNSクエリの結果を返し、DNSクエリの種類（デフォルトの種類A）を選択し、5つのパブリックDNSサーバー（デフォルトのGoogleパブリックDNSサーバー）に対してクエリを実行できます。'
        model['keywords'] = 'Nslookup、DNSオンラインクエリ'
        model['image'] = '/image/comic-nslookup.png'
        return render_template(template_dir + 'template_nslookup_jp.html', model=model)


@Web_MyIpAddress_blueprint.route('/jp/traceroute', methods=['GET', 'POST'])
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
        model['url'] = '/jp/traceroute'
        model['enUrl'] = "/traceroute"
        model['headerTitle'] = 'ルーターオンライン追跡ツール  - Coding.Tools'
        model['bodyTitle'] = 'ルーターオンライン追跡ツール'
        model['description'] = 'このオンラインルータートレーサーは、Linuxサーバーからtracerouteの結果を返しますルーター追跡には、3種類の追跡方法（IMCP ECHO、TCP SYN、UDP）から選択できます。'
        model['keywords'] = 'traceroute、ルータトラッキング'
        model['image'] = '/image/comic-traceroute.png'
        return render_template(template_dir + 'template_traceroute_jp.html', model=model)


@Web_MyIpAddress_blueprint.route('/jp/whois', methods=['GET', 'POST'])
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
        model['url'] = '/jp/whois'
        model['enUrl'] = "/whois"
        model['headerTitle'] = 'Whoisオンラインドメインクエリツール  - Coding.Tools'
        model['bodyTitle'] = 'Whoisオンラインドメイン名問い合わせツール'
        model['description'] = 'このオンラインWhoisドメインクエリツールは、Linuxサーバーからwhoisクエリの結果を返し、電話番号や電子メールアドレスなどのドメイン所有者の連絡先情報を取得します。'
        model['keywords'] = 'Whois、Whoisクエリー'
        model['image'] = '/image/comic-whois.png'
        return render_template(template_dir + 'template_whois_jp.html', model=model)


@Web_MyIpAddress_blueprint.route('/jp/port-checker', methods=['GET', 'POST'])
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
        model['url'] = '/jp/port-checker'
        model['enUrl'] = "/port-checker"
        model['headerTitle'] = 'ポートオンライン検出ツール  - Coding.Tools'
        model['bodyTitle'] = 'ポートオンライン検出ツール'
        model['description'] = 'このオンラインオープンポートオンライン検出ツールは、特定のポートでサーバーが開かれているかどうか、またはサーバーのポート転送設定が正しいかどうかを検出するのに役立ちます。'
        model['keywords'] = 'ポート検出'
        model['image'] = '/image/comic-port-checker.png'
        return render_template(template_dir + 'template_port_checker_jp.html', model=model)


@Web_MyIpAddress_blueprint.route('/jp/url-encode', methods=['GET', 'POST'])
def url_encode():
    model = get_default_model()
    model['url'] = '/jp/url-encode'
    model['enUrl'] = "/url-encode"
    model['headerTitle'] = 'URLエンコーディングオンラインツール  - Coding.Tools'
    model['bodyTitle'] = 'URLエンコードオンラインツール'
    model['description'] = 'このオンラインURLエンコードツールは、入力文字列をURL形式の文字列に変換するのに役立ちます。'
    model['keywords'] = 'URLエンコード、URLエンコード'
    model['image'] = '/image/comic-url-encode.png'
    return render_template(template_dir + 'template_url_encode_jp.html', model=model)


@Web_MyIpAddress_blueprint.route('/jp/url-decode', methods=['GET', 'POST'])
def url_decode():
    model = get_default_model()
    model['url'] = '/jp/url-decode'
    model['enUrl'] = "/url-decode"
    model['headerTitle'] = 'URLデコードオンラインツール  - Coding.Tools'
    model['bodyTitle'] = 'URLデコードオンラインツール'
    model['description'] = 'このオンラインURLデコードツールは、URLフォーマット文字列をプレーンなUTF-8文字列に変換するのに役立ちます。'
    model['keywords'] = 'URLデコード、URLデコード'
    model['image'] = '/image/comic-url-decode.png'
    return render_template(template_dir + 'template_url_decode_jp.html', model=model)
