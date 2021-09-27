from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):

    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('Username already exist')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(label='', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='', validators=[DataRequired()])
    password = StringField(label='', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')
