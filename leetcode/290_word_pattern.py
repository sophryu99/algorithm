# https://leetcode.com/problems/word-pattern/
"""
1. check the length of pattern and s: len(pattern)==len(s.split())
2. check the form of pattern
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return len(pattern)==len(s.split()) and len(set(pattern))==len(set(s.split()))==len(set(zip(pattern,s.split())))

"""
Runtime: 27 ms, faster than 82.83% of Python3 online submissions for Word Pattern.
Memory Usage: 14.3 MB, less than 23.79% of Python3 online submissions for Word Pattern.
"""