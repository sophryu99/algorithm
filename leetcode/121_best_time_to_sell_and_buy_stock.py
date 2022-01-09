# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""
Solving Time: 4:00 - 4:10
Find the point where maximum increase is followed by minimum decrease.

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = inf
        maxprofit = 0
        
        for i in range(len(prices)):
            # If curr prices is less than minprice, minprice becomes the currprice
            if prices[i] < minprice:
                minprice = prices[i]
            # If the difference of the currprice and the minprice is larger than maxprofit, maxprofit becomes the difference
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice
                
        return maxprofit
                    
"""
Runtime: 1814 ms, faster than 7.63% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25.2 MB, less than 11.88% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""
            
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit

"""
Runtime: 1362 ms, faster than 20.43% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 24.8 MB, less than 98.23% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""