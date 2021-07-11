# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1 ):
            if i not in nums:
                return i
        
"""
Runtime: 3420 ms, faster than 5.03% of Python3 online submissions for Missing Number.
Memory Usage: 15.5 MB, less than 48.80% of Python3 online submissions for Missing Number.
"""