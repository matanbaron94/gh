from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, SelectField, FileField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from Crow_app.models import User


class NewProduct(FlaskForm):
    user_id = IntegerField(validators=[DataRequired()])
    owner = StringField(validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    description = StringField("Description")
    part_id = IntegerField('Part ID')
    main_photo = FileField('Main photo')
    status = SelectField('Status',
    validators=[DataRequired()],
    choices=[('public', 'Public'), ('private', 'Private')])
    submit = SubmitField('Add new product')
