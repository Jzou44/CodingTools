from flask import Blueprint, render_template, request
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

logger = Logic_UTIL.get_logger(__name__)
Web_MyIpAddress_blueprint = Blueprint('Web_MyIpAddress_blueprint_KR', __name__)
template_dir = 'MyIpAddress/kr/'

def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'ko'
    return model

@Web_MyIpAddress_blueprint.route('/kr/my-ip-address', methods=['GET', 'POST'])
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
        model['url'] = '/kr/my-ip-address'
        model['enUrl'] = "/my-ip-address"
        model['headerTitle'] = '내 IP 주소 온라인 쿼리 도구  - Coding.Tools'
        model['bodyTitle'] = '내 IP 주소 온라인 쿼리 도구'
        model['description'] = '이 온라인 IP 주소 조회 도구는 경도, 위도 및 우편 번호와 같은 IP 주소에 대한 공용 IP 주소 및 지리적 위치 정보를 찾는 데 도움을줍니다.'
        model['keywords'] = '내 IP 주소, IP 주소 쿼리, IP 위치 쿼리'
        model['image'] = '/image/comic-my-ip-addresss.png'
        return render_template(template_dir + 'template_ip_address_kr.html', model=model)


@Web_MyIpAddress_blueprint.route('/kr/ping', methods=['GET', 'POST'])
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
        model['url'] = '/kr/ping'
        model['enUrl'] = "/ping"
        model['headerTitle'] = 'Ping 온라인 탐지 도구  - Coding.Tools'
        model['bodyTitle'] = 'Ping 온라인 탐지 도구'
        model['description'] = '이 온라인 ping 도구는 Linux 서버에서 ping 결과를 반환합니다. 두 개의 ping 쿼리 사이에 도메인 이름과 시간 간격을 ping 할 횟수를 선택할 수 있습니다.'
        model['keywords'] = 'Ping, Ping 온라인 탐지'
        model['image'] = '/image/comic-ping.png'
        return render_template(template_dir + 'template_ping_kr.html', model=model)


@Web_MyIpAddress_blueprint.route('/kr/nslookup', methods=['GET', 'POST'])
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
        model['url'] = '/kr/nslookup'
        model['enUrl'] = "/nslookup"
        model['headerTitle'] = 'DNS 온라인 쿼리 도구  - Coding.Tools'
        model['bodyTitle'] = 'DNS 온라인 쿼리 도구'
        model['description'] = '이 온라인 DNS 쿼리 도구는 Linux 서버에서 DNS 쿼리 결과를 반환하며, DNS 쿼리 유형 (기본 유형 A)을 선택하고 5 개의 공용 DNS 서버 (기본 Google 공개 DNS 서버)를 쿼리 할 수 있습니다.'
        model['keywords'] = 'Nslookup, DNS 온라인 쿼리'
        model['image'] = '/image/comic-nslookup.png'
        return render_template(template_dir + 'template_nslookup_kr.html', model=model)


@Web_MyIpAddress_blueprint.route('/kr/traceroute', methods=['GET', 'POST'])
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
        model['url'] = '/kr/traceroute'
        model['enUrl'] = "/traceroute"
        model['headerTitle'] = '라우터 온라인 추적 도구  - Coding.Tools'
        model['bodyTitle'] = '라우터 온라인 추적 도구'
        model['description'] = '이 온라인 라우터 추적기는 Linux 서버의 traceroute 결과를 반환합니다. 라우터 추적을위한 세 가지 추적 방법 (IMCP ECHO, TCP SYN, UDP) 중에서 선택할 수 있습니다.'
        model['keywords'] = 'Traceroute, 라우터 추적'
        model['image'] = '/image/comic-traceroute.png'
        return render_template(template_dir + 'template_traceroute_kr.html', model=model)


@Web_MyIpAddress_blueprint.route('/kr/whois', methods=['GET', 'POST'])
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
        model['url'] = '/kr/whois'
        model['enUrl'] = "/whois"
        model['headerTitle'] = 'Whois 온라인 도메인 쿼리 도구  - Coding.Tools'
        model['bodyTitle'] = '후이즈 온라인 도메인 이름 쿼리 도구'
        model['description'] = '이 온라인 후이즈 도메인 쿼리 도구는 Linux 서버에서 whois 쿼리 결과를 반환하여 전화 번호 및 전자 메일 주소와 같은 도메인 소유자의 연락처 정보를 가져옵니다.'
        model['keywords'] = '후이즈, 후이즈 쿼리'
        model['image'] = '/image/comic-whois.png'
        return render_template(template_dir + 'template_whois_kr.html', model=model)


@Web_MyIpAddress_blueprint.route('/kr/port-checker', methods=['GET', 'POST'])
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
        model['url'] = '/kr/port-checker'
        model['enUrl'] = "/port-checker"
        model['headerTitle'] = '포트 온라인 탐지 도구  - Coding.Tools'
        model['bodyTitle'] = '포트 온라인 탐지 도구'
        model['description'] = '이 온라인 열린 포트 온라인 탐지 도구는 특정 포트에서 서버가 열려 있는지 또는 서버 포트 전달 설정이 올바른지 여부를 감지하는 데 도움을줍니다.'
        model['keywords'] = '포트 감지'
        model['image'] = '/image/comic-port-checker.png'
        return render_template(template_dir + 'template_port_checker_kr.html', model=model)


@Web_MyIpAddress_blueprint.route('/kr/url-encode', methods=['GET', 'POST'])
def url_encode():
    model = get_default_model()
    model['url'] = '/kr/url-encode'
    model['enUrl'] = "/url-encode"
    model['headerTitle'] = 'URL 인코딩 도구  - Coding.Tools'
    model['bodyTitle'] = 'URL 인코딩 온라인 도구'
    model['description'] = '이 온라인 URL 인코딩 도구는 입력 문자열을 URL 형식 문자열로 변환하는 데 도움을줍니다.'
    model['keywords'] = 'URL 인코딩, URL 인코딩'
    model['image'] = '/image/comic-url-encode.png'
    return render_template(template_dir + 'template_url_encode_kr.html', model=model)


@Web_MyIpAddress_blueprint.route('/kr/url-decode', methods=['GET', 'POST'])
def url_decode():
    model = get_default_model()
    model['url'] = '/kr/url-decode'
    model['enUrl'] = "/url-decode"
    model['headerTitle'] = 'URL 디코딩 온라인 도구  - Coding.Tools'
    model['bodyTitle'] = 'URL 디코딩 온라인 도구'
    model['description'] = '이 온라인 URL 디코딩 도구는 URL 형식 문자열을 일반 UTF-8 문자열로 변환하는 데 도움을줍니다.'
    model['keywords'] = 'URL 디코딩, URL 디코딩'
    model['image'] = '/image/comic-url-decode.png'
    return render_template(template_dir + 'template_url_decode_kr.html', model=model)
