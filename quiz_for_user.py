from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
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
        message = "Correct!"
    else:
        message = "Incorrect!"
    return render_template('message.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
