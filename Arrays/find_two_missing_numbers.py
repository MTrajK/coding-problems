'''
Find two missing numbers in a sequence

Find two missing numbers in a sequence,
all numbers are integers and they're smaller or equal to N+2 (N is length of the array).

Input: [2, 1, 4]
Output: [3, 5]

=========================================
Searching for 2 unknowns, math problem.
This solution is extension of 'find_one_missing_number.py'.
But in this case we also need the sum formula for the first squared N numbers (1^2 + 2^2 + ... + N^2).
And using those 2 formulas, we'll solve equations with 2 unknowns.
    a + b = diff_sum                     (diff_sum = formula_sum + list_sum)
    a^2 + b^2 = diff_squared_sum         (diff_squared_sum = formula_squared_sum + list_squared_sum)
But in the end we'll need quadratic formula to find those values.
b1,2 = (diff_sum +- sqrt(2*diff_squared_sum - diff_sum^2)) / 2
Sum formula = N*(N+1)/2
Squared sum formula = N*(N+1)*(2*N+1)/6
    Time Complexity:    O(N)
    Space Complexity:   O(1)

Note: this idea also could be used when more than 2 numbers are missing,
but you'll need more computations/equations, because you'll have K unknowns.
'''

############
# Solution #
############

import math

def missing_numbers(nums):
    # find sums from the array
    s = 0
    s_2 = 0
    for i in nums:
        s += i
        s_2 += i * i

    n = len(nums) + 2

    # using formulas, compute the sums of the sequence
    f_s = n * (n + 1) // 2
    f_s_2 = n * (n + 1) * (2 * n + 1) // 6

    # difference of sums
    d = f_s - s
    d_2 = f_s_2 - s_2

    # using quadratic formula find the values
    r = int(math.sqrt(2 * d_2 - d * d))

    a = (d - r) // 2
    b = (d + r) // 2

    return [a, b]


###########
# Testing #
###########

# Test 1
# Correct result => [4, 5]
print(missing_numbers([2, 3, 1]))

# Test 2
# Correct result => [1, 2]
print(missing_numbers([5, 3, 4]))

# Test 3
# Correct result => [1, 5]
print(missing_numbers([2, 3, 4]))