# Trace Grain RIT software program

# Import and load modules
import requests
import pandas
from securities import Securities
from orders import OrderBook
from keys import api_key
from endpoints import base_url, case_ep, trader_ep, limits_ep, news_ep, assets_ep, securities_ep, tenders_ep, leases_ep, his_ep, order_book_ep, tas_ep, orders_ep, id_ep, bulk_cancel_ep
from trading_functions import get_case, get_assets, get_securities, get_securities_hist, get_orders, get_securities_book, post_order


def main():
    print("Starting Program...")
    market_order_book = OrderBook(ticker = "HAR", api_key = api_key)

    x = market_order_book.get_order_book_quantity(side = "bids", quantity=1000, equality_side=">", col_subset_list="price")

    print(x)
if __name__ == "__main__":
    main()

