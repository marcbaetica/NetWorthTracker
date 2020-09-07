import os
import time
from dotenv import load_dotenv
from finnhubApiClient import FinnhubApiClient


load_dotenv()
companySymbol = 'TSLA'


fhClinet = FinnhubApiClient(os.environ.get('FINNHUB_TOKEN'))

if fhClinet.isUsCompany(companySymbol):
	while True:
		currentPrice = fhClinet.getUsCompanyCurrentStockPrice(companySymbol)
		print(f"\nCurrent stock price for {companySymbol} is: ${currentPrice}")

		minima, maxima = fhClinet.getUsCompanyDayMinimaAndMaxima(companySymbol)
		print(f"Low of the day is ${minima} and the high of the day is ${maxima}.")

		time.sleep(2) #2 calls every 2 seconds. max 60 calls per minute as per rate minited API