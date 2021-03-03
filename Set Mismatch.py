# https://leetcode.com/problems/set-mismatch/
# Logic: In one pass find the element which is duplicate and store it. In the next pass find which is missing.

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        n = len(nums)
        result = []
        j = 0
        for i in range(0, len(nums)):
            if(nums[i] == nums[i+1]):
                result.append(nums[i])
                del nums[i]
                break
        
        miss = 0
        for i in range(0, n-1):
            if(nums[i] != i+1):
                miss = i+1
                break
        
        if(miss == 0):
            result.append(n)
        else:
            result.append(miss)
        return result
