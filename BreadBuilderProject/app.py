from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


# routes to pages
@app.route("/index")
@app.route("/")  # takes you to index page
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route("/quiz")  # takes you to quiz page
def quiz():
    return render_template('quiz.html')


@app.route("/home")  # this is for after users login
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
