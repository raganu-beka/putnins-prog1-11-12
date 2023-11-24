from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Length, EqualTo, DataRequired


class UserRegisterForm(FlaskForm):
    username = StringField('Username',
                         validators=[Length(min=4, max=24),
                                     DataRequired()])
    password = PasswordField('Password',
                           validators=[Length(min=8, max=24),
                                       DataRequired()])
    confirm_password = PasswordField('Confirm password',
                           validators=[Length(min=8, max=24),
                                       EqualTo('password'),
                                       DataRequired()])


class UserLoginForm(FlaskForm):
    username = StringField('Username',
                         validators=[Length(min=4, max=24),
                                     DataRequired()])
    password = PasswordField('Password',
                           validators=[Length(min=8, max=24),
                                       DataRequired()])
