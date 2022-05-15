from app.sqla import sqla
from sqlalchemy.orm import validates
from werkzeug.security import check_password_hash, generate_password_hash


from uuid import uuid4
from flask_login import UserMixin
from app.login import login_manager 

class User(UserMixin, sqla.Model) : 
    id = sqla.Column(sqla.Integer, primary_key = True)
    uuid = sqla.Column(sqla.String(64), nullable = False, default = lambda: str(uuid4()))
    username = sqla.Column(sqla.Text, nullable = False, unique = False)
    email = sqla.Column(sqla.Text, nullable = False, unique = True)
    password = sqla.Column(sqla.Text, nullable = False)
    # portfolios = sqla.relationship('Portfolio', backref = sqla.backref('user_id', lazy=True))
    #  -> relation moved to Portfolio 

    @validates('username', 'email', 'password')
    def validate_not_empty(self, key, value) : 
        if not value :
            raise ValueError(f'{key.capitalize()} is required.')

        if key == 'email' : 
            self.validate_is_unique(key, value, error_message = "This email is already registered.", error_type = "email-error")

        if key == 'password': 
            value = generate_password_hash(value) 
        return value 
    
    def validate_is_unique(self, key, value, error_message = None, error_type = None) : 
        if  (User
        .query
        .filter_by(**{key: value})
        .first() is not None):
            print(f"{value} already in db!!!!", flush = True)
            raise ValueError(error_message, error_type)

            if not error_message: 
                error_message = f'{key} must be unique.'


    def correct_password(self, text) : 
        return check_password_hash(self.password, text)

    def get_id(self) : 
        return self.uuid
    
    def __repr__(self) : 
        return self.username

@login_manager.user_loader 
def load_user(user_uuid) :
    return User.query.filter_by(uuid=user_uuid).first()