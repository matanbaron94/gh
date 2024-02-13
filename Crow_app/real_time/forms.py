from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, SelectField, FileField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from Crow_app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')




class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password_confirmation', message='Passwords must match')])
    password_confirmation = PasswordField('Password Confirmation', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Email has been registered')
    def validate_username(self, username):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError('Username has been registered')



class ResetPassword(FlaskForm):
    new_password = PasswordField('Password', validators=[DataRequired(), EqualTo('password_confirmation', message='Passwords must match')])
    password_confirmation = PasswordField('Password Confirmation', validators=[DataRequired()])
    submit = SubmitField('Reset password')




