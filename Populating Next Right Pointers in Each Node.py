# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# Logic: First approach is to use extra space to do a level order traversal and each time linking the previous element in the level to the next element. O(n) space
#        Best approach, level order traversal but in level N-1 we process level N. This way the next pointer of parent and siblings is established by - node.left.next = node.right
#        The link across the children of different parent can then be established by node.right.next = node.next.left if node.next exists.

class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        L = []
        def connectNext(node, level):
            if(node == None or(node.left == node.right == None)):
                return
            node.left.next = node.right
            try:
                node.right.next = node.next.left
            except:
                pass
            connectNext(node.left, level+1)
            connectNext(node.right, level+1)
        connectNext(root, 0)
        return root
            
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        L = []
        def connectNext(node, level):
            if(node == None):
                return
            try:
                L[level][-1].next = node
                L[level].append(node)
            except:
                L.append([node])
            connectNext(node.left, level+1)
            connectNext(node.right, level+1)
        connectNext(root, 0)
        return root
            
                        
