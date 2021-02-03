# https://leetcode.com/problems/trim-a-binary-search-tree/
# Logic: Using recursion go to each node. If node value is greater than high or less than low, then whole side of the BST will be outside [low, high] so trim
         If the node is in [low, high] then proceed with trim of it's children until the end.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def check(self, node, low, high):
        if not node:
            return None
        if(node.val > high):
            return self.check(node.left, low, high)
        elif(node.val < low):
            return self.check(node.right, low, high)
        else:
            node.left = self.check(node.left, low, high)
            node.right = self.check(node.right, low, high)
            return node
    
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        return self.check(root, low, high)        
