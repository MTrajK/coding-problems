'''
Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from A to B?

=========================================
The solution is the least common multiple for more than 2 numbers (in this case all numbers from "start" to "end")
    Time Complexity:    O(N)    , N = start - end, GCD complexity is O(Log min(a, b))
    Space Complexity:   O(1)
'''


############
# Solution #
############

def smallest_multiple(start, end):
    result = 1

    for k in range(start, end + 1):
        result = lcm(max(result, k), min(result, k))

    return result

# least common multiple
def lcm(a, b):
    return a * b // gcd(a, b)

# Greatest common divisor (euclidian algorithm, fast algorithm)
# https://en.wikipedia.org/wiki/Euclidean_algorithm
# For more than 2 numbers: gcd(a, b, c) = gcd(a, gcd(b, c)) or gcd(gcd(a, b), c) or gcd(gcd(a, c), b)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

###########
# Testing #
###########

# Test 1
# Correct result => 2520
print(smallest_multiple(1, 10))

# Test 2
# Correct result => 232792560
print(smallest_multiple(1, 20))