# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#Second attempt

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Two pointer approach
        left = 0
        right = 1
        """
        nums = [1, 1, 1, 2]
        left = 0, right = 1 -> 1 == 1, right = 2
        left = 0, right = 2 -> 1 == 1, right = 3
        left = 0, right = 3 -> 1 < 2, nums[1: 3] = nums[3] * (3 - 0) = 2 * 2, nums = [1, 2, 2, 2], left = 1, right = left + 1 = 2
        left = 1, right = 2 -> 2 == 2, right = 3
        left = 1, right = 3 -> 2 == 2, right = 4
        
        """

        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            elif nums[left] < nums[right]:
                nums[left + 1: right] = [nums[right]] * (right - left - 1 )
                left += 1
                right = left + 1 
        
        return (left+1)
        
