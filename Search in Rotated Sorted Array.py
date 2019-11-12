# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Logic: Problem is an extended version of binary search. One Approach is find point of rotation and then binary search from start/end to that point.
#        Another approach is to directly do binary search but move low and high based on 2 conditions.
#        1. Pivot element is larger than the first element in the array, i.e. the part of array from the first element to the pivot one is non-rotated.
#           If the target is in that non-rotated part as well: go left: end = mid - 1. Otherwise: go right: start = mid + 1.
#        2. Pivot element is smaller than the first element of the array, i.e. the rotation index is somewhere between 0 and mid. That means that the part of array from the pivot element to the last one is non-rotated.
#           If target is in that non-rotated part as well: go right: end = mid + 1. Otherwise: go left: start = mid - 1.
class Solution:
    # shreyas
    def search(self, nums: List[int], target: int) -> int:        
        l,h = 0,len(nums)-1
        if(l == h ):
            if (nums[l] == target):
                return l
            else:
                return -1
        while(l < h):
            i = int((l+h)/2)
            if(target == nums[i]):
                return i
            elif(target == nums[l]):
                return l
            elif(target == nums[h]):
                return h
            elif(nums[i] > nums[l]):
                if(target > nums[l] and target < nums[i]):
                    h = i-1
                else:
                    l = i+1
            else:
                if(target < nums[h] and target > nums[i]):
                    l = i+1
                else:
                    h = i-1
        return -1
