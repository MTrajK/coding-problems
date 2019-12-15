'''
Helpers used in all Linked List solutions.
This file is created to avoid duplicate code in all solutions.
'''

class ListNode:
    def __init__(self, x, n = None):
        '''Definition for singly-linked list'''
        self.val = x
        self.next = n

def build_ll(arr):
    '''Build a linked list from array'''
    res = ListNode(None)
    pt = res

    for num in arr:
        pt.next = ListNode(num)
        pt = pt.next

    return res.next

def print_ll(head):
    '''Print the linked list in this format x -> y -> z'''
    res = []

    while head != None:
        res.append(str(head.val))
        head = head.next

    print(' -> '.join(res))