# https://leetcode.com/problems/search-insert-position/

"""
Binary Search Algorithm
1. Search from the middle index of the array
2. If the element at the index is less than the target, move right
3. If the element at the index is larger than the target, move left
4. Continue this until the left and the right index equates
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
                    
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            else:
                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return left
            
            
"""
Runtime: 89 ms, faster than 8.74% of Python3 online submissions for Search Insert Position.
Memory Usage: 14.9 MB, less than 94.14% of Python3 online submissions for Search Insert Position.
"""