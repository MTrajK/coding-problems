'''
The power set

The power set of a set is the set of all its subsets.
Write a function that, given a set, generates its power set.

Input: {1, 2, 3}
Output: {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
* You may also use a list or array to represent a set.

=========================================
Simple recursive combinations algorithm.
    Time Complexity:    O(Sum(C(I, N)))     , sum of all combinations between 0 and N = C(0, N) + C(1, N) + ... + C(N, N)
    Space Complexity:   O(Sum(C(I, N)))     , this is for the result array, if we print the number then the space complexity will be O(1)
'''


############
# Solution #
############

def power_set(arr):
    return combinations(arr, [], 0)

# arr and taken are the same pointer always
# the same arrays are used always
def combinations(arr, taken, pos):
    result = []
    result.append([arr[i] for i in taken]) # create the current combination

    if len(arr) == pos:
        return result

    n = len(arr)
    # start from the last position (don't need duplicates)
    for i in range(pos, n):
        taken.append(i)
        result += combinations(arr, taken, i + 1) # append the combinations
        del taken[-1] # return to the old state

    return result


###########
# Testing #
###########

# Test 1
# Correct result => [[], [1], [1, 2], [2]]
print(power_set([1, 2]))

# Test 2
# Correct result => [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
print(power_set([1, 2, 3]))