from app.sqla import sqla 
from app.api.api_coingecko import cg
# import numpy as np 
class Asset(sqla.Model) : 
    id = sqla.Column(sqla.Integer, primary_key = True) 
    portfolio_id = sqla.Column(sqla.Integer, sqla.ForeignKey("portfolio.id"), nullable = False) 

    name = sqla.Column(sqla.Text, nullable = False)
    cost = sqla.Column(sqla.Float, nullable = False)
    average_buy_price = sqla.Column(sqla.Float, nullable = False)
    total_amount = sqla.Column(sqla.Float)
    average_sell_price = sqla.Column(sqla.Float) 

    portfolio = sqla.relationship('Portfolio', backref = sqla.backref('assets'))

    def count_profit(self) : 
        return self.entry_price - cg.get_current_price(self.name)


    def count_historical_profit(self, datetime) :
        return self.entry_price - cg.get_historical_price(datetime)
    
    # def count_average_buy_price(self, current_price) :
        
    def update_holdings(self, amount, transaction_type, current_price) : 
        if transaction_type == "SELL":
            amount = (-1)*amount
            # self.average_sell_price = np.average([self.average_sell_price, current_price], weights = [total_amount, amount])
        
        if transaction_type == "BUY": 
            pass
            # self.average_buy_price = np.average([self.average_buy_price, current_price], weights = [total_amount, amount])

            
        self.total_amount = self.total_amount + amount



            