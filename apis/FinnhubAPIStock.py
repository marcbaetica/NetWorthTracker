# https://finnhub.io/api/v1/quote?symbol=TSLA&token=MY_TOKEN

import os
import requests as req
from apis.AbstractAPIStockClass import AbstractAPIStockClass
from dotenv import load_dotenv
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from urllib.parse import urlencode

load_dotenv()


class FinnhubAPIStock(AbstractAPIStockClass):
    def __init__(self, symbol):
        self.base_url = 'https://finnhub.io/api/v1/quote'
        self.url_encoded_params = {
                'symbol': symbol,
                'token': os.getenv('FINNHUB_TOKEN')
        }

    @property
    def stock_price(self):
        price = None
        query_url = self.base_url + '?' + urlencode(self.url_encoded_params)
        try:
            res = req.get(query_url)
            res.raise_for_status()
            price = float(res.json()['c'])
        except ConnectionError:
            print(f'Failed to connect to {query_url}.')
        except Timeout:
            print(f'Request to connect to {query_url} resulted in a timeout error.')
        except TooManyRedirects:
            print(f'The request to {query_url} exceeds the configured number of maximum redirections.')
        return price
