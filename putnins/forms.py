from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Length, EqualTo

class UserRegisterForm(FlaskForm):
    username = StringField('Username',
                         validators=[Length(min=4, max=24)])
    password = PasswordField('Password',
                           validators=[Length(min=8, max=24)])
    confirm_password = PasswordField('Confirm password',
                           validators=[Length(min=8, max=24),
                                       EqualTo('password')])
