# https://leetcode.com/problems/ugly-number/
"""
1. While n > 1, check if it is divisible by 2, 3, 5. If so, divide n.
2. If n is not divisible anymore, return False
3. Return true if while loop finishes without break
"""
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n > 1:
            if n == 7:
                return False
            if n % 2 == 0:
                n = n / 2
            elif n % 3 == 0:
                n = n / 3
            elif n % 5 == 0:
                n = n / 5
            else:
                return False
        
        return True
        
"""
Runtime: 51 ms, faster than 12.15% of Python3 online submissions for Ugly Number.
Memory Usage: 14 MB, less than 90.35% of Python3 online submissions for Ugly Number.
"""