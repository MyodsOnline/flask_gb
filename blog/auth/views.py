from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from flask_login import login_user, logout_user, login_required


auth = Blueprint('auth', __name__, static_folder='../static')


@auth.route('/login', endpoint='login', methods=['GET', 'POST'])
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

    login_user(user)

    return redirect(url_for('auth.index', pk=user.id))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.index'))


@auth.route('/', endpoint='index')
def index():
    time = datetime.now().strftime('%d.%m.%Y %H:%M')
    return render_template('auth/index.html', time=time)
