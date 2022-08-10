##############
# Solution 1 #
##############

def rotate_array_1(arr, k, right = True):
    n = len(arr)
    right %= n

    # going right for K places is same like going left for N-K places
    if right:
        k = n - k

    # the shortest way to swap 2 parts of the array
    return arr[k:] + arr[:k]


##############
# Solution 2 #
##############

def rotate_array_2(arr, k, right = True):
    n = len(arr)
    right %= n

    # going right for K places is same like going left for N-K places
    if not right:
        k = n - k

    # different sets
    sets = gcd(n, k)
    # elements in each set
    elements = n // sets
    i = 0

    while i < sets:
        j = 1
        curr = arr[i]

        while j <= elements:
            idx = (i + j * k) % n
            j += 1

            # add the previous element on this position
            curr, arr[idx] = arr[idx], curr
            '''same as
            temp = curr
            curr = arr[idx]
            arr[idx] = temp
            '''

        i += 1

    return arr

# greatest common divisor
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)