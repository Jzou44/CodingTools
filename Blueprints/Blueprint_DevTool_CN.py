from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_DevTool_blueprint = Blueprint('Web_DevTool_blueprint_CN', __name__)
template_dir = 'DevTool/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'zh-Hans'
    return model


@Web_DevTool_blueprint.route('/cn')
def home_page_handle_get():
    model = get_default_model()
    model['url'] = '/cn'
    model['enUrl'] = "/"
    model['headerTitle'] = '开发者工具箱  - Coding.Tools'
    model['bodyTitle'] = '开发者工具箱'
    model['description'] = '此开发者工具箱能辅助大家, 节省各位宝贵的时间.'
    model['keywords'] = '开发者工具箱'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_devtool_list_cn.html', model=model)
