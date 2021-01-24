#https://leetcode.com/problems/two-sum/submissions/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force approach
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[j] == target - nums[i]:
                        return i, j
                        break

"""
Runtime: 48 ms, faster than 63.01% of Python3 online submissions for Two Sum.
Memory Usage: 14.3 MB, less than 75.07% of Python3 online submissions for Two Sum.
"""
                        
