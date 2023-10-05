import click
from flask.cli import with_appcontext


@click.command(name='init-db')
@with_appcontext
def init_db():
    """
    Command to initiate the database
    """
    from blog.app import db
    from wsgi import app

    from blog.models import User
    db.create_all(app=app)
