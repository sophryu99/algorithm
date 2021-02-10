# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

"""
Approach:
Binary search - two pointer approach
1. Add up elements from start and end point
2. If the target is less than the sum, shift the end pointer 
3. If the target is larger than the sum, shift the start pointer
4. Repeat until the sum equates the target

"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0                                           # left index
        end = len(numbers) - 1                              # right index
        
        while start < end:                                  # while the pointers to not meet
            if numbers[start] + numbers[end] == target:     # if the sum equals to the target
                return [start + 1, end + 1]                 # return the index of both pointers
            elif numbers[start] + numbers[end] > target:    # if the target is smaller
                end -= 1                                    # shift the right pointer
            else:                                           # if the target is larger
                start += 1                                  # shift the left pointer
        
"""
Runtime: 56 ms, faster than 95.94% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 14.5 MB, less than 86.35% of Python3 online submissions for Two Sum II - Input array is sorted.
"""
