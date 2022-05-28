from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_DevTool_blueprint = Blueprint('Web_DevTool_blueprint_FR', __name__)
template_dir = 'DevTool/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'fr'
    return model


@Web_DevTool_blueprint.route('/fr')
def home_page_handle_get():
    model = get_default_model()
    model['url'] = '/fr'
    model['enUrl'] = "/"
    model['headerTitle'] = 'Developer Toolbox - Coding.Tools'
    model['bodyTitle'] = 'Boîte à outils du développeur'
    model['description'] = 'Cette boîte à outils de développement peut vous aider et vous faire gagner un temps précieux.'
    model['keywords'] = 'Boîte à outils du développeur'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_devtool_list_fr.html', model=model)
