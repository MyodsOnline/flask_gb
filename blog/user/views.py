from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound
from flask_login import login_required

from blog.models import User

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@user.route('/')
def user_list():
    users = User.query.all()
    return render_template('users/users.html', users=users)


@user.route('/<int:pk>', endpoint='detail')
@login_required
def get_user(pk):
    _user = User.query.filter_by(id=pk).one_or_none()
    if not _user:
        raise NotFound(f'User #{pk} not found')
    return render_template('users/detail.html', user=_user)
