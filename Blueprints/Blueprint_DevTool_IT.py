from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_DevTool_blueprint = Blueprint('Web_DevTool_blueprint_IT', __name__)
template_dir = 'DevTool/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'it'
    return model


@Web_DevTool_blueprint.route('/it')
def home_page_handle_get():
    model = get_default_model()
    model['url'] = '/it'
    model['enUrl'] = "/"
    model['headerTitle'] = 'Developer Toolbox  - Coding.Tools'
    model['bodyTitle'] = 'Toolbox per sviluppatori'
    model['description'] = 'Questo toolbox per sviluppatori può aiutarti e farti risparmiare tempo prezioso.'
    model['keywords'] = 'Toolbox per sviluppatori'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_devtool_list_it.html', model=model)
