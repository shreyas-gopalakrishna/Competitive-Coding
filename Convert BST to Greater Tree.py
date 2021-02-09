# https://leetcode.com/problems/convert-bst-to-greater-tree/
# Logic: The tree must be traversed such that we visit all the nodes greater than that node in the tree. So all nodes in the right sub tree then the current node 
#        and finally the left sub tree. This is a reverse inorder traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def greaterBST(self, node, value):
        if(node == None):
            return value
        total = self.greaterBST(node.right, value)
        node.val += total
        return self.greaterBST(node.left, node.val)
        
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.greaterBST(root, 0)
        return root
