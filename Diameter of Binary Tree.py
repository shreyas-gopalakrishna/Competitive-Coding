# https://leetcode.com/problems/diameter-of-binary-tree/
# Logic: We can find the longest path by using the depth at each level. The leaf node has depth 0 and increases towards the root. Use DFS to reach depth wise to find the diameter.
#        At each level we need 2 information, the result which will be the max(result, l+r+1) i.e either result of left depth + right depth + 1. The second information is
#        to pass on to the function caller about which path should the caller go with - that is the longer path so - max(l,r) + 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.m = 1
            
        def level(node):
            if(node == None):
                return 0
            l = level(node.left)
            r = level(node.right)
            self.m = max(self.m, l+r+1)
            return max(l,r) + 1
        level(root)
        return self.m - 1
