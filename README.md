# Net worth tracker
Calculates net worth based on investments portofolio, as well as cash & physical assets and liabilities.
Investments are calculated using real time data from 3 apis (tracking US & Canadian stocks and the real USD to CAD exchange rate).

### 3rd party dependencies:
- [dotenv](https://pypi.org/project/python-dotenv/)

### APIs access:
3 APIs are used in the calculation of the most up-to-date value of the stock investment across 2 markets:
- [Finnhub](https://finnhub.io/)
- [Free Currency API](https://freecurrencyapi.net/)
- [Alpha Vantage](https://www.alphavantage.co/)

Though the services are free to use, each one requites an api token. The tokens are received by signing up for free on
each service and updating the local .env file appropriately. 

### TODOs:
- financial_portofolio.json is currently static. Need to automate this data to reflect monthly changes.
- Add integration with led matrix display and RaspberryPi for on-desk instrument.