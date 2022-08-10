def find_kth_smallest_recursive(arr, k):
    n = len(arr)
    if k > n:
        return None
    if k < 1:
        return None
    return kth_smallest(arr, k - 1, 0, n - 1)

def kth_smallest(arr, k, left, right):
    pivot = pivoting(arr, left, right)

    if pivot > k:
        return kth_smallest(arr, k, left, pivot - 1)
    if pivot < k:
        return kth_smallest(arr, k, pivot + 1, right)

    return arr[pivot]

def pivoting(arr, left, right):
    # Linear time complexity pivoting
    # takes the last element as pivot
    pivot = right
    new_pivot = left

    # iterate the whole array (without the last element)
    # and put all elements smaller than the pivot (last element) in the first K spots
    # with the new_pivot we're "counting" how many smaller elements are there
    for j in range(left, right):
        if arr[j] < arr[pivot]:
            swap(arr, new_pivot, j)
            new_pivot += 1

    # swap the last (pivot) element with the new_pivot position
    swap(arr, new_pivot, pivot)

    # return the new pivot
    return new_pivot

def swap(arr, i, j):
    # swaps two elements in an array
    arr[i], arr[j] = arr[j], arr[i]