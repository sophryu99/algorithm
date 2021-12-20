# https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        1
        1 1
        1 2 1
        1 3 3 1
        """
        base = [1]
        for _ in range(rowIndex):
            row = [1]
            for i in range(1, len(base)):
                firstele = base[i - 1]
                secondele = base[i]
                row.append(firstele + secondele)
            row.append(1)
            base = row
        
        return base
                    
"""
Runtime: 32 ms, faster than 66.64% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 14.2 MB, less than 77.98% of Python3 online submissions for Pascal's Triangle II.
"""