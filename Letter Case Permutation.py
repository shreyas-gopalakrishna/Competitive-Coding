# https://leetcode.com/problems/letter-case-permutation/
# Logic: Start with a digit or letter - [a, A]. Each time a digit is added, add it directly - [a1, A1]. While adding letter, duplicate the elements 
#        [a1, A1, a1, A1] and then add the lower case letter to first half and upper case letter to second half. [a1b, A1b, a1B, A1B]

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:        
        result = []
        
        for i in range(len(S)):
            if(S[i].isdigit()):
                if(not result):
                    result = [S[i]]
                else:
                    result = [ s + S[i] for s in result]
            else:
                if(not result):
                    result = [S[i].lower(), S[i].upper()]
                else:
                    result *= 2
                    result = [ result[j] + S[i].lower() if j < (len(result)/2) else result[j] + S[i].upper() for j in range(len(result))]
        
        return result
        
