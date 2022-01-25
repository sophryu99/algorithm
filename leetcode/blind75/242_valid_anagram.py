# https://leetcode.com/problems/valid-anagram/

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the length of the two strings are different, return False
        if len(s) != len(t):
            return False
        
        d = defaultdict(int)
        for l in s:
            d[l] += 1
        for l in t:
            if l in d:
                d[l] -=1
        for c in d.values():
            if c != 0:
                return False
        
        return True
        
        
"""
Runtime: 62 ms, faster than 43.41% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.4 MB, less than 81.71% of Python3 online submissions for Valid Anagram.
"""