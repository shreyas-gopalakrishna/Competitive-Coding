# https://leetcode.com/problems/validate-binary-search-tree/
# Logic: Inorder traversal of BST will be a sorted output.
#        Checking if the traversal is sorted gives if BST is valid.
#        For iterative approach, use stack to retrive order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # shreyas
    def inorder(self, root, L):
        if(root == None):
            return L
        self.inorder(root.left,L)
        L.extend([root.val])
        self.inorder(root.right,L)
        return L
    
    def isValidBST(self, root: TreeNode) -> bool:
        if(root == None):
            return True
        else:
            L = list()
            L = self.inorder(root,L)
            for i in range(0,len(L)-1):
                if(L[i+1] > L[i]):
                    continue
                else:
                    return False
            return True
