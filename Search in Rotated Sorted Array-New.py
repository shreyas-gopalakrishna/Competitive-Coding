# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Logic: Use 3 or 4 pointers to look in the first last and middle elements
#        Divide the array into half each time, there will be one side always in order, use it to continue search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) -1
        if nums == None or len(nums) == 0:
            return -1
        else:
            first = 0
            last = n
            
            while(first <= last):
                if(first == last and nums[first] == target):
                    return first
                elif(first == last and nums[first] != target):
                    return -1
                else:
                    left = min(first + int((last - first)/2), n)
                    right = min(left+1, n)

                    if(nums[first] == target):
                        return first
                    elif(nums[last] == target):
                        return last
                    elif(nums[left] == target):
                        return left
                    elif(nums[right] == target):
                        return right

                    if(nums[first] < nums[left] and (target > nums[first] and target < nums[left])):
                        last = left
                    elif(nums[first] < nums[left] and not(target > nums[first] and target < nums[left])):
                        first = right
                    elif(nums[right] < nums[last] and (target > nums[right] and target < nums[last])):
                        first = right
                    elif(nums[right] < nums[last] and not(target > nums[right] and target < nums[last])):
                        last = left
                    else:
                        return -1
            return -1
