'''
Calculate Area of Polygon

Given ordered coordinates of a polygon with n vertices. Find area of the polygon.
Here ordered mean that the coordinates are given either in clockwise manner or anticlockwise from first vertex to last.

Input: [(0, 0), (3, 0), (3, 2), (0, 2)]
Output: 6.0
Output explanation: The polygon is a 3x2 rectangle parallel with the X axis. The area is 6 (3*2).

=========================================
Use Shoelace formula (https://en.wikipedia.org/wiki/Shoelace_formula).
abs( 1/2 ((X1Y2 + X2Y3 + ... + Xn-1Yn + XnY1) - (X2Y1 + X3Y2 + ... + XnYn-1 + X1Yn)) )
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def calculate_area_of_polygon(polygon):
    n = len(polygon)
    prev = polygon[-1]
    area = 0

    for curr in polygon:
        area += (prev[0] + curr[0]) * (prev[1] - curr[1])
        prev = curr

    return abs(area / 2) # return absolute value


###########
# Testing #
###########

# Test 1
# Correct result => 6.0
print(calculate_area_of_polygon([(0, 0), (3, 0), (3, 2), (0, 2)]))