'''
Transform Number Ascending Digits

Given a number and we need to transform to a new number where all its digits are ordered in a non descending order.
All digits can be increased, decreased, over/underflow are allowed.
Find the minimum number of operations we need to do to create a new number with its ordered digits.

Input: '5982'
Output: 4
Output explanation: 5999, 1 operation to transform 8 to 9, 3 operations to transform 2 to 9.

=========================================
Dynamic programming solution.
    Time Complexity:    O(N)    , O(N * 10 * 10) = O(100 N) = O(N)
    Space Complexity:   O(1)    , O(10 * 10) = O(100) = O(1)
'''


############
# Solution #
############

def operations(number):
    n = len(number)
    diff = lambda i, j: abs(j - int(number[i]))
    # compute diff between the current digit and wanted digit, and fill the dp
    prev_dp = [min(diff(0, i), 10 - diff(0, i)) for i in range(10)]

    # go through all digits and see all possible combinations using dynamic programming
    for i in range(1, n):
        curr_dp = [min(diff(i, j), 10 - diff(i, j)) for j in range(10)]
        for j in range(10):
            # find the min value for the previous digit and add it to the current value
            curr_dp[j] += min(prev_dp[0 : j + 1])
        prev_dp = curr_dp

    # min value from the last digit
    min_dist = min(prev_dp)

    return min_dist


###########
# Testing #
###########

# Test 1
# Correct result => 1
print(operations('901'))

# Test 2
# Correct result => 3
print(operations('301'))

# Test 3
# Correct result => 4
print(operations('5982'))