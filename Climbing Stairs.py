# https://leetcode.com/problems/climbing-stairs/
# Logic: Hash previous solutions and count using recursion.
class Solution:
    def climb(self, D, n):
        if(n in D):
            return D[n]
        a = self.climb(D,n-1)
        b = self.climb(D, n-2)
        D[n-1] = a
        D[n-2] = b
        return a+b
    
    def climbStairs(self, n: int) -> int:
        D = dict()
        D[0] = 0
        D[1] = 1
        D[2] = 2
        return self.climb(D,n)
