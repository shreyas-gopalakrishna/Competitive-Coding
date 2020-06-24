# https://leetcode.com/problems/single-number-ii/
# Logic: Map counts, and delete if reaches 3. The key left is answer
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        D = dict()
        for num in nums:
            if(num in D):
                if D[num] == 2:
                    del D[num]
                else:
                    D[num] += 1
            else:
                D[num] = 1
        return list(D.keys())[0]
                
