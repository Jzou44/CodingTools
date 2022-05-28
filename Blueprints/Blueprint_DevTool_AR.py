from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_DevTool_blueprint = Blueprint('Web_DevTool_blueprint_AR', __name__)
template_dir = 'DevTool/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'ar'
    return model


@Web_DevTool_blueprint.route('/ar')
def home_page_handle_get():
    model = get_default_model()
    model['url'] = '/ar'
    model['enUrl'] = "/"
    model['headerTitle'] = 'مربع أدوات المطور  - Coding.Tools'
    model['bodyTitle'] = 'مربع أدوات المطور'
    model['description'] = 'يمكن أن يساعدك مربع أدوات المطور هذا في توفير وقتك الثمين.'
    model['keywords'] = 'مربع أدوات المطور'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_devtool_list_ar.html', model=model)
