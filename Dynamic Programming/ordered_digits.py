'''
Ordered Digits

We are given a number and we need to transform to a new number where all its digits are ordered in a non descending order.
We are allowed to increase or decrease a digit by 1, and each of those actions counts as one operation.
We are also allowed to over/underflow a number meaning from '9' we can change to '0' and also from '0' to '9', also costing only one operation.
One same digit can be changed multiple times.
Find the minimum number of operations we need to do do to create a new number with its ordered digits.

Input: 301
Output: 3
Output explanation: 301 -> 201 -> 101 -> 111, in this case 3 operations are required to get an ordered number.

Input: 901
Output: 1
Output explanation: 901 -> 001, in this case 1 operation is required to get an ordered number.

Input: 5982
Output: 4
Output explanation: 5982 -> 5981 -> 5980 -> 5989 -> 5999, in this case 4 operations are required to get an ordered number.

=========================================
Dynamic programming solution. For each position, calculate the cost of transformation to each possible digit (0-9).
And take the minimum value from the previous position (but smaller than the current digit).
    Time Complexity:    O(N)    , O(N*10) = O(N), N = number of digits
    Space Complexity:   O(N)    , same O(N*2) = O(N)
'''


############
# Solution #
############

def ordered_digits(number):
    n = len(number)
    dp = [[0 for j in range(10)] for i in range(2)]

    for i in range(n):
        min_prev = float('inf')
        for j in range(10):
            # find the min value from the previous digit and add it to the current value
            min_prev = min(min_prev, dp[(i - 1) % 2][j])
            # compute diff between the current digit and wanted digit
            diff = abs(j - int(number[i]))
            dp[i % 2][j] = min(diff, 10 - diff) + min_prev

    # min value from the last digit
    return min(dp[(n - 1) % 2])


###########
# Testing #
###########

# Test 1
# Correct result => 3
print(ordered_digits('301'))

# Test 2
# Correct result => 1
print(ordered_digits('901'))

# Test 3
# Correct result => 4
print(ordered_digits('5982'))