'''
Reverse a linked list

Reverse a linked list in one iteration without using additional space.

Input: 1 -> 2 -> 3 -> 4
Output: 4 -> 3 -> 2 -> 1

=========================================
Iterate LL and change the pointer of the current nodes to point to the previous nodes.
    Time Complexity:    O(N)
    Space Complexity:   O(1)
Solution 2: Same approach using recursion.
    Time Complexity:    O(N)
    Space Complexity:   O(N)        , because of the recursion stack (the stack will be with N depth till the last node of the linked list is reached)

'''


############
# Solution #
############

class ListNode:
    def __init__(self, v, n=None):
        self.val = v
        self.next = n

def reverse_ll(ll):
    prev_node = None

    while ll is not None:
        # save the current node
        current = ll
        # go to the next node
        ll = ll.next

        # change the pointer of the current node to point to the previous node
        current.next = prev_node
        # save the current node for the next iteration
        prev_node = current

    return prev_node

##############
# Solution 2 #
##############

def reverse_ll_2(ll):
    return reverse(ll, None)

def reverse(node, prev_node):
    if node is None:
        # the end of the ll is reached, return the previous node
        # that'll be the first node in the reversed ll
        return prev_node

    # send node.next as current node and node as previous node in the next step
    result = reverse(node.next, node)
    # change the pointer of the current node to point to the previous node
    node.next = prev_node

    return result


###########
# Testing #
###########

# Test 1
# Correct result => 4 -> 3 -> 2 -> 1
ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
res = reverse_ll(ll)
while res is not None:
    print(res.val)
    res = res.next

# Test 2
# Correct result => 4 -> 3 -> 2 -> 1
ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
res = reverse_ll_2(ll)
while res is not None:
    print(res.val)
    res = res.next