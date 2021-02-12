# https://leetcode.com/problems/move-zeroes

"""
Approach:
Two pointers
1. If the current element is nonzero, append the element just infront of last non zero element.
2. Keep track of lastzero index
3. After shifting every nonzero element to the front of the list, fill in the rest of the list with zeros

Exception:
- Don't use extra memory, modify nums in-place instead.
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lastzeroindex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastzeroindex] = nums[i]
                lastzeroindex += 1
        for i in range(lastzeroindex, len(nums)):
            nums[i] = 0
"""
Runtime: 44 ms, faster than 93.64% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.4 MB, less than 21.94% of Python3 online submissions for Move Zeroes.
"""    
        
