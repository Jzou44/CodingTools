from flask import Blueprint, render_template, abort
from Logic import Logic_UTIL, Logic_MyIpAddress

Web_Blog_blueprint = Blueprint('Web_Blog_blueprint_CN', __name__)
template_dir = 'Blog/cn/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'zh-Hans'
    return model


blogList = list()
blogList.append({
    'title': '在Ubuntu Linux中命令行工具使用代理v2ray privoxy proxychains学习笔记',
    'url': '/cn/blog/using-proxy-in-linux-ubuntu-with-v2ray-privoxy-proxychains',
    'description': '在Ubuntu Linux中各种命令行工具在GFW下无法工作,这是用v2ray privoxy proxychains等工具的学习心得.',
    'datetime': '2020-02-14',
    'date': 'Feb 14, 2020'
})

urlList = [blog['url'].lstrip('/cn/blog/') for blog in blogList]


@Web_Blog_blueprint.route('/cn/blog')
def blog_list():
    return blog_list_handle_get()


@Web_Blog_blueprint.route('/cn/blog/<path:path>')
def blog_article(path):
    return blog_article_handle_get(path)


def blog_list_handle_get():
    model = get_default_model()
    model['blogList'] = blogList
    return render_template(template_dir + 'template_blog_list.html', model=model)


def blog_article_handle_get(path):
    model = get_default_model()
    if path not in urlList:
        abort(404)
    return render_template(template_dir + path + '.html', model=model)
