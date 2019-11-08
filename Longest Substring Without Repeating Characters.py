# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Logic: Track the latest index a char occurs using hashmap. 
#        Sliding window grows by 1 every new char found.
#        If char already seen is encountered, update start of substring 
#        to previous occurance index + 1 - only if the char is in the current window. 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # shreyas
        max1  = 0
        start = 0
        end = 0
        d = dict()
        if(len(s) <= 1 ):
            return len(s)
        for i in range(0,len(s)):
            end = i
            if(s[i] in d and start <= d[s[i]]):
                start = d[s[i]] + 1
            if((end - start)+1 > max1):
                max1 = (end - start)+1
            d[s[i]] = i
        return max1
