'''
Flatten an Arbitrarily Deep List

Given a list that can contain arbitrary lists as its elements, which in turn can contain arbitrary lists
as elements, and so on, create and return a new list that contains all the atomic (that is, anything
that is not a list) elements listed in a linear sequence without any nesting.

Input: [1, [2, 3, [4, 'bob', 6], [7]], [8, 9]]
Output: [1, 2, 3, 4, 'bob', 6, 7, 8, 9]

=========================================
Recursive solution, extend the result with each sublist.
    Time Complexity:    O(N)
    Space Complexity:   O(N)
'''


############
# Solution #
############

def flatten_deep_list(arr):
    if not isinstance(arr, list):
        return [arr]

    result = []
    for a in arr:
        result.extend(flatten_deep_list(a))

    return result


###########
# Testing #
###########

# Test 1
# Correct result => [1, 2, 3, 4, 'bob', 6, 7, 8, 9]
print(flatten_deep_list([1, [2, 3, [4, 'bob', 6], [7]], [8, 9]]))

# Test 2
# Correct result => [89, 85, 72, 84, 65, 88, 31, 64, 11, 60, 42, 57, 55, 16, 79, 34, 82, 94, 36, 89, 26, 39, 94, 47, 72, 30, 72, 3, 73, 18, 37, 51, 75, 83, 94, 57, 37, 10, 62, 62, 13]
print(flatten_deep_list([[], [[[[89, 85, 72, 84, 65], [[88, 31, 64, 11, 60, 42, 57, 55], 16, [79, 34, 82], [], 94, 36, [89, 26, 39, 94, 47, 72, 30], [72, 3, 73]], 18]], [[37, [51, 75, 83], 94, 57]], [37, 10, 62, 62], [[], 13]]]))

# Test 3
# Correct result => [ ]
print(flatten_deep_list([ [ [ [ [ [ ] ] ] ] ] ]))