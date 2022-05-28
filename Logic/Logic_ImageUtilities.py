import os
from Logic import Logic_Config, Logic_UTIL
import base64
import json
from flask import request
from werkzeug.utils import secure_filename
import time
from PIL import Image
import subprocess
import exifread

logger = Logic_UTIL.get_logger(__name__)


def clear_cache():
    for filename in os.listdir(Logic_Config.UPLOAD_TEMP_FOLDER_PATH):
        cache_dir_path = os.path.join(Logic_Config.UPLOAD_TEMP_FOLDER_PATH, filename)
        delete_cache_cmd = 'rm -rf ' + cache_dir_path

        cache_time_log_path = os.path.join(cache_dir_path, 'time.txt')
        if not os.path.exists(cache_time_log_path):
            os.popen(delete_cache_cmd)
            continue

        cache_time = open(cache_time_log_path, 'r').read()
        cache_time = float(cache_time)
        time_pass = time.time() - cache_time
        if time_pass > (60 * 60):
            os.popen(delete_cache_cmd)
            continue


def save_upload_file(session):
    upload_file = request.files['file']
    upload_file_name = secure_filename(upload_file.filename)
    os.makedirs(os.path.join(Logic_Config.UPLOAD_TEMP_FOLDER_PATH, session), exist_ok=True)
    time_log_path = os.path.join(Logic_Config.UPLOAD_TEMP_FOLDER_PATH, session, 'time.txt')
    with open(time_log_path, 'w') as time_log:
        time_log.write(str(time.time()))

    upload_folder_path = os.path.join(Logic_Config.UPLOAD_TEMP_FOLDER_PATH, session, 'upload')
    os.makedirs(upload_folder_path, exist_ok=True)
    upload_file_path = os.path.join(upload_folder_path, upload_file_name)
    upload_file.save(upload_file_path)
    download_folder_path = os.path.join(Logic_Config.UPLOAD_TEMP_FOLDER_PATH, session, 'result')
    os.makedirs(download_folder_path, exist_ok=True)
    return upload_file_path, download_folder_path, upload_file_name


def zip_finish(session):
    zip_path = os.path.join(Logic_Config.UPLOAD_TEMP_FOLDER_PATH, session, 'result.zip')

    remove_old_zip_cmd = 'rm -rf ' + zip_path
    logger.info('remove_old_zip_cmd:' + remove_old_zip_cmd)
    os.popen(remove_old_zip_cmd)

    download_folder_path = os.path.join(Logic_Config.UPLOAD_TEMP_FOLDER_PATH, session, 'result')
    create_new_zip_cmd = 'zip -r -j ' + zip_path + ' ' + download_folder_path
    subprocess.call(create_new_zip_cmd, shell=True)
    logger.info('create_new_zip_cmd:' + create_new_zip_cmd)

    result = dict()
    result['download_file_path'] = Logic_Config.DOWNLOAD_URL_PREFIX + zip_path.lstrip(Logic_Config.UPLOAD_TEMP_FOLDER_PATH)
    logger.info('compress_png_finish:' + json.dumps(result))
    return json.dumps(result)


def handle_compress_post_request():
    session = request.form['session']
    if 'finish' in request.form and request.form['finish'] == "finished":
        message = zip_finish(session)
        return message
    else:
        upload_file_path, download_folder_path, upload_file_name = save_upload_file(session)
        return compress_image(upload_file_path, download_folder_path, upload_file_name)


def compress_image(upload_file_path, download_folder_path, upload_file_name):
    original_image = Image.open(upload_file_path)
    image_suffix = str(original_image.format).lower()
    download_file_name = ''.join(upload_file_name.split('.')[:-1]) + '-min.' + image_suffix
    download_file_path = os.path.join(download_folder_path, download_file_name)
    if image_suffix == 'png':
        original_image.convert('P').save(download_file_path, optimize=True, quality=80)
    elif image_suffix == 'jpg' or image_suffix == 'jpeg':
        original_image.save(download_file_path, optimize=True, quality=80, progressive=True)
    else:
        original_image.save(download_file_path, optimize=True, quality=80)

    original_image_size = os.path.getsize(upload_file_path)
    compress_image_size = os.path.getsize(download_file_path)

    compress_rate = 100 * (compress_image_size - original_image_size) / original_image_size
    compress_rate = str(int(compress_rate)) + '%'

    result = dict()
    result['compress_rate'] = compress_rate
    result['download_file_path'] = Logic_Config.DOWNLOAD_URL_PREFIX + download_file_path.lstrip(Logic_Config.UPLOAD_TEMP_FOLDER_PATH)
    logger.info('compress_png:' + json.dumps(result))
    return json.dumps(result)


def handle_progressive_jpeg_post_request():
    session = request.form['session']
    if 'finish' in request.form and request.form['finish'] == "finished":
        message = zip_finish(session)
        return message
    else:
        upload_file_path, download_folder_path, upload_file_name = save_upload_file(session)
        return progressive_jpeg(upload_file_path, download_folder_path, upload_file_name)


def progressive_jpeg(upload_file_path, download_folder_path, upload_file_name):
    upload_file_name = ''.join(upload_file_name.split('.')[:-1]) + '-progressive.jpeg'
    download_file_path = os.path.join(download_folder_path, upload_file_name)
    original_image = Image.open(upload_file_path).convert('RGB')
    original_image.save(download_file_path, optimize=True, quality=100, progressive=True)

    result = dict()
    result['download_file_path'] = Logic_Config.DOWNLOAD_URL_PREFIX + download_file_path.lstrip(Logic_Config.UPLOAD_TEMP_FOLDER_PATH)
    logger.info('progressive_jpeg:' + json.dumps(result))
    return json.dumps(result)


def handle_image_to_base64_post_request():
    session = request.form['session']
    if 'finish' in request.form and request.form['finish'] == "finished":
        message = image_to_base64(session)
        return message
    else:
        upload_file_path, download_folder_path, upload_file_name = save_upload_file(session)
        return "upload Success"


def image_to_base64(session):
    download_folder_path = os.path.join(Logic_Config.UPLOAD_TEMP_FOLDER_PATH, session, 'upload')
    download_file_path = os.path.join(download_folder_path, os.listdir(download_folder_path)[0])

    with open(download_file_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    result = dict()
    result['base64'] = "data:image/" + str(download_file_path).split('.')[-1] + ";base64," + encoded_string.decode()
    logger.info('image_to_base64:' + json.dumps(result))
    return json.dumps(result)


def handle_exif_viewer_post_request():
    session = request.form['session']
    if 'finish' in request.form and request.form['finish'] == "finished":
        message = exif_viewer(session)
        return message
    else:
        upload_file_path, download_folder_path, upload_file_name = save_upload_file(session)
        return "upload Success"


def exif_viewer(session):
    download_folder_path = os.path.join(Logic_Config.UPLOAD_TEMP_FOLDER_PATH, session, 'upload')
    download_file_path = os.path.join(download_folder_path, os.listdir(download_folder_path)[0])

    with open(download_file_path, "rb") as image_file:
        tags = exifread.process_file(image_file)

    result = dict()

    for key in tags.keys():
        if 'MakerNote' in key or 'Thumbnail' in key:
            continue
        value = str(tags[key])
        if key == 'GPS GPSLongitude' or key == 'GPS GPSLatitude' or key == 'GPS GPSAltitude':
            value_split = value.replace('[', '').replace(']', '').replace(' ', '').split(',')
            degree_result = 0
            for i in range(len(value_split)):
                degree_result += eval(value_split[i]) / pow(60, i)
            value = round(degree_result, 4)

        if key == 'GPS GPSTimeStamp':
            value_split = value.replace('[', '').replace(']', '').replace(' ', '').split(',')
            time_result = [str(int(eval(x))) for x in value_split]
            value = ':'.join(time_result)

        result[key] = str(value)

    if 'GPS GPSLatitudeRef' in result and 'GPS GPSLatitude' in result and result['GPS GPSLatitudeRef'] != 'N':
        result['GPS GPSLatitude'] = '-' + result['GPS GPSLatitude']
    if 'GPS GPSLongitudeRef' in result and 'GPS GPSLongitude' in result and result['GPS GPSLongitudeRef'] != 'E':
        result['GPS GPSLongitude'] = '-' + result['GPS GPSLongitude']

    logger.info('image_to_base64:' + json.dumps(result))
    return json.dumps(result)



def handle_exif_remover_post_request():
    session = request.form['session']
    if 'finish' in request.form and request.form['finish'] == "finished":
        message = zip_finish(session)
        return message
    else:
        upload_file_path, download_folder_path, upload_file_name = save_upload_file(session)
        return exif_remover(upload_file_path, download_folder_path, upload_file_name)


def exif_remover(upload_file_path, download_folder_path, upload_file_name):
    original_image = Image.open(upload_file_path)
    image_suffix = str(original_image.format).lower()
    download_file_name = ''.join(upload_file_name.split('.')[:-1]) + '-exif-remove.' + image_suffix
    download_file_path = os.path.join(download_folder_path, download_file_name)
    original_image.save(download_file_path)

    result = dict()
    result['download_file_path'] = Logic_Config.DOWNLOAD_URL_PREFIX + download_file_path.lstrip(Logic_Config.UPLOAD_TEMP_FOLDER_PATH)
    logger.info('compress_png:' + json.dumps(result))
    return json.dumps(result)