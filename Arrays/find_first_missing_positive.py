'''
Find first missing positive integer (>0)

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.
Note: you can modify the input array in-place.

Input: [3, 4, -1, 1]
Output: 2

Input: [1, 2, 0]
Output: 3

=========================================
Move all values to their positions (val position = val - 1), in the end find the first
position which doesn't have the needed value.
    Time Complexity:    O(N)    , maybe nested loops look like O(N^2) but that not true
    Space Complexity:   O(1)
Play with indicies and mark them (make it negative),
a marked index means that the number equals to that index exist in the array.
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


##############
# Solution 1 #
##############

def find_first_missing_1(a):
    n = len(a)

    for i in range(n):
        while (a[i] > 0) and (a[i] <= n):
            swap = a[i] - 1
            if a[i] == a[swap]:
                break

            # swap elements
            a[i], a[swap] = a[swap], a[i]

    for i in range(n):
        if a[i] - 1 != i:
            return i + 1

    return n + 1


##############
# Solution 2 #
##############

def find_first_missing_2(a):
    n = len(a)

    # eliminate all zeros and all negative numbers
    for i in range(n):
        if a[i] <= 0:
            a[i] = n + 1 # those values won't be used later

    # find all numbers in the range and mark all numbers at those positions as negative numbers
    for i in range(n):
        idx = abs(a[i]) - 1
        if idx >= n:
            continue

        # mark the element as found
        a[idx] = -abs(a[idx])

    # find the first non-negative position
    for i in range(n):
        if a[i] > 0:
            return i + 1

    return n + 1


###########
# Testing #
###########

# Test 1
# Correct result => 1
test = [-1, 2, 3]
print(find_first_missing_1(list(test))) # make a copy, the list will be changed inside the function
print(find_first_missing_2(list(test)))

# Test 2
# Correct result => 2
test = [3, 4, -1, 1]
print(find_first_missing_1(list(test)))
print(find_first_missing_2(list(test)))

# Test 3
# Correct result => 3
test = [1, 2, 0]
print(find_first_missing_1(list(test)))
print(find_first_missing_2(list(test)))

# Test 4
# Correct result => 4
test = [1, 2, 3]
print(find_first_missing_1(list(test)))
print(find_first_missing_2(list(test)))

# Test 5
# Correct result => 1
test = [-4, -1, -3, -1]
print(find_first_missing_1(list(test)))
print(find_first_missing_2(list(test)))

# Test 6
# Correct result => 3
test = [2, 1, 2, -1, 0, 20]
print(find_first_missing_1(list(test)))
print(find_first_missing_2(list(test)))

# Test 7
# Correct result => 3
test = [1, 2, 5, 5, 1, 2]
print(find_first_missing_1(list(test)))
print(find_first_missing_2(list(test)))

# Test 8
# Correct result => 4
test = [1, 2, 3, 5, 1, 2, 3, 3]
print(find_first_missing_1(list(test)))
print(find_first_missing_2(list(test)))