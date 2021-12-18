# https://leetcode.com/problems/spiral-matrix-ii/

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initiate a n*n matrix
        mapp = [[0] * n for _ in range(n)]
        
        # 1. Iterate the first row left -> right : mapp[i][j + 1]
        # 2. Iterate the last column up -> down: mapp[i + 1][j]
        # 3. Iterate the last row right -> left: mapp[i][j - 1]
        # 4. Iterate the first column down -> up: mapp[i - 1][j]
        
        col_start, col_end = 0, n - 1
        row_start, row_end = 0, n - 1
        mapp[0][0] = 1
        num = 1
        while col_start <= col_end and row_start <= row_end:
            # Fill left -> right
            for j in range(col_start, col_end + 1):
                mapp[row_start][j] = num
                num += 1
                            
            # Fill up -> down
            for i in range(row_start + 1, row_end + 1):
                mapp[i][col_end] = num
                num += 1
                
            # Fill right -> left
            for j in range(col_end - 1, col_start - 1, -1):
                mapp[row_end][j] = num
                num += 1

            # Fill down -> up
            for i in range(row_end - 1, row_start, -1):
                mapp[i][col_start] = num
                num += 1

            col_start += 1
            col_end -= 1
            row_start += 1
            row_end -= 1
        
        return mapp

"""
Runtime: 20 ms, faster than 99.33% of Python3 online submissions for Spiral Matrix II.
Memory Usage: 14.4 MB, less than 18.42% of Python3 online submissions for Spiral Matrix II.
"""