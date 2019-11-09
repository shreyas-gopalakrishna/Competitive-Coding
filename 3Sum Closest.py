# https://leetcode.com/problems/3sum-closest/
# Logic: Same as 3Sum problem. Choose a number then find a pair which reduces the differnece for the target
#        If if find sum == target return since that is the closest difference 
class Solution:
    # shreyas
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        mainD = float("inf")
        mainS = 0
        nums.sort()
        for i in range(0,len(nums)-2):
            l = i+1
            h = len(nums) - 1
            while(l<h):
                s = nums[l] + nums[h] + nums[i]
                d = abs(target-s)
                if(d < mainD):
                    mainD = d
                    mainS = s
                if(s == target):
                    return target
                elif(s > target):
                    h-=1
                else:
                    l+=1
        return mainS
