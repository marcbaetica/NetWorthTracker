from apis.stock_api_factory import stock_api_factory
from lib.calculations import convert_usd_to_cad


stocks = [
    {'SYMBOL': 'TSLA', 'EXCHANGE_MARKET': 'NASDAQ'},
    {'SYMBOL': 'VFV.TO', 'EXCHANGE_MARKET': 'TSE'}
]

for stock in stocks:
    stock_price = stock_api_factory(stock['SYMBOL'], stock['EXCHANGE_MARKET']).stock_price
    print(stock_price)

print(convert_usd_to_cad(1000))
