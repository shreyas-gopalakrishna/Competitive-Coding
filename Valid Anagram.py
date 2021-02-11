# https://leetcode.com/problems/valid-anagram/
# Logic: Use hashmap to count char from first string and remove when seen in second string. Length of hashmap will give if the string is anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(s is None or t is None):
            return False
        
        if(len(s) != len(t)):
            return False
        
        D = dict()
        
        for i in range(len(s)):
            if(s[i] in D):
                D[s[i]] += 1
                if(D[s[i]] == 0):
                    del D[s[i]]
            else:
                D[s[i]] = 1
            
            if(t[i] in D and D[t[i]] == 1):
                del D[t[i]]
            elif(t[i] in D and D[t[i]] > 1):
                D[t[i]] -= 1
            elif(t[i] in D and D[t[i]] < 0):
                D[t[i]] -= 1
            else:
                D[t[i]] = -1        
        return len(D) == 0
