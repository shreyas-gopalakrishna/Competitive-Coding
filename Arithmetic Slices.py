# https://leetcode.com/problems/arithmetic-slices/
# Logic: Every time a number is added, if the difference is same, the number of new combinations is (1 + prev no. of new combinations).
#        The total will be sum of all the new combinations (cumulative sum).
# [1,2,3] --> [1,2,3] --> 1 combination
# [1,2,3,4] --> add new combination [2,3,4], [1,2,3,4] --> 2 new combs. Total = 2 + 1
# [1,2,3,4,5] --> add new combination [3,4,5],[2,3,4,5],[1,2,3,4,5] --> 3 new combs. Total = 3 + 2 + 1

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if(len(A) < 3):
            return 0
        
        result = 0
        count = 0
        n = len(A)
        
        for i in range(0, n-2):
            if(A[i+1] - A[i] == A[i+2] - A[i+1]):
                count += 1
            else:
                count = 0
            result += count
        return result
            
