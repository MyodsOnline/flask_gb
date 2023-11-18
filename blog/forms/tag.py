from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField


class CreateTagForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])
    submit = SubmitField('Create tag')
