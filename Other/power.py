'''
Power

Implement pow (a^b , a**b) method

=========================================
Using divide and conquer approach.
    Time Complexity:    O(LogB)
    Space Complexity:   O(LogB)     , because of recursion calls stack
'''

############
# Solution #
############

def power(a, b):
    if b < 0:
        # negative power
        return 1 / power_recursive(a, -b)

    return power_recursive(a, b)

def power_recursive(a, b):
    if b == 0:
        return 1

    res = power_recursive(a, b // 2)
    res *= res

    if b % 2 == 1:
        res *= a

    return res


###########
# Testing #
###########

# Test 1
# Correct result => 1
print(power(2, 0))

# Test 2
# Correct result => 2
print(power(2, 1))

# Test 3
# Correct result => 4
print(power(2, 2))

# Test 4
# Correct result => 8
print(power(2, 3))

# Test 5
# Correct result => 16
print(power(2, 4))

# Test 6
# Correct result => 32
print(power(2, 5))

# Test 7
# Correct result => 1024
print(power(2, 10))

# Test 8
# Correct result => 0.5
print(power(2, -1))

# Test 9
# Correct result => 0.25
print(power(2, -2))

# Test 10
# Correct result => 0.125
print(power(2, -3))

# Test 11
# Correct result => 0.0625
print(power(2, -4))

# Test 12
# Correct result => -8
print(power(-2, 3))

# Test 13
# Correct result => 16
print(power(-2, 4))