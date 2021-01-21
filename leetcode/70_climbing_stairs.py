class Solution:
    def climbStairs(self, n: int) -> int:
        # loop fib algorithm
        if n == 0 or n == 1 or n == 2:
            return n
        count, one_step, two_step = 0, 1, 2
        for i in range(2, n):
            count = one_step + two_step
            one_step = two_step
            two_step = count
        return count
        
        
        
"""
Runtime: 32 ms, faster than 54.46% of Python3 online submissions for Climbing Stairs.
Memory Usage: 14.3 MB, less than 46.79% of Python3 online submissions for Climbing Stairs.
"""
