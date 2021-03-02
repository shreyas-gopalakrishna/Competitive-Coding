# https://leetcode.com/problems/distribute-candies/
# Logic: Use hashmap to count unique candy type. Result will be the amount of candies which can be eaten or the total unique ones

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        
        canEatCount = int(n / 2)
        
        D = dict()
        uniqueType = 0
        for i in range(n):
            if(not candyType[i] in D):
                D[candyType[i]] = 1
                uniqueType += 1
        
        if(uniqueType <= canEatCount):
            return uniqueType
        else:
            return canEatCount
