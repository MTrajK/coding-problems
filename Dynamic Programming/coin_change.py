'''
Coin Change

You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Input: coins = [1, 2, 5], amount = 11
Output: 3

Input: coins = [2], amount = 3
Output: -1

=========================================
Dynamic programming solution 1
    Time Complexity:    O(A*C)  , A = amount, C = coins
    Space Complexity:   O(A)
Dynamic programming solution 2 (don't need the whole array, just use modulo to iterate through the partial array)
    Time Complexity:    O(A*C)  , A = amount, C = coins
    Space Complexity:   O(maxCoin)
'''


##############
# Solution 1 #
##############

def coin_change_1(coins, amount):
    if amount == 0:
        return 0
    if len(coins) == 0:
        return -1

    max_value = amount + 1  # use this instead of math.inf
    dp = [max_value for i in range(max_value)]
    dp[0] = 0

    for i in range(1, max_value):
        for c in coins:
            if c <= i:
                # search on previous positions for min coins needed
                dp[i] = min(dp[i], dp[i - c] + 1)

    if (dp[amount] == max_value):
        return -1
    return dp[amount]


##############
# Solution 2 #
##############

def coin_change_2(coins, amount):
    if amount == 0:
        return 0
    if len(coins) == 0:
        return -1

    max_value = amount + 1
    max_coin = min(max_value, max(coins) + 1)
    dp = [max_value for i in range(max_coin)]
    dp[0] = 0

    for i in range(1, max_value):
        i_mod = i % max_coin
        dp[i_mod] = max_value # reset current position

        for c in coins:
            if c <= i:
                # search on previous positions for min coins needed
                dp[i_mod] = min(dp[i_mod], dp[(i - c) % max_coin] + 1)

    if (dp[amount % max_coin] == max_value):
        return -1
    return dp[amount % max_coin]


###########
# Testing #
###########

# Test 1
# Correct result => 3
coins = [1, 2, 5]
amount = 11
print(coin_change_1(coins, amount))
print(coin_change_2(coins, amount))

# Test 2
# Correct result => -1
coins = [2]
amount = 3
print(coin_change_1(coins, amount))
print(coin_change_2(coins, amount))
