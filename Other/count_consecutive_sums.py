'''
Count Consecutive Sums

Positive integers can be expressed as sums of consecutive positive integers in various ways.

Input: 42
Output: 4
Output explanation: (a) 3 + 4 + 5 + 6 + 7 + 8 + 9, (b) 9 + 10 + 11 + 12, (c) 13 + 14 + 15 and (d) 42

=========================================
Iterate all N elements and add each to the sum, but store the start element and if the current sum is
bigger than N substract the front elements.
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def count_consecutive_sums(n):
    start = 1
    curr_sum = count = 0

    for end in range(1, n + 1):
        curr_sum += end

        while curr_sum > n:
            # remove all numbers from the front
            curr_sum -= start
            start += 1

        if curr_sum == n:
            count += 1

    return count


###########
# Testing #
###########

# Test 1
# Correct result => 4
print(count_consecutive_sums(42))

# Test 2
# Correct result => 6
print(count_consecutive_sums(99))

# Test 3
# Correct result => 2
print(count_consecutive_sums(92))