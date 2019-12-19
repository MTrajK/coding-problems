'''
Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Input: [2,3,1,1,4]
Output: True

Input: [3,2,1,0,4]
Output: False

=========================================
Just iterate the array and in each step save the farthest reachable position.
If the current position is smaller than the farthest position, then the end isn't reachable.
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def can_jump(nums):
    n = len(nums)
    if n == 0:
        return False

    last = 0
    for i in range(n):
        # if this field isn't reachable return False
        if last < i:
            return False

        max_jump = i + nums[i]
        last = max(last, max_jump)

        # if the jump is greater or equal to the last element return True
        if last >= n - 1:
            return True


###########
# Testing #
###########

# Test 1
# Correct result => True
print(can_jump([2,3,1,1,4]))

# Test 2
# Correct result => False
print(can_jump([3,2,1,0,4]))