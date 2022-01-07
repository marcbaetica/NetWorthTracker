import os
import requests as req
from apis.abstractAPIStockClass import AbstractAPIStockClass
from dotenv import load_dotenv
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from urllib.parse import urlencode

load_dotenv()


class AlphavantageAPIStock(AbstractAPIStockClass):
    def __init__(self, stock):
        self.base_url = 'https://www.alphavantage.co/query'
        self.url_encoded_params = {
                'function': 'GLOBAL_QUOTE',
                'symbol': stock,
                'apikey': os.getenv('ALPHAVANTAGE_KEY')
        }

    @property
    def stock_price(self):
        price = None
        query_url = self.base_url + '?' + urlencode(self.url_encoded_params)
        try:
            res = req.get(query_url)
            res.raise_for_status()
            price = float(res.json()['Global Quote']['05. price'])
        except ConnectionError:
            print(f'Failed to connect to {query_url}.')
        except Timeout:
            print(f'Request to connect to {query_url} resulted in a timeout error.')
        except TooManyRedirects:
            print(f'The request to {query_url} exceeds the configured number of maximum redirections.')
        return price
