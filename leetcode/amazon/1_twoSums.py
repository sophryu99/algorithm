class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in nums[i + 1:]:
                return [i, nums[i + 1:].index(remainder) + len(nums) - len(nums[i+1:])]
                        
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in nums[i + 1:]:
                return [i, nums[i + 1:].index(remainder) + len(nums) - len(nums[i+1:])]
                
"""
Runtime: 682 ms, faster than 36.76% of Python3 online submissions for Two Sum.
Memory Usage: 14.6 MB, less than 98.24% of Python3 online submissions for Two Sum.
"""