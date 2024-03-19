## This file houses all the trading
import requests
import pandas as pd
from orders import OrderBook
from keys import api_key
from endpoints import base_url, case_ep, assets_ep, securities_ep, his_ep, orders_ep, order_book_ep


class Trading(OrderBook):
    def __init__(self, ticker, api_key):
        super().__init__(ticker, api_key)

    def get_case(self):
        with requests.Session() as sess:
            sess.headers.update(self.api_key)
            response = sess.get(base_url + case_ep)
            if response.ok:
                case = response.json()
        return case

    def calc_bid_ask_spread(self):
        bids = self.get_bid_ask()
        asks = self.get_bid_ask()
        spread = asks[1] - bids[0]
        return spread
    
    def calc_spread_percent(self):
        spread = self.calc_bid_ask_spread()
        ask_price = self.get_last_price()
        spread_percent = (spread / ask_price) * 100
        return spread_percent
    
    def calculate_bullish(self):
        ohlc = self.get_ohlc()
        open_price = ohlc["open"][0]
        close_price = ohlc["close"][0]
        bullish = close_price > open_price
        return bullish
    
    def bull_bear_tick_distribution(self, ticks):
        ohlc = self.get_ohlc()
        if len(ohlc) > ticks:
            ohlc_sub = ohlc.head(ticks)
            open_price = ohlc_sub["open"]
            close_price = ohlc_sub["close"]
            distribution = close_price > open_price
            while True:
                try:
                    sum_distribution = distribution.sum()
                    return sum_distribution
                except:
                    continue


"""
PARAMETERS: None

RETURNS: case

DESCRIPTION:

get_case() gets the current simulation Case name period number,
tick_per_period, total periods, status and enforcement of trading limits JSON object

returns a variable called case that is a JSON string
"""
def get_case():
    with requests.Session() as sess:
        sess.headers.update(api_key)
        response = sess.get(base_url + case_ep)
        if response.ok:
            case = response.json()
    return case


"""
get_assets() 
"""
def get_assets(ticker):
    payload = {'ticker': ticker}
    with requests.Session() as sess:
        sess.headers.update(api_key)
        response = sess.get(base_url + assets_ep, params = payload)
        if response.ok:
            assets = response.json()
    return assets


"""
PARAMETERS: ticker

RETURNS:  
get_securities()
"""
def get_securities(ticker):
    payload = {'ticker': ticker}
    with requests.Session() as sess:
        sess.headers.update(api_key)
        response = sess.get(base_url + securities_ep, params = payload)
        if response.ok:
            securities = response.json()
    return securities

"""
get_securities_history()
"""
def get_securities_hist(ticker):
    payload = {'ticker': ticker}
    with requests.Session() as sess:
        sess.headers.update(api_key)
        response = sess.get(base_url + securities_ep + his_ep, params = payload)
        if response.ok:
            securities = response.json()
            securities_df = pd.json_normalize(securities)

    return securities_df


"""
get_securities_book()
"""
def get_securities_book(ticker, side):
    payload = {'ticker': ticker}
    with requests.Session() as sess:
        sess.headers.update(api_key)
        response = sess.get(base_url + securities_ep + order_book_ep, params = payload)
        if response.ok:
            sec_order_book = response.json()
            sec_order_book_df = pd.json_normalize(sec_order_book[side])
    return sec_order_book_df


"""
get_orders() takes one parameter called order_type

order_type can take on the values of "OPEN", "TRANSACTED", "CANCELLED"

Returns all orders of the type specified 
"""
def get_orders(order_type):
    payload = {'status': order_type}
    with requests.Session() as sess:
        sess.headers.update(api_key)
        response = sess.get(base_url + orders_ep, params = payload)
        if response.ok:
            orders = response.json()
    return orders