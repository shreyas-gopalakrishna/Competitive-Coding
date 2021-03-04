# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Logic: Best: Find length of both lists. Move pointer of longer list such that both are at same length level. Then continue checking both node after node.
# Not the best: Use a hash map to add all nodes from list A. Then check if a node is already present in the map while traversing list B. (More memory)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def length(node):
            count = 0
            while(node != None):
                count += 1
                node = node.next
            return count
        
        lenA = length(headA)
        lenB = length(headB)
        if(lenA == 0 or lenB == 0):
            return None
        
        if(lenA != lenB):
            if(lenA > lenB):
                while(lenA != lenB):
                    if(headA == headB):
                        return headA
                    headA = headA.next
                    lenA -= 1
            else:
                while(lenA != lenB):
                    if(headA == headB):
                        return headA
                    headB = headB.next
                    lenB -= 1
        while(headA != None or headB != None):
            print(headA.val, headB.val)

            if(headA == headB):
                return headA
            if(headA.next != None):
                headA = headA.next
            else:
                break
            if(headB.next != None):
                headB = headB.next
            else:
                break
        return None
        
