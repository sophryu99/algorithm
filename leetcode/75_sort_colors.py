# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        [2,0,2,1,1,0]
        
        minn_idx = 1, temp = 2, nums[0] = 0, nums[1] = 2, left = 1
        nums = [0, 2, 2, 1, 1, 0], part = [2, 2, 1, 1, 0]
        
        minn_idx = 5, temp = 2, nums[1] = nums[5] = 0, nums[5] = 2, left = 2
        nums = [0, 0, 2, 1, 1, 2], part = [2, 1, 1, 2]
        
        minn_idx = 3, temp = 2, nums[2] = nums[3] = 1, nums[3] = 2, left = 3
        nums = [0, 0, 1, 2, 1, 2], part = [2, 1, 2]
        
        minn_idx = 4, temp = 2, nums[3] = nums[4] = 1, nums[4] = temp = 2, left = 4
        nums = [0, 0, 1, 1, 2, 2], part = [2,2]
        
        part[0] = 2, min(part) = 2, part = nums[5:]
        nums = [0, 0, 1, 1, 2, 2], part = [2], left = 5
        """
        
        
        if len(nums) == 1:
            return nums
        
        left = 0
        part = nums
        while left < len(nums):
            # Check if the first element is minimum
            if part[0] == min(part):
                part = nums[left + 1:]
                left += 1
            # If not the first element, swap with minimum val
            else:
                minn_idx = nums[left:].index(min(part)) + left
                #print(minn_idx)
                temp = part[0]
                nums[left] = nums[minn_idx]
                nums[minn_idx] = temp
                part = nums[left + 1:]
                left += 1
            
                #print(left, part)
        
"""
Runtime: 53 ms, faster than 14.53% of Python3 online submissions for Sort Colors.
Memory Usage: 14.1 MB, less than 92.11% of Python3 online submissions for Sort Colors.
"""