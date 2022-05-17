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

from sqlalchemy.exc import IntegrityError
import sqlite3
import os 

from app.sqla import sqla
from app.models.user import User
from app.utils import redirect_to_next_page

from app.auth.forms import LoginForm, RegisterForm


bp = Blueprint("auth", __name__, url_prefix="/auth", template_folder="templates")

@bp.route('/login', methods = ['GET', 'POST']) 
def login() :
    email = None 
    password = None 
    form = LoginForm()

    if request.method == "POST": 
        if form.validate_on_submit() : 

            try : 
                email = form.email.data
                password = form.password.data
                form.email.data = ''
                form.password.data = '' 

                user = User.query.filter_by(email = email).first()
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
                return e
                # flash(str(e), "error") 

        return render_template("login.html", form = form, email = email, password = password)
    return render_template("login.html", form = form, email = email, password = password)


@bp.route('/register', methods = ['GET', 'POST']) 
def register():
    name = None
    email = None 
    password = None 
    confirm = None
    form = RegisterForm()

    if request.method == "POST": 
        if form.validate_on_submit() : 

            try: 
                name = form.name.data
                email = form.email.data 
                password = form.password.data 
                form.name.data = ''
                form.email.data = ''
                form.password.data = ''
                
                user = User(
                    username = name,
                    email = email,
                    password = password
                )
            except ValueError as e :
                message = e.args[0]
                error_type = e.args[1] 
                flash(message, error_type)
                return render_template("register.html", form = form, name = name, email = email, password = password, confirm = confirm)


        
            sqla.session.add(user) 
            sqla.session.commit()
            return redirect(url_for("auth.login"))

        errors = [{'field': key, 'messages': form.errors[key]} for key in form.errors.keys()] if form.errors else []    

        return render_template("register.html", form = form, name = name, email = email, password = password, confirm = confirm, errors = errors)

    if current_user.is_authenticated : 
        return redirect_to_next_page("index")

    return render_template("register.html", form = form)

    

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