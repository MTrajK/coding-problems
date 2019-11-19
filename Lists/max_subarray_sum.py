'''
Maximum subarray sum 

The subarray must be contiguous

Sample input: [-2, -3, 4, -1, -2, 1, 5, -3]
Sample output: 7
Output explanation: [4, -1, -2, 1, 5]

=========================================
Need only one iteration, in each step add the current element to the current sum. 
When the sum is equal or less than 0, reset the sum to 0 and continue with adding. (we care only about the positive sums)
After each addition, check if the current sum is greater than the max sum. (Called Kadane's algorithm)
	Time Complexity: 	O(N)
	Space Complexity: 	O(1)
'''


############
# Solution #
############

def max_subarray_sum(a):
    # max_sum, max_start_idx, max_end_idx
    max_sum = (0, 0, 0)

    i = 0
    n = len(a)
    curr_sum = 0
    start_idx = 0

    while i < n:
        curr_sum += a[i]

        if curr_sum <= 0:
            # restart the current sum, we care only about positive sums
            start_idx = i + 1
            curr_sum = 0
        else:
            # check if this is the max sum
            if curr_sum > max_sum[0]:
                max_sum = (curr_sum, start_idx, i + 1)    

        i += 1

    return max_sum[0]


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