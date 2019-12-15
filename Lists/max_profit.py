'''
Max Profit (Best Time to Buy and Sell Stock)

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time
(i.e., you must sell the stock before you buy again).

Input: [7, 1, 5, 3, 6, 4]
Output: 7
Output explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
                    Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Input: [1, 2, 3, 4, 5]
Output: 4
Output explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
                    Or buy day 1 -> sell day 2, buy day 2 -> sell day 3, buy day 3 -> sell day 4, buy day 4 -> sell day 5.
                    Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
                    engaging multiple transactions at the same time. You must sell before buying again.

=========================================
Sum only the positive differences between neighbouring elements.
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def max_profit(prices):
    total = 0

    for i in range(1, len(prices)):
        total += max(0, prices[i] - prices[i - 1])

    return total


###########
# Testing #
###########

# Test 1
# Correct result => 7
print(max_profit([7, 1, 5, 3, 6, 4]))

# Test 2
# Correct result => 5
print(max_profit([1, 2, 3, 4, 5]))

# Test 3
# Correct result => 0
print(max_profit([7, 6, 4, 3, 1]))