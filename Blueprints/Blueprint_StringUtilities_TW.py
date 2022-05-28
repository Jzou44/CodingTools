from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_StringUtilities_blueprint = Blueprint('Web_StringUtilities_blueprint_TW', __name__)
template_dir = 'StringUtilities/tw/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'zh-Hant'
    return model


@Web_StringUtilities_blueprint.route('/tw/text-editor')
def text_editor():
    model = get_default_model()
    model['url'] = '/tw/text-editor'
    model['enUrl'] = '/text-editor'
    model['headerTitle'] = '在線文本編輯器  - Coding.Tools'
    model['bodyTitle'] = '在線文本編輯器'
    model['description'] = '這個在線文本編輯器可以幫助您在線修改文本. 支持Markdown高亮標記, 關鍵詞搜索和替換.'
    model['keywords'] = '在線文本編輯器'
    model['image'] = '/image/20190308/cartoon_text_editor.png'
    return render_template(template_dir + 'template_text_editor_tw.html', model=model)


@Web_StringUtilities_blueprint.route('/tw/regex-tester')
def regex_tester():
    model = get_default_model()
    model['url'] = '/tw/regex-tester'
    model['enUrl'] = '/regex-tester'
    model['headerTitle'] = '正則表達式在線測試工具  - Coding.Tools'
    model['bodyTitle'] = '正則表達式在線測試工具'
    model['description'] = '這個正則表達式在線測試工具可以幫助您測試您的正則化表達式是否正確. 支持高亮標記和6種flags.'
    model['keywords'] = '正則表達式測試'
    model['image'] = '/image/20190308/cartoon_regex_tester.png'
    return render_template(template_dir + 'template_regex_tester_tw.html', model=model)


@Web_StringUtilities_blueprint.route('/tw/regex-replace')
def regex_replace():
    model = get_default_model()
    model['url'] = '/tw/regex-replace'
    model['enUrl'] = '/regex-replace'
    model['headerTitle'] = '正則表達式在線替換工具  - Coding.Tools'
    model['bodyTitle'] = '正則表達式在線替換工具'
    model['description'] = '這個正則表達式在線替換工具可以幫助您替換字符串中符合您的正則化表達式部分.'
    model['keywords'] = '正則表達式替換'
    model['image'] = '/image/20190308/cartoon_regex_replace.png'
    return render_template(template_dir + 'template_regex_replace_tw.html', model=model)


@Web_StringUtilities_blueprint.route('/tw/word-counter')
def word_counter():
    model = get_default_model()
    model['url'] = '/tw/word-counter'
    model['enUrl'] = '/word-counter'
    model['headerTitle'] = '單詞統計在線工具  - Coding.Tools'
    model['bodyTitle'] = '單詞統計在線工具'
    model['description'] = '這個單詞統計在線工具可以幫助您統計text文件中英文單詞的數量. 同時也統計句子, 段落, 行數和字符數.'
    model['keywords'] = '單詞統計在線, 單詞統計'
    model['image'] = '/image/20190308/cartoon_word_counter.png'
    return render_template(template_dir + 'template_word_counter_tw.html', model=model)


@Web_StringUtilities_blueprint.route('/tw/character-count')
def character_count():
    model = get_default_model()
    model['url'] = '/tw/character-count'
    model['enUrl'] = '/character-count'
    model['headerTitle'] = '字符數統計在線工具  - Coding.Tools'
    model['bodyTitle'] = '字符數統計在線工具'
    model['description'] = '這個字符數統計在線工具可以幫助您統計text文件中字符的數量. 同時也統計空格數, 單詞數和Twitter消息剩餘字符數.'
    model['image'] = '/image/20190308/cartoon_character_count.png'
    return render_template(template_dir + 'template_character_count_tw.html', model=model)


@Web_StringUtilities_blueprint.route('/tw/case-converter')
def case_converter():
    model = get_default_model()
    model['url'] = '/tw/case-converter'
    model['enUrl'] = '/case-converter'
    model['headerTitle'] = '英文字母大小寫轉換在線工具  - Coding.Tools'
    model['bodyTitle'] = '英文字母大小寫轉換在線工具'
    model['description'] = '這個英文字母大小寫轉換在線工具可以幫助您把英文字符轉換為大寫, 小寫, 句子正確大小寫, 標題正確大小寫和大小寫反轉.'
    model['keywords'] = '大小寫轉換'
    model['image'] = '/image/20190308/cartoon_case_converter.png'
    return render_template(template_dir + 'template_case_converter_tw.html', model=model)


@Web_StringUtilities_blueprint.route('/tw/reverse-text')
def reverse_text():
    model = get_default_model()
    model['url'] = '/tw/reverse-text'
    model['enUrl'] = '/reverse-text'
    model['headerTitle'] = '翻轉字符串在線工具  - Coding.Tools'
    model['bodyTitle'] = '翻轉字符串在線工具'
    model['description'] = '這個翻轉字符串在線工具可以幫助您把字符串的字符順序翻轉.'
    model['keywords'] = '翻轉字符串'
    model['image'] = '/image/20190308/cartoon_reverse_text.png'
    return render_template(template_dir + 'template_reverse_text_tw.html', model=model)


@Web_StringUtilities_blueprint.route('/tw/number-to-words')
def number_to_words():
    model = get_default_model()
    model['url'] = '/tw/number-to-words'
    model['enUrl'] = '/number-to-words'
    model['headerTitle'] = '數字到英文轉換在線工具  - Coding.Tools'
    model['bodyTitle'] = '數字到英文轉換在線工具'
    model['description'] = '這個數字到英文轉換在線工具可以幫助您把數字轉換為英文.'
    model['keywords'] = '數字到英文轉換在線工具'
    model['image'] = '/image/20190308/cartoon_number_to_words.png'
    return render_template(template_dir + 'template_number_to_words_tw.html', model=model)
