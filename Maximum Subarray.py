# https://leetcode.com/problems/maximum-subarray/
# Logic: Problem can be visualized better in 2D DP approach. But since we only access one row at a time DP in not needed
#        In a 1D greedy approach, each time, current max will be the (element or element + previous sum). Can be done with just 1 variable
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        A = 0
        result = -float('inf')
        for i in range(n):
            if(i == 0):
                A = nums[i]
            else:
                A = max(nums[i],nums[i] + A)
            result = max(A, result)
        return result

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        A = [-float('inf') for i in range(n)]
        result = -float('inf')
        for i in range(n):
            if(i == 0):
                A[i] = nums[i]
            else:
                A[i] = max(nums[i],nums[i] + A[i-1])
            result = max(A[i], result)
        return result

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        A = list()
        result = -float('inf')
        for i in range(0,n):
            a = list()
            for j in range(0,n):
                a.append(-float('inf'))
            A.append(a)
        for i in range(0,n):
            for j in range(0,n):
                if(i == j):
                    A[i][j] = nums[i]
                elif(j > i):
                    if(i == 0):
                        A[i][j] = nums[j] + A[0][j-1]
                    else:
                        A[i][j] = nums[j] + A[i][j-1]
                if(A[i][j] > result):
                    result = A[i][j]
        return result
