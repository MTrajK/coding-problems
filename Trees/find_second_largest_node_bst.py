'''
Find second largest node in bst

Given the root to a binary search tree, find the second largest node in the tree.

=========================================
There are 4 possible cases (see the details in the code). 
Only 1 branch is searched to the end (leaf), not the whole tree.
	Time Complexity: 	O(LogN)      , if balanced bst, worst case if all elements are in the right branch O(N)
	Space Complexity: 	O(1)
'''


############
# Solution #
############

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left= left
        self.right = right

def find_second_largest_bst(root):
    if root == None:
        return None
    return find_second_largest(root, False)

def find_second_largest(node, visited_left):
    # the right child is bigger than the current node
    if node.right is not None:
        result = find_second_largest(node.right, visited_left)
        if result is None:
            # return this node, because the bottom is reached and the leaf is bigger than this node
            return node
        # result node is found
        return result
    
    # if this node is a part of a left subtree and this node doesn't have right child
    # then this is the solution
    if visited_left:
        return node
    
    # go to the left subtree 
    # the current node is bigger than all nodes in the left subtree, search for the biggest one there
    if node.left is not None:
        return find_second_largest(node.left, True)
    
    # this is a tree leaf (the right most element)
    return None


###########
# Testing #
###########

# Test 1
# Correct result => 10
tree = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(8, TreeNode(7), TreeNode(12, TreeNode(10, TreeNode(9)))))
print(find_second_largest_bst(tree).val)

# Test 2
# Correct result => 8
tree = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(8, TreeNode(7), TreeNode(12)))
print(find_second_largest_bst(tree).val)

# Test 3
# Correct result => 4
tree = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)))
print(find_second_largest_bst(tree).val)

# Test 4
# Correct result => 7
tree = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(8, TreeNode(6, None, TreeNode(7))))
print(find_second_largest_bst(tree).val)

# Test 5
# Correct result => 11
tree = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(8, TreeNode(7), TreeNode(12, TreeNode(9, None, TreeNode(10, None, TreeNode(11))))))
print(find_second_largest_bst(tree).val)