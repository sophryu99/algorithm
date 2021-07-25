# https://leetcode.com/problems/longest-harmonious-subsequence/

"""
1. Iterate through the list to add to the dictionary
2. Traverse through the dictionary and check if key + 1 exists.
3. If exists, calculate the localsum and compare it with the maxsum
4. Return the maxsum
"""

from collections import defaultdict

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        diction = defaultdict(int)
        for num in nums:                            # 1
            diction[num] += 1
        maxsum = 0
        for key, val in diction.items():            # 2
            if key + 1 in diction:
                newsum = val + diction[key + 1]     # 3
                if newsum > maxsum:                 
                    maxsum = newsum
                    
        return (maxsum)                             # 4
            
"""
Runtime: 316 ms, faster than 56.28% of Python3 online submissions for Longest Harmonious Subsequence.
Memory Usage: 16 MB, less than 37.69% of Python3 online submissions for Longest Harmonious Subsequence.
"""
            