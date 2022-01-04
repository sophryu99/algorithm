# https://leetcode.com/problems/rotate-image/

"""
1. Transpose the matrix
2. Reverse every row elements of the transposed matrix
"""
import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i, row in enumerate(np.array(matrix).T):
            matrix[i] = row[::-1]
        
        
        
"""
Runtime: 92 ms, faster than 5.07% of Python3 online submissions for Rotate Image.
Memory Usage: 30.9 MB, less than 30.52% of Python3 online submissions for Rotate Image."""
