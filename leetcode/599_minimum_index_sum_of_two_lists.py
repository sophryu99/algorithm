# https://leetcode.com/problems/minimum-index-sum-of-two-lists/
"""
1. Traverse through list1 and check if the element exists in list2:
2. If True, calculate the local sum of the values and add to the dictionary
3. Get the minimum value of the dictionary and return all.
"""

from collections import defaultdict

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = defaultdict(int)
        for i in range(len(list1)):                             # 1
            if list1[i] in list2:                               # 2
                localsum = i + list2.index(list1[i])
                res[list1[i]] = localsum
        min_val = min(res.values())
        min_keys = [k for k, v in res.items() if v == min_val]
        return (min_keys)

                
"""
Runtime: 268 ms, faster than 26.77% of Python3 online submissions for Minimum Index Sum of Two Lists.
Memory Usage: 14.8 MB, less than 39.57% of Python3 online submissions for Minimum Index Sum of Two Lists.
"""