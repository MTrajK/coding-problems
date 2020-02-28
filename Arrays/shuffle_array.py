'''
Shuffle an Array

Given an array (array elements could be of any type/kind),
write a program to generate in-place a random permutation of array elements.
This question is also asked as “shuffle a deck of cards” or “randomize a given array”.
Here shuffle means that every permutation of array element should equally likely.

Input: [1, 2, 3]
Output: This is a nondeterministic algorithm, N! solutions/permutations exist.
    In this case 3! = 6. All permutations are a valid solution.
    [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]

=========================================
Easy in-place solution, choose an random index/position from I (I is the current position) to N-1
(or choose from 0 to I, it's same), swap the element at random position with the element at I position.
Increase I and continue with the same algorithm.
This algorithm is called Fisher–Yates shuffle (https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle).
    Time Complexity:    O(N)
    Space Complexity:   O(1)

Note: In Python there is already implemented shuffle (in random module "from random import shuffle") method
which works in similar way. But it's easy to be implemented and I wanted to show how to implement it.
'''


############
# Solution #
############

from random import randint

def shuffle_array(arr):
    n = len(arr)

    for i in range(n):
        rand = randint(i, n - 1) # or randint(0, i) it's same
        arr[i], arr[rand] = arr[rand], arr[i] # swap elements

    # the original arr is already changed
    return arr

###########
# Testing #
###########

# Test 1
# Correct result => One of these: [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]
print(shuffle_array([1, 2, 3]))