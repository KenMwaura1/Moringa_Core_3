from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import Required, Email, EqualTo
from ..models import User


class RegistrationForm(FlaskForm):
    email = StringField('Your email address', validators=[Required(), Email()])
    username = StringField('Enter your username', validators=[Required()])
    password = PasswordField('Password', validators=[Required(),
                                                     EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords', validators=[Required()])
    submit = SubmitField('Sign Up', )

    def validate_email(self, data_field):
        if User.query.filter(User.email == data_field.data).first():
            raise ValidationError("There is an account with that email")

    def validate_username(self, data_field):
        if User.query.filter(User.username == data_field.data).first():
            raise ValidationError("There is an account with that username")


class LoginForm(FlaskForm):
    email = StringField("Your email address", validators=[Required(), Email()])
    password = StringField("Your password", validators=[Required()])
    remember = BooleanField("Remember me")
    submit = SubmitField('Sign In')


