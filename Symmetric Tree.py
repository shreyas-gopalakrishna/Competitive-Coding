# https://leetcode.com/problems/symmetric-tree/
# Logic: A tree is symmetric if root are same and left sub tree is reflection of right sub tree 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # shreyas
    def validate(self, root1, root2):
        if(root1 == None and root2 == None):
            return True
        if(root1 == None or root2 == None):
            return False
        return root1.val == root2.val and self.validate(root1.left,root2.right) and self.validate(root2.left,root1.right)
        
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.validate(root,root)
        
