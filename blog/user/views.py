from flask import Blueprint, render_template, redirect


user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

USERS = {
    1: 'Tech',
    2: 'Stud',
    3: 'Tren',
}


@user.route('/')
def user_list():
    return render_template('users/users.html', users=USERS)


@user.route('/<int:pk>')
def get_user(pk):
    try:
        user = USERS[pk]
    except KeyError:
        return redirect('/users')
    return render_template('users/detail.html', user=user)
