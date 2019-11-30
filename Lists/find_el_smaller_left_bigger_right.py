'''
Find the element before which all the elements are smaller than it, and after which all are greater

Given an array, find an element before which all elements are smaller than it, and after which all are greater than it.
Return the index of the element if there is such an element, otherwise, return -1.

Input: [5, 1, 4, 3, 6, 8, 10, 7, 9]
Output: 4

=========================================
Traverse the array starting from left and find all max elements till that element.
Also traverse the array starting from right and find all min elements till that element.
In the end only compare mins and maxs with the curent element.
    Time Complexity:    O(N)
    Space Complexity:   O(N)
'''


############
# Solution #
############

import math

def find_element_smaller_left_bigger_right(arr):
    n = len(arr)
    left_maxs = [-math.inf]
    right_min = math.inf

    # find all mins from the front
    for i in range(n - 1):
        left_maxs.append(max(left_maxs[-1], arr[i]))

    for i in range(n - 1, -1, -1):
        # check if all left are smaller
        # and all right are bigger
        if (left_maxs[i] < arr[i]) and (right_min > arr[i]):
            return i

        # don't need a separate for loop for this as mins
        right_min = min(right_min, arr[i])

    return -1


###########
# Testing #
###########

# Test 1
# Correct result => 4
print(find_element_smaller_left_bigger_right([5, 1, 4, 3, 6, 8, 10, 7, 9]))

# Test 2
# Correct result => -1
print(find_element_smaller_left_bigger_right([5, 1, 4, 4]))