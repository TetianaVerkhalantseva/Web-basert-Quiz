#To avoid circular references, third-party modules and files need to be placed in a separate file.
#Eg. SQLAlchemy and Flask-Mail etc.

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()