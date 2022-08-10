def min_swaps(a):
    n = len(a)
    swaps = 0

    for i in range(n):
        # swap the elements till the right element isn't found
        while a[i] - 1 != i:
            swap = a[i] - 1
            # swap the elements
            a[swap], a[i] = a[i], a[swap]

            swaps += 1

    return swaps