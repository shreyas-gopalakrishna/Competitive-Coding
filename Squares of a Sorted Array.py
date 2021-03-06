# https://leetcode.com/problems/squares-of-a-sorted-array/
# Logic: Approach 1: Use absolute value of all elements and then sort - O(nlog n)
#        Appeoach 2: This is better. Use 2 pointers at either end to check which element has abs() value greater and update that in a copy list. - O(n) but extra memory.

class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l,r = 0, n-1
        
        result = [0 for i in range(n)]
        
        for i in range(n-1, -1, -1):
            if(abs(nums[l]) > abs(nums[r])):
                result[i] = nums[l] ** 2
                l += 1
            else:
                result[i] = nums[r] ** 2
                r -= 1
        return result
                
class Solution:
   def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        nums.sort()
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        return nums
        
