"""
https://leetcode.com/problems/rotate-image/

Implementation

Time complexity: O(M)
- M: number of cells in the matrix
- Each cell is getting read once and written once

Space complexity: O(1)
- Not using extra space
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                # Temp stores the lower left element of the array
                tmp = matrix[n - 1 - j][i]
                # Lower-right to Lower-left
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                # Upper-right to Lower-right
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                # Upper-left to Upper-right
                matrix[j][n - 1 - i] = matrix[i][j]
                # Lower-left(temp) to Upper-right
                matrix[i][j] = tmp
        
        
        
        