# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        while k > 0:
            popped = nums.pop()
            nums.insert(0, popped)
            k -=1
            
"""
Runtime: 4147 ms, faster than 5.09% of Python3 online submissions for Rotate Array.
Memory Usage: 25.5 MB, less than 53.58% of Python3 online submissions for Rotate Array.
"""