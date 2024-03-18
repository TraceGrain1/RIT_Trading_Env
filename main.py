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
        print("My Transactions:")
        print(my_t_orders)
        print("My Closed Orders:")
        print(my_c_orders)
        print("------------------------------------------------------------------------------------")

        input_order = input("Do you want to place an order? (1/0)")
        print("\n")
        if input_order == "1":
            print("Placing order...")
            side = input("Choose side: (1) Buy (2) Sell")
            if side == "1":
                while True:
                    try:
                        print("Quantity Hot Keys: (1): 100, (2): 200, (3): 300, (4): 400, (5): 500, (6): Custom Quantity")
                        hot_key = input("Enter Hot Key: ")
                        if hot_key == "1":
                            quantity = 100
                            quantity = float(quantity)
                            break
                        elif hot_key == "2":
                            quantity = 200
                            quantity = float(quantity)
                            break
                        elif hot_key == "3":
                            quantity = 300
                            quantity = float(quantity)
                            break
                        elif hot_key == "4":
                            quantity = 400
                            quantity = float(quantity)
                            break
                        elif hot_key == "5":
                            quantity = 500
                            quantity = float(quantity)
                            break
                        elif hot_key == "6":
                            quantity = input("Enter quantity: ")
                            quantity = float(quantity)
                            break
                        else:
                            break
                    except ValueError:
                        print("Invalid input...")
                while True:
                    try:
                        price = input("Enter Price: ")
                        price = float(price)
                        break
                    except ValueError:
                        print("Invalid input...")
                order = trader.post_order(order_type = "LIMIT", quantity = quantity, action = "BUY", price = price)
            else:
                while True:
                    try:
                        print("Quantity Hot Keys: (1): 100, (2): 200, (3): 300, (4): 400, (5): 500, (6): Custom Quantity")
                        hot_key = input("Enter Hot Key: ")
                        if hot_key == "1":
                            quantity = 100
                            quantity = float(quantity)
                            break
                        elif hot_key == "2":
                            quantity = 200
                            quantity = float(quantity)
                            break
                        elif hot_key == "3":
                            quantity = 300
                            quantity = float(quantity)
                            break
                        elif hot_key == "4":
                            quantity = 400
                            quantity = float(quantity)
                            break
                        elif hot_key == "5":
                            quantity = 500
                            quantity = float(quantity)
                            break
                        elif hot_key == "6":
                            quantity = input("Enter quantity: ")
                            quantity = float(quantity)
                            break
                        else:
                            break
                    except ValueError:
                        print("Invalid input...")
                while True:
                    try:
                        price = input("Enter Price: ")
                        price = float(price)
                        break
                    except ValueError:
                        print("Invalid input...")
                order = trader.post_order(order_type = "LIMIT", quantity = quantity, action = "SELL", price = price)
            print(order)
        else:
            print("No order placed...")


if __name__ == "__main__":
    main()

