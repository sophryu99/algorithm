# https://leetcode.com/problems/longest-palindromic-substring/

"""
Approach1:
Brute Force
- Pick all possible starting and ending positions for a substring, and verify it's palindrome
- Time limit exceeded

Approach2:
- Expand from the center

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        def searchFromCenter(left, right):
            l, r = left, right
            
            while (l >= 0 and r < len(s)):
                if l == 0 or r == len(s) - 1:
                    if s[l] == s[r]:
                        return s[l: r + 1]
                    return s[l + 1: r]
                
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    return s[l + 1 : r]

            return s[l: r + 1]
        
        maxstr = ""
        for i in range(len(s) - 1):
            odd = searchFromCenter(i, i)
            even = searchFromCenter(i, i + 1)
            if len(odd) > len(maxstr):
                maxstr = odd
            if len(even) > len(maxstr):
                maxstr = even
                
        return (maxstr)
            
            
"""
Runtime: 2138 ms, faster than 31.13% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14.3 MB, less than 60.53% of Python3 online submissions for Longest Palindromic Substring.
"""
