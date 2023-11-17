import flask

from putnins import app
from putnins.models import Post
from putnins.forms import UserRegisterForm


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

        new_post = Post(post_text=post_text)
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


@app.route('/user/register')
def register_user():
    form = UserRegisterForm()
    return flask.render_template('register_form.html', form=form)


if __name__ == '__main__':
    Post.create_table(fail_silently=True)
    app.run(host='0.0.0.0', port=81, debug=True)