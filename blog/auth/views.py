from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime


auth = Blueprint('auth', __name__, static_folder='../static')


@auth.route('/login', endpoint='login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        title = 'Login page'
        return render_template('auth/auth.html', title=title)

    username = request.form.get('Username')
    password = request.form.get('Password')

    from blog.models import User

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        flash('Check your login details')
        return redirect(url_for('auth.login'))

    return redirect(url_for('user.detail', pk=user.id))


@auth.route('/logout')
def logout():
    return '13'


@auth.route('/', endpoint='index')
def index():
    data = 'Welcome, friend!'
    time = datetime.now().strftime('%d.%m.%Y %H:%M')
    return render_template('auth/index.html', data=data, time=time)
