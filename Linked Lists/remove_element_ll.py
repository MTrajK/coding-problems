'''
Remove Element

Given a linked list nums and a value val, remove all instances of that value in-place and return the new linked list.
Do not allocate extra space for another linked list, you must do this by modifying the input linked list in-place with O(1) extra memory.

Input: 3 -> 2 -> 2 -> 3
Output: 2 -> 2

Input: 0 -> 1 -> 2 -> 2 -> 3 -> 0 -> 4 -> 2
Output: 0 -> 1 -> 3 -> 0 -> 4

=========================================
Iterate the linked list and jump the values that needs to be deleted (change the next pointer). 
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

class ListNode:
    def __init__(self, x, n=None):
        self.val = x
        self.next = n

def remove_element(nums, val):
    res = ListNode(0)
    res.next = nums
    pointer = res

    while pointer.next is not None:
        if pointer.next.val == val:
            # skip the next value because it's value that needs to be deleted
            pointer.next = pointer.next.next
        else:
            # search next
            pointer = pointer.next

    return res.next


###########
# Testing #
###########

# Test 1
# Correct result => 2 -> 2
ll = ListNode(3, ListNode(2, ListNode(2, ListNode(3))))
res = remove_element(ll, 3)
while res is not None:
    print(res.val)
    res = res.next

# Test 2
# Correct result => 0 -> 1 -> 3 -> 0 -> 4
ll = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(0, ListNode(4, ListNode(2)))))))
res = remove_element(ll, 2)
while res is not None:
    print(res.val)
    res = res.next