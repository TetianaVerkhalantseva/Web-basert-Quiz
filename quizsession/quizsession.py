from flask import Blueprint, render_template
from sqlalchemy import func
from sqlalchemy.orm import joinedload

from models import Quiz, QuestionCategory, Question, QuestionHasQuiz, db_session


quizsession = Blueprint("quizsession", __name__, template_folder="templates", static_folder="static")


@quizsession.route("/choose-quiz")
def choose_quiz():

    quizzes = (
        db_session.query(
            Quiz.id,
            Quiz.navn,
            Quiz.beskrivelse,
            func.count(func.distinct(QuestionHasQuiz.spørsmål_id)).label('number_of_questions'),
            func.group_concat(QuestionCategory.navn, ',').label('categories')
        )
        .join(QuestionHasQuiz, Quiz.id == QuestionHasQuiz.quiz_id)
        .join(Question, QuestionHasQuiz.spørsmål_id == Question.id)
        .join(QuestionCategory, Question.kategori_id == QuestionCategory.id)
        .group_by(Quiz.id, Quiz.navn)
        .all()
    )

    quizzes = list(map(
        lambda row: {
            'id': row[0], 'name': row[1], 'description': row[2], 'number_of_questions': row[3], 'categories': list(set(filter(bool, row[4].split(','))))
        },
        quizzes
    ))

    return render_template("quizsession/choose_quiz.html", quizzes=quizzes)


@quizsession.route("/quiz-greeting/<int:quiz_id>")
def quiz_greeting(quiz_id):

    quiz = db_session.query(Quiz).filter_by(id=quiz_id).first()

    return render_template("quizsession/quiz_greeting.html", quiz=quiz)


@quizsession.route("/quiz/<int:quiz_id>", methods=["GET", "POST"])
def quiz(quiz_id):

    quiz = db_session.query(Quiz).filter_by(id=quiz_id).first()

    questions_from_db = (
        db_session.query(Question)
        .join(QuestionHasQuiz)
        .filter(QuestionHasQuiz.quiz_id == quiz_id)
        .options(joinedload(Question.answer_options))
        .all()
    )

    questions = []

    for question in questions_from_db:

        question_data = {
            "id": question.id,
            "question": question.spørsmål,
            "answer_options": []
        }

        for answer_option in question.answer_options:

            answer_option_data = {
                "id": answer_option.id,
                "answer": answer_option.svar,
                "correct": answer_option.korrekt
            }

            question_data["answer_options"].append(answer_option_data)
            
        questions.append(question_data)

    for question in questions:
        print(question, end="\n\n")

    return f"Quiz {quiz_id}"
