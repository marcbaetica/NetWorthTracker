import sys
from apis.freecurrencyAPIExchange import FreecurrencyAPIExchange
from apis.stock_api_factory import stock_api_factory


def convert_usd_to_cad(value):
    try:
        usd_to_cad_rate = FreecurrencyAPIExchange().current_exchange_rate_usd_to('CAD')
    except ValueError as e:
        print(e)
        sys.exit(1)
    return round(value * usd_to_cad_rate, 2)


def calculate_stock_investment_value(stock):
    current_value = stock_api_factory(stock['SYMBOL'], stock['EXCHANGE_MARKET']).stock_price
    investment_value = round(stock['SHARES_OWNED'] * current_value, 2)
    if stock['EXCHANGE_MARKET'] == 'NASDAQ':
        investment_value_cad = convert_usd_to_cad(investment_value)
        print(f'{stock["SYMBOL"]} value is currently US${current_value}. Total investment value is: US${investment_value}.'
              f' Converted to CAD at current conversion rate of {current_value} yields CA${investment_value_cad}.')
        return investment_value_cad
    else:
        print(f'{stock["SYMBOL"]} value is currently CA${current_value}. Total investment value is: CA${investment_value}.')
        return round(investment_value, 2)


def calculate_stock_investments_value(assets):
    print(f'Calculating stocks investment:')
    stock_investments = 0
    for stock in assets['stocks']:
        stock_investments += calculate_stock_investment_value(stock)
    stock_investments = round(stock_investments, 2)
    return round(stock_investments, 2)


def calculate_portofolio_cash(assets):
    print('Calculating unused portofolio cash:')
    unused_investment_cash = 0
    for account_cash in assets['investment_account_unused_cash_balance']:
        if account_cash['type'] == 'usd':
            unused_investment_cash += convert_usd_to_cad(account_cash['amount'])
        else:
            unused_investment_cash += convert_usd_to_cad(account_cash['amount'])
    print(f'Found unused CA${unused_investment_cash} cash in the broker investment account(s).')
    emergency_fund = assets['emergency_fund']
    print(f'Found CA${emergency_fund} stored as emergency fund.')
    debit_account = assets['debit_account']
    print(f'Found CA${debit_account} in debit account.')
    cash = assets['cash']
    print(f'Found CA${cash} as cash.')
    return round(unused_investment_cash + emergency_fund + debit_account + cash, 2)


def calculate_physical_assets_value(assets):
    print('Calculating physical assets value:')
    physical_assets_value = 0
    for asset in assets['physical_assets']:
        print(f'Found asset {asset["type"]} worth CA${asset["estimated_value"]}.')
        physical_assets_value += asset['estimated_value']
    return round(physical_assets_value, 2)


def calculate_debt_liabilities(liabilities):
    print('Calculating physical assets value:')
    debt_liabilities = 0
    for debt in liabilities['debt']:
        if debt['remaining_principal'] > 0:
            print(f'Found debt liability on {debt["type"]} of CA${debt["remaining_principal"]}.')
            debt_liabilities += debt["remaining_principal"]
    return round(debt_liabilities, 2)
