'''
Rotate List

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL

Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

===================================================

Solution : Using Floyd's slow and fast pointers
1. Find the length of the list. Then do a modulus to get the right value for k. Note k cannot be negative. If k is zero, simply return head.
2. Initialize slow and fast pointers to head. Move the fast pointer ahead by k. Now the algorithm is to move slow and fast by one until fast.next reaches None. Sketch several examples of this for even and odd lists.
3. Now we are almost done and just need to tweak pointers. How did we get this above algorithm? The intuition is from the algorithms to rotate an array by k using an in-place algorithm. That algorithm uses reversing the array as an intermediate step. In a linked list, we do not need that intermediate step - we can simply move pointers.
4. Make fast,next point to head.
5. Make slow.next as new head.
6. Make slow.next as None.

Time Complexity = O(N)
Space Complexity = O(1)

'''

############
# Solution #
############

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def get_length(self, head):
        N = 0
        while head:
            N, head = N+1, head.next
        return N
    
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        N = self.get_length(head)
        k = int(k % N)
        if k == 0:
            return head
        else:
            slow, fast = head, head
            while k:
                k, fast = k-1, fast.next
            while fast.next:
                slow, fast = slow.next, fast.next
            fast.next, head, slow.next = head, slow.next, None
            return head
            
###########
# Testing #
###########

'''
Input: 0->1->2->NULL, k = 4
Expected Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
'''
