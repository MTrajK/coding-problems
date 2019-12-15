'''
Longest Increasing Subarray

Find the longest increasing subarray (subarray is when all elements are neighboring in the original array).

Input: [10, 1, 3, 8, 2, 0, 5, 7, 12, 3]
Output: 4

=========================================
Only in one iteration, check if the current element is bigger than the previous and increase the counter if true.
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def longest_increasing_subarray(arr):
    n = len(arr)
    longest = 0
    current = 1
    i = 1

    while i < n:
        if arr[i] < arr[i - 1]:
            longest = max(longest, current)
            current = 1
        else:
            current += 1

        i += 1

    # check again for max, maybe the last element is a part of the longest subarray
    return max(longest, current)


###########
# Testing #
###########

# Test 1
# Correct result => 4
print(longest_increasing_subarray([10, 1, 3, 8, 2, 0, 5, 7, 12, 3]))