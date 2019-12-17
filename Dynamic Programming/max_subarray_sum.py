'''
Maximum subarray sum

The subarray must be contiguous.

Sample input: [-2, -3, 4, -1, -2, 1, 5, -3]
Sample output: 7
Output explanation: [4, -1, -2, 1, 5]

=========================================
Need only one iteration, in each step add the current element to the current sum.
When the sum is less than 0, reset the sum to 0 and continue with adding. (we care only about non-negative sums)
After each addition, check if the current sum is greater than the max sum. (Called Kadane's algorithm)
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def max_subarray_sum(a):
    curr_sum = 0
    max_sum = 0

    for val in a:
        # extend the current sum with the curren value; 
        # reset it to 0 if it is smaller than 0, we care only about non-negative sums
        curr_sum = max(0, curr_sum + val)

        # check if this is the max sum
        max_sum = max(max_sum, curr_sum)

    return max_sum


###########
# Testing #
###########

# Test 1
# Correct result => 7
print(max_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3]))

# Test 2
# Correct result => 5
print(max_subarray_sum([1, -2, 2, -2, 3, -2, 4, -5]))

# Test 3
# Correct result => 7
print(max_subarray_sum([-2, -5, 6, -2, -3, 1, 5, -6]))

# Test 4
# Correct result => 0
print(max_subarray_sum([-6, -1]))