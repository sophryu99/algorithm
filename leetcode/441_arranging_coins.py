# https://leetcode.com/problems/arranging-coins/

"""
Approach:
1. Form a while loop with the condition that n is bigger than count
2. Track num of rows by incrementing count by 1 for one while loop
3. Reduction of n by count as coins are used for the row
3. If count for coin exceeds remaining coins(n), break while loop and return count

Exception:
- When n = 1, return 1

"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        
        count = 0
        while n > count:
            count += 1
            n = n - count
            
        return count

    
"""
Runtime: 888 ms, faster than 38.96% of Python3 online submissions for Arranging Coins.
Memory Usage: 14.1 MB, less than 89.86% of Python3 online submissions for Arranging Coins.
"""
