'''
Intersecting linked lists

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
In this example, assume nodes with the same value are the exact same node objects.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

=========================================
Find the longer linked list and move the pointer (now both list will have same number of elements). 
After that move both pointers from the both lists and compare elements.
    Time Complexity:    O(N + M)
    Space Complexity:   O(1)
'''


############
# Solution #
############

class ListNode:
    def __init__(self, x, n = None):
        self.val = x
        self.next = n

def findIntersectingNode(ll1, ll2):
    # count how many nodes contains the first ll
    count1 = 0
    temp1 = ll1
    while (temp1 is not None):
        count1 += 1
        temp1 = temp1.next

    # count how many nodes contains the second ll
    count2 = 0
    temp2 = ll2
    while (temp2 is not None):
        count2 += 1
        temp2 = temp2.next
  
    # move only one of the lls for the difference
    m = min(count1, count2)

    for i in range(count1 - m):
        ll1 = ll1.next

    for i in range(count2 - m):
        ll2 = ll2.next

    # find the intersecting node
    intersect = None
    while ll1 is not None:
        # if the values are different, this is not the intersecting node
        if (ll1.val != ll2.val):
            intersect = None
        else:
            # if the values are equal and there is no an intersecting node from before
            # then this is the intersecting node
            if (intersect == None):
                intersect = ll1

        ll1 = ll1.next
        ll2 = ll2.next

    return intersect


###########
# Testing #
###########

# Test 1
# Correct result => 8
in1 = ListNode(3, ListNode(7, ListNode(8, ListNode(10))))
in2 = ListNode(1, ListNode(8, ListNode(10)))
print(findIntersectingNode(in1, in2).val)