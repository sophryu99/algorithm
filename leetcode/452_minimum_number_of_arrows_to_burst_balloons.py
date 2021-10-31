# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # Sort by the second element of each points
        points.sort(key = lambda x: x[1])
        arrows = 1
        first_end = points[0][1]
        
        for x, y in points:
            # If the end point is less than the next start point
            if first_end < x:
                # Increment arrows and reset first_end as the end point for the current point
                arrows += 1
                first_end = y
                
        return arrows


"""Runtime: 1308 ms, faster than 69.47% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.
Memory Usage: 59.1 MB, less than 69.29% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons
"""