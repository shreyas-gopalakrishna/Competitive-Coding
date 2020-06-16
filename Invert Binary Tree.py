# https://leetcode.com/problems/invert-binary-tree/
# Logic: Swap left and right at each node
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.invert(root)
        return root
    
    def invert(self, root):
        if root == None or root.left == root.right == None:
            return
        else:
            root.left, root.right = root.right, root.left
            self.invert(root.left)
            self.invert(root.right)
