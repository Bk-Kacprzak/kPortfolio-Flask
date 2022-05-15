from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, FloatField, SelectField
from wtforms.validators import DataRequired, NumberRange

class PortfolioForm(FlaskForm) : 
    portfolio_name = StringField("PORTFOLIO NAME", validators=[DataRequired()])
    total_cost = FloatField("TOTAL COST", validators = [NumberRange(1, 1000000)])
    submit = SubmitField("SAVE")

class AssetForm(FlaskForm) : 
    portfolio = SelectField("PORTFOLIO NAME")
    asset_name = StringField("Asset Name", validators=[DataRequired()])
    amount = FloatField("TOTAL COST")
    date = DateTimeField("Date",format='%Y-%m-%d %H:%M:%S')
    price = FloatField("PRICE", validators=[DataRequired()])
    submit = SubmitField("ADD")