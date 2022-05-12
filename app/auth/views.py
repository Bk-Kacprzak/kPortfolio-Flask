from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import abort
from flask import redirect
from flask import url_for
from flask import session
from flask_login import login_user, current_user
import functools
import is_safe_url 

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, FormField
from wtforms.validators import DataRequired, Email, EqualTo

from sqlalchemy.exc import IntegrityError
import sqlite3


from app.sqla import sqla
from app.models.user import User
from app.utils import redirect_to_next_page

bp = Blueprint("auth", __name__, url_prefix="/auth", template_folder="templates")

@bp.route('/login', methods = ['GET', 'POST']) 
def login() :
    if request.method == "POST":
        try:
            email = request.form["email"]
            password = request.form["password"]

            user = User.query.filter_by(email = email).first()
            print(user, flush = True)
            error = None 
            if user is None: 
                error ="Incorrect email address."
                flash(error, "email-error")

            elif not user.correct_password(password):
                error = "Incorrect password."
                flash(error, "password-error")
            
            if error is None: 
                login_user(user)
                return redirect_to_next_page('index')

        except ValueError as e:
            flash(str(e), "error")
        # get login and password
        # find user with specific login in db 
        # if found -> get password hash from db 
        # hash current password and check if they are equal
        # if equal -> authorize 


    return render_template("login.html")


@bp.route('/register', methods = ['GET', 'POST']) 
def register():
    if request.method == "POST": 
        try: 
            user = User(
                username = request.form["username"],
                email = request.form["email"],
                password = request.form["password"]
            )
        except ValueError as e :
            flash(str(e), "email-error")
            return render_template("register.html")
        
        sqla.session.add(user) 
        sqla.session.commit()
    
        return redirect(url_for("auth.login"))
    
    
        # check if email already exists in db
        # check password strength
        # create User record in try except block
        # push it to db 
        # redirect to login
        # TODO: redirect to /register/confirmation to inform user confirmation email was sent 


    if current_user.is_authenticated : 
        return redirect_to_next_page("index")

    return render_template("register.html")

@bp.route('/logout', methods = ['GET'])
def logout() : 
    session.clear()
    return redirect(url_for('index'))


@bp.route('/forgot', methods = ['GET', 'POST'])
def forgot() : 
    if request.method == "POST" : 
        email = request.form["email"]
        user = User.query.filter_by(email = email).first() 
        if user is None : 
            flash("Incorrect email address.", "email-error")
            return render_template("forgot.html")

        return render_template("email-sent.html")

    return render_template('forgot.html')


def login_required(view) :
    """view decorator that redirects unknown user to login to the service."""
    @functools.wraps(view)
    def check_if_authenticated(**settings) : 
        if not current_user.is_authenticated: 
            return redirect_to_next_page('auth.login')

        return view(**settings)

    return check_if_authenticated