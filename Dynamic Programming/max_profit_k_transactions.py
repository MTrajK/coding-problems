'''
Max Profit With K Transactions

You are given an array of integers representing the prices of a single stock on various days
(each index in the array represents a different day).
You are also given an integer k, which represents the number of transactions you are allowed to make.
One transaction consists of buying the stock on a given day and selling it on another, later day.
Write a function that returns the maximum profit that you can make buying and selling the stock,
given k transactions. Note that you can only hold 1 share of the stock at a time; in other words,
you cannot buy more than 1 share of the stock on any given day, and you cannot buy a share of the
stock if you are still holding another share.
In a day, you can first sell a share and buy another after that.

Input: [5, 11, 3, 50, 60, 90], 2
Output: 93
Output explanation: Buy 5, Sell 11; Buy 3, Sell 90

=========================================
Optimized dynamic programming solution.
For this solution you'll need only the current and previous rows.
The original (not optimized) DP formula is: MAX(dp[t][d-1], price[d] + MAX(dp[t-1][x] - price[x])),
but this is O(K * N^2) Time Complexity, and O(N * K) space complexity.
    Time Complexity:    O(N * К)
    Space Complexity:   O(N)
'''


############
# Solution #
############

import math

def max_profit_with_k_transactions(prices, k):
    days = len(prices)
    if days < 2:
        # not enough days for a transaction
        return 0

    # transaction = buy + sell (2 separate days)
    # in a day you can sell and after that buy a share
    # (according to this, can't exists more transactions than the number of the prices/days)
    k = min(k, days)
    # create space optimized dp matrix
    dp = [[0 for j in range(days)] for i in range(2)]

    for t in range(k):
        max_prev = -math.inf

        # compute which row is previous and which is the current one
        prev_idx = (t - 1) % 2
        curr_idx = t % 2

        # the values in dp table for these days will be same
        # just ignore them, don't update them (because those combinations were tried)
        past_days = t
        # only save the last one
        dp[curr_idx][past_days] = dp[prev_idx][past_days]

        for d in range(past_days + 1, days):
            # first try to buy with the current price
            max_prev = max(max_prev, dp[prev_idx][d - 1] - prices[d - 1])
            # after that try to sell with the current price
            dp[curr_idx][d] = max(dp[curr_idx][d - 1], max_prev + prices[d])

    # return the last value from the last transaction
    return dp[(k - 1) % 2][-1]


###########
# Testing #
###########

# Test 1
# Correct result => 9
print(max_profit_with_k_transactions([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))

# Test 2
# Correct result => 93
print(max_profit_with_k_transactions([5, 11, 3, 50, 60, 90], 2))