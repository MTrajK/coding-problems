'''
Check if Two Rectangles Overlap

Given two rectangles, find if the given two rectangles overlap or not.
Note that a rectangle can be represented by two coordinates, top left and bottom right.
So mainly we are given following four coordinates (min X and Y and max X and Y).
    - l1: Bottom Left coordinate of first rectangle. (mins)
    - r1: Top Right coordinate of first rectangle. (maxs)
    - l2: Bottom Left coordinate of second rectangle. (mins)
    - r2: Top Right coordinate of second rectangle. (maxs)
It may be assumed that the rectangles are PARALLEL to the coordinate axis.

Input: (0, 0), (3, 2), (1, 1), (5, 4)
Output: True

=========================================
First check if rectangles are overlapping on X axis and
after that if they are overlapping on Y axis.
    Time Complexity:    O(1)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def check_if_two_rectangles_overlap(l1, r1, l2, r2):
    # first check by X coordinates, if rectangles can overlap on X axis
    # longer form (l1[0] < l2[0] and r1[0] < l2[0]) or (l1[0] > r2[0] and r1[0] > r2[0])
    # but we know that l1[0] is always smaller than r1[0]
    if (r1[0] < l2[0]) or (l1[0] > r2[0]):
        return False

    # now we know that the rectangles are overlapping on X axis
    # check if they are overlapping on Y axis
    # (use the same logic from previous)
    if (r1[1] < l2[1]) or (l1[1] > r2[1]):
        return False

    return True


###########
# Testing #
###########

# Test 1
# Correct result => True
print(check_if_two_rectangles_overlap((0, 0), (3, 2), (1, 1), (5, 4)))

# Test 2
# Correct result => True
print(check_if_two_rectangles_overlap((0, 0), (3, 2), (3, 2), (5, 4)))

# Test 3
# Correct result => True
print(check_if_two_rectangles_overlap((0, 0), (3, 2), (1, -1), (5, 4)))

# Test 4
# Correct result => False
print(check_if_two_rectangles_overlap((0, 0), (3, 2), (2, 3), (5, 4)))