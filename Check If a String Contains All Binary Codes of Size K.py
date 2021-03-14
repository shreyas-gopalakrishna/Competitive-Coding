# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/solution/
# Logic: All we have to check for are binary strings of length k. That would cover all the binary substrings of length less than k. 
#        We take all the substrings of length k of the given string and add it to a set. If length of the set is pow(2,k) then we have all substrings. So return true.

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        D = set()
        for i in range(len(s)-k+1):
            D.add(s[i:i+k])
        # print(D)
        return len(D) == 2**k
