def dcf_valuation(fcf, growth_rate, discount_rate, years):
    """
    Performs a simple Discounted Cash Flow (DCF) Valuation.

    Parameters:
    - fcf: current Free Cash Flow
    - growth_rate: expected annual growth rate
    - discount_rate: rate used to discount future cash flows
    - years: number of years to forecast

    Returns:
    - Intrinsic value based on projected cash flows
    """
    
    future_fcf = []
    current_fcf = fcf

    # Step 1: Project future cash flows
    for _ in range(years):
        current_fcf *= (1 + growth_rate)
        future_fcf.append(current_fcf)

    # Step 2: Discount each future cash flow to present value
    discounted_fcf = [
        f / ((1 + discount_rate) ** i)
        for i, f in enumerate(future_fcf, start=1)
    ]

    # Step 3: Sum all discounted cash flows
    intrinsic_value = sum(discounted_fcf)
    
    return discounted_fcf
