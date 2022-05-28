from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_DevTool_blueprint = Blueprint('Web_DevTool_blueprint_KR', __name__)
template_dir = 'DevTool/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'ko'
    return model


@Web_DevTool_blueprint.route('/kr')
def home_page_handle_get():
    model = get_default_model()
    model['url'] = '/kr'
    model['enUrl'] = "/"
    model['headerTitle'] = '개발자 도구 상자 - Coding.Tools'
    model['bodyTitle'] = '개발자 도구 상자'
    model['description'] = '이 개발자 툴박스는 귀중한 시간을 절약 할 수 있도록 도와줍니다.'
    model['keywords'] = '개발자 도구 상자'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_devtool_list_kr.html', model=model)
