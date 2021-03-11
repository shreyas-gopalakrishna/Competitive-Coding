# https://leetcode.com/problems/integer-to-roman/solution/
# Logic: Use greedy approach to first add in the symbols if they are in the predefined set of dict. If not then compute it using multiples.

class Solution:
    def intToRoman(self, num: int) -> str:
        
        def roman(a):
            key = None
            s = ''
            for k,v in D.items():
                if(a - k < 0):
                    break
                key = k
            for i in range(int(a/key)):
                a -= key
                s += D[key]
            return s,a
            
        
        D = { 1:'I',  5:'V', 10:'X', 50:'L', 100:'C', 500:'D',  1000:'M'}
        S = {4:'IV', 9:'IX', 40: 'XL', 90:'XC', 400: 'CD', 900:'CM'}
        
        count = 1
        
        result = ''
        
        while(num > 0):
            a = (num % 10)*(count)
            if(a in S):
                result = S[a] + result
            elif(a in D):
                result = D[a] + result
            else:
                b = ''
                while(a > 0):
                    s,a = roman(a)
                    b += s
                
                result = b + result
                
            count *= 10
            num = int(num/10)
        
        return result
        
        
        
