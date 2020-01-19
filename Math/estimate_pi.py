'''
Estimation of Pi

Write a program to compute the value of PI using a random number generator/method.


=========================================
To solve this problem we'll use the Monte Carlo simulation/method.
Generate N random points (0 <= X, Y <= 1) in the first quadrant.
Count all points that are inside the circle using the squared euclidean distance (between origin <0,0> and point <X,Y>).
The ratio between all points in the quarter circle and quarter square should be
approximately equal to the ratio between a quarter of the circle area and a quarter of the square area.
(more points = better estimation)
Equation: (((r^2)*PI)/4) / (((2*r)^2)/4) = circle_points / total_points
Solve the first part: (((r^2)*PI)/4) / (((2*r)^2)/4) = ((1^2)*PI) / ((2*1)^2) = (1*PI) / (2^2) = PI/4
Simple equation: PI / 4 = circle_points / total_points
Final form: PI = 4 * circle_points / total_points
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

from random import random

def estimate_pi(n):
    total_points = 0
    circle_points = 0

    for i in range(n):
        # generate N random points in the first quadrant
        x, y = random(), random()

        if x*x + y*y <= 1:
            # using squared euclidean distance find the distance from (0, 0) to (x, y)
            circle_points += 1
        total_points += 1

    # this formula is a short form of this: quarter_circle_area / quarter_square_area = circle_points / total_points
    return 4 * circle_points / total_points


###########
# Testing #
###########

# Test 1
# Correct result => Doesn't give a good estimation at all (often the integer part is wrong)
print(estimate_pi(10))

# Test 2
# Correct result => Gives a good estimation to the first decimal (3.1xxx)
print(estimate_pi(10000))

# Test 3
# Correct result => Gives a good estimation to the second decimal (3.14xxx)
print(estimate_pi(10000000))