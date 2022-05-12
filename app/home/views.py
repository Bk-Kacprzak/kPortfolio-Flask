from flask import Blueprint
from flask import render_template
from app.api import api_coingecko as cg


bp = Blueprint("", __name__,url_prefix = "/", template_folder= "templates")
@bp.route("/")
def index():
    coins = cg.get_coins_by_mc(amount = 5)
    coin_list = list()
    return render_template("index.html", coins = coins) 

# index()

# {'id': 'bitcoin', 'symbol': 'btc', 'name': 'Bitcoin', 'image': 'https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579', 'current_price': 35885, 'market_cap': 682873487067, 'market_cap_rank': 1, 'fully_diluted_valuation': 753448031320, 'total_volume': 29881783762, 'high_24h': 36499, 'low_24h': 35487, 'price_change_24h': -580.079182167523, 'price_change_percentage_24h': -1.59078, 'market_cap_change_24h': -11606398991.034912, 'market_cap_change_percentage_24h': -1.67124, 'circulating_supply': 19032956.0, 'total_supply': 21000000.0, 'max_supply': 21000000.0, 'ath': 69045, 'ath_change_percentage': -48.00877, 'ath_date': '2021-11-10T14:24:11.849Z', 'atl': 67.81, 'atl_change_percentage': 52838.73303, 'atl_date': '2013-07-06T00:00:00.000Z', 'roi': None, 'last_updated': '2022-05-07T06:33:46.684Z'}
