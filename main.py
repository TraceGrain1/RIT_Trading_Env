# Trace Grain RIT software program

# Import and load modules
import requests
import pandas
from keys import api_key
from endpoints import base_url, case_ep, trader_ep, limits_ep, news_ep, assets_ep, securities_ep, tenders_ep, leases_ep, his_ep, order_book_ep, tas_ep, orders_ep, id_ep, bulk_cancel_ep

def main():
    print("Starting Program...")
    with requests.Session() as sess:
        sess.headers.update(api_key)
        response = sess.get(base_url + case_ep)
        print(response)
        if response.ok:
            case = response.json()
            print(case)

if __name__ == "__main__":
    main()

