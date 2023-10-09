from flask import Blueprint, render_template
import json


item = Blueprint('item', __name__, url_prefix='/items', static_folder='../static')


@item.route('/', endpoint='items')
def item_list():
    with open('blog/static/info.json', encoding='utf-8') as f:
        data = json.load(f)
    return render_template('main/hello.html', data=data)
