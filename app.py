from flask import Flask, request, render_template, redirect
from dotenv import load_dotenv
import os
from utils.utils import *


### Initial variable ###
app = Flask(__name__)
load_dotenv()


### Load .env ###
GIST_CONFIG_LINK = os.getenv('GIST_CONFIG_LINK')


### App errors handler ###
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')




### Main Routes ###


@app.route('/', methods=['GET'])
def index():
    gist_config = get_gist_content(GIST_CONFIG_LINK)

    return render_template('index.html',
                           alert_status=gist_config['announcement'],
                           subtitle_status=gist_config['subtitle_status']
                           )


@app.route('/l/')
def path_redirect_none():
    return '/l/ is used to redirect something'


@app.route('/l/<id>/')
def path_redirect(id):
    url_id = request.view_args['id']
    id_list = get_gist_content(GIST_CONFIG_LINK)['redirect_link']

    for ids in id_list:
        if ids['id'] == url_id:
            url = ids['url']

            return render_template('components/redirect.html', redirect_url=url)
    
    else:
        return f'"{url_id}" is invalid url id.'