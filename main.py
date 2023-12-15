from putnins import app, Post, User, Comment, Like


if __name__ == '__main__':
    User.create_table(fail_silently=True)
    Post.create_table(fail_silently=True)
    Comment.create_table(fail_silently=True)
    Like.create_table(fail_silently=True)
    
    app.run(host='0.0.0.0', port=81, debug=True)
