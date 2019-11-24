'''
Find unpaired element

Given an array with odd number of elements, where (N - 1)/2 elements have duplicates and ONLY 1 is unique.

Input: [1, 5, 3, 1, 5]
Output: 3

=========================================
Using XOR find the unique element.
* Example: 13 XOR 13 = 1101 XOR 1101 = 0.
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def find_unpaired_element(arr):
    unique = 0

    for el in arr:
        unique ^= el

    return unique


###########
# Testing #
###########

# Test 1
# Correct result => 3
print(find_unpaired_element([1, 5, 3, 1, 5]))