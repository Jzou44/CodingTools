from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_DevTool_blueprint = Blueprint('Web_DevTool_blueprint_ID', __name__)
template_dir = 'DevTool/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'id'
    return model


@Web_DevTool_blueprint.route('/id')
def home_page_handle_get():
    model = get_default_model()
    model['url'] = '/id'
    model['enUrl'] = "/"
    model['headerTitle'] = 'Kotak Alat Pengembang  - Coding.Tools'
    model['bodyTitle'] = 'Kotak alat pengembang'
    model['description'] = 'Kotak alat pengembang ini dapat membantu Anda dan menghemat waktu Anda yang berharga.'
    model['keywords'] = 'Kotak alat pengembang'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_devtool_list_id.html', model=model)
