'''
Perfect Rectangle

Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.
Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2].
(coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).

Input: [
        [1, 1, 3, 3],
        [3, 1, 4, 2],
        [3, 2, 4, 4],
        [1, 3, 2, 4],
        [2, 3, 3, 4]
    ]
Output: True
Output explanation: All 5 rectangles together form an exact cover of a rectangular region.

Input: [
        [1, 1, 2, 3],
        [1, 3, 2, 4],
        [3, 1, 4, 2],
        [3, 2, 4, 4]
    ]
Output: False
Output explanation: Because there is a gap between the two rectangular regions.

Input: [
        [1, 1, 3, 3],
        [3, 1, 4, 2],
        [1, 3, 2, 4],
        [3, 2, 4, 4]
    ]
Output: False
Output explanation: Because there is a gap in the top center.

Input: [
        [1, 1, 3, 3],
        [3, 1, 4, 2],
        [1, 3, 2, 4],
        [2, 2, 4, 4]
    ]
Output: False
Output explanation: Because two of the rectangles overlap with each other.

=========================================
Check if 4 unique points exist. If 4 unique points exist, then
check if the sum of all rectangles is equal to the final rectangle.
    Time Complexity:    O(N)
    Space Complexity:   O(N)
'''


############
# Solution #
############

import math

def is_perfect_rectangle(rectangles):
    areas_sum = 0
    all_points = set()

    for rect in rectangles:
        # sum the areas of all rectangles
        areas_sum += (rect[2] - rect[0]) * (rect[3] - rect[1])

        # find all points of the rectangle and check if they already exist
        rect_points = [
            (rect[0], rect[1]),   # left bottom
            (rect[0], rect[3]),   # left top
            (rect[2], rect[3]),   # right top
            (rect[2], rect[1])    # right bottom
        ]

        for point in rect_points:
            if point in all_points:
                all_points.remove(point)
            else:
                all_points.add(point)

    # if we want a perfect rectangle then the rectangle must have 4 unique points
    if len(all_points) != 4:
        return False

    # find the bounding rectangle coordinates (minX, minY, maxX, maxY)
    bounding_rectangle = [math.inf, math.inf, -math.inf, -math.inf]
    for point in all_points:
        bounding_rectangle = [
            min(bounding_rectangle[0], point[0]),
            min(bounding_rectangle[1], point[1]),
            max(bounding_rectangle[2], point[0]),
            max(bounding_rectangle[3], point[1])
        ]

    # calculate the area of bounding rectangle
    bounding_rectangle_area = (bounding_rectangle[2] - bounding_rectangle[0]) * (bounding_rectangle[3] - bounding_rectangle[1])

    # to see if there are overlapping, compare the sum of areas with the final rectangle area
    return areas_sum == bounding_rectangle_area


###########
# Testing #
###########

# Test 1
# Correct result => True
rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
print(is_perfect_rectangle(rectangles))

# Test 2
# Correct result => False
rectangles = [[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]]
print(is_perfect_rectangle(rectangles))

# Test 3
# Correct result => False
rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [3, 2, 4, 4]]
print(is_perfect_rectangle(rectangles))

# Test 4
# Correct result => False
rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [2, 2, 4, 4]]
print(is_perfect_rectangle(rectangles))