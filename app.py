from flask import Flask
import time
from flask_sqlalchemy import SQLAlchemy


DEBUG = False
SECRET_KEY = '0c19e6ed-08a3-46cf-aecf-84e5219fe355'
SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///database.db'


app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)


class Result(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.Integer, primary_key=True)
    born_1 = db.Column(db.String(16), nullable=False)
    born_2 = db.Column(db.String(16), nullable=False)
    name_1 = db.Column(db.String(16), nullable=False)
    name_2 = db.Column(db.String(16), nullable=False)
    zodiac_1 = db.Column(db.Integer, nullable=False)
    zodiac_2 = db.Column(db.Integer, nullable=False)
    percent = db.Column(db.Integer, nullable=False, default=0)
    creation_date = db.Column(db.Integer, default=int(time.time()))

    def __repr__(self):
        return f'<result {self.id}>'
