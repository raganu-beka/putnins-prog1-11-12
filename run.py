from putnins import app, Post


if __name__ == '__main__':
    Post.create_table(fail_silently=True)
    app.run(host='0.0.0.0', port=81, debug=True)
