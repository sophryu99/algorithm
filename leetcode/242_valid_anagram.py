# https://leetcode.com/problems/valid-anagram/

"""
1. Create a dictionary for s and map the values onto dictionary
2. Iterate through t and if the key does not exist in s dict, return False, if the key's value is 0, return False
3. If the sum of all values of s dict is 0, return True, else False
"""

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        sdict = defaultdict(int)
        for i in s:
            sdict[i] += 1
            
        for i in t:
            if i in sdict and sdict[i] > 0:
                sdict[i] -=1
            else:
                return False
                
        if (sum(sdict.values())) == 0:
            return True
        else:
            return False

"""
Runtime: 52 ms, faster than 53.74% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.6 MB, less than 55.23% of Python3 online submissions for Valid Anagram.
"""
        