import yfinance as yf

def get_stock(ticker):
    stock = yf.Ticker(ticker)

def get_free_cash_flow(ticker):
    stock = get_stock(ticker)
    cashflow = stock.cashflow

    try:
        fcf_series = cashflow.loc["Free Cash Flow"]
        return fcf_series.iloc[0]
    except Exception:
        return None


def get_market_price(ticker):
    stock = get_stock(ticker)

    try:
        price = stock.history(period="1d")["Close"].iloc[-1]
        return price
    except Exception:
        return None
                              
