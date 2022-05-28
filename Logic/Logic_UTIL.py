from Logic import Logic_Config
import logging

def get_logger(name):
    logger = logging.getLogger(name)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    file_logging_handler = logging.FileHandler(filename=Logic_Config.LOG_FILE_PATH)
    file_logging_handler.setFormatter(formatter)
    logger.addHandler(file_logging_handler)
    logger.setLevel(logging.INFO)
    return logger


logger = get_logger(__name__)


def create_default_model():
    model = dict()
    model['is_production_env'] = Logic_Config.FLAG_IS_PRODUCTION_ENV
    model['year'] = Logic_Config.YEAR
    model['enUrl'] = '/'
    model['main_color'] = Logic_Config.MAIN_COLOR
    model['css_version_unit'] = Logic_Config.CSS_VERSION_UNIT
    model['css_version_fontawesome'] = Logic_Config.CSS_VERSION_FONTAWESOME
    model['cdnjs_version_jquery'] = Logic_Config.CDNJS_VERSION_JQUERY
    model['cdnjs_version_bootstrap'] = Logic_Config.CDNJS_VERSION_BOOTSTRAP
    model['cdnjs_version_codemirror'] = Logic_Config.CDNJS_VERSION_CODEMIRROR
    model['cdnjs_version_crypto_js'] = Logic_Config.CDNJS_VERSION_CRYPTO_JS
    model['cdnjs_version_js_beautify'] = Logic_Config.CDNJS_VERSION_JS_BEAUTIFY
    model['cdnjs_version_html_minifier'] = Logic_Config.CDNJS_VERSION_HTML_MINIFIER
    model['cdnjs_version_jxon'] = Logic_Config.CDNJS_VERSION_JXON
    model['cdnjs_version_bignumber'] = Logic_Config.CDNJS_VERSION_BIGNUMBER
    model['cdnjs_version_cookie_consent'] = Logic_Config.CDNJS_VERSION_COOKIE_CONSENT
    model['cdnjs_version_file_saver'] = Logic_Config.CDNJS_VERSION_FileSaver
    model['cdnjs_version_drop_zone'] = Logic_Config.CDNJS_VERSION_DropZone
    return model

