# https://leetcode.com/problems/container-with-most-water/

"""
Two pointer approach:
1. Set left index as 0, right index as the length of the array. Continue the process until left == right.
2. If height[left] < height[right], increment left index, else, decrement right index
2-1. This is because for height[0] -> 1, height[8] -> 7, the width is going to be only smaller. The smaller height does not need to be compared as height[0] -> 1 * height[7] -> 3 ... height[6] -> 8 is guaranteed to be smaller than the current maxwater.

[1,8,6,2,5,4,8,3,7]

left: 1 right: 8
left ele: 8 right ele: 7
maxwater: 8
---
left: 1 right: 7
left ele: 8 right ele: 3
maxwater: 49
---
left: 1 right: 6
left ele: 8 right ele: 8
maxwater: 49
---
left: 2 right: 5
left ele: 6 right ele: 4
maxwater: 49
---
left: 2 right: 4
left ele: 6 right ele: 5
maxwater: 49
---
left: 2 right: 3
left ele: 6 right ele: 2
maxwater: 49
---
left: 2 right: 2
left ele: 6 right ele: 6
maxwater: 49
---
Time Complexity: O(n)
- Will be a linear scan with a two pointer approach

Space Complexity: O(1)
- No extra space needed
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxwater = 0
        l, r = 0, len(height) - 1
        while l < r:
            h = min(height[l], height[r])
            maxwater = max(maxwater, h * (r - l))
            # If the left element is the height, increment left index
            l = l + (height[l] == h)
            # If the right element is the height, decrement right index
            r = r - (height[r] == h)            
            
            # print('left:', l, 'right:', r)
            # print('left ele:', height[l], 'right ele:', height[r])
            # print('maxwater:', maxwater)
            # print('---')
        return maxwater
    
"""
Runtime: 756 ms, faster than 62.56% of Python3 online submissions for Container With Most Water.
Memory Usage: 27.6 MB, less than 23.31% of Python3 online submissions for Container With Most Water.
"""
        
        