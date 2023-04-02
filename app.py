from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#MySQL informations
HOSTNAME = "kark.uit.no"
PORT = 3306
USERNAME = "stud_v23_ylu002"
PASSWORD = "Bts.12580123"
DATABASE = "stud_v23_ylu002"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql:\
//{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"

db = SQLAlchemy(app)

#with app.app_context():
    #db.drop_all()
    #db.create_all()

from models import *
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True)
