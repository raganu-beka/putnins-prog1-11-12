import flask

from putnins import app
from putnins.models import Post, User
from putnins.forms import UserRegisterForm, UserLoginForm

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/', methods=['GET', 'POST'])
def index():

    posts = Post.select().order_by(Post.created_at.desc())
    return flask.render_template('index.html',
                                 posts=posts)


@app.route('/post/new', methods=['GET', 'POST'])
def new_post():
    # ja metode ir POST mēs aizsūtīsim formas datus
    # mēs ierakstam datus serverī
    if flask.request.method == 'POST':
        post_text = flask.request.form.get('post_text')
        author = User.get(username=flask.session['logged_user'])

        new_post = Post(post_text=post_text, author=author)
        new_post.save()

        return flask.render_template('post.html',
                                     post=new_post)

    # ja metode ir GET mēs dabūsim form
    # nolasīsim datus no servera
    elif flask.request.method == 'GET':
        return flask.render_template('post_form.html')
    

@app.route('/post/<int:post_id>')
def get_post(post_id):
    post = Post.get_by_id(post_id)
    return flask.render_template('post.html',
                                post=post)


@app.route('/user/register', methods=['GET', 'POST'])
def register_user():
    form = UserRegisterForm()

    if form.validate_on_submit():
        user = User.get_or_none(username=form.username.data)
        if user is None:
            new_user = User(username=form.username.data,
                            password=bcrypt.generate_password_hash(form.password.data))
            new_user.save()
            
            flask.flash(f'User {form.username.data} is registered now')
            return flask.redirect(flask.url_for('login_user'))

        else:
            flask.flash(f'User {form.username.data} already exists')

    return flask.render_template('register_form.html', form=form)


@app.route('/user/login', methods=['GET', 'POST'])
def login_user():
    form = UserLoginForm()

    if form.validate_on_submit():
        user = User.get_or_none(username=form.username.data)
        if user is not None and bcrypt.check_password_hash(
            user.password,
            form.password.data
        ):
            flask.session['logged_user'] = user.username

            flask.flash('Logged in!')
            return flask.redirect(flask.url_for('index'))

        else:
            flask.flash('Incorrect username or password')


    return flask.render_template('login_form.html', form=form)


@app.route('/user/logout')
def logout_user():
    if flask.session['logged_user']:
        flask.session.pop('logged_user')

    return flask.redirect(flask.url_for('index'))


@app.route('/user/<username>')
def get_user(username):
    user = User.get_or_none(username=username)
    return flask.render_template('user.html', user=user)
