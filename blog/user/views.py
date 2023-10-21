from flask import Blueprint, render_template, redirect, request, url_for
from werkzeug.exceptions import NotFound
from flask_login import login_required, login_user
from werkzeug.security import generate_password_hash


from blog.models import User
from blog.forms.user import UserRegistrationForm
from blog.extensions import db

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@user.route('/register', methods=['GET', 'POST'], endpoint='register')
def register():
    form = UserRegistrationForm(request.form)
    errors = []

    if request.method == 'POST' and form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append('email is not unique!')
            render_template('users/register.html', form=form, errors=errors)

        _user = User(
            username = form.username.data,
            first_name = form.first_name.data,
            email = form.email.data,
            password = generate_password_hash(form.password.data),
        )

        db.session.add(_user)
        db.session.commit()

        login_user(_user)
        return redirect(url_for('user.user_list'))

    return render_template('users/register.html',
                           form=form,
                           errors=errors,
                           )


@user.route('/', endpoint='user_list')
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
