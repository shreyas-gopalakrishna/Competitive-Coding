# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Logic: left -> node -> right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        def travel(node):
            if(node == None):
                return
            travel(node.left)
            result.append(node.val)
            travel(node.right)
        travel(root)
        return result
