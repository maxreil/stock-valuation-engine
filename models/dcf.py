def dcf_valuation(fcf, growth_rate, discount_rate, years):
    future_fcf = []
    current_fcf = fcf

    for _ in range(years):
        current_fcf *= (1 + growth_rate)
        future_fcf.append(current_fcf)

    discounted_fcf = [
        f / ((1 + discount_rate) ** i)
        for i, f in enumerate(future_fcf, start=1)
    ]

    return sum(discounted_fcf)
