'''
Reverse Integer

Given signed integer, reverse digits of an integer.

Input: 123
Output: 321

Input: -123
Output: -321

Input: 120
Output: 21

=========================================
Simple solution, mod 10 to find all digits.
    Time Complexity:    O(N)    , N = number of digits
    Space Complexity:   O(1)
'''


############
# Solution #
############

def reverse_integer(x):
    if x == 0:
        return 0

    sign = x // abs(x)  # find the sign, -1 or 1
    x *= sign  # make positive x, or x = abs(x)

    res = 0
    while x > 0:
        res = (res * 10) + (x % 10)
        x //= 10

    return res * sign


###########
# Testing #
###########

# Test 1
# Correct result => 321
print(reverse_integer(123))

# Test 2
# Correct result => -321
print(reverse_integer(-123))

# Test 3
# Correct result => 21
print(reverse_integer(120))