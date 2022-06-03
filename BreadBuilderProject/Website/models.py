# Laras code for creating classes for database information

from . import db
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import SubmitField, DateField, RadioField, HiddenField, StringField, SelectField, FloatField
from wtforms.validators import InputRequired, Length, Regexp, NumberRange
from datetime import date

# Creating user class with database model

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

# Creating transaction class with transaction model

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transType = db.Column(db.Boolean)
    name = db.Column(db.String(150))
    amount = db.Column(db.Float)
    dateDue = db.Column(db.Date)
    frequency = db.Column(db.String)

    def __init__(self, transType, name, amount, dateDue, frequency):
        self.transType = transType
        self.name = name
        self.amount = amount
        self.dateDue = dateDue
        self.frequency = frequency

# Adding the transaction input to database

class AddRecord(FlaskForm):
    # id used only by update/edit
    id_field = HiddenField()
    transType = RadioField([ InputRequired()], choices=[ ('expense', 'Expense'), ('income', 'Income') ])
    name = StringField('Name', [ InputRequired(), Regexp(r'^[A-Za-z\s\-\'\/]+$', message="Invalid name"),
        Length(min=1, max=30, message="Invalid name length")
        ])
    amount = FloatField('Amount', [ InputRequired(),
        NumberRange(min=1, max=10000, message="Invalid range")
        ])
    dateDue = DateField('Date', [ InputRequired()])
    frequency = SelectField('Frequency', [ InputRequired()],  choices=[ ('', ''), ('once', 'Once'), ('weekly', 'Weekly'), ('fortnightly', 'Fortnightly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')] )
    submit = SubmitField('Add Transaction')
