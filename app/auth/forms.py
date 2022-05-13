from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, TextAreaField, PasswordField, FormField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired, Length
from app.models import user

class LoginForm(FlaskForm) : 
    email = EmailField("Email address", validators=[DataRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Log in")


class RegisterForm(FlaskForm) : 
    name = StringField("Name", validators = [DataRequired(), Length(min = 3, max =32)])
    email = EmailField("Email address", validators=[DataRequired()])
    password = PasswordField("Password", validators=[InputRequired(), Length(min= 8), EqualTo('confirm', message = "Passwords must match")])
    confirm = PasswordField("Confirm Password", validators=[InputRequired()])
    submit = SubmitField("Create Account")

    # def validate(self) : 
    #     if self.password.data != self.confirm.data :
    #         raise ValueError("Passwords must match.", "password-error")