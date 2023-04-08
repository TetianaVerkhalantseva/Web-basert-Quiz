#To make sure this file is working properly, filename need to be "app.py"

from flask import Flask, render_template, request, redirect, flash
from validators import LoginForm
from config import DevelopmentConfig
from models import Admin

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)

# db.init_app(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user-login')
def user_login():
    return render_template('user_login.html')

@app.route('/success', methods=['POST'])
def success():
    form = LoginForm(request.form)

    if form.validate():
        first_name = form.firstname.data
        last_name = form.lastname.data
        return render_template('success.html', fName=first_name, lName=last_name)
    else:
        for errors in form.errors.values():
            for error in errors:
                flash(error)
        return redirect("/user-login")

@app.route('/make-quiz')
def make_quiz():
    return render_template('make_quiz.html')

@app.route('/category')
def category():
    return render_template("quiz_categories.html")

@app.route('/take-quiz')
def take_quiz():
    quizzes = [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "Rome", "Madrid"],
            "answer": "Paris"
        }
    ]
    return render_template('quiz.html', quizzes=quizzes)


@app.route('/check-answer', methods=['POST'])
def check_answer():
    user_answer = request.form['answer']
    correct_answer = request.form['correct_answer']
    if user_answer == correct_answer:
        message = "Korrekt!"
    else:
        message = "Stemmer ikke!"
    return render_template('message.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
