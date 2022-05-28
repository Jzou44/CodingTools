from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_DevTool_blueprint = Blueprint('Web_DevTool_blueprint_PT', __name__)
template_dir = 'DevTool/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'pt'
    return model


@Web_DevTool_blueprint.route('/pt')
def home_page_handle_get():
    model = get_default_model()
    model['url'] = '/pt'
    model['enUrl'] = "/"
    model['headerTitle'] = 'Developer Toolbox - Coding.Tools'
    model['bodyTitle'] = 'Caixa de ferramentas do desenvolvedor'
    model['description'] = 'Esta caixa de ferramentas do desenvolvedor pode ajudá-lo e economizar seu valioso tempo.'
    model['keywords'] = 'Caixa de ferramentas do desenvolvedor'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_devtool_list_pt.html', model=model)
