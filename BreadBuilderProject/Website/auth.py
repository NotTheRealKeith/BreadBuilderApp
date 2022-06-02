from flask import Blueprint, Markup, jsonify, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

labels = [
    'Gas', 'Rent', 'Food'
]

values = [
    70, 200, 70
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C"
]
# @auth.route('/home', methods=['GET', 'POST'])
# def dash(username):
#     if request.method == 'POST':
#         transType = request.form.get('transType')
#         name = request.form.get('name')
#         amount = request.form.get('amount')
#         dateDue = request.form.get('dateDue')
#         frequency = request.form.get('frequency')
#
#         user = User.query.filter_by(username=username).first()
#
#     return render_template("home.html", user=current_user)

@auth.route('/report')
def report():
    pie_labels = labels
    pie_values = values
    return render_template('report.html', title='Weekly Spending Graph', max=17000, set=zip(values, labels, colors))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Username does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 5:
            flash('Password must be at least 5 characters.', category='error')
        else:
            new_user = User(username=username, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.quiz'))

    return render_template("signup.html", user=current_user)


@auth.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        if request.form['week_button'] in quiz.form:
            pass
    else:
        return redirect(url_for('views.home'))
    return render_template('quiz.html', user=current_user)


