'''
Sum of non-adjacent numbers

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

Input: [2, 4, 6, 2, 5]
Output: 13
Output explanation: We pick 2, 6, and 5.

Input: [5, 1, 1, 5]
Output: 10
Output explanation: We pick 5 and 5.

=========================================
Dynamic programming solution, but don't need the whole DP array, only the last 3 sums (DPs) are needed.
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def sum_non_adjacent(arr):
    n = len(arr)
    # from the dp matrix you only need the last 3 sums
    sums = [0, 0, 0]

    # TODO: refactor these if-elses, those are to skip using of DP matrix
    if n == 0:
        return 0

    # if negative or zero, the sum will be 0
    sums[0] = max(arr[0], 0)

    if n == 1:
        return sums[0]

    sums[1] = arr[1]
    # if the second number is negative or zero, then jump it
    if sums[1] <= 0:
        sums[1] = sums[0]

    if n == 2:
        return max(sums[0], sums[1])

    sums[2] = arr[2]
    # if the third number is negative or zero, then jump it
    if sums[2] <= 0:
        sums[2] = max(sums[0], sums[1])
    else:
        sums[2] += sums[0]

    # THE SOLUTION
    for i in range(3, n):
        temp = 0

        if arr[i] > 0:
            # take this number, because it's positive and the sum will be bigger
            temp = max(sums[0], sums[1]) + arr[i]
        else:
            # don't take this number, because the sum will be same or smaller
            temp = max(sums)

        # remove the first sum
        sums = sums[1:] + [temp]

    # return the max sum
    return max(sums)


###########
# Testing #
###########

# Test 1
# Correct result => 13
print(sum_non_adjacent([2, 4, 6, 2, 5]))

# Test 2
# Correct result => 15
print(sum_non_adjacent([2, 4, 2, 6, 2, -3, -2, 0, -3, 5]))

# Test 3
# Correct result => 10
print(sum_non_adjacent([5, 1, 1, 5]))

# Test 4
# Correct result => 10
print(sum_non_adjacent([5, 1, -1, 1, 5]))