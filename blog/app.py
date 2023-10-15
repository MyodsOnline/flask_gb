from flask import Flask

from config import Development
from blog import commands
from .extensions import login_manager, db, migrate


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Development)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from blog.models import User
        return User.query.get(int(user_id))


def register_blueprints(app: Flask):
    from blog.user.views import user
    from blog.main.views import item
    from blog.auth.views import auth

    app.register_blueprint(user)
    app.register_blueprint(item)
    app.register_blueprint(auth)


def register_commands(app: Flask):
    app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_users)
    app.cli.add_command(commands.create_init_user)
