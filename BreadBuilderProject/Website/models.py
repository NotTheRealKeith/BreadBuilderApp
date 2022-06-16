# Laras code for creating classes for database information

from . import db
from flask_login import UserMixin
from datetime import datetime, date

# Creating user class with database model

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

# Creating transaction class with transaction model

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transType = db.Column(db.String(50))
    name = db.Column(db.String(150))
    amount = db.Column(db.Float)
    dateDue = db.Column(db.DateTime, default=datetime.utcnow)
    frequency = db.Column(db.String)
