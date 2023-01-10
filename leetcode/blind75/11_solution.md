### https://leetcode.com/problems/container-with-most-water
# Approach
<!-- Describe your approach to solving the problem. -->
Two pointer approach:
1. Set left index as 0, right index as the length of the array. Continue the process until left == right.
2. If height[left] < height[right], increment left index, else, decrement right index. 
3. This is because for height[0] -> 1, height[8] -> 7, the width is going to be only smaller. 
The smaller height does not need to be compared as height[0] -> 1 * height[7] -> 3 ... height[6] -> 8 is guaranteed to be smaller than the current maxwater.

# Complexity
- Time complexity: O(n) -> worst case a complete scan through the list
- Space complexity: O(1) -> no extra space used

# Code
```
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxwater = 0

        while left < right:
            if height[left] < height[right]:
                area = height[left] * (right - left)
                maxwater = max(maxwater, area)
                left += 1
            else:
                area = height[right] * (right - left)
                maxwater = max(maxwater, area)
                right -= 1
        
        return maxwater






```
