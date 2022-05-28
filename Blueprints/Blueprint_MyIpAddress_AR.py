from flask import Blueprint, render_template, request
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

logger = Logic_UTIL.get_logger(__name__)
Web_MyIpAddress_blueprint = Blueprint('Web_MyIpAddress_blueprint_AR', __name__)
template_dir = 'MyIpAddress/ar/'

def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'ar'
    return model

@Web_MyIpAddress_blueprint.route('/ar/my-ip-address', methods=['GET', 'POST'])
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
        model['url'] = '/ar/my-ip-address'
        model['enUrl'] = "/my-ip-address"
        model['headerTitle'] = 'أداة الاستعلام عبر الإنترنت لعنوان IP الخاص بي  - Coding.Tools'
        model['bodyTitle'] = 'عنوان IP الخاص بي على الانترنت'
        model['description'] = 'يمكن أن تساعدك أداة بحث عنوان IP عبر الإنترنت في العثور على عنوان IP العام الخاص بك ومعلومات الموقع الجغرافي لعنوان IP الخاص بك ، بما في ذلك خطوط الطول وخطوط العرض والرمز البريدي.'
        model['keywords'] = 'عنوان IP الخاص بي ، استعلام عنوان IP ، استعلام موقع IP'
        model['image'] = '/image/comic-my-ip-addresss.png'
        return render_template(template_dir + 'template_ip_address_ar.html', model=model)


@Web_MyIpAddress_blueprint.route('/ar/ping', methods=['GET', 'POST'])
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
        model['url'] = '/ar/ping'
        model['enUrl'] = "/ping"
        model['headerTitle'] = 'أداة اختبار Ping عبر الإنترنت  - Coding.Tools'
        model['bodyTitle'] = 'بينغ أداة الكشف على الانترنت'
        model['description'] = 'تقوم أداة ping عبر الإنترنت بإرجاع نتيجة ping من خادم Linux ، ويمكنك اختيار عدد مرات اختبار اتصال اسم المجال والفاصل الزمني بين استعلامين ping.'
        model['keywords'] = 'بينغ ، بينغ على الانترنت الكشف'
        model['image'] = '/image/comic-ping.png'
        return render_template(template_dir + 'template_ping_ar.html', model=model)


@Web_MyIpAddress_blueprint.route('/ar/nslookup', methods=['GET', 'POST'])
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
        model['url'] = '/ar/nslookup'
        model['enUrl'] = "/nslookup"
        model['headerTitle'] = 'أداة استعلام DNS عبر الإنترنت  - Coding.Tools'
        model['bodyTitle'] = 'أداة استعلام DNS عبر الإنترنت'
        model['description'] = 'تعمل أداة استعلام DNS عبر الإنترنت هذه على إرجاع نتائج استعلام DNS من خادم Linux ، ويمكنك تحديد نوع استعلام DNS (النوع الافتراضي A) والاستعلام عن أي خوادم DNS عامة (خادم Google العام DNS الافتراضي).'
        model['keywords'] = 'Nslookup ، DNS الاستعلام عبر الإنترنت'
        model['image'] = '/image/comic-nslookup.png'
        return render_template(template_dir + 'template_nslookup_ar.html', model=model)


@Web_MyIpAddress_blueprint.route('/ar/traceroute', methods=['GET', 'POST'])
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
        model['url'] = '/ar/traceroute'
        model['enUrl'] = "/traceroute"
        model['headerTitle'] = 'أداة تتبع التوجيه عبر الإنترنت  - Coding.Tools'
        model['bodyTitle'] = 'جهاز التوجيه على الانترنت أداة تتبع'
        model['description'] = 'يقوم جهاز التوجيه عبر الإنترنت هذا بإرجاع نتائج التتبع من خادم Linux ، ويمكنك الاختيار من بين ثلاثة طرق تتبع مختلفة (IMCP ECHO و TCP SYN و UDP) لتتبع جهاز التوجيه.'
        model['keywords'] = 'تتبع المسار ، وتتبع جهاز التوجيه'
        model['image'] = '/image/comic-traceroute.png'
        return render_template(template_dir + 'template_traceroute_ar.html', model=model)


@Web_MyIpAddress_blueprint.route('/ar/whois', methods=['GET', 'POST'])
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
        model['url'] = '/ar/whois'
        model['enUrl'] = "/whois"
        model['headerTitle'] = 'Whois Online Domain Query Tool  - Coding.Tools'
        model['bodyTitle'] = 'أداة استعلام اسم المجال على الإنترنت Whois'
        model['description'] = 'تقوم أداة استعلام domain Whois عبر الإنترنت بإرجاع نتائج استعلام whois من خادم Linux للحصول على معلومات الاتصال الخاصة بمالك النطاق ، مثل رقم الهاتف وعنوان البريد الإلكتروني.'
        model['keywords'] = 'Whois ، استعلام Whois'
        model['image'] = '/image/comic-whois.png'
        return render_template(template_dir + 'template_whois_ar.html', model=model)


@Web_MyIpAddress_blueprint.route('/ar/port-checker', methods=['GET', 'POST'])
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
        model['url'] = '/ar/port-checker'
        model['enUrl'] = "/port-checker"
        model['headerTitle'] = 'أداة الكشف عن المنفذ عبر الإنترنت  - Coding.Tools'
        model['bodyTitle'] = 'ميناء أداة الكشف على الانترنت'
        model['description'] = 'يمكن أن تساعدك أداة الكشف عبر الإنترنت المفتوحة عبر الإنترنت في اكتشاف ما إذا كان أي خادم مفتوحًا على منفذ معين أو إذا كانت إعدادات إعادة توجيه منفذ الخادم صحيحة.'
        model['keywords'] = 'كشف الميناء'
        model['image'] = '/image/comic-port-checker.png'
        return render_template(template_dir + 'template_port_checker_ar.html', model=model)


@Web_MyIpAddress_blueprint.route('/ar/url-encode', methods=['GET', 'POST'])
def url_encode():
    model = get_default_model()
    model['url'] = '/ar/url-encode'
    model['enUrl'] = "/url-encode"
    model['headerTitle'] = 'أداة ترميز URL على الإنترنت - الترميز. أدوات'
    model['bodyTitle'] = 'ترميز URL أداة عبر الإنترنت'
    model['description'] = 'يمكن أن تساعدك أداة ترميز عنوان URL عبر الإنترنت في تحويل سلسلة إدخال إلى سلسلة تنسيق عنوان URL.'
    model['keywords'] = 'ترميز Url ، تشفير عنوان URL'
    model['image'] = '/image/comic-url-encode.png'
    return render_template(template_dir + 'template_url_encode_ar.html', model=model)


@Web_MyIpAddress_blueprint.route('/ar/url-decode', methods=['GET', 'POST'])
def url_decode():
    model = get_default_model()
    model['url'] = '/ar/url-decode'
    model['enUrl'] = "/url-decode"
    model['headerTitle'] = 'أداة فك تشفير عنوان URL عبر الإنترنت  - Coding.Tools'
    model['bodyTitle'] = 'أداة فك تشفير عنوان URL على الإنترنت'
    model['description'] = 'يمكن أن تساعدك أداة فك تشفير عنوان URL عبر الإنترنت في تحويل سلسلة تنسيق عنوان URL إلى سلسلة UTF-8 عادية.'
    model['keywords'] = 'Url decode ، URL decoding'
    model['image'] = '/image/comic-url-decode.png'
    return render_template(template_dir + 'template_url_decode_ar.html', model=model)
