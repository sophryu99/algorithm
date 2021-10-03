# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        """
        [[1, 1, 1, 1, 1, 1, 1], 
         [1, 0, 0, 0, 0, 0, 0], 
         [1, 0, 0, 0, 0, 0, 0]]
        """
        t = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # Initialize border lines of the map as 1
                if i == 0 or j == 0:
                    t[i][j] = 1
                else:
                    t[i][j] = t[i-1][j] + t[i][j - 1]
                    
        return t[m - 1][n - 1]
                    
"""
Runtime: 32 ms, faster than 70.05% of Python3 online submissions for Unique Paths.
Memory Usage: 14.2 MB, less than 86.10% of Python3 online submissions for Unique Paths
"""