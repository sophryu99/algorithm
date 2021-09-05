# https://leetcode.com/problems/power-of-four/

"""
1. If n is divisible by four, divide n by four and continue the loop
2. If n is not divisible by four, break the loop and return False
3. If the loop finished executing, return True
"""

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: 
            return False
        
        while n > 1:
            if n % 4 == 0:
                n = n / 4
            else:
                return False
            
        return True
    

"""
Runtime: 24 ms, faster than 96.11% of Python3 online submissions for Power of Four.
Memory Usage: 14.3 MB, less than 8.45% of Python3 online submissions for Power of Four.
"""