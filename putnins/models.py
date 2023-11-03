import peewee
import datetime

from putnins import db


class Post(db.Model):
    post_text = peewee.TextField()
    created_at = peewee.DateTimeField(default=datetime.datetime.now)
