'''
Maximum of All Subarrays of Size K

Given an array and an integer k, find the maximum for each and every contiguous subarray of size k.
O(n) time and O(k) space!

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)

=========================================
Sliding window solution using deque or linked lists
(only need to be able to remove from both sides and to add on both sides in constant time).
    Time Complexity:    O(N)
    Space Complexity:   O(K)
'''


############
# Solution #
############

from collections import deque

def max_el_subarrays(arr, k):
    n = len(arr)
    if n == 0:
        return -1

    deq = deque()
    result = []

    # starting sliding window
    for i in range(min(k, n)):
        # start from the end and remove all previous indicies
        # which have smaller values than the current one
        # using this logic, we're sure that there is no smaller element (in the previous added indicies, the whole deque) than the last added
        while (deq) and (arr[i] >= arr[deq[-1]]):
            deq.pop()
        # add the current index on back/right
        deq.append(i)

    # add the biggest element in the result array
    # the biggest element is always located in front/left
    result.append(arr[deq[0]])

    # move element by element (slide the window)
    for i in range(k, n):
        # remove the front index if it's outside the window
        if (deq) and (deq[0] == i - k):
            deq.popleft()

        # use the same logic as before, remove from back/right and add to front/left
        while (deq) and (arr[i] >= arr[deq[-1]]):
            deq.pop()

        deq.append(i)
        result.append(arr[deq[0]])

    return result