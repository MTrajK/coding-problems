def reverse_ascending_sublists(arr):
    n = len(arr)
    if n == 0:
        return []

    start = 0

    for i in range(1, n):
        # check if this the end of the strictly ascending sublist
        if arr[i] < arr[i - 1]:
            reverse_arr(arr, start, i - 1)
            # a new sublist starts
            start = i

    reverse_arr(arr, start, n - 1)

    return arr

def reverse_arr(arr, start, end):
    while start < end:
        # reverse the array from the start index to the end index by
        # swaping each element with the pair from the other part of the array
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr