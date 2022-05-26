
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def welcome():
    return render_template('welcome.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route("/quiz")  # takes you to quiz page
def quiz():
    return render_template('quiz.html')

@views.route("/home")  # takes you to home page when logged in
def home():
    return render_template('home.html')

@views.route("/report")  # takes you to report page
def report():
    return render_template('report.html')