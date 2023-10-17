from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class UserRegistrationForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    first_name = StringField('First name', [validators.DataRequired()])
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm password', [validators.DataRequired()])
    submit = SubmitField('Register')
