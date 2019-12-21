'''
Same Tree

Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Input: 1         1
      / \       / \
     2   3     2   3
Output: True

Input:  1         1
       /           \
      2             2
Output: False

=========================================
Traverse both trees in same time and if something isn't equal, return False.
    Time Complexity:    O(N)
    Space Complexity:   O(N)    , because of the recursion stack (but this is if the tree is one branch), O(LogN) if the tree is balanced.
'''


############
# Solution #
############

# import TreeNode class from tree_helpers.py
from tree_helpers import TreeNode

def is_same_tree(p, q):
    if (p is None) and (p == q):
        return True

    if (p is None) or (q is None):
        return False

    if p.val != q.val:
        return False

    # check left
    if not is_same_tree(p.left, q.left):
        return False

    # check right
    if not is_same_tree(p.right, q.right):
        return False

    return True


###########
# Testing #
###########

# Test 1
# Correct result => True
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
print(is_same_tree(p, q))

# Test 2
# Correct result => False
p = TreeNode(1, TreeNode(2))
q = TreeNode(1, None, TreeNode(2))
print(is_same_tree(p, q))