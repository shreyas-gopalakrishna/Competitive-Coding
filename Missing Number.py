# https://leetcode.com/problems/missing-number/solution/
# Logic: Sum of numers from 1-n = (n*(n+1))/2

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actual = int((n * (n+1))/2)
        current = sum(nums)
        
        if(actual == current):
            return 0
        else:
            return abs(actual - current)
