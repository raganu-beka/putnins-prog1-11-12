import flask
from flask_peewee.db import Database


DATABASE = {
    'name': 'putnins.db',
    'engine': 'peewee.SqliteDatabase'
}
DEBUG = True
SECRET_KEY = 'noslepums'

app = flask.Flask(__name__)
app.config.from_object(__name__)

db = Database(app)

from putnins.routes import *
