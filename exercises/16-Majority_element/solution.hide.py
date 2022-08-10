def majority_element_1(nums):
    nums.sort()
    return nums[len(nums) // 2]