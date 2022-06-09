# Laras code for creating classes for database information

from . import db, db2
from flask_login import UserMixin

# Creating user class with database model

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

# Creating transaction class with transaction model

class Transaction(db2.Model):
    __bind_key__ = 'trans'
    id = db.Column(db.Integer, primary_key=True)
    transType = db.Column(db.Boolean, default=False, nullable=False)
    name = db.Column(db.String(150))
    amount = db.Column(db.Float)
    dateDue = db.Column(db.Date)
    frequency = db.Column(db.String)

