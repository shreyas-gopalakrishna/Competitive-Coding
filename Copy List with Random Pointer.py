# https://leetcode.com/problems/copy-list-with-random-pointer/
# Logic: Recursively run through all the nodes and store them in a map. Key being the original node and value the newly created node.
#        For every new node created, Recursively update the next and random pointer.

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.nodeDict = dict()
    
    def copyRandomList(self, node: 'Node') -> 'Node':
        
        if(node == None):
            return None

        if(node in self.nodeDict):
            return self.nodeDict[node]

        newNode = Node(node.val, None, None)
        self.nodeDict[node] = newNode

        newNode.next = self.copyRandomList(node.next)
        newNode.random = self.copyRandomList(node.random)
        return newNode
