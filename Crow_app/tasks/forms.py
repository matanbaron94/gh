from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, SelectField, FileField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from Crow_app.models import User


class NewTask(FlaskForm):
    task = TextAreaField("New Task", validators=[DataRequired()])
    user_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('Add')

