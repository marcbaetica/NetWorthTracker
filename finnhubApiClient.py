import requests
import os
from urllib.parse import urlencode


class FinnhubApiClient:
	def __init__(self, token):
		self.base_url = "https://finnhub.io/api/v1/"
		self.url_encoded_params = {"token": token}

	def makeApiCall(self, symbol, pathname):
		self.url_encoded_params['symbol'] = symbol
		res = requests.get(self.base_url + pathname + "?" + urlencode(self.url_encoded_params))
		if res.status_code == 429:
			requestsLimitError = "Requests reached the maximum 60 calls / minute rate limit that the free Finnhub account allows."
			print(requestsLimitError) #printing to console since all these exceptions are already caught by out scripts
			raise Exception(requestsLimitError)	
		return res

	def isUsCompany(self, symbol):
		try:
			res = self.makeApiCall(symbol, "stock/profile2")
		except Exception:
			return True #TODO: So not legible and counter-intuitive. Look for better way to render. Using Trybool might be an option.

		if res.json()['country'] == 'US':
			return True
		print(f"'{symbol}' is not a US company. Server response: {res.status_code} {res.json()}")
		return False

	def getUsCompanyCurrentStockPrice(self, symbol):
		try:
			res = self.makeApiCall(symbol, "quote")
		except Exception:
			return "unknown"

		return res.json()['c']

	def getUsCompanyDayMinimaAndMaxima(self, symbol):
		try:
			res = self.makeApiCall(symbol, "quote")
		except Exception:
			return "unknown", "unknown"

		low = res.json()['l']
		high = res.json()['h']
		return low, high
