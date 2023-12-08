from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import (
    StringField,
    PasswordField,
    TextAreaField,
)
from wtforms.validators import (
    Length,
    EqualTo, 
    DataRequired,
)

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


class PostForm(FlaskForm):
    post_text = TextAreaField('Post text',
                              validators=[Length(min=1, max=560),
                                          DataRequired()])
    post_image = FileField('Image',
                           validators=[FileAllowed(['jpg', 'png'])])
    

class CommentForm(FlaskForm):
    comment_text = TextAreaField('Comment text',
                              validators=[Length(min=1, max=560),
                                          DataRequired()])
