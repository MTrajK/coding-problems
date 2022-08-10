############
# Solution #
############

def get_minimum_X(arr, k):
    n = len(arr)

    if n == 0 or k > n:
        return -1

    if k == n:
        return 1

    arr.sort()

    if k == 0:
        return arr[-1] + 1

    if arr[-k] == arr[-(k + 1)]:
        return -1

    return arr[-(k + 1)] + 1


print(get_minimum_X([3, 8, 5, 1, 10, 3, 20, 24], 2))