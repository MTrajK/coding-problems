def reverse_arr(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        # reverse the array from the start index to the end index by
        # swaping each element with the pair from the other part of the array
        swap(arr, start, end)
        start += 1
        end -= 1

    return arr

def swap(arr, i, j):
    # swapping two elements from a same array
    arr[i], arr[j] = arr[j], arr[i]
    '''same as
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    '''