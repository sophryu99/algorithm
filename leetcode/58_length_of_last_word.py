# https://leetcode.com/problems/length-of-last-word/

"""
1. Split the string by " ".
2. Iterate in a reverse order and return the first element that contains string val.
3. If iteration ends, return 0
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.split(' ')
        for i in range(len(lst) - 1 , -1, -1):
            if len(lst[i]) != 0:
                return (len(lst[i]))
        return 0
    
"""
Runtime: 32 ms, faster than 61.34% of Python3 online submissions for Length of Last Word.
Memory Usage: 14.1 MB, less than 87.91% of Python3 online submissions for Length of Last Word.
"""
        