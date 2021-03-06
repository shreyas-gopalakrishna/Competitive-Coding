# https://leetcode.com/problems/majority-element/
# Logic: The majority element is the element that appears more than ⌊n / 2⌋ times in an array. This can be solved using a hashmap in O(n) which uses O(n) space.
#        A much better approach is using the Boyer-Moore Voting Algorithm. https://www.youtube.com/watch?v=n5QY3x_GNDg
#        Use a result to update majority element and then a counter to count. After traversal, we get a majortity element. It must be checked again to verify if true.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        f = math.floor(n/2)
        
        result = nums[0]
        counter = 1
        for i in range(1, n):
            if nums[i] != result:
                counter -= 1
            else:
                counter += 1
                
            if(counter == 0):
                result = nums[i]
                counter += 1
            # print(result, counter)
        c = 0
        for i in range(n):
            if(nums[i] == result):
                c += 1
        if(c > f):
            return result
        
