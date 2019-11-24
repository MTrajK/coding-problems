'''
Find missing number in second array

Given 2 arrays, first array with N elements and second array with N-1 elements.
All elements from the first array exist in the second array, except one. Find the missing number.

Sample input:   [1, 2, 3, 4, 5], [1, 2, 3, 4]
Sample output:  5

Sample input:   [2131, 2122221, 64565, 33333333, 994188129, 865342234],
                [994188129, 2122221, 865342234, 2131, 64565]
Sample output:  33333333

=========================================
The simplest solution is to substract the sum of the second array from the sum of the first array:
missing_number = sum(arr1) - sum(arr2)
But what if we have milions of elements and all elements are with 8-9 digits values?
In this case we'll need to use modulo operation. Make two sums, the first one from MODULO of each element
and the second one from the DIVIDE of each element. In the end use these 2 sums to compute the missing number.
    Time Complexity:    O(N)
    Space Complexity:   O(1)
The second solution is XOR soulution, make XOR to each element from the both arrays (same as find_unpaired.py).
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


##############
# Solution 1 #
##############

def find_missing_number(arr1, arr2):
    n = len(arr2)
    mod = 10000	    # this can be every number, this should be true max_length * mod < max_integer
    sum_diff = 0
    mod_diff = 0
    i = 0

    while i < n:
        # this is in case if we have too big numbers and to big arrays
        sum_diff += arr1[i] % mod - arr2[i] % mod
        mod_diff += arr1[i] // mod - arr2[i] // mod
        i += 1

    # don't forget the last element from the first array!
    sum_diff += arr1[n] % mod
    mod_diff += arr1[n] // mod

    return mod * mod_diff + sum_diff


##############
# Solution 2 #
##############

def find_missing_number_2(arr1, arr2):
    n = len(arr2)
    missing = 0
    i = 0

    while i < n:
        missing ^= arr1[i] ^ arr2[i]
        i += 1

    # don't forget the last element from the first array!
    missing ^= arr1[n]

    return missing


###########
# Testing #
###########

# Test 1
# Correct result => 33333333
arr1 = [2131, 2122221, 64565, 33333333, 994188129, 865342234]
arr2 = [994188129, 2122221, 865342234, 2131, 64565]
print(find_missing_number(arr1, arr2))
print(find_missing_number_2(arr1, arr2))

# Test 2
# Correct result => 5
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4]
print(find_missing_number(arr1, arr2))
print(find_missing_number_2(arr1, arr2))