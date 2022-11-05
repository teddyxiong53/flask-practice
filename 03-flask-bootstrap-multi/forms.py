from flask_wtf import FlaskForm
from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField
from wtforms import StringField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, IntegerField, FormField, validators, PasswordField,\
    DateField
from wtforms.validators import DataRequired, Email

class SignupForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    email = StringField('email', validators=[Email()])
    birthday = DateField('birthday')
    submit = SubmitField('signup')
    