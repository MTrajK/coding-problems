'''
Diamter of a Binary Tree.

Given a binary tree, write a function diameter to find the diamter of the given binary tree.
Diameter of a binary tree is the maximum distance between any two nodes.

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
Recursively find the height and diameter of left and right subtree.
Diameter will be the maximum of either sum of left and right subtree height plus 1 or left diameter or right diameter.
    Time Complexity:    O(N)
    Space Complexity:   O(N)        , because of the recursion stack (but this is if the tree is one branch), O(LogN) if the tree is balanced.
'''


############
# Solution #
############

# import TreeNode class from tree_helpers.py
from tree_helpers import TreeNode


class Height:
    def __init__(self, h=0):
        self.height = h

    def __add__(self, other):
        return self.height + other.height


def diameter(root, height):
    if not root:
        height.height = 0
        return 0
    left_ht, right_ht = Height(), Height()
    left_diameter, right_diameter = diameter(root.left, left_ht), diameter(root.right, right_ht)
    height.height = max(left_ht.height, right_ht.height) + 1
    return max(left_diameter, right_diameter, left_ht + right_ht + 1)


# Test 1
# Correct result => 5
tree = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(2)), TreeNode(6, TreeNode(10), TreeNode(8)))
height = Height()
print(diameter(tree, height))
