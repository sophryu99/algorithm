# https://leetcode.com/problems/container-with-most-water/

### Time Limit Exceeded
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxh = 0
        for i in range(len(height)):
            w = 0
            for j in range(i + 1, len(height)):
                h = min(height[i], height[j])
                w += 1
                if (h * w) > maxh:
                    maxh = h * w
                    
        return maxh


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        i = 0
        j = l-1
        area = 0
        h = height
        while(i < j):
            if h[i] < h[j]:
                area = max(area, h[i] * (j -  i))
                i += 1
            else:
                area = max(area, h[j] * (j - i))
                j -= 1
        return area


"""
Runtime: 716 ms, faster than 78.67% of Python3 online submissions for Container With Most Water.
Memory Usage: 27.7 MB, less than 25.26% of Python3 online submissions for Container With Most Water.
"""