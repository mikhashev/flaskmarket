from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
    username = StringField(label='')
    email_address = StringField(label='')
    password1 = PasswordField(label='')
    password2 = PasswordField(label='')
    submit = SubmitField(label='Create Account')