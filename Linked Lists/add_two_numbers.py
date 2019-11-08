'''
Add two numbers

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Output explanation: 342 + 465 = 807

=========================================
Iterate LL and add values on same position (just like adding real numbers).
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, n = None):
        self.val = x
        self.next = n

def add_two_numbers(l1, l2):
    start = ListNode(None)
    # use the same linked list as result so the Space complexity will be O(1)
    start.next = l1
    pointer = start
    transfer = 0

    while (l1 is not None) or (l2 is not None) or (transfer != 0):
        v1 = 0
        if l1 is not None:
            v1 = l1.val
            l1 = l1.next
        
        v2 = 0
        if l2 is not None:
            v2 = l2.val
            l2 = l2.next
            
        total = transfer + v1 + v2
        transfer = total // 10

        if l1 is None:
            # if the first list is shorter than the second, add new elements at the end
            pointer.next = ListNode(None)
        pointer = pointer.next
        pointer.val = total % 10
        
    return start.next


###########
# Testing #
###########

# Test 1
# Correct result => 7 -> 0 -> 8
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
res = add_two_numbers(l1, l2)
st = ''
while res != None:
    st += str(res.val) + ' '
    res = res.next
print(st)

# Test 2
# Correct result => 8 -> 9 -> 0 -> 0 -> 1 
l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
l2 = ListNode(9, ListNode(9))
res = add_two_numbers(l1, l2)
st = ''
while res != None:
    st += str(res.val) + ' '
    res = res.next
print(st)