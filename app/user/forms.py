from flask_wtf import FlaskForm
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, TextAreaField, PasswordField, FormField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired, Length, NumberRange


class PortfolioForm(FlaskForm) : 
    portfolio_name = StringField("PORTFOLIO NAME", validators=[DataRequired()])
    total_cost = IntegerField("TOTAL COST", validators = [NumberRange(1, 1000000)])
    submit = SubmitField("SAVE")



class AssetForm(FlaskForm) : 
    pass 