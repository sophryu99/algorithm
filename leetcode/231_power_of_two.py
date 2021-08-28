# https://leetcode.com/problems/power-of-two/

"""
1. if n == 1, return True
2. if n == 0 or less than 0, return False
3. While n is an integer larger than 1, check if it is divisible by 2.
4. If it is not divisible, break loop and return False
5. If the while loop execution is over, return True
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0:
            return False
        
        while n > 1:
            if n % 2 == 0:
                n = n / 2
            else:
                return False
        
        return True
       
"""
Runtime: 28 ms, faster than 87.47% of Python3 online submissions for Power of Two.
Memory Usage: 14.3 MB, less than 8.01% of Python3 online submissions for Power of Two.
"""