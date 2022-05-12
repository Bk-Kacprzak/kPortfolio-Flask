from app.sqla import sqla 
from app.api.api_coingecko import cg
class Asset(sqla.Model) : 
    id = sqla.Column(sqla.Integer, primary_key = True) 
    name = sqla.Column(sqla.Text, nullable = False)
    transaction_date = sqla.Column(sqla.DateTime, nullable = False)
    entry_price = sqla.Column(sqla.Integer, nullable = False)


    portfolio_id = sqla.Column(sqla.Integer, sqla.ForeignKey("Portfolio.id"), nullable = False) 

    portfolio = sqla.relationship('Portfolio', backref = sqla.backref('assets'))

    
    # portfolio_id = sqla.Column(sqla.Integer, sqla.ForeignKey("Portfolio.id"), nullable = False)
    # portoflio = sqla.relationship("Portfolio", backref= sqla.backref('portfolios', lazy = True))

    # user_id = sqla.Column(sqla.Integer, sqla.ForeignKey('user.id'), nullable = False) 

    def count_profit(self) : 
        return self.entry_price - cg.get_current_price(self.name)
    
    # TODO :
    # 

    def count_historical_profit(self, datetime) :
        return self.entry_price - cg.get_historical_price(datetime)
    