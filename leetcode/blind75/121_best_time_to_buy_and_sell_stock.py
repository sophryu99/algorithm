# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""
n = len(prices)
Runtime Complexity: O(n)
- One pass of very elements

Space complexity: O(1)
- No extra space used
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:                    
        max_profit, min_price = 0, float('inf')
        
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        
        return (max_profit)
    
"""
Runtime: 1151 ms, faster than 49.35% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25.2 MB, less than 55.44% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""
    
    
