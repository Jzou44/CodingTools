from flask import Blueprint, render_template, request
from Logic import Logic_UTIL, Logic_MyIpAddress, Logic_ImageUtilities

Web_ImageUtilities_blueprint = Blueprint('Web_ImageUtilities_blueprint_CN', __name__)
template_dir = 'ImageUtilities/cn/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'zh-Hans'
    return model


@Web_ImageUtilities_blueprint.route('/cn/compress-png', methods=['GET', 'POST'])
def compress_png():
    if request.method == 'POST':
        return Logic_ImageUtilities.handle_compress_post_request()
    else:
        model = get_default_model()
        model['url'] = '/cn/compress-png'
        model['enUrl'] = '/compress-png'
        model['headerTitle'] = '压缩PNG图片在线工具  - Coding.Tools'
        model['bodyTitle'] = '压缩PNG图片在线工具'
        model['description'] = '这个在线批量压缩PNG在线工具可以帮助您减少PNG图片的大小,同时保持其背景透明度,以便更快地跨互联网传输.'
        model['keywords'] = '压缩PNG'
        model['image'] = '/image/20190308/cartoon_compress_png.png'
        return render_template(template_dir + 'template_compress_png_cn.html', model=model)


@Web_ImageUtilities_blueprint.route('/cn/compress-jpeg', methods=['GET', 'POST'])
def compress_jpeg():
    if request.method == 'POST':
        return Logic_ImageUtilities.handle_compress_post_request()
    else:
        model = get_default_model()
        model['url'] = '/cn/compress-jpeg'
        model['enUrl'] = '/compress-jpeg'
        model['headerTitle'] = '压缩JPEG图片在线工具  - Coding.Tools'
        model['bodyTitle'] = '压缩JPEG图片在线工具'
        model['description'] = '这个在线批量压缩JPEG在线工具可以帮助您减少JPEG图片的大小,以便更快地跨互联网传输.'
        model['keywords'] = '压缩JPEG'
        model['image'] = '/image/20190308/cartoon_compress_jpeg.png'
        return render_template(template_dir + 'template_compress_jpeg_cn.html', model=model)


@Web_ImageUtilities_blueprint.route('/cn/progressive-jpeg', methods=['GET', 'POST'])
def progressive_jpeg():
    if request.method == 'POST':
        return Logic_ImageUtilities.handle_progressive_jpeg_post_request()
    else:
        model = get_default_model()
        model['url'] = '/cn/progressive-jpeg'
        model['enUrl'] = '/progressive-jpeg'
        model['headerTitle'] = '渐进式JPEG在线转换工具  - Coding.Tools'
        model['bodyTitle'] = '渐进式JPEG在线转换工具'
        model['description'] = '这个渐进式JPEG在线转换工具可以帮助您把Baseline JPEG(标准型)转换为Progressive JPEG(渐进式), 让图片在网页中更快的展示.'
        model['keywords'] = 'progressive jpeg, 渐进式JPEG'
        model['image'] = '/image/20190308/cartoon_progressive_jpeg.png'
        return render_template(template_dir + 'template_progressive_jpeg_cn.html', model=model)


@Web_ImageUtilities_blueprint.route('/cn/image-to-base64', methods=['GET', 'POST'])
def image_to_base64():
    if request.method == 'POST':
        return Logic_ImageUtilities.handle_image_to_base64_post_request()
    else:
        model = get_default_model()
        model['url'] = '/cn/image-to-base64'
        model['enUrl'] = '/image-to-base64'
        model['headerTitle'] = '图片到Base64在线转换工具  - Coding.Tools'
        model['bodyTitle'] = '图片到Base64在线转换工具'
        model['description'] = '这个图片到Base64在线转换工具可以帮助您把图片转换为Base64字符串, 并内嵌到html页面中.'
        model['keywords'] = '图片转Base64'
        model['image'] = '/image/20190308/cartoon_image_to_base64.png'
        return render_template(template_dir + 'template_image_to_base64_cn.html', model=model)


@Web_ImageUtilities_blueprint.route('/cn/exif-viewer', methods=['GET', 'POST'])
def exif_viewer():
    if request.method == 'POST':
        return Logic_ImageUtilities.handle_exif_viewer_post_request()
    else:
        model = get_default_model()
        model['url'] = '/cn/exif-viewer'
        model['enUrl'] = '/exif-viewer'
        model['headerTitle'] = 'EXIF信息在线查看工具  - Coding.Tools'
        model['bodyTitle'] = 'EXIF信息在线查看工具'
        model['description'] = '这个EXIF信息在线查看工具可以帮助您从照片中提取EXIF信息, 例如经度纬度, 相机参数等.'
        model['keywords'] = 'EXIF查看'
        model['image'] = '/image/20190308/cartoon_exif_viewer.png'
        return render_template(template_dir + 'template_exif_viewer_cn.html', model=model)


@Web_ImageUtilities_blueprint.route('/cn/exif-remover', methods=['GET', 'POST'])
def exif_remover():
    if request.method == 'POST':
        return Logic_ImageUtilities.handle_exif_remover_post_request()
    else:
        model = get_default_model()
        model['url'] = '/cn/exif-remover'
        model['enUrl'] = '/exif-remover'
        model['headerTitle'] = 'EXIF信息在线删除工具  - Coding.Tools'
        model['bodyTitle'] = 'EXIF信息在线删除工具'
        model['description'] = '这个EXIF信息在线删除工具可以帮助您从照片中删除EXIF信息, 例如经度纬度, 相机参数等.'
        model['keywords'] = 'exif删除'
        model['image'] = '/image/20190308/cartoon_exif_remover.png'
        return render_template(template_dir + 'template_exif_remover_cn.html', model=model)
