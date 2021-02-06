# https://leetcode.com/problems/binary-tree-right-side-view/
# Logic: Recursively traverse every node, visiting the rightmost child first. OR Use pre order traversal and update the latest
#        visited right child in a list at every level.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def right(self, node, level, levels):
        if(node == None):
            return
        try:
            levels[level] = node.val
        except:
            levels.append(node.val)
        self.right(node.left, level+1, levels)
        self.right(node.right, level+1, levels)
        
    
    def rightSideView(self, root: TreeNode) -> List[int]:
        levels = []
        self.right(root, 0, levels)
        return levels
        
