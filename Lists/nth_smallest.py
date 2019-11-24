'''
N-th Smallest Number

Find the N-th smallest number in an unordered list.

Input: [6, 2, 4, 8, 10, 1, 11], 1
Output: 0

Input: [6, 2, 4, 8, 10, 0, 11], 2
Output: 2

Input: [6, 2, 4, 8, 10, 0, 11], 4
Output: 6

=========================================
This solution is based on the quick sort algorithm (pivoting, divide and conquer).
More precisly in-place quick sort (without using additional space).
   Time Complexity:     O(N)    , O(N + N/2 + N/4 + N/8 + ... + 1 = 2*N = N)
   Space Complexity:    O(LogN) , because of the recursion stack (if this doesn't count, then O(1))
'''


############
# Solution #
############

def find_nth_smallest(arr, n):
    size = len(arr)
    if n > size:
        return None
    if n < 1:
        return None
    return nth_smallest(arr, n - 1, 0, size - 1)

def nth_smallest(arr, n, left, right):
    pivot = pivoting(arr, left, right)

    if pivot > n:
        return nth_smallest(arr, n, left, pivot - 1)
    if pivot < n:
        return nth_smallest(arr, n, pivot + 1, right)

    return arr[pivot]

def pivoting(arr, left, right):
    # O(N) pivoting
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
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


###########
# Testing #
###########

# Test 1
# Correct result => 1 1 1 1 1 1
arr = [1, 1, 1, 1, 1, 1]
for i in range(1, len(arr) + 1):
    print(find_nth_smallest(arr, i))

# Test 2
# Correct result => 0 1 2 4 4 4 6 8 8 10 11 12
arr = [6, 4, 2, 12, 4, 8, 10, 1, 11, 0, 8, 4]
for i in range(1, len(arr) + 1):
    print(find_nth_smallest(arr, i))

# Test 3
# Correct result => 1 2 3 4 5
arr = [5, 4, 3, 2, 1]
for i in range(1, len(arr) + 1):
    print(find_nth_smallest(arr, i))