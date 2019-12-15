'''
Find second largest node (not search tree)

Given the root to a tree (not bst), find the second largest node in the tree.

=========================================
Traverse tree and compare the current value with the saved 2 values.
    Time Complexity:    O(N)
    Space Complexity:   O(N)        , because of the recursion stack (but this is the tree is one branch), O(LogN) if the tree is balanced.
'''


############
# Solution #
############

# import TreeNode class from tree_helpers.py
from tree_helpers import TreeNode

import math

def find_second_largest(root):
    arr = [TreeNode(-math.inf), TreeNode(-math.inf)]
    traverse_tree(root, arr)
    if arr[1] == -math.inf:
        # the tree has 0 or 1 elements
        return None
    return arr[1]

def traverse_tree(node, arr):
    if node == None:
        return

    if arr[0].val < node.val:
        arr[1] = arr[0]
        arr[0] = node
    elif arr[1].val < node.val:
        arr[1] = node

    # search left
    traverse_tree(node.left, arr)
    # search right
    traverse_tree(node.right, arr)


###########
# Testing #
###########

# Test 1
# Correct result => 8
tree = TreeNode(1, TreeNode(5, TreeNode(2), TreeNode(8)), TreeNode(4, TreeNode(12), TreeNode(7)))
print(find_second_largest(tree).val)