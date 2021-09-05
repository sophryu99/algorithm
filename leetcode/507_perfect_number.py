# https://leetcode.com/problems/perfect-number/

"""
1.Check every number from [2, sqrt(n)]
2.If the number num is divisible by the divisor then the sum so far is sum += divisor + num / divisor as num will also be divisible by num / divisor.
3.We did not check with 1 as everynumber is divisble by 1 and simply add that in the end.
"""
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1: return False

        divisior_sum, divisior = 0, 2
        while divisior * divisior <= num:
            if num % divisior == 0:
                divisior_sum += (divisior + num // divisior)
            divisior += 1
        return (divisior_sum + 1) == num

"""
Runtime: 40 ms, faster than 63.16% of Python3 online submissions for Perfect Number.
Memory Usage: 14.1 MB, less than 69.74% of Python3 online submissions for Perfect Number.
"""