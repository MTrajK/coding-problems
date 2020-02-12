'''
Check if Point is Inside Polygon

Given a polygon (created by counterclockwise ordered points, more than 2 points) and a point "p", find if "p" lies inside the polygon or not.
The points lying on the border are considered inside.

Input: [(0, 0), (3, 0), (3, 2), (0, 2)], (1, 1)
Output: True
Output explanation: The polygon is a 3x2 rectangle parallel with the X axis.

=========================================
To check if a point is inside a polygon you'll need to draw a straight line (in any of the 4 directions: up, right, down, left),
and count the number of times the line intersects with polygon edges. If the number of intersections is odd then the point
is inside or lies on an edge of the polygon, otherwise the point is outside.
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def check_if_point_inside_polygon(polygon, p):
    n = len(polygon)
    prev = polygon[-1]
    is_inside = False   # or you can use counter and return (counter % 2) == 1

    for curr in polygon:
        if intersect(prev, curr, p):
            is_inside = not is_inside
        prev = curr

    return is_inside

def intersect(a, b, p):
    # Y coordinate of p should be between Y coordinates
    # the following check is a short form from (p[1] < max(a[1], b[1]) and p[1] >= min(a[1], b[1]))
    if (a[1] > p[1]) != (b[1] > p[1]):
        '''
        Equation of line:
        y = (x - x0) * ((y1 - y0) / (x1 - x0)) + y0
        This formula is computed using the gradients (slopes, changes in the coordinates).
        The following formula differs from the previous in that it finds X instead of Y (because Y is known).
        '''
        x_intersect = (p[1] - a[1]) * ((b[0] - a[0]) / (b[1] - a[1])) + a[0]

        # check if the point is on the left of the intersection (because in this case you're drawing a line to the right)
        return x_intersect <= p[1]
        '''
        There exists a more complicated solution. (just in case if you're trying to compare X coordinates and find an intersection)
        Compare X coordinates, if both line X coordinates are bigger than point X then there is an intersection.
        If both line X coordinates are bigger than point X then there is no intersection.
        Else compute the angle between point-lineA and point-lineB (using math.atan2),
        if the angle is smaller or equal than 180 (Pi) there is an interesection else there is no intersection.
        '''

    return False


###########
# Testing #
###########

# Test 1
# Correct result => True
print(check_if_point_inside_polygon([(0, 0), (3, 0), (3, 2), (0, 2)], (1, 1)))

# Test 2
# Correct result => True
print(check_if_point_inside_polygon([(0, 0), (3, 0), (3, 2), (0, 2)], (1, 0)))

# Test 3
# Correct result => True
print(check_if_point_inside_polygon([(0, 0), (3, 0), (3, 2), (0, 2)], (3, 1)))

# Test 3
# Correct result => True
print(check_if_point_inside_polygon([(0, 0), (3, 0), (3, 2), (0, 2)], (3, 0)))

# Test 3
# Correct result => False
print(check_if_point_inside_polygon([(0, 0), (3, 0), (3, 2), (0, 2)], (3, 3)))