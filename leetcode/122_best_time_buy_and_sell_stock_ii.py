# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        prices = [7,1,5,3,6,4]
        i = 0, j = 1
        diff = 0
        if p[i] < p[j]: 
        i = 1, j = i + 1
        
        """
        i = 0
        v = prices[0]
        p = prices[0]
        maxprofit = 0
        while i < len(prices) - 1:
            # while i is less than the length and the element at prices[i] is larger than the next element
            # Increment i until the condition is broken (finding points where profit is made)
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            # Re-assign valley
            v = prices[i]
            # From the valley, increment i until the next element is larger than the current element
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            # Re-assign peak
            p = prices[i]
            maxprofit += p - v
        return maxprofit
                
        
        
"""
Runtime: 60 ms, faster than 78.23% of Python3 online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 15 MB, less than 89.37% of Python3 online submissions for Best Time to Buy and Sell Stock II.
"""