# https://leetcode.com/problems/reverse-string/

"""
Approach:
Two pointers
1. While iterating through the list, swap the first and last element for each search

Exception:
- Don't use extra memory, modify nums in-place instead.

"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            origin = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = origin

            """
Runtime: 196 ms, faster than 67.37% of Python3 online submissions for Reverse String.
Memory Usage: 18.6 MB, less than 41.95% of Python3 online submissions for Reverse String.
"""
