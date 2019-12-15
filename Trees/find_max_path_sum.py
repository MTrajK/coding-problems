'''
Find max path sum

Wrie a function that takes a Binary Tree and returns its max path sum.

Input:
        1
       / \
      2   3
     / \ / \
    4  5 6  7
Output: 18
Output explanation: 5 -> 2 -> 1 -> 3 -> 7

Input:
       -1
       / \
     -2   3
     / \ / \
   -4 -5 2  5
Output: 10
Output explanation: 2 -> 3 -> 5

=========================================
Traverse the tree and in each node compare create a new path where the left and right max subpaths are merging in the current node.
    Time Complexity:    O(N)
    Space Complexity:   O(N)        , because of the recursion stack (but this is the tree is one branch), O(LogN) if the tree is balanced.
'''


############
# Solution #
############

# import TreeNode class from tree_helpers.py
from tree_helpers import TreeNode

def max_path_sum(tree):
    return find_max_path_sum(tree)[0]

def find_max_path_sum(node):
    if node is None:
        return (0, 0)

    # get the result from the left subtree
    left_result = find_max_path_sum(node.left)
    # get the result from the right subtree
    right_result = find_max_path_sum(node.right)

    # create a new path by merging the max left and right subpaths
    current_path = left_result[1] + node.val + right_result[1]
    # find the max path till now, comparing the new path, max path from the left and right subtree
    max_path = max(left_result[0], current_path, right_result[0])
    # find the max subpath, min value for a subpath sum is 0
    max_subpath = max(left_result[1] + node.val, right_result[1] + node.val, node.val, 0)

    return (max_path, max_subpath)


###########
# Testing #
###########

# Test 1
# Correct result => 18
tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(max_path_sum(tree))

# Test 2
# Correct result => 10
tree = TreeNode(-1, TreeNode(-2, TreeNode(-4), TreeNode(-5)), TreeNode(3, TreeNode(2), TreeNode(5)))
print(max_path_sum(tree))

# Test 3
'''
        1
       / \
      7   3
     / \ / \
   -4 -5 6  2
'''
# Correct result => 17 (7 -> 1 -> 3 -> 6)
tree = TreeNode(1, TreeNode(7, TreeNode(-4), TreeNode(-5)), TreeNode(3, TreeNode(6), TreeNode(2)))
print(max_path_sum(tree))

# Test 4
'''
        1
       / \
      2   3
     / \ / \
   -4 -5 -2 -3
'''
# Correct result => 6 (2 -> 1 -> 3)
tree = TreeNode(1, TreeNode(2, TreeNode(-4), TreeNode(-5)), TreeNode(3, TreeNode(-2), TreeNode(-3)))
print(max_path_sum(tree))