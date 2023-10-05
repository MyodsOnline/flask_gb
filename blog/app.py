from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from blog.user.views import user
from blog.main.views import item
from config import Development
from blog import commands


db = SQLAlchemy()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Development)

    db.init_app(app)

    register_blueprints(app)
    register_commands(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(item)


def register_commands(app: Flask):
    app.cli.add_command(commands.init_db)
