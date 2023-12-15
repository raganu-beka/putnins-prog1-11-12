import peewee
import datetime

from putnins import db

class User(db.Model):
    username = peewee.TextField(unique=True)
    password = peewee.TextField()


class Post(db.Model):
    post_text = peewee.TextField()
    created_at = peewee.DateTimeField(default=datetime.datetime.now)
    author = peewee.ForeignKeyField(User, related_name='posts')
    image = peewee.TextField()


class Comment(db.Model):
    comment_text = peewee.TextField()
    author = peewee.ForeignKeyField(User, related_name='comments')
    post = peewee.ForeignKeyField(Post, related_name='comments')


class Like(db.Model):
    user = peewee.ForeignKeyField(User, related_name='likes')
    post = peewee.ForeignKeyField(Post, related_name='likes')
