'''
Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Input: 1 -> 2 -> 3 -> 4 -> 5, 2.
Output: 1 -> 2 -> 3 -> 5

=========================================
Playing with the pointers.
    Time Complexity:    O(N)
    Space Complexity:   O(1)
Recursive solution.
    Time Complexity:    O(N)
    Space Complexity:   O(N)  , because of the recursive calls stack
'''


##############
# Solution 1 #
##############

# import ListNode class from ll_helpers.py
from ll_helpers import ListNode

def remove_nth_from_end_1(head, n):
    helper = ListNode(0)
    helper.next = head

    first = helper
    second = helper

    # count to N with the first pointer
    for i in range(n + 1):
        first = first.next

    # go (Length - N) elements with first pointer
    # and in that way the second pointer will be Nth from the end
    while first != None:
        first = first.next
        second = second.next

    # remove the element (change the next pointer from the previous element)
    second.next = second.next.next

    return helper.next


##############
# Solution 2 #
##############

def remove_nth_from_end_2(head, n):
    result = remove_recursively(head, n)
    if result[0] == n:
        return head.next
    return head

def remove_recursively(pointer, n):
    if pointer is None:
        return (0, None)

    # go to the end and count how many are there
    result = remove_recursively(pointer.next, n)

    if result[0] == n:
        pointer.next = result[1]

    return (result[0] + 1, pointer.next)