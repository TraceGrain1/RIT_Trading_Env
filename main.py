# Trace Grain RIT software program

# Import and load modules
import requests
import pandas
import time
from securities import Securities
from orders import OrderBook
from trading import Trading
from keys import api_key
from endpoints import base_url, case_ep, trader_ep, limits_ep, news_ep, assets_ep, securities_ep, tenders_ep, leases_ep, his_ep, order_book_ep, tas_ep, orders_ep, id_ep, bulk_cancel_ep
from trading import post_order


def main():
    print("Starting Program...")

    trader_init = input("Do you want to start the trader? (y/n)")
    if trader_init == "y":
        print("Starting trader...")
        game = True
        trader = Trading(ticker = "HAR", api_key = api_key)
    else:
        print("Exiting program...")
        exit()

    print("Getting case information...")
    while game == True:
        time.sleep(0.5)
        spread = trader.calc_bid_ask_spread()
        spread_percent = trader.calc_spread_percent()
        # Print the spread and spread percent in a formatted string table separated by tabs
        print(f"Spread: {spread}\tSpread Percent: {spread_percent}")

        input_order = input("Do you want to place an order? (y/n)")
        if input_order == "y":
            print("Placing order...")
            order = post_order(ticker = "HAR", quantity = 100, price = 100, side = "buy", order_type = "limit", api_key = api_key)
            print(order)
        else:
            print("No order placed...")


if __name__ == "__main__":
    main()

