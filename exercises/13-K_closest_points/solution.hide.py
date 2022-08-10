def find_k_closes_recursive(arr, pt, k):
    n = len(arr)
    if k > n:
        return arr
    if k < 1:
        return []

    kth_closest(arr, k - 1, 0, n - 1, pt)

    return arr[:k]

def kth_closest(arr, k, left, right, pt):
    pivot = pivoting(arr, left, right, pt)

    if pivot > k:
        kth_closest(arr, k, left, pivot - 1, pt)
    elif pivot < k:
        kth_closest(arr, k, pivot + 1, right, pt)

def pivoting(arr, left, right, pt):
    # Linear time complexity pivoting
    # takes the last element as pivot
    pivot_dist = sqr_dist(pt, arr[right])
    new_pivot = left

    # iterate the whole array (without the last element)
    # and put all elements closer than the pivot (last element) in the first K spots
    # with the new_pivot we're "counting" how many closer elements are there
    for j in range(left, right):
        if sqr_dist(pt, arr[j]) < pivot_dist:
            swap(arr, new_pivot, j)
            new_pivot += 1

    # swap the last (pivot) element with the new_pivot position
    swap(arr, new_pivot, right)

    # return the new pivot
    return new_pivot

def swap(arr, i, j):
    # swaps two elements in an array
    arr[i], arr[j] = arr[j], arr[i]

def sqr_dist(a, b):
    # no need from the square root
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


##############
# Solution 2 #
##############

def find_k_closes(arr, pt, k):
    n = len(arr)
    if k > n:
        return arr
    if k < 1:
        return []

    k -= 1
    left = 0
    right = n - 1

    while True:
        pivot = pivoting(arr, left, right, pt) # the same method from the previous solution

        if pivot > k:
            right = pivot - 1
        elif pivot < k:
            left = pivot + 1
        else:
            return arr[:k + 1]

    # not possible
    return None