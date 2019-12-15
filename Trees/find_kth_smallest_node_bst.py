'''
Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it

Input: 3    , k = 1
      / \
     1   4
      \
       2
Output: 1

Input: 5    , k = 3
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

=========================================
Traverse Inorder the tree (Type of depth first traversal: left, root, right) and count the nodes.
When the Kth node is found, return that node.
    Time Complexity:    O(N)
    Space Complexity:   O(N)        , because of the recursion stack (but this is if the tree is one branch), O(LogN) if the tree is balanced.
'''


############
# Solution #
############

# import TreeNode class from tree_helpers.py
from tree_helpers import TreeNode

def find_kth_smallest_node_bst(root, k):
    return search(root, k)[1]

def search(node, k):
    if node is None:
        return (k, None)

    # check left
    left = search(node.left, k)
    if left[0] == 0:
        return left

    # check current node
    k = left[0] - 1
    if k == 0:
        return (k, node)

    # check right
    return search(node.right, k)


###########
# Testing #
###########

# Test 1
# Correct result => 9
tree = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(8, TreeNode(7), TreeNode(12, TreeNode(10, TreeNode(9)))))
print(find_kth_smallest_node_bst(tree, 7).val)

# Test 2
# Correct result => 5
tree = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(8, TreeNode(7), TreeNode(12)))
print(find_kth_smallest_node_bst(tree, 4).val)

# Test 3
# Correct result => 3
tree = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)))
print(find_kth_smallest_node_bst(tree, 2).val)

# Test 4
# Correct result => 6
tree = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(8, TreeNode(6, None, TreeNode(7))))
print(find_kth_smallest_node_bst(tree, 5).val)

# Test 5
# Correct result => 9
tree = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(8, TreeNode(7), TreeNode(12, TreeNode(9, None, TreeNode(10, None, TreeNode(11))))))
print(find_kth_smallest_node_bst(tree, 7).val)