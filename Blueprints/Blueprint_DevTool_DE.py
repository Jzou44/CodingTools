from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_DevTool_blueprint = Blueprint('Web_DevTool_blueprint_DE', __name__)
template_dir = 'DevTool/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'de'
    return model


@Web_DevTool_blueprint.route('/de')
def home_page_handle_get():
    model = get_default_model()
    model['url'] = '/de'
    model['enUrl'] = "/"
    model['headerTitle'] = 'Entwickler-Toolbox  - Coding.Tools'
    model['bodyTitle'] = 'Entwickler-Toolbox'
    model['description'] = 'Diese Entwickler-Toolbox kann Ihnen helfen und wertvolle Zeit sparen.'
    model['keywords'] = 'Entwickler-Toolbox'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_devtool_list_de.html', model=model)
