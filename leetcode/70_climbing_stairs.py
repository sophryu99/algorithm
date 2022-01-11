"""
Intuition: Fibonacci
dp[i] = dp[i - 1] + dp[i - 2]
climb = [climb(0), climb(1), climb(2)n= climb(0) + climb(1),......climb(n) = climb(n-1)+climb(n-2)]
dp = [ 0, 1, 2, 3, 5, dp(i-1)+dp(i-2])]

"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        # Total count, step one, step two
        count, one_step, two_step = 0, 1, 2
        cnt = 2
        while cnt < n:
            # print(count, one_step, two_step)
            count = one_step + two_step
            one_step = two_step
            two_step = count
            cnt += 1
        
        return count

"""
Runtime: 32 ms, faster than 60.13% of Python3 online submissions for Climbing Stairs.
Memory Usage: 14.2 MB, less than 72.92% of Python3 online submissions for Climbing Stairs.
"""

"""
DP Approach
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2, 3]
        if n < 3:
            return dp[n]
        
        while len(dp) < n + 1:
            dp.append(dp[-1] + dp[-2])
        
        return dp[-1]

"""
Runtime: 48 ms, faster than 13.19% of Python3 online submissions for Climbing Stairs.
Memory Usage: 14 MB, less than 98.21% of Python3 online submissions for Climbing Stairs.
"""