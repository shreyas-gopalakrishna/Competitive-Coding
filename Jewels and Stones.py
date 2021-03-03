# https://leetcode.com/problems/jewels-and-stones/
# Logic: Use a map and check if stone is a jewel.

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        D = dict()
        for i in range(len(jewels)):
            D[jewels[i]] = 1
        
        count = 0
        for i in range(len(stones)):
            if(stones[i] in D):
                count += 1
        
        return count
