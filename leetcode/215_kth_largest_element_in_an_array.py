# https://leetcode.com/problems/kth-largest-element-in-an-array/

"""
Level: Medium
1. Sort the array and return the kth element of the array
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse = True)
        return nums[k-1]


"""
Runtime: 64 ms, faster than 74.38% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 15 MB, less than 93.27% of Python3 online submissions for Kth Largest Element in an Array.
"""