from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required

from models import Quiz, Question, QuestionCategory, AnswerOption, QuestionHasQuiz, QuizSession, db_session


quiz = Blueprint("quiz", __name__, template_folder="templates", static_folder="static")


@quiz.route("/remove-quiz/<int:quiz_id>")
@login_required
def remove_quiz(quiz_id):

    try:

        quiz = db_session.query(Quiz).filter_by(id=quiz_id).first()

        question_has_quiz_records = db_session.query(QuestionHasQuiz).filter_by(quiz_id=quiz_id).all()

        for record in question_has_quiz_records:

            quiz_session_records = db_session.query(QuizSession).filter_by(spørsmål_har_quiz_id=record.id).all()

            for quiz_session_record in quiz_session_records:
                db_session.delete(quiz_session_record)

            db_session.delete(record)

        db_session.delete(quiz)

        db_session.commit()

        flash(f"Quizzen '{quiz.navn}' er nå slettet.", category="success")

        return redirect(url_for("admin.admin_profile"))

    except Exception as exception:

        flash(f"{type(exception).__name__}: {exception}", category="error")

        return redirect(url_for("admin.admin_profile"))


@quiz.route("/remove-question/<int:question_id>")
@login_required
def remove_question(question_id):
    
    try:
        
        question = db_session.query(Question).filter_by(id=question_id).first()

        answers = db_session.query(AnswerOption).filter_by(spørsmål_id=question_id).all()

        question_has_quiz_records = db_session.query(QuestionHasQuiz).filter_by(spørsmål_id=question_id).all()

        for record in question_has_quiz_records:
            
            qiuz_session_records = db_session.query(QuizSession).filter_by(spørsmål_har_quiz_id=record.id).all()

            for quiz_session_record in qiuz_session_records:
                    db_session.delete(quiz_session_record)

            db_session.delete(record)

        for answer in answers:
            db_session.delete(answer)

        db_session.delete(question)
        
        db_session.commit()
        
        flash(f"Spørsmålet '{question.spørsmål}' er nå slettet.", category="success")
        
        return redirect(url_for("admin.admin_profile"))
    
    except Exception as exception:
        
        flash(f"{type(exception).__name__}: {exception}", category="error")
        
        return redirect(url_for("admin.admin_profile"))


@quiz.route("/add-question", methods=["GET", "POST"])
@login_required
def add_question():

    categories = db_session.query(QuestionCategory).all()

    if request.method == "POST":
        print(request.form)

    return render_template("quiz/add_question.html", answers=[], categories=categories)
