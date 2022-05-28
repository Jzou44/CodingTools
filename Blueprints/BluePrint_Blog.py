from flask import Blueprint, render_template, abort
from Logic import Logic_UTIL, Logic_MyIpAddress

Web_Blog_blueprint = Blueprint('Web_Blog_blueprint', __name__)
template_dir = 'Blog/en/'


def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'en'
    return model


blogList = list()
blogList.append({
    'title': 'Force file download instead of opening in browser Using HTTP Header and Flask',
    'url': '/blog/force-file-download-instead-of-opening-in-browser-using-http-header-and-flask',
    'description': 'By adding Content-Disposition: attachment HTTP header field to HTTP response in Flask, browser will download the file as an attachment and saved at your laptop\'s local disk.',
    'datetime': '2019-04-21',
    'date': 'Apr 21, 2019'
})
blogList.append({
    'title': 'How to build IP GeoLocation Service with IP2Location database and SQLite',
    'url': '/blog/how-to-build-ip-geolocation-service-with-ip2location-database-and-sqlite',
    'description': 'Lite IP2Location free database provides information include latitude, longitude. By combine IP2Location Database with SQLite, you can build your own IP Geolocation Services.',
    'datetime': '2019-03-20',
    'date': 'Mar 20, 2019'
})
blogList.append({
    'title': 'Credit Card Fraud Detection Using Oversample and Denoising AutoEncoder (with TensorFlow Source Code)',
    'url': '/blog/credit-card-fraud-detection-using-oversample-and-denoising-autoencoder',
    'description': 'This paper proposed a denoising autoencoder neural network (DAE) algorithm which can not only oversample minority class sample through misclassification cost, but also denoise and classify the sampled dataset.',
    'datetime': '2018-12-19',
    'date': 'Dec 19, 2018'
})
blogList.append({
    'title': 'CASIA Handwritten Chinese Character Recognition Using Convolutional Neural Network and Similarity Ranking (with TensorFlow Source Code)',
    'url': '/blog/casia-handwritten-chinese-character-recognition-using-convolutional-neural-network-and-similarity-ranking',
    'description': 'This paper proposed to combine cross entropy with similarity ranking function and use it as loss function, SoftMax cross entropy with Average variance similarity produce the highest accuracy on handwritten Chinese characters recognition.',
    'datetime': '2018-11-19',
    'date': 'Nov 19, 2018'
})

urlList = [blog['url'].lstrip('/blog/') for blog in blogList]


@Web_Blog_blueprint.route('/blog')
def blog_list():
    return blog_list_handle_get()


@Web_Blog_blueprint.route('/blog/<path:path>')
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
