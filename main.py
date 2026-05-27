from data.fetch_data import get_stock_data
# connect main.py to data_layer

def main():
    # Step 1: Ask user for ticker
    ticker = input("Enter stock ticker: ").upper() # this is the user input

    print(f"\nFetching data for {ticker}...\n")

    # Step 2: Fetch stock data
    data = get_stock_data(ticker) # Calling the data pipeline

    # Step 3: Basic check
    if data:
        print("Data fetched successfully.\n")

        # Print what we received (for debugging/understanding)
        print("Available data:")
        print("Cashflow:", data["cashflow"] is not None)
        print("Financials:", data["financials"] is not None)
        print("Balance Sheet:", data["balance_sheet"] is not None)
        # This is verifiying the output
    else:
        print("Failed to fetch data.")


if __name__ == "__main__":
    main()
