import sys
from apis.freecurrencyAPIExchange import FreecurrencyAPIExchange


def convert_usd_to_cad(value):
    try:
        usd_to_cad_rate = FreecurrencyAPIExchange().current_exchange_rate_usd_to('CAD')
    except ValueError as e:
        print(e)
        sys.exit(1)
    return round(value * usd_to_cad_rate, 2)
