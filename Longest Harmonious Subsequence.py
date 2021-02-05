# https://leetcode.com/problems/longest-harmonious-subsequence
# Logic: Traverse elements to add them to a Dict. Check for +1 and -1 of those elements and choose which gives the max Longest Harmonious Subsequence
#        Key insight is ordering doesn’t matter. 

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n = len(nums)
        
        D = dict()
        maxi = 0
        for i in range(n):
            if nums[i] in D:
                D[nums[i]] += 1
            else:
                D[nums[i]] = 1
            
            if(nums[i]+1 in D and D[nums[i]] + D[nums[i] + 1] > maxi):
                maxi = D[nums[i]] + D[nums[i] + 1]
            elif(nums[i]-1 in D and D[nums[i]] + D[nums[i] - 1] > maxi):
                maxi = D[nums[i]] + D[nums[i] - 1]
        return maxi
