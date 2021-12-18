# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        left = 0
        right = 1
        maxlen = 1
        s = list(s)
        while right < len(s) + 1:
            window = s[left: right]
            if right == len(s):
                return max(maxlen, len(window))
            
            if s[right] in window:
                maxlen = max(maxlen, len(window))
                left = left + window.index(s[right]) + 1
                right += 1
            else:
                right += 1     
                 
        return maxlen


"""
Runtime: 85 ms, faster than 34.94% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.4 MB, less than 25.13% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""