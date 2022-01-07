from apis.stock_api_factory import stock_api_factory


SYMBOL = "TSLA"
EXCHANGE_MARKET = "NASDAQ"

stock_price = stock_api_factory(SYMBOL, EXCHANGE_MARKET).stock_price
# stock_price = stock_api_factory(SYMBOL, EXCHANGE_MARKET)
print(stock_price)
