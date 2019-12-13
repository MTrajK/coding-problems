'''
Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

Input: [1, 1, 1, 2, 2, 3], 2
Output: [1, 2]

Input: [1], 1
Output: [1]

=========================================
Using Priority Queue, add each frequency and remove the last if there are more than K elements inside the Priority Queue.
    Time Complexity:    O(N LogK)
    Space Complexity:   O(N)
Using pivoting, this solution is based on the quick sort algorithm (divide and conquer). 
Same pivoting solution as the nth_smallest.py,
    Time Complexity:    O(N)
    Space Complexity:   O(N)
'''


##############
# Solution 1 #
##############

def top_k_frequent_1(nums, k):
    frequency = {}

    # count the frequency of each element
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    arr = [(frequency[el], el) for el in frequency]
    n = len(arr)

    if k > n:
        return [el[1] for el in arr]
    if k < 1:
        return []

    # TODO: Implement Priority Queue and solve it


##############
# Solution 2 #
##############

def top_k_frequent_2(nums, k):
    frequency = {}

    # count the frequency of each element
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    arr = [(frequency[el], el) for el in frequency]
    n = len(arr)

    if k > n:
        return [el[1] for el in arr]
    if k < 1:
        return []

    # pivoting, find the first k element with the biggest frequency, O(U), U = num of unique nums
    k -= 1
    left = 0
    right = n - 1

    while True:
        pivot = pivoting(arr, left, right)

        if pivot > k:
            right = pivot - 1
        elif pivot < k:
            left = pivot + 1
        else:
            return [el[1] for el in arr[:k + 1]]

    # not possible
    return None

def pivoting(arr, left, right):
    # O(N) pivoting
    # takes the last element as pivot
    pivot = right
    new_pivot = left

    # iterate the whole array (without the last element)
    # and put all elements bigger than the pivot (last element) in the first K spots
    # with the new_pivot we're "counting" how many bigger elements are there
    for j in range(left, right):
        if arr[j] > arr[pivot]:
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
# Correct result => [1, 2]
print(top_k_frequent_1([1, 1, 1, 2, 2, 3], 2))
print(top_k_frequent_2([1, 1, 1, 2, 2, 3], 2))

# Test 2
# Correct result => [1]
print(top_k_frequent_1([1], 1))
print(top_k_frequent_2([1], 1))