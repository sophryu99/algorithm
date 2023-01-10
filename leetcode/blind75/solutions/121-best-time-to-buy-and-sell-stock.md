### https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
- Scan through the list with a nested for loop and calculate every possible combination of profit
- TLE as runtime is O(n^n)
# Approach
<!-- Describe your approach to solving the problem. -->
- Two pointer approach with first and second index
- Loop until right index reaches the length of the array. If the left index is less than the right index, reset the two pointers and continue scan until the two pointers equate to len(prices).

# Complexity
- Time complexity: O(log(n))
- Space complexity: O(1)

# Code
```python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxprofit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxprofit = max(profit, maxprofit)
            else:
                left = right
            right += 1
            if right == len(prices) and left <= right:
                left += 1
                right = left + 1
            
        return maxprofit
            
```
