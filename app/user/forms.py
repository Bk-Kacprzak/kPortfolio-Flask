from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, FloatField, SelectField
from wtforms.validators import DataRequired, NumberRange
from flask import flash 
class PortfolioForm(FlaskForm) : 
    portfolio_name = StringField("PORTFOLIO NAME", validators=[DataRequired()])
    total_cost = FloatField("TOTAL COST", validators = [NumberRange(1, 1000000000)])
    submit = SubmitField("SAVE")

class AssetForm(FlaskForm) : 
    portfolio = SelectField("PORTFOLIO NAME")
    asset_name = StringField("Asset Name", validators=[DataRequired()])
    amount = FloatField("AMOUNT")
    date = DateTimeField("Date",format='%Y-%m-%d %H:%M:%S')
    price = FloatField("PRICE", validators=[DataRequired()])
    cost = FloatField("TOTAL COST", validators = [DataRequired()])
    submit = SubmitField("ADD")


    def validate(self) : 
        # _isValid = super().validate(self)
        isValid = True
        if self.amount.data is None: 
            flash("Insert correct amount.", "amount-error") 
            isValid = False 
        
        if self.price.data is None :
            flash("Insert correct price.", "price-error")
            isValid = False 

        if self.cost.data is None :
            print(self.cost.data, flush = True)
            flash("Insert correct price.", "cost-error")
            isValid = False 


        return (isValid)


