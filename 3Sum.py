# https://leetcode.com/problems/3sum/
# Logic: First sort array since it helps decide if we need to choose a low number or high number
#        if we encounter a number greater than target(0) then break. sum can't get any bigger
#        choose a number and then choose pair which adds up to (target - number)
#        choose pair by have pointers low and high which are moved based on (target - number) greater or smaller
#        ignore same numbers during all steps since we don't want duplicates
class Solution:
    # shreyas
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # if(len(nums) == 3 and sum(nums)==0):
        #     return [nums]
        # if(len(nums) < 3):
        #     return []
        # if(len(set(nums)) == 1 and 0 in set(nums)):
        #     return [[0,0,0]]
        nums.sort()
        output = list()
        for i in range(0,len(nums)-2):
            # choose pair, skip if same number
            if(nums[i] > 0):
                break
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            l = i+1
            h = len(nums) - 1
            target = 0 - nums[i]
            while(l<h):
                if(nums[l] + nums[h] == target):
                    output.append([nums[i],nums[l],nums[h]])
                    while(l<h and nums[l]==nums[l+1]):
                        l += 1
                    while(l<h and nums[h]==nums[h-1]):
                        h -= 1
                    l+=1
                    h-=1
                elif(nums[l] + nums[h] > target):
                    h-=1
                else:
                    l+=1
        return output
