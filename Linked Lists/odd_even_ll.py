'''
Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.
The first node is considered odd, the second node even and so on ...

Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 3 -> 5 -> 2 -> 4

Input: 2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7
Output: 2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4

=========================================
Count the index of the node and add it to the odd or even linked list (without creating new nodes).
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

# import ListNode class from ll_helpers.py
from ll_helpers import ListNode

def odd_even_ll(head):
    odd = ListNode(None)
    oddPointer = odd

    even = ListNode(None)
    evenPointer = even

    i = 1
    while head is not None:
        if i % 2 == 1:
            oddPointer.next = head
            oddPointer = oddPointer.next
        else:
            evenPointer.next = head
            evenPointer = evenPointer.next

        head = head.next
        i += 1

    evenPointer.next = None
    oddPointer.next = even.next

    return odd.next


###########
# Testing #
###########

# import build_ll and print_ll methods from ll_helpers.py
from ll_helpers import build_ll, print_ll

# Test 1
# Correct result => 1 -> 3 -> 5 -> 2 -> 4
print_ll(odd_even_ll(build_ll([1, 2, 3, 4, 5])))

# Test 2
# Correct result => 2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4
print_ll(odd_even_ll(build_ll([2, 1, 3, 5, 6, 4, 7])))