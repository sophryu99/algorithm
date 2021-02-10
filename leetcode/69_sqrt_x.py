# https://leetcode.com/problems/sqrtx/

"""
Approach:
1. Num ** 1/2
2. Truncate only the integer part
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x ** 0.5)

"""
Runtime: 28 ms, faster than 94.60% of Python3 online submissions for Sqrt(x).
Memory Usage: 14.3 MB, less than 44.31% of Python3 online submissions for Sqrt(x).
"""
