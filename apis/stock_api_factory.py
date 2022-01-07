from apis.AlphavantageAPIStock import AlphavantageAPIStock
from apis.FinnhubAPIStock import FinnhubAPIStock


def stock_api_factory(stock, exchange_market):
    if exchange_market == "NASDAQ":
        return FinnhubAPIStock(stock)
    elif exchange_market == "TSE":
        return AlphavantageAPIStock(stock)
