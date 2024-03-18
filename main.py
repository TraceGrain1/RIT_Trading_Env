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
        spread = round(trader.calc_bid_ask_spread(), 2)
        spread_percent = round(trader.calc_spread_percent(), 2)
        position = trader.get_position()
        nlv = trader.get_nlv()
        bid = trader.get_bid()
        ask = trader.get_ask()
        my_o_orders = trader.get_my_orders("OPEN")
        my_t_orders = trader.get_my_orders("TRANSACTED")
        my_c_orders = trader.get_my_orders("CLOSED")

        print("------------------------------------------------------------------------------------")
        print(f"Bid: {bid}\tAsk: {ask}")
        print(f"Spread: {spread}\tSpread Percent: {spread_percent} %\tPosition: {position} shares")
        print(f"Net Liquidation Value: {nlv}")
        print("------------------------------------------------------------------------------------")
        print("My Open Orders:")
        print(my_o_orders)
        print("\n")
        print("My Transactions:")
        print(my_t_orders)
        print("\n")
        print("My Closed Orders:")
        print(my_c_orders)
        print("------------------------------------------------------------------------------------")

        input_order = input("Do you want to place an order? (1/0)")
        print("\n")
        if input_order == "1":
            print("Placing order...")
            while True:
                try:
                    quantity = input("Enter quantity: ")
                    quantity = float(quantity)
                    break
                except ValueError:
                    print("Invalid input...")
            while True:
                try:
                    price = input("Enter Price: ")
                    price = float(quantity)
                    break
                except ValueError:
                    print("Invalid input...")
            order = trader.post_order(order_type = "LIMIT", quantity = quantity, action = "BUY", price = price)
            print(order)
        else:
            print("No order placed...")


if __name__ == "__main__":
    main()

