# https://leetcode.com/problems/valid-parentheses/

"""
1. Create a dictionary with key-val as open bracket - close bracket
2. Iterate through the string and check if the element is in the key or the value of the dictionary

N = input string size
Time Complexity: O(N)
- One pass through the array
- Stack deletion: O(1)
- Stack insertion: O(1)
- Hash table Search: O(N)

"""
class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        
        d = {'}':'{', ')': '(', ']': '['}
        
        for i, ele in enumerate(s):
            # If opening bracket, append to the stack
            if ele in d.values():
                stck.append(ele)
            # If closing bracket, 
            else:
                # If stck is empty, return false
                if not stck:
                    return False
                # check if the paired opening bracket is the uppermost element in the stck
                if stck[-1] == d[ele]:
                    stck.pop()
                else:
                    return False
        if not stck:
            return True
        return False 
                
"""
Runtime: 47 ms, faster than 24.75% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.5 MB, less than 7.56% of Python3 online submissions for Valid Parentheses.
"""