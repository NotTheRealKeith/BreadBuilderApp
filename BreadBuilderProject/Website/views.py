from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/home')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/about')
def about():
    return render_template('about.html', user=current_user)

@views.route('/report')
def report():
    return render_template('report.html', user=current_user)

@views.route('/quiz')
def quiz():
    return render_template('quiz.html', user=current_user)

@views.route('/')
def welcome():
<<<<<<< HEAD
    return render_template('welcome.html', user=current_user)
<<<<<<< HEAD

=======
>>>>>>> fabf7ffdb717deb247a6419d400e3ef1dcb2bb84
=======
    return render_template('welcome.html', user=current_user)
>>>>>>> parent of fabf7ff (Merge pull request #8 from NotTheRealKeith/keith)
