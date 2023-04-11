from wtforms import Form, StringField, SubmitField
from wtforms.validators import length, email, DataRequired
from wtforms.fields import TextAreaField, HiddenField

class KategoriForm(Form):
    id = HiddenField()
    navn = StringField("Navn på kategori", validators=[DataRequired()])
    submit = SubmitField("Oppdater")

class SpørsmålForm(Form):
    id = HiddenField()
    spørsmål = StringField('Spørsmål', validators=[DataRequired()])
    kategori = StringField('Kategori', validators=[DataRequired()])
    svar1 = StringField('Svaralternativ 1', validators=[DataRequired()])
    svar2 = StringField('Svaralternativ 2', validators=[DataRequired()])
    svar3 = StringField('Svaralternativ 3', validators=[DataRequired()])
    svar4 = StringField('Svaralternativ 4', validators=[DataRequired()])
    riktig_svar = StringField('Riktig svar', validators=[DataRequired()])

    submit = SubmitField('Oppdater')


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
