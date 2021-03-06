# https://leetcode.com/problems/majority-element-ii/
# Logic: This can be solved using the Boyer-Moore Voting Algorithm. The intuition is that There can be at most one majority element which is more than ⌊n/2⌋ times.
# There can be at most two majority elements which are more than ⌊n/3⌋ times. There can be at most three majority elements which are more than ⌊n/4⌋ times. And so on
# So to find elements greater that ⌊n/3⌋ times, we just need 2 variables and we apply Boyer-Moore Voting Algorithm to get the result.

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        f = math.floor(n/3)
                
        result_1 = result_2 = None
        counter_1 = counter_2 = 0
        
        for i in range(0, n):
            if(nums[i] == result_1):
                counter_1 += 1
            elif(nums[i] == result_2):
                counter_2 += 1
            elif(counter_1 == 0):
                result_1 = nums[i]
                counter_1 += 1
            elif(counter_2 == 0):
                result_2 = nums[i]
                counter_2 += 1
            else:
                counter_1 -= 1
                counter_2 -= 1

        c1, c2 = 0, 0
        for i in range(n):
            if(nums[i] == result_1):
                c1 += 1
            if(nums[i] == result_2):
                c2 += 1
        answer = []
        if(c1 > f):
            answer.append(result_1)
        if(c2 > f):
            answer.append(result_2)
        return answer
