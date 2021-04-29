# https://leetcode.com/problems/triangle/
# https://sophuu.tistory.com/72

"""
2
3 4
6 5 7
4 1 8 3

"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] = triangle[i][j] + triangle[i-1][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] = triangle[i][j] + triangle[i-1][j - 1]
                else:
                    triangle[i][j] = triangle[i][j] + min(triangle[i - 1][j - 1], triangle[i - 1][j])
                    
        
        return min(triangle[-1])
            
        
"""
Runtime: 64 ms, faster than 36.01% of Python3 online submissions for Triangle.
Memory Usage: 15.2 MB, less than 24.34% of Python3 online submissions for Triangle."""