'''
Find second largest node in bst

Given the root to a binary search tree, find the second largest node in the tree.

=========================================
There are 4 possible cases (see the details in the code).
Only 1 branch is searched to the end (leaf), not the whole tree.
    Time Complexity:    O(N)        , this is the worst case when all elements are in one (the right) branch O(N), O(LogN) if the tree is balanced (balanced bst)
    Space Complexity:   O(N)        , because of the recursion stack (but this is if the tree is one branch), O(LogN) if the tree is balanced.
The second solution is simpler and it's same as find_kth_smallest_node_bst.py but K is 2.
    Time Complexity:    O(N)
    Space Complexity:   O(N)
'''


##############
# Solution 1 #
##############

# import TreeNode class from tree_helpers.py
from tree_helpers import TreeNode

def find_second_largest_bst_1(root):
    if root == None:
        return None
    return search_1(root, False)

def search_1(node, visited_left):
    # the right child is bigger than the current node
    if node.right is not None:
        result = search_1(node.right, visited_left)
        if result is None:
            # return this node, because the bottom is reached and the leaf is bigger than this node
            return node
        # result node is found
        return result

    # if this node is a part of the left subtree and this node doesn't have right child
    # then this is the solution
    if visited_left:
        return node

    # go to the left subtree
    # the current node is bigger than all nodes in the left subtree, search for the biggest one there
    if node.left is not None:
        return search_1(node.left, True)

    # this is a tree leaf (the right most element)
    return None


##############
# Solution 2 #
##############

def find_second_largest_bst_2(root):
    return search_2(root, 2)[1]

def search_2(node, k):
    if node == None:
        return (k, None)

    # check right
    right = search_2(node.right, k)
    if right[0] == 0:
        return right

    # check current node
    k = right[0] - 1
    if k == 0:
        return (0, node)

    # check left
    return search_2(node.left, k)


###########
# Testing #
###########

# Test 1
# Correct result => 10
tree = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(8, TreeNode(7), TreeNode(12, TreeNode(10, TreeNode(13)))))
print(find_second_largest_bst_1(tree).val)
print(find_second_largest_bst_2(tree).val)

# Test 2
# Correct result => 8
tree = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(8, TreeNode(7), TreeNode(12)))
print(find_second_largest_bst_1(tree).val)
print(find_second_largest_bst_2(tree).val)

# Test 3
# Correct result => 4
tree = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)))
print(find_second_largest_bst_1(tree).val)
print(find_second_largest_bst_2(tree).val)

# Test 4
# Correct result => 7
tree = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(8, TreeNode(6, None, TreeNode(7))))
print(find_second_largest_bst_1(tree).val)
print(find_second_largest_bst_2(tree).val)

# Test 5
# Correct result => 11
tree = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(8, TreeNode(7), TreeNode(12, TreeNode(9, None, TreeNode(10, None, TreeNode(11))))))
print(find_second_largest_bst_1(tree).val)
print(find_second_largest_bst_2(tree).val)