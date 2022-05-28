import os
import socket
import threading
import json
from flask import request
import sqlite3
import pandas
import os.path
from Logic import Logic_Config, Logic_UTIL
# from flask_sqlalchemy import SQLAlchemy
import ipaddress
import dns.resolver
import smtplib
import tld
import re
from flask_caching import Cache

logger = Logic_UTIL.get_logger(__name__)


def create_cache_server():
    cache = Cache(config={'CACHE_TYPE': 'simple'})
    return cache


cache = create_cache_server()

# db = SQLAlchemy()


network_interface = os.popen('ifconfig | head -1 | cut -d ":" -f1').read().strip()
network_interface = network_interface.replace("<html><head></head><body>", "").replace("</body></html>", "")
production_env = Logic_Config.FLAG_IS_PRODUCTION_ENV

# if Logic_Config.FLAG_IS_PRODUCTION_ENV:
#     tld.update_tld_names()


# class IpFour(db.Model):
#     __tablename__ = 'IpFour'
#     index = db.Column(db.Integer, primary_key=True)
#     ip_from = db.Column(db.String(40))
#     ip_to = db.Column(db.String(40), index=True)
#     country_code = db.Column(db.String(120))
#     country_name = db.Column(db.String(120))
#     region_name = db.Column(db.String(120))
#     city_name = db.Column(db.String(120))
#     latitude = db.Column(db.String(120))
#     longitude = db.Column(db.String(120))
#     zip_code = db.Column(db.String(120))
#     time_zone = db.Column(db.String(120))
#
#     def __init__(self, ip_from, ip_to, country_code, country_name, region_name, city_name, latitude, longitude,
#                  zip_code, time_zone):
#         self.ip_from = ip_from
#         self.ip_to = ip_to
#         self.country_code = country_code
#         self.country_name = country_name
#         self.region_name = region_name
#         self.city_name = city_name
#         self.latitude = latitude
#         self.longitude = longitude
#         self.zip_code = zip_code
#         self.time_zone = time_zone
#
#
# class IpSix(db.Model):
#     __tablename__ = 'IpSix'
#     index = db.Column(db.Integer, primary_key=True)
#     ip_from = db.Column(db.String(40))
#     ip_to = db.Column(db.String(40), index=True)
#     country_code = db.Column(db.String(120))
#     country_name = db.Column(db.String(120))
#     region_name = db.Column(db.String(120))
#     city_name = db.Column(db.String(120))
#     latitude = db.Column(db.String(120))
#     longitude = db.Column(db.String(120))
#     zip_code = db.Column(db.String(120))
#     time_zone = db.Column(db.String(120))
#
#     def __init__(self, ip_from, ip_to, country_code, country_name, region_name, city_name, latitude, longitude,
#                  zip_code, time_zone):
#         self.ip_from = ip_from
#         self.ip_to = ip_to
#         self.country_code = country_code
#         self.country_name = country_name
#         self.region_name = region_name
#         self.city_name = city_name
#         self.latitude = latitude
#         self.longitude = longitude
#         self.zip_code = zip_code
#         self.time_zone = time_zone


def add_zero(str):
    MAX_LENGTH = 40
    return '0' * (MAX_LENGTH - len(str)) + str


def check_str_is_ip_address_or_domain(input_str):
    input_str = input_str.strip()
    try:
        ipaddress.IPv4Address(input_str)
        return "IPV4"
    except ipaddress.AddressValueError:
        pass
    try:
        ipaddress.IPv6Address(input_str)
        return "IPV6"
    except ipaddress.AddressValueError:
        pass
    return "DOMAIN"


def strip_str_to_sub_domain(input_str):
    input_str = input_str.strip()
    if "DOMAIN" != check_str_is_ip_address_or_domain(input_str):
        return input_str
    input_str = input_str.replace(' ', '').split('://')[-1]
    input_str = 'http://' + input_str
    domain_extension = '.' + tld.get_tld(input_str)
    input_str = input_str.split(domain_extension)[0] + domain_extension
    domain = input_str.replace('http://', '')
    if domain == '':
        raise Exception('Name or service not known')
    return domain


def strip_str_to_root_domain(input_str):
    input_str = input_str.strip()
    if "DOMAIN" != check_str_is_ip_address_or_domain(input_str):
        return input_str
    input_str = input_str.replace(' ', '').split('://')[-1]
    input_str = 'http://' + input_str
    domain_extension = '.' + tld.get_tld(input_str)
    input_str = input_str.replace('http://', '')
    domain = input_str.split(domain_extension)[0].split('.')[-1] + domain_extension
    if domain == '':
        raise Exception('Name or service not known')
    return domain


def public_ip_address_api():
    if production_env and 'X-Forwarded-For' in request.headers:
        ip_str = str(request.headers['X-Forwarded-For'].split(',')[0])
        return ip_str
    else:
        return '8.8.8.8'


def public_ip_country_api():
    if production_env and 'CF-IPCountry' in request.headers:
        country_str = request.headers['CF-IPCountry']
        return country_str
    else:
        return 'US'


def ip_geo_search(ip_str=""):
    logger.info('query IpGeo result: {0}'.format(ip_str))

    if ip_str.strip() == "":
        ip_str = public_ip_address_api()

    ip_str = ip_str.replace(" ", "")
    output_msg = cache.get('ipgeo-' + str(ip_str))
    if output_msg is not None:
        return output_msg

    # ipv4
    if "IPV4" == check_str_is_ip_address_or_domain(ip_str):
        ip_number = int(ipaddress.IPv4Address(ip_str))
        ip_number = add_zero(str(ip_number))
        con_ipv4 = sqlite3.connect(Logic_Config.IP2LOCATION_DATABASE_PATH)
        cur = con_ipv4.cursor()
        cur.execute('SELECT * FROM IpFour WHERE ip_to > ? LIMIT 1;', (ip_number,))

        columns_name = ["ip_from", "ip_to", "country_code", "country_name", "region_name", "city_name", "latitude", "longitude",
                        "zip_code", "time_zone"]

        row = cur.fetchall()[0]
        result = {k: v for k, v in zip(columns_name, row[1:])}
        cur.close()
        con_ipv4.close()
        #
        # result = IpFour.query.filter(IpFour.ip_to >= add_zero(str(ip_number))).first()
    elif "IPV6" == check_str_is_ip_address_or_domain(ip_str):
        ip_number = int(ipaddress.IPv6Address(ip_str))
        return ""
        # result = IpSix.query.filter(IpSix.ip_to >= add_zero(str(ip_number))).first()
    else:
        return ip_geo_search(ip_str=socket.gethostbyname(strip_str_to_sub_domain(ip_str)))
    # https://lite.ip2location.com/database/ip-country-region-city-latitude-longitude-zipcode-timezone
    output_msg = dict()
    output_msg['ip'] = ip_str
    output_msg['country_code'] = result["country_code"]
    output_msg['country_name'] = result["country_name"]
    output_msg['region_name'] = result["region_name"]
    output_msg['city_name'] = result["city_name"]
    output_msg['latitude'] = result["latitude"]
    output_msg['longitude'] = result["longitude"]
    output_msg['zip_code'] = result["zip_code"]
    output_msg['time_zone'] = result["time_zone"]
    output_msg = str(json.dumps(output_msg))
    cache.set('ipgeo-' + str(ip_str), output_msg, timeout=3600 * 24 * 30)
    return output_msg


def ping_command(options):
    queryStr = str(options['queryStr'])
    logger.info('query ping result: {0}'.format(queryStr))
    pingcount = int(options['pingcount'])
    timeinterval = float(options['timeinterval'])

    if queryStr.strip() == '':
        queryStr = 'example.com'
    domain = strip_str_to_sub_domain(queryStr)
    if (pingcount > 10 or pingcount < 1):
        return 'Invalid ping count number'
    if (timeinterval > 2 or timeinterval < 0.2):
        return 'Invalid time interval'
    cmd = 'timeout --signal=Kill 30 ping -I ' + network_interface + ' -c ' + str(pingcount) + ' -i ' + str(
        timeinterval) + ' ' + domain
    output_msg = os.popen(cmd).read().strip().rstrip('Killed')
    output_msg = output_msg.replace("<html><head></head><body>", "").replace("</body></html>", "")
    return output_msg


def nslookup_command(options):
    queryStr = str(options['queryStr'])
    logger.info('query nslookup result: {0}'.format(queryStr))
    querytype = str(options['querytype'])
    dnsserver = str(options['dnsserver'])

    if queryStr.strip() == '':
        queryStr = 'example.com'
    domain = strip_str_to_sub_domain(queryStr)
    if querytype not in ['ANY', 'A', 'AAAA', 'CNAME', 'TXT', 'MX', 'NS', 'SOA', 'PTR']:
        return 'Invalid query type'
    if dnsserver not in ['8.8.8.8', '209.244.0.3', '9.9.9.9', '208.67.222.222', '64.6.64.6']:
        return "Invalid DNS server"

    cmd = 'timeout --signal=Kill 10 nslookup -type=' + querytype + ' ' + domain + ' ' + dnsserver
    output_msg = os.popen(cmd).read().strip().rstrip('Killed')
    output_msg = output_msg.replace("<html><head></head><body>", "").replace("</body></html>", "")
    return output_msg


def traceroute_command(options):
    queryStr = str(options['queryStr'])
    logger.info('query traceroute result: {0}'.format(queryStr))
    querytype = str(options['querytype'])
    resolveDomain = '-n' if str(options['resolveDomain']) == 'Dont' else ''
    probesnumber = int(options['probesnumber'])

    if queryStr.strip() == '':
        queryStr = 'example.com'
    domain = strip_str_to_sub_domain(queryStr)
    if querytype not in ['-I', '-T', '-U']:
        return 'Invalid query type'
    if (probesnumber > 6 or probesnumber < 1):
        return 'Invalid probes number'

    cmd = 'timeout --signal=Kill 20 traceroute -i ' + network_interface + ' -N 90 ' + querytype + ' -q ' + str(
        probesnumber) + ' ' + resolveDomain + ' ' + domain
    output_msg = os.popen(cmd).read().strip().rstrip('Killed')
    output_msg = output_msg.replace("<html><head></head><body>", "").replace("</body></html>", "")
    return output_msg


def whois_command(options):
    queryStr = str(options['queryStr'])
    if queryStr.strip() == '':
        queryStr = 'example.com'
    logger.info('query whois result: {0}'.format(queryStr))
    domain = strip_str_to_root_domain(queryStr)
    output_msg = cache.get('whois-' + str(domain))
    if output_msg is not None:
        return output_msg

    cmd = 'timeout --signal=Kill 10 whois -H ' + domain
    output_msg = os.popen(cmd).read().strip().rstrip('Killed')
    output_msg = output_msg.replace("<html><head></head><body>", "").replace("</body></html>", "")
    if output_msg.strip() != '':
        cache.set('whois-' + str(domain), output_msg, timeout=3600 * 24 * 30)
        logger.info('saved whois result to cache: {0}'.format(domain))
    return output_msg


def check_one_port(ip_address_or_domain, port_number, result_str_list):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(4)
    try:
        sock.connect((str(ip_address_or_domain), int(port_number)))
        result_str_list.append("PORT {0} is OPEN on '{1}'.\n".format(port_number, ip_address_or_domain))
    except:
        result_str_list.append("PORT {0} is CLOSED on '{1}'.\n".format(port_number, ip_address_or_domain))
    finally:
        sock.close()


def port_checker(options):
    ip_address_or_domain = str(options['queryStr'])
    if ip_address_or_domain.strip() == '':
        ip_address_or_domain = 'example.com'
    ip_address_or_domain = strip_str_to_sub_domain(ip_address_or_domain)
    logger.info('query port checker result: {0}'.format(ip_address_or_domain))
    ports = str(options['portsNumber']).strip()
    if ports.strip() == '':
        ports = '53 80 443'
    ports = ports.split(' ')
    ports = [int(port) for port in ports if port != ''][:10]
    ports = set(ports)
    result_str_list = []
    threads = [threading.Thread(target=check_one_port, args=(ip_address_or_domain, port, result_str_list)) for port in
               ports]
    [t.start() for t in threads]
    [t.join() for t in threads]
    output_msg = ''.join(result_str_list)
    return output_msg


def email_checker(options):
    address_to_verify = str(options['queryStr'])
    address_to_verify = address_to_verify.strip()
    if address_to_verify == '':
        address_to_verify = 'store-news@amazon.com'

    valid_flag = "VALID"
    log_str = "Processing log:\n\n".format(address_to_verify)
    # step 1: check Syntax
    log_str += "step 1: Checking Email Syntax...\n"
    if re.match('[^@]+@[^@]+\.[^@]+', address_to_verify):
        log_str += "Syntax is Valid.\n\n"
    else:
        log_str += "Syntax is BAD. Abort.\n"
        return log_str
    # step 2: find email server
    email_exchange_server = address_to_verify.split('@')[1]
    log_str += "step 2: Resolve Email Exchange Server Address '{0}' ...\n".format(email_exchange_server)
    try:
        records = dns.resolver.query(email_exchange_server, 'MX')
        mx_record = str(records[0].exchange)
        log_str += "Found Email Exchange Server Address:'{0}'.\n\n".format(mx_record)
    except:
        log_str += "Can't Find Email Exchange Server Address. Abort.\n"
        return log_str
    # step 3: contact smtp server
    log_str += "step 3: Contact Email Exchange Server to verify email ...\n"
    host = socket.gethostname()
    server = smtplib.SMTP()
    try:
        server.connect(mx_record)
        server.helo(host)
        server.mail('me@domain.com')
        code, msg = server.rcpt(str(address_to_verify))
        # Assume 250 as Success
        if code == 250:
            valid_flag = "VALID"
            log_str += "Email Address '{0}' DOES EXIST.\n".format(address_to_verify)
        else:
            valid_flag = "NOT VALID"
            log_str += "Email Address '{0}' DOES NOT EXIST.\n".format(address_to_verify)
        try:
            server.quit()
            server.close()
        except:
            pass
    except Exception as e:
        valid_flag = "NOT ABLE TO VERIFY"
        log_str += "Error During Contact Email Server."
        logger.error(str(e))
    output_msg = "'{0}' is {1}\n\n".format(address_to_verify, valid_flag) + log_str
    return output_msg


def generate_db_IpFour():
    print("start generate_db_IpFour")
    con = sqlite3.connect(Logic_Config.IP2LOCATION_DATABASE_PATH)
    df = pandas.read_csv(Logic_Config.IP2LOCATION_IPV4_CSV_PATH,
                         names=["ip_from", "ip_to", "country_code", "country_name", "region_name", "city_name",
                                "latitude",
                                "longitude", "zip_code", "time_zone"], dtype=str)
    df["ip_from"] = [add_zero(x) for x in df["ip_from"]]
    df["ip_to"] = [add_zero(x) for x in df["ip_to"]]
    df.to_sql('IpFour', con=con)
    cur = con.cursor()
    cur.execute('CREATE INDEX ip4_index on IpFour (ip_to);')
    cur.close()
    con.commit()
    con.close()
    print("end generate_db_IpFour")

#
#
# def generate_db_IpSix():
#     con = sqlite3.connect(Logic_Config.IP2LOCATION_DATABASE_PATH)
#     df = pandas.read_csv(Logic_Config.IP2LOCATION_IPV6_CSV_PATH,
#                          names=["ip_from", "ip_to", "country_code", "country_name", "region_name", "city_name",
#                                 "latitude", "longitude", "zip_code", "time_zone"], dtype=str)
#     df["ip_from"] = [add_zero(x) for x in df["ip_from"]]
#     df["ip_to"] = [add_zero(x) for x in df["ip_to"]]
#     df.to_sql('IpSix', con=con)
#     cur = con.cursor()
#     cur.execute('CREATE INDEX ip6_index on IpSix (ip_to);')
#     cur.close()
#     con.commit()
#     con.close()
#
#
def init_IP2Location_database():
    if not os.path.isfile(Logic_Config.IP2LOCATION_DATABASE_PATH):
        generate_db_IpFour()
        # generate_db_IpSix()
