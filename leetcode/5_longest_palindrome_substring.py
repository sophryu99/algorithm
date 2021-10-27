# https://leetcode.com/problems/longest-palindromic-substring/

"""
Expand Around Center: Palindrome mirrors around its center
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return ""
        
        # Starting from the center, if the starting letter and the end letter of the string is equal, expand
        def startFromCenter(s, left, right):
            l, r = left, right
            
            # While the left and the right index has not reached the start and the end of the string
            # And the start and the end letters are identical
            # Increment left index and decrement right index
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            
            # Return the length of the string
            return r - l - 1

        start = 0 
        end = 0
        for i in range(len(s)):
            # For odd numbered palindrome
            len1 = startFromCenter(s, i, i)
            # For even numbered palindrome
            len2 = startFromCenter(s, i, i + 1)
            # Get the longer string
            maxlen = max(len1, len2)
            if maxlen > end - start:
                start = i - (maxlen - 1) // 2
                end = i + maxlen // 2
                
        return s[start: end + 1]
            
        
"""
Runtime: 980 ms, faster than 75.21% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14.3 MB, less than 81.30% of Python3 online submissions for Longest Palindromic Substring.
"""