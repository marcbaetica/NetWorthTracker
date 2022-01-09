from lib.portofolio_parser import parse_portofolio_from_file
from lib.calculations import calculate_stock_investments_value, calculate_portofolio_cash, \
    calculate_physical_assets_value, calculate_debt_liabilities


FINANCIAL_PORTOFOLIO = 'financial_portofolio.json'

assets, liabilities, date = parse_portofolio_from_file(FINANCIAL_PORTOFOLIO)

stock_investments = calculate_stock_investments_value(assets)
print(f'Stock investments are currently worth CA${stock_investments}.\n')

portofolio_cash = calculate_portofolio_cash(assets)
print(f'Unused cash in portofolio is currently worth CA${portofolio_cash}.\n')

physical_assets_value = calculate_physical_assets_value(assets)
print(f'Total physical assets are currently worth CA${physical_assets_value}.\n')

assets_value = stock_investments + portofolio_cash + physical_assets_value

debt_liabilities = calculate_debt_liabilities(liabilities)
print(f'Total debt liabilities are currently totaling CA${physical_assets_value}.\n')

print("SUMMARY:")
print(f'Assets: CA${assets_value}')
print(f'Liabilities: CA${debt_liabilities}')
print(f'Current net worth as of [{date}]: CA${round(assets_value - debt_liabilities, 2)}')
