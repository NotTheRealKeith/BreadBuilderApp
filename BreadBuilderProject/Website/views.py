# Laras code for rendering html files

from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from Website.models import UpdateAccountForm
from . import db

views = Blueprint('views', __name__)


# Shows home page
@views.route('/home')
@login_required
def home():
    return render_template("home.html", user=current_user)


# Shows about page
@views.route('/about')
def about():
    return render_template('about.html', user=current_user)


# Shows report page
@views.route('/report')
def report():
    return render_template('report.html', user=current_user)


# Shows quiz page
@views.route('/quiz')
def quiz():
    return render_template('quiz.html', user=current_user)


@views.route('/income')
def income():
    return render_template('income.html', user=current_user)


# Shows profile page
@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateAccountForm()

    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.income = form.income.data
        db.session.commit()
        flash('You have updated your details!', 'success')
        return redirect(url_for('views.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.income.data = current_user.income

    return render_template('profile.html', user=current_user, form=form)


# Shows welcome page
@views.route('/')
def welcome():
    return render_template('welcome.html', user=current_user)
