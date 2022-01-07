import json
import os
import requests as req
import sys
from dotenv import load_dotenv
from urllib.parse import urlencode

load_dotenv()


class FreecurrencyAPIExchange:
    def __init__(self):
        self.base_url = 'https://freecurrencyapi.net/api/v2/latest'
        token_env_variable = 'FREECURENCY_TOKEN'
        try:
            self.encoded_params = {'apikey': os.environ[token_env_variable]}
        except KeyError as e:
            print(f'No environment variable {token_env_variable} was found at runtime. Check .env file for definition.')
            sys.exit(1)

    def current_exchange_rate_usd_to(self, currency_symbol):
        query_url = self.base_url + '?' + urlencode(self.encoded_params)
        try:
            res = req.get(query_url)
            res.raise_for_status()
            exchange_rates = json.loads(res.content)['data']
        except req.exceptions.HTTPError as e:
            print(f'ERROR: API call to {query_url} resulted in status code {res.status_code}.'
                  f' Check request url is correct. Error: {e}')
            sys.exit(1)
        # TODO: Handle requests.exceptions.ConnectionError and also add to some base class.
        # TODO: requests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: https://finnhub.io/api/v1/quote?symbol=TSLA&token=YOUR_TOKEN
        if currency_symbol not in exchange_rates:
            raise ValueError(f'ERROR: Currency symbol {currency_symbol} was not found under the response payloads.')
        return exchange_rates[currency_symbol]
