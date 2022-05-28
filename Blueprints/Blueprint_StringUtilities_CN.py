from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_StringUtilities_blueprint = Blueprint('Web_StringUtilities_blueprint_CN', __name__)
template_dir = 'StringUtilities/cn/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'zh-Hans'
    return model


@Web_StringUtilities_blueprint.route('/cn/text-editor')
def text_editor():
    model = get_default_model()
    model['url'] = '/cn/text-editor'
    model['enUrl'] = '/text-editor'
    model['headerTitle'] = '在线文本编辑器  - Coding.Tools'
    model['bodyTitle'] = '在线文本编辑器'
    model['description'] = '这个在线文本编辑器可以帮助您在线修改文本. 支持Markdown高亮标记, 关键词搜索和替换.'
    model['keywords'] = '在线文本编辑器'
    model['image'] = '/image/20190308/cartoon_text_editor.png'
    return render_template(template_dir + 'template_text_editor_cn.html', model=model)


@Web_StringUtilities_blueprint.route('/cn/regex-tester')
def regex_tester():
    model = get_default_model()
    model['url'] = '/cn/regex-tester'
    model['enUrl'] = '/regex-tester'
    model['headerTitle'] = '正则表达式在线测试工具  - Coding.Tools'
    model['bodyTitle'] = '正则表达式在线测试工具'
    model['description'] = '这个正则表达式在线测试工具可以帮助您测试您的正则化表达式是否正确. 支持高亮标记和6种flags.'
    model['keywords'] = '正则表达式测试'
    model['image'] = '/image/20190308/cartoon_regex_tester.png'
    return render_template(template_dir + 'template_regex_tester_cn.html', model=model)


@Web_StringUtilities_blueprint.route('/cn/regex-replace')
def regex_replace():
    model = get_default_model()
    model['url'] = '/cn/regex-replace'
    model['enUrl'] = '/regex-replace'
    model['headerTitle'] = '正则表达式在线替换工具  - Coding.Tools'
    model['bodyTitle'] = '正则表达式在线替换工具'
    model['description'] = '这个正则表达式在线替换工具可以帮助您替换字符串中符合您的正则化表达式部分.'
    model['keywords'] = '正则表达式替换'
    model['image'] = '/image/20190308/cartoon_regex_replace.png'
    return render_template(template_dir + 'template_regex_replace_cn.html', model=model)


@Web_StringUtilities_blueprint.route('/cn/word-counter')
def word_counter():
    model = get_default_model()
    model['url'] = '/cn/word-counter'
    model['enUrl'] = '/word-counter'
    model['headerTitle'] = '单词统计在线工具  - Coding.Tools'
    model['bodyTitle'] = '单词统计在线工具'
    model['description'] = '这个单词统计在线工具可以帮助您统计text文件中英文单词的数量. 同时也统计句子, 段落, 行数和字符数.'
    model['keywords'] = '单词统计在线, 单词统计'
    model['image'] = '/image/20190308/cartoon_word_counter.png'
    return render_template(template_dir + 'template_word_counter_cn.html', model=model)


@Web_StringUtilities_blueprint.route('/cn/character-count')
def character_count():
    model = get_default_model()
    model['url'] = '/cn/character-count'
    model['enUrl'] = '/character-count'
    model['headerTitle'] = '字符数统计在线工具  - Coding.Tools'
    model['bodyTitle'] = '字符数统计在线工具'
    model['description'] = '这个字符数统计在线工具可以帮助您统计text文件中字符的数量. 同时也统计空格数, 单词数和Twitter消息剩余字符数.'
    model['image'] = '/image/20190308/cartoon_character_count.png'
    return render_template(template_dir + 'template_character_count_cn.html', model=model)


@Web_StringUtilities_blueprint.route('/cn/case-converter')
def case_converter():
    model = get_default_model()
    model['url'] = '/cn/case-converter'
    model['enUrl'] = '/case-converter'
    model['headerTitle'] = '英文字母大小写转换在线工具  - Coding.Tools'
    model['bodyTitle'] = '英文字母大小写转换在线工具'
    model['description'] = '这个英文字母大小写转换在线工具可以帮助您把英文字符转换为大写, 小写, 句子正确大小写, 标题正确大小写和大小写反转.'
    model['keywords'] = '大小写转换'
    model['image'] = '/image/20190308/cartoon_case_converter.png'
    return render_template(template_dir + 'template_case_converter_cn.html', model=model)


@Web_StringUtilities_blueprint.route('/cn/reverse-text')
def reverse_text():
    model = get_default_model()
    model['url'] = '/cn/reverse-text'
    model['enUrl'] = '/reverse-text'
    model['headerTitle'] = '翻转字符串在线工具  - Coding.Tools'
    model['bodyTitle'] = '翻转字符串在线工具'
    model['description'] = '这个翻转字符串在线工具可以帮助您把字符串的字符顺序翻转.'
    model['keywords'] = '翻转字符串'
    model['image'] = '/image/20190308/cartoon_reverse_text.png'
    return render_template(template_dir + 'template_reverse_text_cn.html', model=model)


@Web_StringUtilities_blueprint.route('/cn/number-to-words')
def number_to_words():
    model = get_default_model()
    model['url'] = '/cn/number-to-words'
    model['enUrl'] = '/number-to-words'
    model['headerTitle'] = '数字到英文转换在线工具  - Coding.Tools'
    model['bodyTitle'] = '数字到英文转换在线工具'
    model['description'] = '这个数字到英文转换在线工具可以帮助您把数字转换为英文.'
    model['keywords'] = '数字到英文转换在线工具'
    model['image'] = '/image/20190308/cartoon_number_to_words.png'
    return render_template(template_dir + 'template_number_to_words_cn.html', model=model)
