from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash
from flask import abort
from flask import redirect
from flask import url_for
from flask import session
from app.auth.views import login_required
from flask_login import current_user
import functools

from app.models.portfolio import Portfolio
from app.sqla import sqla
from app.utils import redirect_to_next_page


bp = Blueprint("portfolio", __name__,url_prefix = "/portfolio", template_folder="templates")

def portfolio_required(view) : 
    """Returns true if user has any portfolio."""
    @functools.wraps(view) 
    def check_if_portfolio_exist(**settings) : 
        if Portfolio.query.filter_by(user_id = current_user.id).first() is None:
            # return redirect_to_next_page('portfolio.portfolio')
            return redirect(url_for("portfolio.portfolio"))

        return view(**settings)
        
    return check_if_portfolio_exist



@bp.route('/', methods = ['GET', 'POST'])
@login_required
def portfolio():
    if request.method == "POST":
        try: 
            portfolio = Portfolio(
                name = request.form["portfolioName"], 
                total_cost = request.form["totalCost"], 
                user_id = current_user.id)
                    
        except ValueError as e: 
            flash(str(e), "email-error")

        sqla.session.add(portfolio)
        sqla.session.commit()
        return redirect(url_for("portfolio.overview"))
    if Portfolio.query.filter_by(user_id = current_user.id).first() is None:
        return render_template("tracker/portfolio.html")
    return redirect(url_for("portfolio.overview"))

@bp.route('/overview', methods = ['GET', 'POST'])
@login_required
@portfolio_required
def overview(): 
    portfolios = Portfolio.query.filter_by(user_id = current_user.id).all()
    assets = []

    
    return render_template("tracker/overview.html", portfolios = portfolios, assets = assets)

