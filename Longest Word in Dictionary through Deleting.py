# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
# Logic: Since we need the longest string in list, we sort the list based on length. We check if the string is sub-sequence, if yes we found the longest word. 
# https://techdevguide.withgoogle.com/resources/former-interview-question-find-longest-word/ - A much better approach

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        
        def check(s1, s2):
            j = 0
            for i in range(len(s1)):
                if(j < len(s2) and s1[i] == s2[j]):
                    j += 1
            return j == len(s2)
        
        if(s == ""):
            return ""
        d.sort(key=str.lower)
        d.sort(key=len, reverse=True)
        L = d
        for i in range(len(L)):
            if(check(s, L[i])):
                return L[i]
        return ""
