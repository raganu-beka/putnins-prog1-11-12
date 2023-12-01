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
