'''
Secret Santa

Secret Santa is a game in which a group of friends or colleagues exchange Christmas presents anonymously,
each member of the group being assigned another member for whom to provide a small gift.
You're given a list of names, make a random pairs (each participant should have another name as pair).
Return an array with pairs represented as tuples.

Input: ['a', 'b', 'c']
Output: This is a nondeterministic algorithm, more solutions exists, here are 2 possible solutions:
    [('a', 'b'), ('b', 'c'), ('c', 'a')], [('a', 'c'), ('c', 'b'), ('b', 'a')]

=========================================
Shuffle the array (this algorithm is explained in shuffle_array.py) and pair the current element
with the next element (neighbouring).
    Time Complexity:    O(N)
    Space Complexity:   O(N)
'''


############
# Solution #
############

from random import randint

def secret_santa(names):
    # or use shuffle method from random module (from random import shuffle)
    shuffle_array(names)
    pairs = []

    n = len(names)
    prev = names[-1] # or names[n - 1]

    for curr in names:
        pairs.append((prev, curr))
        prev = curr

    return pairs

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
# Correct result => nondeterministic algorithm, many solutions exist
print(secret_santa(['a', 'b', 'c']))