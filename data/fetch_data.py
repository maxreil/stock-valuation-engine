import yfinance as yf

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)

    return {
        "cashflow": stock.cashflow,
        "financials": stock.financials,
        "balance_sheet": stock.balance_sheet
    }
``
