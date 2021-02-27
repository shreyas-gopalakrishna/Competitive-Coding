# https://leetcode.com/problems/validate-stack-sequences/
# Logic: Take a greedy approach. Push until pointer reaches a place where an element can be popped. Whenever an element can be popped pop it, then push other. 

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        if(len(pushed) == len(popped) == 0):
            return True
        
        i = 0
        n = len(pushed)
        
        count = 0
        while(len(pushed) > 0 and len(popped) > 0 and count < 2 * n):
            try:
                if(popped[0] == pushed[i]):
                    del popped[0]
                    del pushed[i]
                    if(i != 0):
                        i -= 1
                else:
                    i += 1
            except:
                pass
            count += 1
        
        if(len(pushed) == len(popped) == 0):
            return True
        else:
            return False
