'''
Ascending Linked List

Determine whether the sequence of items is ascending so that its each element is strictly larger
than (and not merely equal to) the element that precedes it. Return True if that is the case, and
return False otherwise.

Input: -5 -> 10 -> 99 -> 123456
Output: True

=========================================
Iterate node by node and compare the current value with the next value.
If the next node is smaller or equal return false.
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

# import ListNode class from ll_helpers.py
from ll_helpers import ListNode

def is_ascending_ll(ll):
    while ll.next != None:
        if ll.val >= ll.next.val:
            return False
        ll = ll.next

    return True


###########
# Testing #
###########

# import build_ll method from ll_helpers.py
from ll_helpers import build_ll

# Test 1
# Correct result => True
print(is_ascending_ll(build_ll([-5, 10, 99, 123456])))

# Test 2
# Correct result => False
print(is_ascending_ll(build_ll([2, 3, 3, 4, 5])))