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

from app.sqla import sqla
from app.utils import redirect_to_next_page

from app.models.portfolio import Portfolio
from app.user.forms import PortfolioForm, AssetForm

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
    form = PortfolioForm()
    if request.method == "POST":
        add_new_portfolio(form)

    print(Portfolio.query.filter_by(user_id = current_user.id).first(), flush = True)
    if Portfolio.query.filter_by(user_id = current_user.id).first() is None:
        return render_template("portfolio.html", form = form)

    # return redirect(url_for("portfolio.overview"), form = form)
    return redirect(url_for("portfolio.overview"))



@bp.route('/overview', methods = ['GET', 'POST'])
@login_required
@portfolio_required
def overview(): 
    portfolio_form = PortfolioForm()
    asset_form = AssetForm()
    assets = [] 
    form = None
    portfolios = Portfolio.query.filter_by(user_id = current_user.id).all()

    return render_template(
                            "overview.html", 
                            portfolio_form = portfolio_form, 
                            asset_form = asset_form, 
                            portfolios = portfolios, 
                            assets = assets,
    )

def add_new_portfolio(form) : 
    portfolio_name = None
    total_cost = None
    if form.validate_on_submit() :
        try:
            portfolio_name = form.portfolio_name.data
            total_cost = form.total_cost.data
            
            portfolio = Portfolio(
                name = portfolio_name, 
                total_cost = total_cost, 
                    user_id = current_user.id)


        except ValueError as e: 
            flash(str(e), "portfolio-error")
            return render_template("index.html", form = form, portfolio_name = portfolio_name, total_cost = total_cost)

        sqla.session.add(portfolio)
        sqla.session.commit()

        return redirect(url_for("portfolio.overview"))

    errors = [{'field': key, 'messages': form.errors[key]} for key in form.errors.keys()] if form.errors else []    
    if Portfolio.query.filter_by(user_id = current_user.id).first() is None:
        return render_template("portfolio.html", form = form)