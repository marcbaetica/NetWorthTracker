import json
import os
import requests as req
import sys
from dotenv import load_dotenv
from pprintpp import pprint
from urllib.parse import urlencode

load_dotenv()


class FreecurrencyAPIExchange:
    def __init__(self):
        self.base_url = 'https://freecurrencyapi.net/api/v2/latest'
        print(os.getenv('FREECURENCY_TOKEN'))
        self.encoded_params = {'apikey': os.getenv('FREECURENCY_TOKEN')}

    def current_exchange_rate_usd_to(self, currency):
        query_url = self.base_url + '?' + urlencode(self.encoded_params)
        try:
            res = req.get(query_url)
            res.raise_for_status()
            exchange_rates = json.loads(res.content)
            pprint(exchange_rates)
        except req.exceptions.HTTPError as e:
            print(f'ERROR: API call to {query_url} resulted in status code {res.status_code}.'
                  f' Check request url is correct. Error: {e}')
            sys.exit(1)
        # TODO: Handle requests.exceptions.ConnectionError and also add to some base class.
        # TODO: requests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: https://finnhub.io/api/v1/quote?symbol=TSLA&token=YOUR_TOKEN