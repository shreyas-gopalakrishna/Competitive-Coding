# https://leetcode.com/problems/strobogrammatic-number/
# Logic: Construct the reverse of the number while also rotating each number. The result must be equal to the original number

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        n = len(num)
        s = ''
        for i in range(n-1, -1, -1):
            if(num[i] == '0' or num[i] == '1' or num[i] == '8'):
                s += num[i]
            elif( num[i] == '6'):
                s += '9'
            elif( num[i] == '9'):
                s += '6'
            else:
                return False
        
        if(s == num):
            return True
        else:
            return False
