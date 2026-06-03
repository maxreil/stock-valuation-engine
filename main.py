from data.fetch_data import get_free_cash_flow, get_market_price
from models.dcf import dcf_valuation
from config import (
    GROWTH_RATE, 
    DISCOUNT_RATE,
    TERMINAL_GROWTH_RATE,
    FORECAST_YEARS
)
# connect main.py to data_layer

def main():
    # Step 1: Ask user for ticker
    ticker = input("Enter stock ticker: ").upper() # this is the user input

    print(f"\nFetching data for {ticker}...\n")

    # FREE CASH FLOW
    fcf = get_free_cash_flow(ticker) # Calling the data pipeline
    if fcf is None:
        print("Could not retrieve Free Cash Flow.")
        return

    # GET MARKET PRICE
    market_price = get_market_price(ticker)
    if market_price is None:
        print("Failed to retrieve market price.")
        return

    # DCF VALUATION
    intrinsic_value = dcf_valuation(
        fcf,
        GROWTH_RATE,
        DISCOUNT_RATE,
        TERMINAL_GROWTH_RATE,
        FORECAST_YEARS
    )

    # UPSIDE/DOWNSIDE CALCULATION
    upside = (intrinsic_value - market_price) / market_price

    # COMPARING VALUE
    print("\n--- VALUATION RESULTS ---\N")
    
    print(f"Free Cash Flow: {fcf}")
    print(f"Intrinsic Value: {intrinsic_value}")
    print(f"Market Price: {market_price}")
    print(f"Upside/Downside: {upside:.2%}\n")

    # INTERPRETATION
    if upside > 0.2:
        print("Verdict: Significantly Undervalued")
    elif upside > 0.05:
        print("Verdict: Slightly Undervalued")
    elif upside > -0.05:
        print("Verdict: Fairly Valued")
    else:
        print("Verdict: Overvalued")


if __name__ == "__main__":
    main()
