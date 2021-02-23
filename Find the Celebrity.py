# https://leetcode.com/problems/find-the-celebrity/
# Logic: Each time we check if a knows b - we can conclude b is not celebrity if a knows b OR a must be a celebrity so they don't know b
#        Using this logic we loop through and find a celebrity. We once again check if they do not know anyone and if everyone knows them since there can exist no celebrity.

class Solution2:
    def findCelebrity(self, n: int) -> int:
        
        celebrity = 0
        for i in range(1, n):
            if(knows(celebrity,i)):
                celebrity = i
                        
        for i in range(n):
            if(celebrity != i and (knows(celebrity, i) or not knows(i, celebrity))):
                return -1
        return celebrity


# This is a complex approach, assumes everyone is a celebrity and starts eliminating in loop. The one left out will be celebrity or not based on final check.

class Solution:
    def findCelebrity(self, n: int) -> int:
        result = [i for i in range(n)]
        
        while(len(result) > 1):
            choice = result[0]
            
            not_celebrity = []
            
            for i in range(1, len(result)):
                if(not knows(choice,result[i])):
                    not_celebrity.append(result[i])            
            
            if(len(not_celebrity) == 0):
                not_celebrity.append(choice)
            
            for i in range(len(not_celebrity)):
                result.remove(not_celebrity[i])
            
            try:
                result.remove(choice)
                result.append(choice)
            except:
                pass
                        
        for i in range(n):
            if(result[0] != i and (knows(result[0], i) or not knows(i, result[0]))):
                return -1
        return result[0]
