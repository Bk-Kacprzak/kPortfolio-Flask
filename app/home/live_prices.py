from flask import Blueprint
from flask import render_template
from app.api import api_coingecko as cg

bp = Blueprint("live-prices", __name__, url_prefix="/live-prices")
@bp.route("/overview")
def overview():
    # TODO: add pagination
    coins = cg.get_coins_by_mc(amount = 100)
    return render_template("live-prices.html", coins = coins) 

