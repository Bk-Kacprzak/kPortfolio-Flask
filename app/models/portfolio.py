from app.sqla import sqla
from sqlalchemy.orm import validates


class Portfolio(sqla.Model) : 
    id = sqla.Column(sqla.Integer, primary_key = True)
    name = sqla.Column(sqla.String(64), nullable = False)
    total_cost = sqla.Column(sqla.Integer, nullable = True)
    user_id = sqla.Column(sqla.Integer,sqla.ForeignKey("user.id"), nullable  = False)
    # user = sqla.relationship("User", backref= sqla.backref('portfolios', lazy = True)) ->> backref available in user.py 
    
    # assets = sqla.relationship('Asset', backref = sqla.backref('portoflio_id', lazy=True)) #again, one portfolio to many assets 
    user = sqla.relationship('User', backref = sqla.backref('portfolios'))
    # TODO:

    @validates('portfolio_name')
    def validate_not_empty(self, key, value):  
        if not value :
            raise ValueError(f'{key.capitalize()} is required.')
        return value


    

