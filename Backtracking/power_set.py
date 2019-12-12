'''
The Power Set

The power set of a set is the set of all its subsets.
Write a function that, given a set, generates its power set.

Input: [1, 2, 3]
Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
* You may also use a list or array to represent a set.

=========================================
Simple recursive combinations algorithm.
    Time Complexity:    O(Sum(C(I, N)))     , sum of all combinations between 0 and N = C(0, N) + C(1, N) + ... + C(N, N)
    Space Complexity:   O(Sum(C(I, N)))     , this is for the result array, if we print the number then the space complexity will be O(N) (because of the recursive stack)
'''


############
# Solution #
############

def power_set(arr):
    result = []
    combinations(result, arr, [], 0)
    return result

# result, arr and taken are the same references always
def combinations(result, arr, taken, pos):
    result.append([arr[i] for i in taken]) # create the current combination

    n = len(arr)
    if n == pos:
        return

    # start from the last position (don't need duplicates)
    for i in range(pos, n):
        taken.append(i)
        combinations(result, arr, taken, i + 1)
        del taken[-1] # return to the old state


###########
# Testing #
###########

# Test 1
# Correct result => [[], [1], [1, 2], [2]]
print(power_set([1, 2]))

# Test 2
# Correct result => [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
print(power_set([1, 2, 3]))