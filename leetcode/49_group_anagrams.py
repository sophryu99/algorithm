# https://leetcode.com/problems/group-anagrams/

"""
1. Check if their sorted strings are equal
2. Append to the key
3. Return the values of the dict
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strs:
            d[tuple(sorted(s))].append(s)
        return d.values()
        
"""
Runtime: 156 ms, faster than 22.67% of Python3 online submissions for Group Anagrams.
Memory Usage: 18.3 MB, less than 29.41% of Python3 online submissions for Group Anagrams.
"""