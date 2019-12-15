'''
Remove Duplicates from Sorted Linked List

Given a sorted linked list nums, remove the duplicates in-place such that each element appear only once and return the modified linked list.
Do not allocate extra space for another linked list, you must do this by modifying the input linked list in-place with O(1) extra memory.

Input: 1 -> 1 -> 2
Output: 1 -> 2

Input: 0 -> 0 -> 1 -> 1 -> 1 -> 2 -> 2 -> 3 -> 3 -> 4
Output: 0 -> 1 -> 2 -> 3 -> 4

=========================================
Iterate the linked list and jump the neighbouring duplicates (change the next pointer).
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

# import ListNode class from ll_helpers.py
from ll_helpers import ListNode

def remove_duplicates(nums):
    if nums is None:
        return nums
    pointer = nums

    while pointer.next is not None:
        if pointer.val == pointer.next.val:
            # skip the next value because it's a duplicate
            pointer.next = pointer.next.next
        else:
            # search next
            pointer = pointer.next

    return nums


###########
# Testing #
###########

# import build_ll and print_ll methods from ll_helpers.py
from ll_helpers import build_ll, print_ll

# Test 1
# Correct result => 1 -> 2
print_ll(remove_duplicates(build_ll([1, 1, 2])))

# Test 2
# Correct result => 0 -> 1 -> 2 -> 3 -> 4
print_ll(remove_duplicates(build_ll([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])))