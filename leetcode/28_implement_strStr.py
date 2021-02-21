# https://leetcode.com/problems/implement-strstr/

"""
Approach:
Two pointers
1. Search through haystack and shift the start and end index by one if the section is not the same with the needle
2. Repeat this until the end index reaches the end of haystack

Exceptions:
- If needle == "", return.0
- If the needle does not exist in haystack, return -1
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        search = False                          # track search success / failure
        left = 0                                # start index
        right = len(needle)                     # end index (length of the needle)
        
        while right <= len(haystack):           # end search if the end index reaches the end
            if haystack[left:right] == needle:  # compare haystack and needle
                search = True                   
                return left                     # returh the index of the starting index
            left += 1                           # if search failed, shift the index by one
            right += 1
                
        if search == False:
            return -1

        """
Runtime: 28 ms, faster than 88.75% of Python3 online submissions for Implement strStr().
Memory Usage: 14.4 MB, less than 49.10% of Python3 online submissions for Implement strStr().
"""
