# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        
        for i in range(n * 2 - 1):            
            left = i // 2
            right = (i + 1) // 2
            while left >= 0 and right < n and s[left] == s[right]:
                cnt += 1
                left -=1
                right += 1
                
        return cnt

"""
Runtime: 151 ms, faster than 65.17% of Python3 online submissions for Palindromic Substrings.
Memory Usage: 14.2 MB, less than 66.36% of Python3 online submissions for Palindromic Substrings.
"""