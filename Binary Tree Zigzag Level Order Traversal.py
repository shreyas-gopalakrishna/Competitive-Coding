# Binary Tree Zigzag Level Order Traversal
# Logic: Same as level order traversal. But at every odd level reverse the order(insert at start instead of end )
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # shreyas
    def levelOrderT(self, root, L, count):
        if count not in L:
            L[count] = list()
        if(root == None):
            return
        if(count%2 == 0):
            L[count].append(root.val)
        else:
            L[count].insert(0,root.val)
        self.levelOrderT(root.left,L,count+1)
        self.levelOrderT(root.right,L,count+1)
    
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        L = dict()
        self.levelOrderT(root, L, 0)
        output = list()
        print(L)
        for i in range(0,len(L)):
            if(len(L[i]) != 0):
                output.append(L[i])
        return output        
