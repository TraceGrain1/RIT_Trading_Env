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

    while game == True:
        time.sleep(0.5)
        spread = round(trader.calc_bid_ask_spread(), 2)
        spread_percent = round(trader.calc_spread_percent(), 2)
        position = trader.get_position()
        nlv = trader.get_nlv()
        bid = trader.get_bid()
        ask = trader.get_ask()

        print("------------------------------------------------------------------------------------")
        print(f"Bid: {bid}\tAsk: {ask}\n")
        print(f"Spread: {spread}\tSpread Percent: {spread_percent} %\tPosition: {position} shares\n")
        print(f"Net Liquidation Value: {nlv}\n")
        print("------------------------------------------------------------------------------------")

        input_order = input("Do you want to place an order? (y/n)")
        print("\n")
        if input_order == "y":
            print("Placing order...")
            quantity = input("Enter quantity: ")
            quantity = int(quantity)
            price = input("Enter Price: ")
            order = trader.post_order(order_type = "LIMIT", quantity = quantity, action = "BUY", price = price)
            print(order)
        else:
            print("No order placed...")


if __name__ == "__main__":
    main()

