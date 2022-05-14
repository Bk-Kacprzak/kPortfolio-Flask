from flask import Flask, render_template
import os
from flask_login import LoginManager
from app.utils import url_for_other_page
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader


def create_app() : 
    app = Flask(__name__)
    app.config.from_mapping(
        ENV = 'development',
        DEBUG = True, 
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, "flaskr.sqlite")
    )

    register_jinja_env(app)
    # register all blueprints
    import app.home.views as home
    import app.auth.views as auth
    import app.user.views as portfolio
    import app.home.live_prices as live_prices
    app.register_blueprint(auth.bp)
    app.register_blueprint(portfolio.bp)
    app.register_blueprint(home.bp)
    app.register_blueprint(live_prices.bp)
    # init database 
    from app import db 
    db.init_app(app)

    # login manager
    from .login import login_manager 
    login_manager.init_app(app)
    # configure SQLAlchemy
        # SQLALCHEMY_DATABASE_URI=f'sqlite:///{app.config["DATABASE"]}'
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{app.config["DATABASE"]}'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    from .sqla import sqla
    sqla.init_app(app)

    # Flask login
    from app.login import login_manager 
    login_manager.init_app(app)

    # @app.route('/')
    # def index() :
    #     return render_template("index.html")


    app.add_url_rule("/", endpoint="index")

    return app

def register_jinja_env(app):
    """Configure the Jinja env to enable some functions in templates."""
    app.jinja_env.globals.update({
        'timeago': lambda x: arrow.get(x).humanize(),
        'url_for_other_page': url_for_other_page,
    })
