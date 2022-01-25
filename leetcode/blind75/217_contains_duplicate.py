# https://leetcode.com/problems/contains-duplicate/

"""
Compare the set of the array and the array's length
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)