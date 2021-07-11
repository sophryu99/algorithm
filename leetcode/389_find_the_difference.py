# https://leetcode.com/problems/find-the-difference/

"""
1. Iterate through s and check if the elements in s exist in t
2. Pop the element from t if exists
3. Return remaining elements
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t = list(t)
        for i in s:
            if i in t:
                t.pop(t.index(i)) 
        return ''.join(t)
                
"""
Runtime: 80 ms, faster than 6.15% of Python3 online submissions for Find the Difference.
Memory Usage: 14.5 MB, less than 5.72% of Python3 online submissions for Find the Difference.
"""