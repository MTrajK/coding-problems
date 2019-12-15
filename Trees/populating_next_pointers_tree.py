'''
Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
The binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

=========================================
Breadth first (level order) traversal, using queue.
Save the previous node and level and if the current level is same
then make the previous node to point to the current node.
    Time Complexity:    O(N)
    Space Complexity:   O(N)
'''


############
# Solution #
############

from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def populating_next_pointers_tree(root):
    previous = None
    queue = deque()
    queue.append((root, 0))

    while queue:
        el = queue.popleft()
        node = el[0]
        lvl = el[1]

        if node is None:
            continue

        if (previous is not None) and (lvl == previous[1]):
            previous[0].next = node

        previous = (node, lvl)

        lvl += 1
        queue.append((node.left, lvl))
        queue.append((node.right, lvl))

    return root