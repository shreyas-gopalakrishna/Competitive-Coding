# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Logic: Traverse the tree passing the level each time. Use BFS since we need value at each level then their leaves
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderT(self, root, L, count):
        if count not in L:
            L[count] = list()
        if(root == None):
            return
        L[count].append(root.val)
        self.levelOrderT(root.left,L,count+1)
        self.levelOrderT(root.right,L,count+1)
    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        L = dict()
        self.levelOrderT(root, L, 0)
        output = list()
        print(L)
        for i in range(0,len(L)):
            if(not len(L[i]) == 0):
                output.append(L[i])
        
        return output
