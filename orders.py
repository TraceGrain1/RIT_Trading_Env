import requests
import pandas as pd
from keys import api_key
from endpoints import base_url, orders_ep, securities_ep, order_book_ep

class OrderBook:
    def __init__(self, ticker, api_key):
        self.ticker = ticker
        self.api_key = api_key
    
    """
    PARAMETERS:

    RETURNS: securities

    DESC:
    """
    
    def get_order_book(self, side):
        payload = {'ticker': self.ticker}
        with requests.Session() as sess:
            sess.headers.update(self.api_key)
            response = sess.get(base_url + securities_ep + order_book_ep, params = payload)
            if response.ok:
                global_orders = response.json()
                print(global_orders)
                global_orders_df = pd.json_normalize(global_orders[side])
        return global_orders_df
    
    """
    PARAMETERS:

    RETURNS: securities

    DESC:
    """
    def get_my_orders(self, status):
        payload = {'status': status}
        with requests.Session() as sess:
            sess.headers.update(self.api_key)
            response = sess.get(base_url + orders_ep, params = payload)
            if response.ok:
                my_orders = response.json()
        return my_orders
