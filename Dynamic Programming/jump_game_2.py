'''
Jump Game 2

Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

Input: XXX
Output: XXX
Output explanation: XXX

=========================================
Classical 1D Dynamic Programming solution.
    Time Complexity:    O(N)    , maybe looks like O(N^2) but that's not possible
    Space Complexity:   O(N)
If you analyze the previous solution, you'll see that you don't need the whole DP array.
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


##############
# Solution 1 #
##############

def min_jumps_1(nums):
    n = len(nums)
    if n <= 1:
        return 0

    dp = [-1]*n
    dp[0] = 0

    for i in range(n):
        this_jump = i + nums[i]
        jumps = dp[i] + 1

        if this_jump >= n - 1:
            return jumps

        # starging from back, go reverse and
        # change all -1 values and break when first positive is found
        for j in range(this_jump, i, -1):
            if dp[j] != -1:
                break
            dp[j] = jumps


##############
# Solution 2 #
##############

def min_jumps_2(nums):
    n = len(nums)
    if n <= 1:
        return 0

    jumps = 0
    max_jump = 0
    new_max_jump = 0

    for i in range(n):
        if max_jump < i:
            max_jump = new_max_jump
            jumps += 1

        this_jump = i + nums[i]
        if this_jump >= n - 1:
            return jumps + 1

        new_max_jump = max(new_max_jump, this_jump)


###########
# Testing #
###########

# Test 1
# Correct result => 2
nums = [2, 3, 1, 1, 4]
print(min_jumps_1(nums))
print(min_jumps_2(nums))