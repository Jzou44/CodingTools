from flask import Blueprint, render_template, abort
from Logic import Logic_UTIL, Logic_MyIpAddress

Web_DevTool_blueprint = Blueprint('Web_DevTool_blueprint', __name__)
template_dir = 'DevTool/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'en'
    return model



@Web_DevTool_blueprint.route('/')
def home_page_handle_get():
    model = get_default_model()
    model['url'] = '/'
    model['enUrl'] = "/"
    model['headerTitle'] = 'Coding ToolBox for Developers  - Coding.Tools'
    model['bodyTitle'] = 'Coding ToolBox for Developers'
    model[
        'description'] = 'This online Coding ToolBox can help every programmer to save their valuable time. It\'s also a great learning tool for anyone wants to enter the Computer Science field.'
    model['keywords'] = 'coding tool, development tool, programming tool'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_devtool_list.html', model=model)

