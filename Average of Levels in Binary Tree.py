# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Logic: Use DFS to traverse all the nodes to update result array with average at each level. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        average = []
        
        def find(node, level):
            if(node == None):
                return
            try:
                s = ((average[level][0] * average[level][1]) + node.val) / (average[level][1] + 1)
                average[level] = (s,average[level][1]+1)
            except:
                average.append((node.val,1))
            find(node.left, level+1)
            find(node.right, level+1)
        find(root, 0)
        return [i[0] for i in average]
