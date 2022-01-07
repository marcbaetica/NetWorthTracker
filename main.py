from apis.stock_api_factory import stock_api_factory
from lib.calculations import convert_usd_to_cad


SYMBOL = "TSLA"
EXCHANGE_MARKET = "NASDAQ"

stock_price = stock_api_factory(SYMBOL, EXCHANGE_MARKET).stock_price
print(stock_price)

SYMBOL = "VFV.TO"
EXCHANGE_MARKET = "TSE"

stock_price = stock_api_factory(SYMBOL, EXCHANGE_MARKET).stock_price
print(stock_price)

print(convert_usd_to_cad(1000))
