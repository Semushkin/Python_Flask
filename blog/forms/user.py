from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField, Form


class UserRegisterForm(FlaskForm):
    username = StringField('username')
    email = StringField('E-mail', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm_password', message='Field must be equal to password')
    ])
    confirm_password = PasswordField('Confirm Password', [validators.DataRequired()])
    submit = SubmitField('Register')


class UserLoginForm(FlaskForm):
    username = StringField('username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Login')
