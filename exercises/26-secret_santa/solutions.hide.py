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