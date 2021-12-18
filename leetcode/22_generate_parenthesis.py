# https://leetcode.com/problems/generate-parentheses/

# Backtracking
"""
1. If we still have one left to place, we will start an opening bracket
2. Start a closing bracket if it would not exceed the number of opening brackets
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pairs = []
        
        def backtrack(s = [], left = 0, right = 0):
            
            if len(s) == 2 * n:
                pairs.append("".join(s))
                return
            
            if left < n: 
                s.append("(")
                backtrack(s, left + 1, right)
                s.pop()
                
            if right < left:
                s.append(")")
                backtrack(s, left, right + 1)
                s.pop()
            
        backtrack()
        return pairs
        
            
"""
Runtime: 28 ms, faster than 96.03% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14.5 MB, less than 68.44% of Python3 online submissions for Generate Parentheses.
"""

            
        
        
        
        
        
        
        