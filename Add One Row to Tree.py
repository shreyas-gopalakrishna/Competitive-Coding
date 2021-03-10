# https://leetcode.com/problems/add-one-row-to-tree/
# Logic: If the new node has to be added at depth - 1, then we just move the root to the left subtree of the root and return the new node.
#        If new node is to be added at depth > 1, then we perform DFS, if the depth is one less than where we must add, we create 2 new nodes and link them
#        No need to go beyond the required depth. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        
        def add(node, depth, v, d):
            if(node == None or depth > d):
                return
            if(depth == (d - 1)):
                new1 = TreeNode(v, left=node.left)
                new2 = TreeNode(v, right=node.right)
                
                node.left = new1
                node.right = new2
                return
            add(node.left, depth+1, v, d)
            add(node.right, depth+1, v, d)
        if(d == 1):
            new1 = TreeNode(v, left=root)
            return new1
        else:
            add(root, 1, v, d)
            return root
