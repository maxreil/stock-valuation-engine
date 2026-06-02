import yfinance as yf

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)

    return {
        "cashflow": stock.cashflow,
        "financials": stock.financials,
        "balance_sheet": stock.balance_sheet
    }

def get_free_cash_flow(ticker):
    stock = yf.Ticker(ticker)
    cashflow = stock.cashflow

    try:
        fcf = cashflow.loc["Free Cash Flow"]
        latest_fcf = fcf.iloc[0]
        return latest_fcf

    except Exception as e:
        print(f"Error extracting FCF: {e}")
        return None
