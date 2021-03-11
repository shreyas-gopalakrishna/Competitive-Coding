# https://leetcode.com/problems/coin-change/
# Logic: Standard DP question. 
# Video - https://youtu.be/Y0ZqKpToTic

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        DP = [float('inf')] * (amount + 1)
        DP[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                DP[i] = min(DP[i], DP[i - coin] + 1)
        
        if DP[amount] != float('inf'):
            return DP[amount]
        else:
            return -1
