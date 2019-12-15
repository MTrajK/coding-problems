'''
Merge K Sorted Linked Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

=========================================
Using Priority Queue (heap) in each step chose the smallest element from the lists and add it to the result list.
    Time Complexity: 	O(N * LogK)  , LogK is for adding and deleting from Priority queue
    Space Complexity: 	O(N)
Using Divide and Conquer, similar to Merge sort.
    Time Complexity:    O(N * LogK)
    Space Complexity:   O(1)  , (using the same old list)
'''


##############
# Solution 1 #
##############

# import ListNode class from ll_helpers.py
from ll_helpers import ListNode

import heapq

# priority queue comparator class
class PQNode:
    def __init__(self, node):
        self.val = node.val
        self.node = node

    def __lt__(self, other):
        return self.val < other.val

# priority queue
class PriorityQueue:
    def __init__(self):
        self.data = []

    def push(self, node):
        heapq.heappush(self.data, PQNode(node))

    def pop(self):
        return heapq.heappop(self.data).node

    def is_empty(self):
        return len(self.data) == 0

def merge_k_lists_1(lists):
    heap = PriorityQueue()

    # add all linked lists in the heap
    for node in lists:
        if node is not None:
            heap.push(node)

    result = ListNode(-1)
    pointer = result

    while not heap.is_empty():
        # in each step remove the min list from the heap
        node = heap.pop()

        # add the min list to the result
        pointer.next = node
        pointer = pointer.next

        node = node.next
        if node is not None:
            # take the next node from the min list and add it in the heap
            heap.push(node)

    return result.next


##############
# Solution 2 #
##############

def merge_k_lists_2(lists):
    n = len(lists)
    if n == 0:
        return None

    # the step tells with which linked list should be merged the current linked list
    step = 1

    # divide and conquer without recursion
    while step < n:
        i = 0

        while i + step < n:
            lists[i] = merge_2_lists(lists[i], lists[i + step])
            # go to the next pair
            i += 2 * step

        # double the step
        step *= 2

    return lists[0]

def merge_2_lists(l1, l2):
    result = ListNode(-1)
    pointer = result

    while (l1 is not None) and (l2 is not None):
        if l1.val < l2.val:
            pointer.next = l1
            l1 = l1.next
        else:
            pointer.next = l2
            l2 = l2.next

        pointer = pointer.next

    if l1 is not None:
        pointer.next = l1

    if l2 is not None:
        pointer.next = l2

    return result.next