# https://leetcode.com/problems/valid-parentheses/

"""
1. Create an ampty stack and leftchar, rightchar reference
2. Iterate through the string array and if the element is in leftchar, add to stack
3. If it is in rightchar, check if the topmost array of the stack pairs with the element.
4. If the stack is empty return True
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        
        leftchar = ['(', '{', '[']
        rightchar = [')', '}', ']']
        
        for i in range(len(s)):
            if s[i] in leftchar:
                stck.append(s[i])
            
            elif s[i] in rightchar:
                if stck:
                    if leftchar.index(stck[-1]) == rightchar.index(s[i]):
                        stck.pop()
                    else:
                        return False
                else:
                    return False   
            
        if len(stck) == 0:
            return True
        else:
            return False
        

"""
Runtime: 29 ms, faster than 66.72% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.3 MB, less than 63.75% of Python3 online submissions for Valid Parentheses.
"""
        
            