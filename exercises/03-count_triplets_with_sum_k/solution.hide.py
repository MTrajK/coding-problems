##############
# Solution 1 #
##############

def count_triplets_1(arr, k):
    count = 0
    n = len(arr)

    for i in range(n - 2):
        elements = set()
        curr_sum = k - arr[i]

        for j in range(i + 1, n):
            if (curr_sum - arr[j]) in elements:
                count += 1
            elements.add(arr[j])

    return count


##############
# Solution 2 #
##############

def count_triplets_2(arr, k):
    count = 0
    n = len(arr)

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            curr_sum = arr[i] + arr[left] + arr[right]
            if curr_sum == k:
                count += 1
                right -= 1
            elif curr_sum < k:
                left += 1
            else:
                right -= 1

    return count





