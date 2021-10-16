#  https://leetcode.com/problems/minimum-path-sum/

"""
Level: medium

1. Create an empty grid of dimension M * N
2. Iterate through the grid and search right, down
3. For each iteration, increment the value of dp[x][y] with the smaller value searched (right, down)
4. Return the value of the last index
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        # Check if the coordinate is within the grid range
        def check(x, y):
            return 0 <= x < m and 0 <= y < n
        
        # To right or down
        dx, dy = [0, 1], [1, 0]
        
        for x in range(m):
            for y in range(n):
                for dir in range(2):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if check(nx, ny):
                        if not dp[nx][ny]:
                            dp[nx][ny] = dp[x][y] + grid[nx][ny]
                        else:
                            dp[nx][ny] = min(dp[nx][ny], dp[x][y] + grid[nx][ny])
                            
                        
        return dp[-1][-1]
                
"""
Runtime: 128 ms, faster than 35.65% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 15.5 MB, less than 81.47% of Python3 online submissions for Minimum Path Sum.
"""