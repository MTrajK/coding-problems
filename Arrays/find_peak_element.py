'''
Find Peak Element

A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.

Input: [1, 2, 3, 1]
Output: 2
Output explanation: 3 is a peak element and your function should return the index number 2.

Input: [1, 2, 1, 3, 5, 6, 4]
Output: 1 or 5
Output explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

=========================================
Binary search (more description in the code).
    Time Complexity:    O(LogN)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def find_peak_element(nums):
    l = 0
    r = len(nums) - 1

    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[mid + 1]:
            # go left if the current value is smaller than the next one
            # in this moment you're sure that there is a peak element left from this one
            r = mid
        else:
            # go right if the current value is smaller than the next one
            # if the l comes to the end and all elements were in ascending order, then the last one is peak (because nums[n] is negative infinity)
            l = mid + 1

    return l


###########
# Testing #
###########

# Test 1
# Correct result => 2
print(find_peak_element([1, 2, 3, 1]))

# Test 2
# Correct result => 1 or 5
print(find_peak_element([1, 2, 1, 3, 5, 6, 4]))