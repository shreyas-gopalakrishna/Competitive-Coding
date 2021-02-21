# https://leetcode.com/problems/broken-calculator
# Logic: The first thought is to use BFS/Recursion to go through all find steps take mininum. But this is a costly operation even if results are mapped and accessed(DP).
#        A better smart solution is greedy approach. Instead of going from X to Y, go from Y to X - divide by 2 when even and add 1 when odd until Y less than X.
#        Then add more if needed.
# If Y <= X, we won't do Y / 2 anymore.
# We will increase Y until it equals to X
#
# So before that, while Y > X, we'll keep reducing Y, until it's smaller than X.
# If Y is odd, we can do only Y = Y + 1
# If Y is even, if we plus 1 to Y, then Y is odd, we need to plus another 1.
# And because (Y + 1 + 1) / 2 = (Y / 2) + 1, 3 operations are more than 2.
# We always choose Y / 2 if Y is even. - greedy.


class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        count = 0
        while(Y > X):
            count += 1
            if(Y % 2 == 0):
                Y = Y / 2
            else:
                Y += 1
        return count + int(X-Y) 
