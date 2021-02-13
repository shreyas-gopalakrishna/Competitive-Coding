# https://leetcode.com/problems/decode-ways/
# Logic: If the string is of length 1 or 2 we directly use the answer. When the string is more than length 2, we recursively find the count when the string 
#        can be split into 1 char + count(rest) and with 2 char + count(rest). In both cases we must handle having 0.

class Solution:
    def numDecodings(self, s: str) -> int:
        
        def count(s):
            c = 0
            if(len(s) <= 0):
                return 0
            if(s in result):
                return result[s]
            
            if(len(s) == 1 and s in D):
                c += 1
            if(len(s) == 2 and s in D):
                c += 1
            if(len(s) == 2 and s[0] in D and s[1] in D):
                c += 1
            if(len(s) > 2):
                if(s[0] != '0' and s[1] != '0'):
                    c += count(s[1:])
                if(s[0:2] in D and s[2] != '0'):
                    c += count(s[2:])
            result[s] = c
            return c
        
        D = dict()
        result = dict()
        for i in range(26):
            D[str(i+1)] = chr(65+i)
        return count(s)
