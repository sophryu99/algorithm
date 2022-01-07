# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        lst = list(s)

        stck = []
        curstring = ""
        curnum = 0 
        for ele in lst:
            if ele == '[':
                stck.append(curstring)
                stck.append(curnum)
                curstring = ''
                curnum = 0
                
            elif ele == ']':
                num = stck.pop()
                prevstring = stck.pop()
                curstring = prevstring + num * curstring
                
            elif ele.isdigit():
                curnum = curnum * 10 + int(ele)
            else:
                curstring += ele
            
        return curstring

"""
Runtime: 56 ms, faster than 5.44% of Python3 online submissions for Decode String.
Memory Usage: 14.2 MB, less than 79.51% of Python3 online submissions for Decode String.
"""
