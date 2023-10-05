import click
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash


@click.command(name='init-db')
@with_appcontext
def init_db():
    """
    Command to initiate the database.
    Run in terminal: flask init-db
    """
    from blog.app import db
    from wsgi import app
    from blog.models import User

    db.create_all()


@click.command(name='create-users')
def create_users():
    """
    Command to create test data.
    Run in terminal: flask create-users
    """
    from wsgi import app
    from blog.app import db
    from blog.models import User

    User.query.delete()

    diver = User(
        username='diver',
        email='diver@div.er',
        password=generate_password_hash('1111'),
        is_admin=True)
    sitter = User(
        username='sitter',
        email='sitter@sitt.er',
        password=generate_password_hash('2222'))

    db.session.add(diver)
    db.session.add(sitter)
    db.session.commit()

    users = User.query.all()
    for user in users:
        print(f'Done. User {user} create')
