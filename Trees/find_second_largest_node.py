'''
Find second largest node (not search tree)

Given the root to a tree (not bst), find the second largest node in the tree.

=========================================
Traverse tree and compare the current value with the saved 2 values.
	Time Complexity: 	O(N)
	Space Complexity: 	O(N)        , because of the recursion stack (but this is the tree is one branch), O(LogN) if the tree is balanced.
'''


############
# Solution #
############

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left= left
        self.right = right

def find_second_largest(root):
    arr = [None, None]
    traverse_tree(root, arr)
    return arr[1]

def traverse_tree(node, arr):
    if node == None:
        return

    if arr[0] is None:
        arr[0] = node
    elif arr[0].val < node.val:
        arr[1] = arr[0]
        arr[0] = node
    elif arr[1] is None:
        arr[1] = node
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