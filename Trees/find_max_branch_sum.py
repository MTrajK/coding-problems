'''
Find max branch sum

Wrie a function that takes a binary tree and returns its max branch (branch is "root to leaf path") sum.

Input:
        1
       / \
      2   3
     / \ / \
    4  5 6  7
Output: 11
Output explanation: 1 -> 3 -> 7

=========================================
Traverse the tree and in each node compare the left and right subbranch sum, and take the bigger one.
    Time Complexity:    O(N)
    Space Complexity:   O(N)        , because of the recursion stack (but this is the tree is one branch), O(LogN) if the tree is balanced.
'''


############
# Solution #
############

# import TreeNode class from tree_helpers.py
from tree_helpers import TreeNode

def max_branch_sum(node):
    if node is None:
        return 0

    # take the max left subbranch sum and add the current node value
    left_max_sum = max_branch_sum(node.left) + node.val
    # take the max right subbranch sum and add the current node value
    right_max_sum = max_branch_sum(node.right) + node.val

    # return the bigger sum
    return max(left_max_sum, right_max_sum)


###########
# Testing #
###########

# Test 1
# Correct result => 11
tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(max_branch_sum(tree))