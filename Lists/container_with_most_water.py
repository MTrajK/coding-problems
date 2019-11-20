'''
Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

=========================================
Playing with pointers from both sides, eliminate smaller heights and search for a bigger height.
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def max_area(height):
    l = 0
    r = len(height) - 1
    max_height = 0

    while l < r:
        left = height[l]
        right = height[r]

        current_height = min(left, right) * (r - l)
        max_height = max(max_height, current_height)

        # take the smaller side and search for a bigger height on that side
        if left < right:
            while (l < r) and (left >= height[l]):
                l += 1
        else:
            while (l < r) and (right >= height[r]):
                r -= 1

    return max_height


###########
# Testing #
###########

# Test 1
# Correct result => 49
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))