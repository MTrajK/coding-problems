'''
Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.

Input: [4, 5, 6, 7, 0, 1, 2], 0
Output: 4

Input: [4, 5, 6, 7, 0, 1, 2], 3
Output: -1

=========================================
Use binary search twice, first time to find the pivot (index where the array is rotated)
and the second time to find the target.
    Time Complexity:    O(LogN)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def search_rotated_sorted_array(nums, target):
    n = len(nums)
    pivot = find_pivot(nums, 0, n) + 1
    if pivot > n:
        return -1

    if nums[0] <= target:
        return find_element(nums, 0, pivot - 1, target)
    return find_element(nums, pivot, n - 1, target)

def find_pivot(nums, left, right):
    while left < right - 1:
        mid = left + (right - left) // 2

        if nums[left] < nums[mid]:
            left = mid
        else:
            right = mid

    return left

def find_element(nums, left, right, target):
    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


###########
# Testing #
###########

# Test 1
# Correct result => 4
print(search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 0))