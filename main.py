from data.fetch_data import get_stock_data
from models.dcf import dcf_valuation
from config import GROWTH_RATE, DISCOUNT_RATE, FORECAST_YEARS
# connect main.py to data_layer

def main():
    # Step 1: Ask user for ticker
    ticker = input("Enter stock ticker: ").upper() # this is the user input

    print(f"\nFetching data for {ticker}...\n")

    # Step 2: Get free cash flow
    fcf = get_free_cash_flow(ticker) # Calling the data pipeline

    if fcf is None:
        print("Could not retrieve Free Cash Flow.")
        return

    print(f"Free Cash Flow: {fcf}\n")

    # Step 3: Run DCF valuation
    intrinsic_value = dcf_valuation(
        fcf,
        GROWTH_RATE,
        DISCOUNT_RATE,
        FORECAST_YEARS
    )

    # Step 4: Output result
    print(f"Estimated Intrinsic Value: {intrinsic_value}")


if __name__ == "__main__":
    main()
