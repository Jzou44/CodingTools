from flask import Blueprint, render_template, request
from Logic import Logic_UTIL, Logic_MyIpAddress, Logic_ImageUtilities

Web_ImageUtilities_blueprint = Blueprint('Web_ImageUtilities_blueprint', __name__)
template_dir = 'ImageUtilities/en/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'en'
    return model


@Web_ImageUtilities_blueprint.route('/compress-png', methods=['GET', 'POST'])
def compress_png():
    if request.method == 'POST':
        return Logic_ImageUtilities.handle_compress_post_request()
    else:
        model = get_default_model()
        model['url'] = '/compress-png'
        model['enUrl'] = '/compress-png'
        model['headerTitle'] = 'Compress PNG (keep Transparency) Online Tool  - Coding.Tools'
        model['bodyTitle'] = 'Compress PNG (keep Transparency) Online Tool'
        model['description'] = 'This online bulk compress PNG online tool helps you to reduce png PNG size while keep its transparency, to transmit image/photo faster cross Internet.'
        model['keywords'] = 'reduce png size,compress png, png compress'
        model['image'] = '/image/20190308/cartoon_compress_png.png'
        return render_template(template_dir + 'template_compress_png.html', model=model)


@Web_ImageUtilities_blueprint.route('/compress-jpeg', methods=['GET', 'POST'])
def compress_jpeg():
    if request.method == 'POST':
        return Logic_ImageUtilities.handle_compress_post_request()
    else:
        model = get_default_model()
        model['url'] = '/compress-jpeg'
        model['enUrl'] = '/compress-jpeg'
        model['headerTitle'] = 'Compress JPEG Online Tool  - Coding.Tools'
        model['bodyTitle'] = 'Compress JPEG Online Tool'
        model['description'] = 'This online bulk compress JPEG tool helps you to reduce JPEG image size, to transmit image/photo faster cross Internet.'
        model['keywords'] = 'reduce jpeg size,compress jpeg'
        model['image'] = '/image/20190308/cartoon_compress_jpeg.png'
        return render_template(template_dir + 'template_compress_jpeg.html', model=model)


@Web_ImageUtilities_blueprint.route('/progressive-jpeg', methods=['GET', 'POST'])
def progressive_jpeg():
    if request.method == 'POST':
        return Logic_ImageUtilities.handle_progressive_jpeg_post_request()
    else:
        model = get_default_model()
        model['url'] = '/progressive-jpeg'
        model['enUrl'] = '/progressive-jpeg'
        model['headerTitle'] = 'Progressive JPEG Converter Online Tool  - Coding.Tools'
        model['bodyTitle'] = 'Progressive JPEG Converter Online Tool'
        model['description'] = 'This online bulk progressive JPEG image converter online tool helps you to convert baseline JPEG image into progressive JPEG image, to display image faster cross Internet.'
        model['keywords'] = 'progressive jpeg, progressive jpeg converter'
        model['image'] = '/image/20190308/cartoon_progressive_jpeg.png'
        return render_template(template_dir + 'template_progressive_jpeg.html', model=model)


@Web_ImageUtilities_blueprint.route('/image-to-base64', methods=['GET', 'POST'])
def image_to_base64():
    if request.method == 'POST':
        return Logic_ImageUtilities.handle_image_to_base64_post_request()
    else:
        model = get_default_model()
        model['url'] = '/image-to-base64'
        model['enUrl'] = '/image-to-base64'
        model['headerTitle'] = 'Image to Base64 Converter Online Tool  - Coding.Tools'
        model['bodyTitle'] = 'Image to Base64 Converter Online Tool'
        model['description'] = 'This online Image to Base64 Converter tool helps you to convert image into base64 string, to help you embed images within html.'
        model['keywords'] = 'image to base64'
        model['image'] = '/image/20190308/cartoon_image_to_base64.png'
        return render_template(template_dir + 'template_image_to_base64.html', model=model)


@Web_ImageUtilities_blueprint.route('/exif-viewer', methods=['GET', 'POST'])
def exif_viewer():
    if request.method == 'POST':
        return Logic_ImageUtilities.handle_exif_viewer_post_request()
    else:
        model = get_default_model()
        model['url'] = '/exif-viewer'
        model['enUrl'] = '/exif-viewer'
        model['headerTitle'] = 'EXIF(Metadata) Viewer Online Tool  - Coding.Tools'
        model['bodyTitle'] = 'EXIF(Metadata) Viewer Online Tool'
        model['description'] = 'This online EXIF/Metadata viewer helps you to extract exif information from photo, such as longtitude, latitude, camera info and so on.'
        model['keywords'] = 'exif viewer, metadata viewer'
        model['image'] = '/image/20190308/cartoon_exif_viewer.png'
        return render_template(template_dir + 'template_exif_viewer.html', model=model)


@Web_ImageUtilities_blueprint.route('/exif-remover', methods=['GET', 'POST'])
def exif_remover():
    if request.method == 'POST':
        return Logic_ImageUtilities.handle_exif_remover_post_request()
    else:
        model = get_default_model()
        model['url'] = '/exif-remover'
        model['enUrl'] = '/exif-remover'
        model['headerTitle'] = 'EXIF(Metadata) Remover Online Tool  - Coding.Tools'
        model['bodyTitle'] = 'EXIF(Metadata) Remover Online Tool'
        model['description'] = 'This online EXIF/Metadata remover helps you to remove exif information from photo, such as longtitude, latitude, camera info and so on.'
        model['keywords'] = 'exif remover, metadata remover'
        model['image'] = '/image/20190308/cartoon_exif_remover.png'
        return render_template(template_dir + 'template_exif_remover.html', model=model)
