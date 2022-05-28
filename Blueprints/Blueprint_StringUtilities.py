from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_StringUtilities_blueprint = Blueprint('Web_StringUtilities_blueprint', __name__)
template_dir = 'StringUtilities/en/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'en'
    return model


@Web_StringUtilities_blueprint.route('/text-editor')
def text_editor():
    model = get_default_model()
    model['url'] = '/text-editor'
    model['enUrl'] = '/text-editor'
    model['headerTitle'] = 'Text Editor Online  - Coding.Tools'
    model['bodyTitle'] = 'Text Editor Online'
    model['description'] = 'This online text editor helps you to edit txt file online. Support Markdown, quick search and quick replace.'
    model['keywords'] = 'text editor online'
    model['image'] = '/image/20190308/cartoon_text_editor.png'
    return render_template(template_dir + 'template_text_editor.html', model=model)


@Web_StringUtilities_blueprint.route('/regex-tester')
def regex_tester():
    model = get_default_model()
    model['url'] = '/regex-tester'
    model['enUrl'] = '/regex-tester'
    model['headerTitle'] = 'Regex Tester Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Regex Tester Online Tool'
    model['description'] = 'This online Regex Tester tool helps you to test if your regular expression is working correctly. It support Matching h2-highlight and 6 different Flags, powered by Javascript RegExp.'
    model['keywords'] = 'regex tester, regex tester online'
    model['image'] = '/image/20190308/cartoon_regex_tester.png'
    return render_template(template_dir + 'template_regex_tester.html', model=model)


@Web_StringUtilities_blueprint.route('/regex-replace')
def regex_replace():
    model = get_default_model()
    model['url'] = '/regex-replace'
    model['enUrl'] = '/regex-replace'
    model['headerTitle'] = 'Regex Replace Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Regex Replace Online Tool'
    model['description'] = 'This online Regex Replace tool helps you to replace string using regular expression (Javascript RegExp).'
    model['keywords'] = 'Regex Replace Online, Regex Replace'
    model['image'] = '/image/20190308/cartoon_regex_replace.png'
    return render_template(template_dir + 'template_regex_replace.html', model=model)


@Web_StringUtilities_blueprint.route('/word-counter')
def word_counter():
    model = get_default_model()
    model['url'] = '/word-counter'
    model['enUrl'] = '/word-counter'
    model['headerTitle'] = 'Word Counter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Word Counter Online Tool'
    model['description'] = 'This online Word Counter helps you to count word in a text file. It also count Sentences, Paragraphs, Lines and Characters.'
    model['keywords'] = 'Word Counter Online, Word Counter'
    model['image'] = '/image/20190308/cartoon_word_counter.png'
    return render_template(template_dir + 'template_word_counter.html', model=model)


@Web_StringUtilities_blueprint.route('/character-count')
def character_count():
    model = get_default_model()
    model['url'] = '/character-count'
    model['enUrl'] = '/character-count'
    model['headerTitle'] = 'Character Count Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Character Count Online Tool'
    model['description'] = 'This online Character Counter helps you count Character numbers in a text file online. It also count White Space, Words and Twitter Message Character Left.'
    model['keywords'] = 'Character Count Online, Character Count'
    model['image'] = '/image/20190308/cartoon_character_count.png'
    return render_template(template_dir + 'template_character_count.html', model=model)


@Web_StringUtilities_blueprint.route('/case-converter')
def case_converter():
    model = get_default_model()
    model['url'] = '/case-converter'
    model['enUrl'] = '/case-converter'
    model['headerTitle'] = 'Case Converter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Case Converter Online Tool'
    model['description'] = 'This online Case Converter tool helps you to convert case to uppercase, lowercase, sentence case, title case and invert case.'
    model['keywords'] = 'case converter,case converter online'
    model['image'] = '/image/20190308/cartoon_case_converter.png'
    return render_template(template_dir + 'template_case_converter.html', model=model)


@Web_StringUtilities_blueprint.route('/reverse-text')
def reverse_text():
    model = get_default_model()
    model['url'] = '/reverse-text'
    model['enUrl'] = '/reverse-text'
    model['headerTitle'] = 'Reverse Text Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Reverse Text Online Tool'
    model['description'] = 'This online Reverse Text Online Tool helps you to reverse the order of a text content.'
    model['keywords'] = 'Reverse Text Online, Reverse Text'
    model['image'] = '/image/20190308/cartoon_reverse_text.png'
    return render_template(template_dir + 'template_reverse_text.html', model=model)


@Web_StringUtilities_blueprint.route('/number-to-words')
def number_to_words():
    model = get_default_model()
    model['url'] = '/number-to-words'
    model['enUrl'] = '/number-to-words'
    model['headerTitle'] = 'Number To Words Converter Online Tool  - Coding.Tools'
    model['bodyTitle'] = 'Number To Words Converter Online Tool'
    model['description'] = 'This online Number To Words Converter helps you to convert a number to a Word String or a Ordinal Word String.'
    model['keywords'] = 'Number To Words Online, Number To Words'
    model['image'] = '/image/20190308/cartoon_number_to_words.png'
    return render_template(template_dir + 'template_number_to_words.html', model=model)
