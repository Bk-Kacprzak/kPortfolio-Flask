from app.sqla import sqla
from sqlalchemy.orm import validates


class Portfolio(sqla.Model) : 
    id = sqla.Column(sqla.Integer, primary_key = True)
    name = sqla.Column(sqla.String(64), nullable = False)
    total_cost = sqla.Column(sqla.Integer, nullable = True)
    user_id = sqla.Column(sqla.Integer,sqla.ForeignKey("user.id"), nullable  = False)

    user = sqla.relationship('User', backref = sqla.backref('portfolios'))

    @validates('portfolio_name') 
    def validate_is_unique(self, key, value): 
        names = [portfolio.name for portfolio in Portfolio.query.filter_by(user_id = value).all()]
        if name in names: 
            raise ValueError(f"{key} name must be unique.")
        
    


    

