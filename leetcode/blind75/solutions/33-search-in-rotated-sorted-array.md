### https://leetcode.com/problems/search-in-rotated-sorted-array/description/

# Approach
- Binary Search for O(log n) time complexity
- The key is to determine if the array is **right or left rotated**
```
# Original
1 2 3 4 5
    mid

# Left-rotated -> arr[mid] > arr[left]
2 3 4 5 1
    mid

# Right-rotated -> arr[mid] < arr[left]
5 1 2 3 4
    mid
```



# Complexity
- Time complexity: O(log n) with binary search

- Space complexity: O(1) no extra space used

# Code
```python3

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            # The array is left rotated
            if nums[mid] >= nums[left]:
                # If the target number is in between the left side of the array, reset right index to continue search on the left side
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1 
            # The array is right rotated
            else:
                # If the target number is in between the right side of the array, reset left index to continue search on the right side
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        # If not in the array
        return -1

```
