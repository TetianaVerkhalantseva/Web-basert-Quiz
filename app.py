#To make sure this file is working properly, filename need to be "app.py"

from flask import Flask, render_template, request, redirect, flash
from validators import LoginForm
import config
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
    return render_template("make_quiz.html")


class Quiz:
    def __init__(self, question, answer1, answer2, answer3, answer4):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4

@app.route('/review-quiz', methods=['GET', 'POST'])
def review_quiz():
    if request.method == 'GET':
        return render_template("review_quiz.html")
    else:
        question1 = request.form.get('question1')
        answer1_1 = request.form.get('answer1_1')
        answer1_2 = request.form.get('answer1_2')
        answer1_3 = request.form.get('answer1_3')
        answer1_4 = request.form.get('answer1_4')

        quiz = Quiz(question1, answer1_1, answer1_2, answer1_3, answer1_4)
        return render_template("review_quiz.html", quiz=quiz)


@app.route('/category')
def category():
    return render_template("quiz_categories.html")

@app.route('/take-quiz')
def take_quiz():
    #Here we need to get all the questions from database
    #And send them to html file

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
    #Here we need to check if the answer is correct one question at a time/one by one 

    user_answer = request.form['answer']
    correct_answer = request.form['correct_answer']
    if user_answer == correct_answer:
        message = "Korrekt!"
    else:
        message = "Stemmer ikke!"
    return render_template('message.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
