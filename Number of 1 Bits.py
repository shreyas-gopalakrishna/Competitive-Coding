# https://leetcode.com/problems/number-of-1-bits/solution/
# Logic: Dividing by 2 helps compute the binary, inturn counting the 1's in the number. We can also use 1 mask at each place and >> operator to check all digits 

class Solution:
    def hammingWeight(self, n: int) -> int:
        # print(str(n))
        if( n == 0 or n == 1):
            return n
        ans = 0
        while(n >= 2):
            ans += n % 2
            n = int(n / 2)
        return ans + 1
