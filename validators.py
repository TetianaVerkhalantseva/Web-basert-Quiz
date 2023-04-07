from wtforms import Form, StringField
from wtforms.validators import length, email


class LoginForm(Form):
    firstname = StringField(validators=[length(min=3, max=30,\
                message="Du må skrive inn et brukernavn.")])
    
    lastname = StringField(validators=[length(min=3, max=30,\
                message="Du må skrive inn brukernes etternavn.")])
    
    #We can activate email validator if needed!
    #email = StringField(validators=[email(message="Please enter the right email!")])

    #We can validate if the email has been registered
    #First we need to get all the information about emails in the database
    #Eks: registered_email = ["aa@uit.no", "bb@uit.no"]

    #def validate_email(self, field):
        #email = field.data
        #if email in registered_email:
            #raise ValidationError("Email has been registered!")
        #return True
