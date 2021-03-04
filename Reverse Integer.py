# https://leetcode.com/problems/reverse-integer/
# Logic: Reverse and check if it's between the limits

class Solution:
    def reverse(self, num: int) -> int:
        def reverse(num):
            flag = False
            if(num < 0):
                flag = True
            num = abs(num)
            
            count = 0
            while(num != 0):
                count = (count*10) + num%10
                num = int(num/10)
            
            if(flag):
                return -count
            else:
                return count
        
        if(num == 0):
            return 0
        num = reverse(num)
        if(num >= pow(-2, 31) and num <= (pow(2,31)-1)):
            return num
        else:
            return 0
