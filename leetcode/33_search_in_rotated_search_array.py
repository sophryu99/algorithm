# https://leetcode.com/problems/search-in-rotated-sorted-array/

"""
Search for the range where the target is located and implement binary search within the range.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        maxx = max(nums)
        max_idx = nums.index(maxx)
        left = nums[0: max_idx + 1]
        right = nums[max_idx + 1: len(nums)]
        arr = left
        left_bool = True
        
        if left and right:
        # Check if the target is within either array
            if target <= left[-1] and target >= left[0]:
                arr = left
            elif target <= right[-1] and target >= right[0]:
                arr = right
                left_bool = False
            else:
                return -1
        low, high = 0, len(arr) - 1
        # Binary Search
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == target:
                # If right array was selected
                if not left_bool:
                    return mid + len(left)
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
            