# https://leetcode.com/problems/two-sum/
# Logic: Use hash map to track number and its index
#        If target-present number is found in hash map, return with index
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # shreyas
        d = dict()
        l = list()
        for i in range(len(nums)):
            try:
                if(d[target-nums[i]] >= 0):
                    return [d[target-nums[i]],i]
            except:
                pass
            d[nums[i]] = i
