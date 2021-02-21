# https://leetcode.com/problems/roman-to-integer/
# Logic: Checking for the special roman char first, adding them up and then checking for the normal roman char.

class Solution:
    def romanToInt(self, s: str) -> int:
        D1 = { 'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        D2 = { 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        
        count = 0
        for k,v in D2.items():
            if(k in s):
                count += D2[k]
                s = s.replace(k,'')
        for i in range(len(s)):
            count += D1[s[i]]
        
        return count
        
