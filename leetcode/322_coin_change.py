# https://leetcode.com/problems/coin-change/
"""
Approach: DP

coins = [1, 2, 5], amount = 7

1 1 [0, 1, inf, inf, inf, inf, inf, inf]
1 2 [0, 1, 2, inf, inf, inf, inf, inf]
1 3 [0, 1, 2, 3, inf, inf, inf, inf]
1 4 [0, 1, 2, 3, 4, inf, inf, inf]
1 5 [0, 1, 2, 3, 4, 5, inf, inf]
1 6 [0, 1, 2, 3, 4, 5, 6, inf]
1 7 [0, 1, 2, 3, 4, 5, 6, 7]
2 2 [0, 1, 1, 3, 4, 5, 6, 7]
2 3 [0, 1, 1, 2, 4, 5, 6, 7]
2 4 [0, 1, 1, 2, 2, 5, 6, 7]
2 5 [0, 1, 1, 2, 2, 3, 6, 7]
2 6 [0, 1, 1, 2, 2, 3, 3, 7]
2 7 [0, 1, 1, 2, 2, 3, 3, 4]
5 5 [0, 1, 1, 2, 2, 1, 3, 4]
5 6 [0, 1, 1, 2, 2, 1, 2, 4]
5 7 [0, 1, 1, 2, 2, 1, 2, 2]
[0, 1, 1, 2, 2, 1, 2, 2]
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1. Initialize a dp array of amount + 1 dimension
        dp = [inf for _ in range(amount + 1)]           
        dp[0] = 0
        
        # 2. Sort the coin array in an ascending order
        coins = sorted(coins)
        
        # 3. For every coins,
        for x in coins:
            # 3.1 Iterate starting from the coin value
            for y in range(x, amount + 1):
                # 3.2 Set dp[y] value as a smaller value of dp[y - x] and dp[y]
                dp[y] = min(dp[y - x] + 1, dp[y])
                
        # 4. Check if any cases summed up to the amount
        if dp[-1] == inf:
            return -1
        return dp[-1]
        
        
"""
Runtime: 1413 ms, faster than 69.67% of Python3 online submissions for Coin Change.
Memory Usage: 14.4 MB, less than 80.59% of Python3 online submissions for Coin Change.

"""