from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_DevTool_blueprint = Blueprint('Web_DevTool_blueprint_RU', __name__)
template_dir = 'DevTool/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'ru'
    return model


@Web_DevTool_blueprint.route('/ru')
def home_page_handle_get():
    model = get_default_model()
    model['url'] = '/ru'
    model['enUrl'] = "/"
    model['headerTitle'] = 'Инструменты разработчика  - Coding.Tools'
    model['bodyTitle'] = 'Панель инструментов разработчика'
    model['description'] = 'Этот набор инструментов разработчика может помочь вам и сэкономить ваше драгоценное время.'
    model['keywords'] = 'Панель инструментов разработчика'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_devtool_list_ru.html', model=model)
