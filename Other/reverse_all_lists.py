'''
Reverse All Lists

Return a list that contains the items in reverse, but so that whenever each item is
itself a list, its elements are also reversed. This reversal of sublists must keep going on all the way
down, no matter how deep the nesting of these lists,

Input: [1, [2, 3, 4, 'yeah'], 5]
Output: [5, ['yeah', 4, 3, 2], 1]

=========================================
This problem can be solved using queue, stack (or recursion). Use in place reversing and save all
inner lists for reversing later.
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

from collections import deque

def reverse_all_lists(arr):
    queue = deque()
    queue.append(arr)

    while queue:
        inner_arr = queue.popleft()

        # in place reverse
        reverse_arr(inner_arr)

        # take all inner lists and save them for later
        for item in inner_arr:
            if isinstance(item, list):
                queue.append(item)

    # the arr is already reversed
    return arr

def reverse_arr(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        # reverse the array from the start index to the end index by
        # swaping each element with the pair from the other part of the array
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr


###########
# Testing #
###########

# Test 1
# Correct result => [5, ['yeah', 4, 3, 2], 1]
print(reverse_all_lists([1, [2, 3, 4, 'yeah'], 5]))

# Test 2
# Correct result => [[[[['boo!'], 33], 17], 99], 42]
print(reverse_all_lists([42, [99, [17, [33, ['boo!']]]]]))