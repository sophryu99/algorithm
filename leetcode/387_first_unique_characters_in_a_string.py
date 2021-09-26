# https://leetcode.com/problems/first-unique-character-in-a-string/


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        s = "leetcode"
        d = {"l": (1, 0), "e": (2, 1)...}
        
        sort with occurence = 1, min(index)
        
        if not occurence = 1, return -1
        
        """
        
        non_repeating = 0
        
        d = collections.defaultdict(lambda: (0, 0.0))
       
        for i in range(len(s) -1 , -1, -1):
            if s[i] in d.keys():
                d[s[i]] = (d[s[i]][0] + 1, i)
            else:
                d[s[i]] = (1, i)
        
        non_repeating = []
        
        for key, val in d.items():
            # If the occurence is 1, append the index to non_repeating list
            if val[0] == 1:
                non_repeating.append(val[1])
        
        if non_repeating: 
            return min(non_repeating)
        return -1

"""
Runtime analysis:
- Iterating through the list O(n) to append to a defaultdict O(1)
- Iterating through a dictionary O(n) to append to a list O(1)

Big-O: O(n)
"""
            
"""
Runtime: 240 ms, faster than 15.28% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 14.4 MB, less than 43.68% of Python3 online submissions for First Unique Character in a String.
"""


# Better Solution: Creating collections.Counter module

class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1

"""
Runtime: 143 ms, faster than 46.59% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 14.3 MB, less than 87.54% of Python3 online submissions for First Unique Character in a String.
"""
