# Trace Grain RIT software program

# Import and load modules
import requests
import pandas
import time
import numpy as np
import asciichartpy as acp
from securities import Securities
from orders import OrderBook
from trading import Trading
from keys import api_key
from endpoints import base_url, case_ep, trader_ep, limits_ep, news_ep, assets_ep, securities_ep, tenders_ep, leases_ep, his_ep, order_book_ep, tas_ep, orders_ep, id_ep, bulk_cancel_ep


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
        current_price = trader.get_last_price()
        bid = trader.get_bid()
        ask = trader.get_ask()
        market = trader.get_ohlc()
        tick = market["tick"][0]

        if tick >= 1:
            bull_1 = trader.bull_bear_tick_distribution(1)
        else:
            bull_1 = 0

        if tick >= 3:
            bull_3 = trader.bull_bear_tick_distribution(3)
        else:
            bull_3 = 0

        if tick >= 5:
            bull_5 = trader.bull_bear_tick_distribution(5)
        else:
            bull_5 = 0

        if tick >= 7:
            bull_7 = trader.bull_bear_tick_distribution(7)
        else:
            bull_7 = 0

        if tick >= 10:
            bull_10 = trader.bull_bear_tick_distribution(10)
        else:
            bull_10 = 0

        if tick >= 15:
            bull_15 = trader.bull_bear_tick_distribution(15)
        else:
            bull_15 = 0

        if tick >= 20:
            bull_20 = trader.bull_bear_tick_distribution(20)
        else:
            bull_20 = 0

        if tick >= 25:
            bull_25 = trader.bull_bear_tick_distribution(25)
        else:
            bull_25 = 0
        
        if tick >= 30:
            bull_30 = trader.bull_bear_tick_distribution(30)
        else:
            bull_30 = 0

        if tick >= 40:
            bull_40 = trader.bull_bear_tick_distribution(40)
        else:
            bull_40 = 0
        
        if tick >= 50:
            bull_50 = trader.bull_bear_tick_distribution(50)
        else:
            bull_50 = 0

        my_o_orders = trader.get_my_orders("OPEN")
        my_t_orders = trader.get_my_orders("TRANSACTED")

        bull_envelope = [0, bull_1, bull_3, bull_5, bull_7, bull_10, bull_15, bull_20, bull_25, bull_30, bull_40, bull_50, 15]

        if tick >= 70:
            price_series = pandas.Series(market["close"]).head(70)
            #price_series = price_series.tolist().reverse()
        else:
            price_series = pandas.Series(market["close"])
            #price_series = price_series.tolist().reverse()

        print("------------------------------------------------------------------------------------")
        print("Market Data: ")
        print(f"Tick: {tick} out of 300")
        price_plot = acp.plot(price_series, {'height': 5, 'offset': 5})
        print(price_plot)
        print("------------------------------------------------------------------------------------")
        print("Bullish Envelope: ")
        bull_env_plot = acp.plot(bull_envelope, {'height': 5, 'offset': 5})
        print(bull_env_plot)
        print("------------------------------------------------------------------------------------")
        print("Momentum Indicators: ")
        print(f"Bull 1: {bull_1}\tBull 3: {bull_3}\tBull 5: {bull_5}\tBull 7: {bull_7}\tBull 10: {bull_10}")
        print("------------------------------------------------------------------------------------")
        print(f"Price: {current_price}")
        print(f"Bid: {bid}\tAsk: {ask}")
        print(f"Spread: {spread}\tSpread Percent: {spread_percent} %\tPosition: {position} shares")
        print(f"Net Liquidation Value: {nlv}")
        print("------------------------------------------------------------------------------------")
        print("My Open Orders:")
        print(my_o_orders)
        print("My Transactions:")
        print(my_t_orders)
        print("------------------------------------------------------------------------------------")

        input_order = input("Do you want to place an order? (1/0)")
        print("\n")
        if input_order == "1":
            print("Placing order...")
            side = input("Choose side: (1) Buy (2) Sell")
            if side == "1":
                while True:
                    try:
                        print("Quantity Hot Keys: (1): 500, (2): 1000, (3): 1500, (4): 2000, (5): 2500, (6): Custom Quantity")
                        hot_key = input("Enter Hot Key: ")
                        if hot_key == "1":
                            quantity = 500
                            quantity = float(quantity)
                            break
                        elif hot_key == "2":
                            quantity = 1000
                            quantity = float(quantity)
                            break
                        elif hot_key == "3":
                            quantity = 1500
                            quantity = float(quantity)
                            break
                        elif hot_key == "4":
                            quantity = 2000
                            quantity = float(quantity)
                            break
                        elif hot_key == "5":
                            quantity = 2500
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
                        print("Price Hot Keys: (1): Current Price, (2): Bid, (3): Ask, (4): Custom Price, (5): Market Order")
                        price = input("Enter Price: ")
                        if price == "1":
                            order_type = "LIMIT"
                            price = float(current_price)
                            break
                        elif price == "2":
                            order_type = "LIMIT"
                            price = float(bid)
                            break
                        elif price == "3":
                            order_type = "LIMIT"
                            price = float(ask)
                            break
                        elif price == "4":
                            order_type = "LIMIT"
                            price = float(input("Enter Custom Price: "))
                            break
                        elif price == "5":
                            order_type = "MARKET"
                            price = None
                            break
                    except ValueError:
                        print("Invalid input...")
                order = trader.post_order(order_type = order_type, quantity = quantity, action = "BUY", price = price)
            else:
                while True:
                    try:
                        print("Quantity Hot Keys: (1): 500, (2): 1000, (3): 1500, (4): 2000, (5): 2500, (6): Custom Quantity")
                        hot_key = input("Enter Hot Key: ")
                        if hot_key == "1":
                            quantity = 500
                            quantity = float(quantity)
                            break
                        elif hot_key == "2":
                            quantity = 1000
                            quantity = float(quantity)
                            break
                        elif hot_key == "3":
                            quantity = 1500
                            quantity = float(quantity)
                            break
                        elif hot_key == "4":
                            quantity = 2000
                            quantity = float(quantity)
                            break
                        elif hot_key == "5":
                            quantity = 2500
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
                        print("Price Hot Keys: (1): Current Price, (2): Bid, (3): Ask, (4): Custom Price (5): Market Order")
                        price = input("Enter Price: ")
                        if price == "1":
                            order_type = "LIMIT"
                            price = float(current_price)
                            break
                        elif price == "2":
                            order_type = "LIMIT"
                            price = float(bid)
                            break
                        elif price == "3":
                            order_type = "LIMIT"
                            price = float(ask)
                            break
                        elif price == "4":
                            price = price = float(input("Enter Custom Price: "))
                            break
                        elif price == "5":
                            order_type = "MARKET"
                            price = 0
                            break
                    except ValueError:
                        print("Invalid input...")
                order = trader.post_order(order_type = order_type, quantity = quantity, action = "SELL", price = price)
            print(order)
        else:
            print("No order placed...")
            print("\n")


if __name__ == "__main__":
    main()

