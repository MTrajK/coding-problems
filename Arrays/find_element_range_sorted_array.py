'''
Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.
If the target is not found in the array, return [-1, -1].

Input: [5, 7, 7, 8, 8, 10], 8
Output: [3, 4]

Input: [5, 7, 7, 8, 8, 10], 6
Output: [-1, -1]

=========================================
Use binary search twice to find the range.
    Time Complexity:    O(LogN)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def search_range(nums, target):
    left_idx = binary_search(nums, target, True)
    if (left_idx == len(nums)) or (nums[left_idx] != target):
        return [-1, -1]

    right_idx = binary_search(nums, target, False) - 1
    return [left_idx, right_idx]

def binary_search(nums, target, equal=True):
    left = 0
    right = len(nums)

    while left < right:
        mid = (left + right) // 2

        if (nums[mid] > target) or (equal and nums[mid] == target):
            right = mid
        else:
            left = mid + 1

    return left


###########
# Testing #
###########

# Test 1
# Correct result => [3, 4]
print(search_range([5, 7, 7, 8, 8, 10], 8))

# Test 2
# Correct result => [-1, -1]
print(search_range([5, 7, 7, 8, 8, 10], 6))