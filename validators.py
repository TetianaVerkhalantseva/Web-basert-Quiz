from wtforms import Form, StringField
from wtforms.validators import length, email


class LoginForm(Form):
    firstname = StringField(validators=[length(min=3, max=30,\
                message="Please enter the right firstname!")])
    
    lastname = StringField(validators=[length(min=3, max=30,\
                message="Please enter the right lastname!")])
    
    #email = StringField(validators=[email(message="Please enter the right email!")])
    #this is the test
    #123456