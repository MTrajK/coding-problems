def find_subarray(arr, k):
    n = len(arr)

    if n == 0:
        return -1

    start = 0
    end = 0
    current_sum = arr[0]

    while end < n:
        if current_sum == k:
            return (start + 1, end + 1)

        if current_sum < k:
            end += 1
            current_sum += arr[end]
        else:
            current_sum -= arr[start]
            start += 1

    return -1