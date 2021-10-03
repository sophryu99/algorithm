# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        N = len(coins)
        # Initialize a [inf] * amount array to count for cases that make up to ith amount
        dp = [float("infinity") for _ in range(amount + 1) ]
        dp[0] = 0
        
        
        for i in range(len(dp)):
            if dp[i] == float("infinity"): 
                continue
            for coin in coins:
                # If coin + i is within the range of amount
                if i + coin < len(dp): 
                    
                    dp[i+coin] = min(dp[i+coin], 1 + dp[i])
           
        
        return dp[-1] if dp[-1] != float("infinity") else -1
        
        
"""
Runtime: 1976 ms, faster than 26.43% of Python3 online submissions for Coin Change.
Memory Usage: 14.7 MB, less than 48.24% of Python3 online submissions for Coin Change.
"""