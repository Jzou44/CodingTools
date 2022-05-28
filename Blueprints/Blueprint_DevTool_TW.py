from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_DevTool_blueprint = Blueprint('Web_DevTool_blueprint_TW', __name__)
template_dir = 'DevTool/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'zh-Hant'
    return model


@Web_DevTool_blueprint.route('/tw')
def home_page_handle_get():
    model = get_default_model()
    model['url'] = '/tw'
    model['enUrl'] = "/"
    model['headerTitle'] = '開發者工具箱 - Coding.Tools'
    model['bodyTitle'] = '開發者工具箱'
    model['description'] = '此開發者工具箱能輔助大家, 節省各位寶貴的時間.'
    model['keywords'] = '開發者工具箱'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_devtool_list_tw.html', model=model)
