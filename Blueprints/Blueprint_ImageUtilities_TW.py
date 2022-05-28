from flask import Blueprint, render_template, request
from Logic import Logic_UTIL, Logic_MyIpAddress, Logic_ImageUtilities

Web_ImageUtilities_blueprint = Blueprint('Web_ImageUtilities_blueprint_TW', __name__)
template_dir = 'ImageUtilities/tw/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'zh-Hant'
    return model


@Web_ImageUtilities_blueprint.route('/tw/compress-png', methods=['GET', 'POST'])
def compress_png():
    if request.method == 'POST':
        return Logic_ImageUtilities.handle_compress_post_request()
    else:
        model = get_default_model()
        model['url'] = '/tw/compress-png'
        model['enUrl'] = '/compress-png'
        model['headerTitle'] = '壓縮PNG圖片在線工具  - Coding.Tools'
        model['bodyTitle'] = '壓縮PNG圖片在線工具'
        model['description'] = '這個在線批量壓縮PNG在線工具可以幫助您減少PNG圖片的大小,同時保持其背景透明度,以便更快地跨互聯網傳輸.'
        model['keywords'] = '壓縮PNG'
        model['image'] = '/image/20190308/cartoon_compress_png.png'
        return render_template(template_dir + 'template_compress_png_tw.html', model=model)


@Web_ImageUtilities_blueprint.route('/tw/compress-jpeg', methods=['GET', 'POST'])
def compress_jpeg():
    if request.method == 'POST':
        return Logic_ImageUtilities.handle_compress_post_request()
    else:
        model = get_default_model()
        model['url'] = '/tw/compress-jpeg'
        model['enUrl'] = '/compress-jpeg'
        model['headerTitle'] = '壓縮JPEG圖片在線工具  - Coding.Tools'
        model['bodyTitle'] = '壓縮JPEG圖片在線工具'
        model['description'] = '這個在線批量壓縮JPEG在線工具可以幫助您減少JPEG圖片的大小,以便更快地跨互聯網傳輸.'
        model['keywords'] = '壓縮JPEG'
        model['image'] = '/image/20190308/cartoon_compress_jpeg.png'
        return render_template(template_dir + 'template_compress_jpeg_tw.html', model=model)


@Web_ImageUtilities_blueprint.route('/tw/progressive-jpeg', methods=['GET', 'POST'])
def progressive_jpeg():
    if request.method == 'POST':
        return Logic_ImageUtilities.handle_progressive_jpeg_post_request()
    else:
        model = get_default_model()
        model['url'] = '/tw/progressive-jpeg'
        model['enUrl'] = '/progressive-jpeg'
        model['headerTitle'] = '漸進式JPEG在線轉換工具  - Coding.Tools'
        model['bodyTitle'] = '漸進式JPEG在線轉換工具'
        model['description'] = '這個漸進式JPEG在線轉換工具可以幫助您把Baseline JPEG(標準型)轉換為Progressive JPEG(漸進式), 讓圖片在網頁中更快的展示.'
        model['keywords'] = 'progressive jpeg, 漸進式JPEG'
        model['image'] = '/image/20190308/cartoon_progressive_jpeg.png'
        return render_template(template_dir + 'template_progressive_jpeg_tw.html', model=model)


@Web_ImageUtilities_blueprint.route('/tw/image-to-base64', methods=['GET', 'POST'])
def image_to_base64():
    if request.method == 'POST':
        return Logic_ImageUtilities.handle_image_to_base64_post_request()
    else:
        model = get_default_model()
        model['url'] = '/tw/image-to-base64'
        model['enUrl'] = '/image-to-base64'
        model['headerTitle'] = '圖片到Base64在線轉換工具  - Coding.Tools'
        model['bodyTitle'] = '圖片到Base64在線轉換工具'
        model['description'] = '這個圖片到Base64在線轉換工具可以幫助您把圖片轉換為Base64字符串, 並內嵌到html頁面中.'
        model['keywords'] = '圖片轉Base64'
        model['image'] = '/image/20190308/cartoon_image_to_base64.png'
        return render_template(template_dir + 'template_image_to_base64_tw.html', model=model)


@Web_ImageUtilities_blueprint.route('/tw/exif-viewer', methods=['GET', 'POST'])
def exif_viewer():
    if request.method == 'POST':
        return Logic_ImageUtilities.handle_exif_viewer_post_request()
    else:
        model = get_default_model()
        model['url'] = '/tw/exif-viewer'
        model['enUrl'] = '/exif-viewer'
        model['headerTitle'] = 'EXIF信息在線查看工具  - Coding.Tools'
        model['bodyTitle'] = 'EXIF信息在線查看工具'
        model['description'] = '這個EXIF信息在線查看工具可以幫助您從照片中提取EXIF信息, 例如經度緯度, 相機參數等.'
        model['keywords'] = 'EXIF查看'
        model['image'] = '/image/20190308/cartoon_exif_viewer.png'
        return render_template(template_dir + 'template_exif_viewer_tw.html', model=model)


@Web_ImageUtilities_blueprint.route('/tw/exif-remover', methods=['GET', 'POST'])
def exif_remover():
    if request.method == 'POST':
        return Logic_ImageUtilities.handle_exif_remover_post_request()
    else:
        model = get_default_model()
        model['url'] = '/tw/exif-remover'
        model['enUrl'] = '/exif-remover'
        model['headerTitle'] = 'EXIF信息在線刪除工具  - Coding.Tools'
        model['bodyTitle'] = 'EXIF信息在線刪除工具'
        model['description'] = '這個EXIF信息在線刪除工具可以幫助您從照片中刪除EXIF信息, 例如經度緯度, 相機參數等.'
        model['keywords'] = 'exif刪除'
        model['image'] = '/image/20190308/cartoon_exif_remover.png'
        return render_template(template_dir + 'template_exif_remover_tw.html', model=model)
