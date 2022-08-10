def max_profit(prices):
    total = 0

    for i in range(1, len(prices)):
        total += max(0, prices[i] - prices[i - 1])

    return total