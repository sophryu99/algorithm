# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans, pos = 0, 0
        for letter in reversed(columnTitle):
            digit = ord(letter)-64
            ans += digit * 26**pos
            pos += 1
            
        return ans

"""
Runtime: 47 ms, faster than 52.84% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 13.9 MB, less than 62.26% of Python3 online submissions for Excel Sheet Column Number.

"""