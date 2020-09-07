import os
import time
from dotenv import load_dotenv
from finnhubApiClient import FinnhubApiClient

COMPANY_SYMBOL = 'TSLA'
load_dotenv()
fhClinet = FinnhubApiClient(os.environ.get('FINNHUB_TOKEN'))


#TODO: a custom context manager would be better
if fhClinet.isUsCompany(COMPANY_SYMBOL):
	while True:
		currentPrice = fhClinet.getUsCompanyCurrentStockPrice(COMPANY_SYMBOL)
		print(f"\nCurrent stock price for {COMPANY_SYMBOL} is: ${currentPrice}")

		minima, maxima = fhClinet.getUsCompanyDayMinimaAndMaxima(COMPANY_SYMBOL)
		print(f"Low of the day is ${minima} and the high of the day is ${maxima}.")

		time.sleep(2) #2 calls every 2 seconds. max 60 calls per minute as per rate minited API