'''
Random Sample

Given an array and length of the sample, find a random sample from that array.

Input: [1, 2, 3, 4], 2
Output: This is a nondeterministic algorithm, C(N, K) combinations exist.
    In this case 4! / (2! * (4 - 2)!) = 6. All combinations are a valid solution.
    [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]

=========================================
Simple solution in one pass, Reservoir sampling. Maybe the solution looks like the elements don't have an equal probability
to be chosen, but there is a proof that they have equal probability https://en.wikipedia.org/wiki/Reservoir_sampling
Btw this solution works when we don't know the total number of elements.
    Time Complexity:    O(N)
    Space Complexity:   O(K)
Another simple solution in one pass, the probability for each element to be choosen in the first choosing is K/N,
after that we're removing that element. In the second choosing the probability for each element is (K-1)/(N-1),
in the third is (K-2)/(N-2), etc... This solution could be proved using induction hypothesis.
    Time Complexity:    O(N)
    Space Complexity:   O(K)

Note: In Python there is already implemented sample method (in random module "from random import sample", sample(arr, k)).
Note 2: This problem can be solved using the shuffle method (shuffle_array.py), and choosing the first K element from the shuffled array.
Note 3: Don't use solutions which are iterating until K distinct elements/indices are chosen. For example:
    distinct = set()
    while(len(distinct) < k):
        distinct.insert(randint(0, n))
Why? Because if you try it with an array with 100 000 elements and K equal to 99 999, then the code inside the "while"
could be executed more than 1 million times, that's O(10*N). So this algorithm doesn't work good when K is close to N,
to many duplicates will be choosen, read about Birthday Problem (https://en.wikipedia.org/wiki/Birthday_problem).
'''


##############
# Solution 1 #
##############

from random import randint

def reservoir_sampling(arr, k):
    # fill the reservoir array
    sample = []
    for i in range(k):
        sample.append(arr[i])

    # replace elements with gradually decreasing probability
    n = len(arr)
    for i in range(k, n):
        # randint(a, b) generates a uniform integer from the inclusive range {a, ..., b} (a <= X <= b)
        j = randint(0, i)
        if j < k:
            sample[j] = arr[i]

    return sample


##############
# Solution 2 #
##############

from random import random

def probabilistic_sampling(arr, k):
    sample = []
    n = len(arr)

    for el in arr:
        # random() generates a uniform double in this range (0 <= X < 1)
        # (k / n) is the probability for this element to be choosen (0 <= X <= 1)
        if random() < (k / n):
            sample.append(el)
            k -= 1 # left elements to be choosen
        n -= 1 # left elements for choosing

    return sample


###########
# Testing #
###########

# Test 1
# Correct result => One of these: [1, 2], [1, 3], [1, 4], [2, 3], [2, 4]
arr = [1, 2, 3, 4]
k = 2
print(reservoir_sampling(arr, k))
print(probabilistic_sampling(arr, k))