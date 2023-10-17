from flask_login import UserMixin

from blog.app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    first_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    is_admin = db.Column(db.Boolean, default=False)
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'{self.username} - {self.email}'
