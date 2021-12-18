# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        
        leftchar = ['(', '{', '[']
        rightchar = [')', '}', ']']
        
        for i in range(len(s)):
            # 1. If a valid open parenthesis, add to the stack
            if s[i] in leftchar:
                stck.append(s[i])
            # 2. If a valid close parenthesis
            elif s[i] in rightchar:
                # 3. If stack exists
                if stck:
                    # 3.1 Chek if the parenthesis is paired with the topmost parenthesis of the stack and pop
                    if leftchar.index(stck[-1]) == rightchar.index(s[i]):
                        stck.pop()
                    # 3.2 If the parenthesis does not pair, return False
                    else:
                        return False
                # 4. If the stack is empy, return False
                else:
                    return False   
        
        # 5. After the operation, if the stack is empty, return True
        if len(stck) == 0:
            return True
        else:
            return False
    

"""
Runtime: 42 ms, faster than 20.84% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.4 MB, less than 7.86% of Python3 online submissions for Valid Parentheses.
"""
