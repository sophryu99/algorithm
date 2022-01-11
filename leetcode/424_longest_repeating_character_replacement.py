# https://leetcode.com/problems/longest-repeating-character-replacement//
"""
We use a window ranging from index start to end
We only look in characters inside this window and keep track of their counts
We can allow up to K chars that are not the most frequent char in our window

ABBAB, k = 2
ABCBA, k = 2
"""
from collections import Counter
class Solution:
    def characterReplacement(self, s, k):  
        start, end = 0, 0
        counts = Counter()
        res = 0
        while end < len(s):
            counts[s[end]] += 1
            # Store the most frequent occurence of a word
            max_count = counts.most_common(1)[0][1]
            
            # we shift start to the right only if we ran out of replacements
            # we ran out of replacements if (CHARS that are not the most frequent in current window) > k
            # (end - start + 1) is length of our window, because our window range is INCLUSIVE of both ends
            if end - start + 1 - max_count > k:
                counts[s[start]] -= 1 
                # Shift the left of the window
                start += 1
            
            res = max(res, end - start + 1)
            # Shift the right ofthe window
            end += 1
            
        return res
        
"""
Runtime: 692 ms, faster than 5.03% of Python3 online submissions for Longest Repeating Character Replacement.
Memory Usage: 14.4 MB, less than 23.87% of Python3 online submissions for Longest Repeating Character Replacement.
"""