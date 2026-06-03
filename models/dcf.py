def dcf_valuation(fcf, growth_rate, discount_rate, terminal_growth_rate, years):
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

    # Project future cash flows
    for _ in range(years):
        current_fcf *= (1 + growth_rate)
        future_fcf.append(current_fcf)

    # TERMINAL VALUE
    terminal_value = (
        future_fcf[-1] * (1 + terminal_growth_rate)
    ) / (discount_rate - terminal_growth_rate)
    
    # Discount each future cash flow to present value
    discounted_fcf = [
        f / ((1 + discount_rate) ** i)
        for i, f in enumerate(future_fcf, start=1)
    ]

    # Discount terminal Value
    discounted_terminal = terminal_value / ((1 + discounted_rate) ** years)
    
    # TOTAL INSTRINSIC VALUE
    intrinsic_value = sum(discounted_fcf) + discounted_terminal
    
    return intrinsic_value
