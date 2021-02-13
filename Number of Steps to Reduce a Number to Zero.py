# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# Logic: Normal division and increase count. Can also be done bitwise, if bit is 1 increment twice, if 0 increment once.

class Solution:
    def numberOfSteps (self, num: int) -> int:
        if(num == 0):
            return 0
        elif(num == 1):
            return 1
        else:
            n = 2
            count = 0
            while(num > 0):
                if(num % 2 == 0):
                    num = num/2
                else:
                    num -= 1
                count += 1
                # print(num, count)
            return count
