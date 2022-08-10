from random import randint

def shuffle_array(arr):
    n = len(arr)

    for i in range(n):
        rand = randint(i, n - 1) # or randint(0, i) it's same
        arr[i], arr[rand] = arr[rand], arr[i] # swap elements

    # the original arr is already changed
    return arr