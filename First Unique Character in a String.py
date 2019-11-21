# https://leetcode.com/problems/first-unique-character-in-a-string/
# Logic: Use map to store charecters and their index. If a charecter re occurs invalidate it in the map.
class Solution:
    # shreyas
    def firstUniqChar(self, s: str) -> int:
        D = dict()
        for i in range(0,len(s)):
            if not s[i] in D:
                D[s[i]] = i
            else:
                D[s[i]] = -1
        
        index = float("inf")
        for k,v in D.items():
            if(v != -1 and v < index):
                index = v
        
        if(index != float("inf")):
            return index
        else:
            return -1
