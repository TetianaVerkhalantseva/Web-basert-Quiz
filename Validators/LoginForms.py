from wtforms import Form, StringField, BooleanField, SubmitField, ValidationError
from wtforms.validators import length, email
from flask_wtf import FlaskForm

registered_email = ["aa@uit.no", "bb@uit.no"]

class LoginForm_1(Form):
    firstname = StringField(validators=[length(min=3, max=30,\
                message="Please enter the right firstname!")])
    
    lastname = StringField(validators=[length(min=3, max=30,\
                message="Please enter the right lastname!")])
    
    email = StringField(validators=[email(message="Please enter the right email!")])

    def validate_email(self, field):
        email = field.data
        if email in registered_email:
            raise ValidationError("Email has been registered!")
        return True
    

class LoginForm_2(FlaskForm):
    email = StringField(label="Email", validators=[email(message=\
            "Please enter the right email!")], render_kw={\
        "placeholder": "Enter your email"})
    
    password = StringField(label="Password", validators=[length(\
                min=6, max=20, message="Please enter the right \
                length of password!")], render_kw={"placeholder":\
                "Enter your password"})
    
    remember = BooleanField(label="Remember me:")

    submit = SubmitField(label="Submit")
