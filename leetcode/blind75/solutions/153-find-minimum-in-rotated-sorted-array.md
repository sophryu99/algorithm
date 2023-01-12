### https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

# Approach
- The key is to locate the index of the list where the number at the index is smaller than the number at index + 1
- Binary Search since the question needs to be solved O(log(n))
- [Binary Search pseudocode](https://github.com/sophryu99/TIL/issues/43)

# Complexity
- Time complexity: O(log(n)) as binary search

- Space complexity: O(1) no extra space used

# Code
```python3
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # If the array is already sorted, return the first element
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            # If the current number is smaller than mid - 1, located the smallest number
            if 0 < mid and nums[mid] < nums[mid - 1]: 
                return nums[mid]
            # If the nums[mid] is larger nums[right], still need to search through the smallest number on the right side of the list, reset left index
            if nums[mid] > nums[right]:
                left = mid + 1
            # Else, search the minimum on the left side
            else:
                right = mid - 1
                

```
