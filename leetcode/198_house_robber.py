# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        At each house we have the choice of robbing it or leaving it.
        case 1 – if we pick last house:
        then, we cant pick (n-1)th house, hence f(n)= An + f(n-2)
        case 2 – if we leave last house:
        then, we will stick with the max profit till (n-1)th house, hence f(n)= f(n-1)
        n = 0, clearly f(0) = A0.
        n = 1, then f(1) = max(A0, A1).
        f(n)= max( An + f(n-2) , f(n-1) )
        """
        
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        a = [0] * len(nums)
        a[0] = nums[0]
        a[1] = max(nums[0],nums[1])
        
        for i in range(2, len(nums)):
            a[i] = max(nums[i] + a[i - 2], a[i - 1])
        
        return (a[len(nums) - 1])
                
"""
Runtime: 28 ms, faster than 89.21% of Python3 online submissions for House Robber.
Memory Usage: 14.2 MB, less than 76.73% of Python3 online submissions for House Robber.
"""
