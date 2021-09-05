# https://leetcode.com/problems/third-maximum-number/

"""
Level: Easy
1. Convert the list to a set to remove duplicates
2. Sort the list by descending order
3. Return the third maximum number if exists, if not, return the max. 
"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums), reverse = True)
        if len(nums) >= 3:
            return nums[2]
        else:
            return nums[0]


"""
Runtime: 48 ms, faster than 88.62% of Python3 online submissions for Third Maximum Number.
Memory Usage: 15.5 MB, less than 42.73% of Python3 online submissions for Third Maximum Number.
""" 