#To avoid circular references, third-party modules and files need to be placed in a separate file.
#Eg. SQLAlchemy and Flask-Mail etc.

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# This file is not needed, it should be deleted.
# I implemented the code in models.py so what
# in the app.py file we import the classes from models.py.
# And in models.py we don't need to import anything from app.py.
# Therefore, the exts.py file can be deleted