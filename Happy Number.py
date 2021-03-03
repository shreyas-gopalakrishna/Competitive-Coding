# https://leetcode.com/problems/happy-number/
# Logic: The series repeats itself after a while, this tells that there might exist a loop and hence return false. else we reach 1 and return true

class Solution:
    def isHappy(self, n: int) -> bool:
        def check(num):
            total = 0
            while(num != 0):
                total += ((num%10) ** 2)
                num = int(num / 10)
            return total
        D = dict()
        while(True):
            if(n == 1):
                return True
            elif(n in D):
                return False
            D[n] = 1
            n = check(n)
