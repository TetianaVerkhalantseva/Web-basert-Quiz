#We can create class and table objects into database here

from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from config import DevelopmentConfig


engine = create_engine(DevelopmentConfig.SQLALCHEMY_DATABASE_URI)
base = declarative_base()


class Admin(base, UserMixin):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(50), nullable=False, unique=True)
    passord = Column(String(102), nullable=False)
    fornavn = Column(String(50), nullable=True)
    etternavn = Column(String(50), nullable=True)


class Quiz(base):
    __tablename__ = 'quiz'
    id = Column(Integer, primary_key=True, autoincrement=True)
    navn = Column(String(50), nullable=False)
    beskrivelse = Column(Text(1000), nullable=True)
    admin_id = Column(Integer, ForeignKey('admin.id'), nullable=True)
    admin = relationship('Admin')  


class QuestionCategory(base):
    __tablename__ = 'spørsmålskategori'
    id = Column(Integer, primary_key=True, autoincrement=True)
    navn = Column(String(50), nullable=False)


class Question(base):
    __tablename__ = 'spørsmål'
    id = Column(Integer, primary_key=True, autoincrement=True)
    spørsmål = Column(Text(500), nullable=False)
    kategori_id = Column(Integer, ForeignKey('spørsmålskategori.id'), nullable=False)
    admin_id = Column(Integer, ForeignKey('admin.id'), nullable=False)
    kategori = relationship('QuestionCategory')
    admin = relationship('Admin')


class AnswerOption(base):
    __tablename__ = 'svarmulighet'
    id = Column(Integer, primary_key=True, autoincrement=True)
    svar = Column(Text(500), nullable=False)
    korrekt = Column(Boolean, nullable=False)
    spørsmål_id = Column(Integer, ForeignKey('spørsmål.id'), nullable=False)
    spørsmål = relationship('Question')


class QuestionHasQuiz(base):
    __tablename__ = 'spørsmål_har_quiz'
    id = Column(Integer, primary_key=True, autoincrement=True)
    spørsmål_id = Column(Integer, ForeignKey('spørsmål.id'), nullable=False)
    quiz_id = Column(Integer, ForeignKey('quiz.id'), nullable=False)
    spørsmål = relationship('Question')
    quiz = relationship('Quiz')
    

class QuizSession(base):
    __tablename__ = 'quiz_sesjon'
    id = Column(Integer, primary_key=True, autoincrement=True)
    spørsmål_har_quiz_id = Column(Integer, ForeignKey('spørsmål_har_quiz.id'), nullable=False)
    svar_id = Column(Integer, ForeignKey('svarmulighet.id'), nullable=False)
    spørsmål_har_quiz_id = relationship('QuestionHasQuiz')
    svar = relationship('AnswerOption')