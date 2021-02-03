# https://leetcode.com/problems/linked-list-cycle/
# Logic:  2 pointers, one moves by 1 and another by 2 places. If a cycle is present they meet. Else they don't 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if(head is None or head.next is None):
            return False
        tortoise = head
        while(head != None and tortoise != None and tortoise.next != None ):
            head = head.next
            tortoise = tortoise.next.next
            if(head == tortoise):
                return True
        return False        
