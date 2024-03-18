import requests
import pandas as pd
from keys import api_key
from endpoints import base_url, securities_ep, his_ep

"""
TODO Write Docstring
"""
class Securities:
    def __init__(self, ticker, api_key):
        self.ticker = ticker
        self.api_key = api_key

    """
    PARAMETERS:

    RETURNS: securities

    DESC: get_securities_detail() takes on self.ticker as the security that we are using, api_key
    to validate the requests and returns a json object that is a list of all available securities 
    and associated positions
    """
    def get_securities_detail(self):
        payload = {'ticker': self.ticker}
        with requests.Session() as sess:
            sess.headers.update(self.api_key)
            response = sess.get(base_url + securities_ep, params = payload)
            if response.ok:
                securities = response.json()
        return securities

    """
    PARAMETERS:

    RETURNS: string value that represents the numerical position value

    DESC: get_position() calls get_securities_detail() for a particular asset and parses
    the output for the position value
    """
    def get_position(self):
        securities_json = self.get_securities_detail()
        security_position = securities_json[0]["position"]
        return security_position
    
    def get_nlv(self):
        securities_json = self.get_securities_detail()
        security_nlv = securities_json[0]["nlv"]
        return security_nlv
    
    def get_bid(self):
        securities_json = self.get_securities_detail()
        security_bid = securities_json[0]["bid"]
        return security_bid
    
    def get_ask(self):
        securities_json = self.get_securities_detail()
        security_ask = securities_json[0]["ask"]
        return security_ask

    """
    PARAMETERS:

    RETURNS:

    DESC: get_last_price() calls get_securities_detail() for a particular asset and parses
    the output for the last price 
    """
    
    def get_last_price(self):
        securities_json = self.get_securities_detail()
        security_last = securities_json[0]["last"]
        return security_last
    
    
    """
    PARAMETERS:

    RETURNS:

    DESC: get_bid_ask() calls get_securities_detail() for a particular asset and parses
    the output for the bid and the ask
    """
    
    def get_bid_ask(self):
        securities_json = self.get_securities_detail()
        security_bid = securities_json[0]["bid"]
        security_ask = securities_json[0]["ask"]
        bid_ask = [security_bid, security_ask]
        print("Bid, Ask")
        return bid_ask


    """
    PARAMETERS:

    RETURNS:

    DESC: get_bid_ask_size() calls get_securities_detail() for a particular asset and parses
    the output for the bid size and the ask size
    """
    def get_bid_ask_size(self):
        securities_json = self.get_securities_detail()
        security_bid_size = securities_json[0]["bid_size"]
        security_ask_size = securities_json[0]["ask_size"]
        bid_ask_size = [security_bid_size, security_ask_size]
        print("Bid Size, Ask Size")
        return bid_ask_size
    
    
    """
    PARAMETERS:

    RETURNS:

    DESC: get_volume() calls get_securities_detail() for a particular asset and parses
    the output for the total volume
    """


    def get_volume(self):
        securities_json = self.get_securities_detail()
        security_volume = securities_json[0]["total_volume"]
        print("Bid Size, Ask Size")
        return security_volume
    

    """
    PARAMETERS:

    RETURNS:

    DESC: get_trade_size_limits() calls get_securities_detail() for a particular asset and parses
    the output for the min trade size and the max trade size
    """

    def get_trade_size_limits(self):
        securities_json = self.get_securities_detail()
        security_min_trade = securities_json[0]["min_trade_size"]
        security_max_trade = securities_json[0]["max_trade_size"]
        min_max_trade_size = [security_min_trade, security_max_trade]
        print("Min Trade Limit, Max Trade Limit")
        return min_max_trade_size

