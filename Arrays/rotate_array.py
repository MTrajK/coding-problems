'''
Array rotation/shifting

Rotate array in right (or left) for K places.

Input: [1, 2, 3, 4, 5, 6], 1
Output: [6, 1, 2, 3, 4, 5]

Input: [1, 2, 3, 4, 5, 6], 3
Output: [4, 5, 6, 1, 2, 3]

=========================================
The first solution is a simple one, split the array in two parts and swap those parts.
    Time Complexity:    O(N)
    Space Complexity:   O(N)
For the second one we need to compute GCD, to decide how many different sets are there.
And after that shift all elements in that set for one position in right/left.
(elements in a set are not neighboring elements)
(A Juggling Algorithm, https://www.geeksforgeeks.org/array-rotation/)
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


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


###########
# Testing #
###########

# Test 1
# Correct result => [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 7
print(rotate_array_1(arr, k))
print(rotate_array_2(arr, k))

# Test 2
# Correct result => [6, 1, 2, 3, 4, 5]
arr = [1, 2, 3, 4, 5, 6]
k = 1
print(rotate_array_1(arr, k))
print(rotate_array_2(arr, k))

# Test 3
# Correct result => [4, 5, 6, 1, 2, 3]
arr = [1, 2, 3, 4, 5, 6]
k = 3
print(rotate_array_1(arr, k))
print(rotate_array_2(arr, k))