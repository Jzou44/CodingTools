from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_DevTool_blueprint = Blueprint('Web_DevTool_blueprint_ES', __name__)
template_dir = 'DevTool/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'es'
    return model


@Web_DevTool_blueprint.route('/es')
def home_page_handle_get():
    model = get_default_model()
    model['url'] = '/es'
    model['enUrl'] = "/"
    model['headerTitle'] = 'Developer Toolbox  - Coding.Tools'
    model['bodyTitle'] = 'Caja de herramientas del desarrollador'
    model['description'] = 'Esta caja de herramientas para desarrolladores puede ayudarlo y ahorrarle un tiempo valioso.'
    model['keywords'] = 'Caja de herramientas del desarrollador'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_devtool_list_es.html', model=model)
