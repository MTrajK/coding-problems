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
Play with indicies and mark them, a marked index means that the number equals to that index exist in the array.
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def find_first_missing(a):
    n = len(a)
    
    # eliminate all zeros and all negative numbers
    for i in range(n):
        if a[i] < 1:
            a[i] = n + 1 # those elements aren't used later

    # find all numbers in the range and mark all numbers at those positions as negative numbers
    for i in range(len(a)):
        idx = abs(a[i]) - 1
        if idx >= n:
            continue
        val = a[idx]

        if val > 0:
            # mark element as found for the first time
            a[idx] = -val
    
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
print(find_first_missing(test))

# Test 2
# Correct result => 2
test = [3, 4, -1, 1]        # 2
print(find_first_missing(test))

# Test 3
# Correct result => 3
test = [1, 2, 0]            # 3
print(find_first_missing(test))

# Test 4
# Correct result => 4
test = [1, 2, 3]
print(find_first_missing(test))

# Test 5
# Correct result => 5
test = [-4, -1, -3, -1]
print(find_first_missing(test))

# Test 6
# Correct result => 6
test = [2, 1, 2, -1, 0, 20]
print(find_first_missing(test))

# Test 7
# Correct result => 7
test = [1, 2, 5, 5, 1, 2]
print(find_first_missing(test))