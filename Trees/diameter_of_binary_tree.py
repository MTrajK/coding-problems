'''
Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
Note: The length of path between two nodes is represented by the number of nodes.

Input: 3
      / \
     1   4
      \   \
       2   5
      /
     7
Output: 6
Output Explanation: [7, 2, 1, 3, 4, 5] is the diameter of the binary tree.

Input: 5
      / \
     3   6
    / \
   2   4
  /     \
 1       8
Output: 5
Output Explanation: [1, 2, 3, 4, 8] is the diameter of the binary tree.

=========================================
Traverse the tree and keep/return information about the longest/max branch and longest/max diameter.
    Time Complexity:    O(N)
    Space Complexity:   O(N)        , because of the recursion stack (but this is if the tree is one branch), O(LogN) if the tree is balanced.
'''


############
# Solution #
############

# import TreeNode class from tree_helpers.py
from tree_helpers import TreeNode

def diameter(root):
  	return find_diameter(root)[1]

def find_diameter(root):
    ''' returns (max branch length, max diameter) '''
    if not root:
        return 0, 0

    # traverse left and right subtrees
    left, right = find_diameter(root.left), find_diameter(root.right)

    # return the max branch from the left and right subtrees plus the current node
    # and find the max diameter till now (using the current node and the max left and right subtree branches)
    return max(left[0], right[0]) + 1, max(left[1], right[1], left[0] + right[0] + 1)


###########
# Testing #
###########

# Test 1
# Correct result => 6
tree = TreeNode(3, TreeNode(1, None, TreeNode(2, TreeNode(7))), TreeNode(4, None, TreeNode(5)))
print(diameter(tree))

# Test 2
# Correct result => 5
tree = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4, None, TreeNode(8))), TreeNode(6))
print(diameter(tree))