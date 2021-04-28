# https://leetcode.com/problems/k-closest-points-to-origin/

import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        coords = []
        
        for p in range(len(points)):
            x, y = points[p][0], points[p][1]
            dist = math.sqrt(x**2 + y**2)
            coords.append([x, y, dist])
            
        sort_orders = sorted(coords, key=lambda x: x[2], reverse=False)
        
        res = [sort_orders[i][0:2] for i in range(len(sort_orders))]
        return (res[0:k])

"""
Runtime: 688 ms, faster than 50.04% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 20.2 MB, less than 30.96% of Python3 online submissions for K Closest Points to Origin.
"""
