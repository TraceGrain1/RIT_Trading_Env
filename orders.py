import requests
import pandas as pd
from securities import Securities
from keys import api_key
from endpoints import base_url, orders_ep, securities_ep, order_book_ep

"""
TODO Write Docstring
"""
class OrderBook(Securities):
    def __init__(self, ticker, api_key):
        super().__init__(ticker, api_key)

    """
    PARAMETERS:

    RETURNS: global_orders_df

    DESC: get_order_book() takes in two arguments, self and side where side takes on the value
    of either "bids", or "asks" and returns a data frame of the current bids.
    """

    def get_order_book(self, side):
        payload = {'ticker': self.ticker}
        with requests.Session() as sess:
            sess.headers.update(self.api_key)
            response = sess.get(base_url + securities_ep + order_book_ep, params = payload)
            if response.ok:
                global_orders = response.json()
                global_orders_df = pd.json_normalize(global_orders[side])
        return global_orders_df
    
    """
    TODO Write Doc String
    """
    def get_order_book_type(self, side, order_type, col_subset_list):
        orderbook_df = self.get_order_book(side = side)
        key = orderbook_df["type"] == order_type
        order_subset = orderbook_df[key.tolist()]
        order_subset = orderbook_df[col_subset_list]
        return order_subset
    
    """
    PARAMETERS:

    RETURNS: order_subset

    DESC: get_order_book_quantity() takes in five parameters, self, side, quantity, equality_side and col_subset_list
    where side takes on the value of either "bids", or "asks", quantity is the amount of shares that we are looking for,
    equality_side takes on the values of ">", "=", or "<" and col_subset_list is a list of columns that we want to return
    in the data frame. The function returns a data frame of the current bids or asks that meet the criteria of the equality
    side and the quantity of shares that we are looking for.
    """
    def get_order_book_quantity(self, side, quantity, equality_side, col_subset_list):
        orderbook_df = self.get_order_book(side = side)
        if equality_side == ">":
            key = orderbook_df["quantity"] >= quantity
        elif equality_side == "=":
            key = orderbook_df["quantity"] == quantity
        else:
            key = orderbook_df["quantity"] <= quantity
        order_subset = orderbook_df[key.tolist()]
        order_subset = order_subset[col_subset_list]
        return order_subset


    """
    PARAMETERS:

    RETURNS: my_orders

    DESC: get_my_orders() takes in two parameters, self and status where status takes on the values of "OPEN",
    "TRANSACTED" or "CANCELLED" and returns a json string of all of the users OPEN, TRANSACTED or CANCELLED orders
    """
    def get_my_orders(self, status):
        payload = {'status': status}
        with requests.Session() as sess:
            sess.headers.update(self.api_key)
            response = sess.get(base_url + orders_ep, params = payload)
            if response.ok:
                my_orders = response.json()
            else:
                my_orders = "No orders found"
        return my_orders

    """
    PARAMETERS: order_type, quantity, price

    RETURNS: response
    """
    def post_order(self, order_type, quantity, action, price):
        payload = {'ticker': self.ticker, 'type': order_type, 'quantity': quantity, 'action': action, 'price': price }
        with requests.Session() as sess:
            sess.headers.update(self.api_key)
            response = sess.post(base_url + orders_ep, params = payload)
            if response.ok:
                response = response.json()
        return response
