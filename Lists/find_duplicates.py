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
'''


############
# Solution #
############

def find_duplicates(a):
    n = len(a)
    duplicates = set()

    for i in range(len(a)):
        idx = abs(a[i]) - 1
        val = a[idx]

        if val > 0:
            # mark element as found for the first time
            a[idx] = -val
        else:
            # this element is a duplicate
            duplicates.add(idx + 1)

    return duplicates


###########
# Testing #
###########

# Test 1
# Correct result => [1]
print(find_duplicates([1, 1, 1, 1]))

# Test 2
# Correct result => [4, 2]
print(find_duplicates([4, 2, 4, 2, 1, 4]))