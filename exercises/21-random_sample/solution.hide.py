
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