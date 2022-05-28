from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_DevTool_blueprint = Blueprint('Web_DevTool_blueprint_JP', __name__)
template_dir = 'DevTool/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'ja'
    return model


@Web_DevTool_blueprint.route('/jp')
def home_page_handle_get():
    model = get_default_model()
    model['url'] = '/jp'
    model['enUrl'] = "/"
    model['headerTitle'] = '開発者ツールボックス  - Coding.Tools'
    model['bodyTitle'] = '開発者ツールボックス'
    model['description'] = 'この開発者向けツールボックスは、あなたを助け、貴重な時間を節約します。'
    model['keywords'] = '開発者ツールボックス'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_devtool_list_jp.html', model=model)
