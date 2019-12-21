'''
Find duplicates

Find all duplicates in an array where all elements are positive (>0)
and the biggest element in the array could be equal to the length of array.
Note: solve it in one iteration.

=========================================
Each value has its own position/index in the array,
mark the value on that position as negative when the element is found for the first time.
    Time Complexity:    O(N)
    Space Complexity:   O(D)    , array (in this case set) to save all duplicates
In the second solution 2 hashsets are used, one to check if already exists element like current and
the other has same functionality as the hashset in the first solution.
* This solution is for all kind of numbers
(not as the previous solution, only for positive numbers or smaller elements than the length of array).
    Time Complexity:    O(N)
    Space Complexity:   O(D)
'''


##############
# Solution 1 #
##############

def find_duplicates(arr):
    n = len(arr)
    duplicates = set()

    for i in range(n):
        idx = abs(arr[i]) - 1
        val = arr[idx]

        if val > 0:
            # mark element as found for the first time
            arr[idx] = -val
        else:
            # this element is a duplicate
            duplicates.add(idx + 1)

    return duplicates


##############
# Solution 2 #
##############

def find_duplicates_2(arr):
    n = len(arr)
    duplicates = set()
    elements = set()

    for i in range(n):
        if arr[i] in duplicates:
            # this element is already found as duplicate
            continue

        if arr[i] in elements:
            # a duplicate is found
            duplicates.add(arr[i])
            elements.remove(arr[i])
        else:
            # a new number
            elements.add(arr[i])

    return duplicates


###########
# Testing #
###########

# Test 1
# Correct result => [1]
print(find_duplicates([1, 1, 1, 1]))
print(find_duplicates_2([1, 1, 1, 1]))

# Test 2
# Correct result => [4, 2]
print(find_duplicates([4, 2, 4, 2, 1, 4]))
print(find_duplicates_2([4, 2, 4, 2, 1, 4]))