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

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_list = [''.join(sorted(i)) for i in strs]        
        d = collections.defaultdict(lambda: list())
        for idx, word in enumerate(s_list):
            d[word].append(strs[idx])
            
        ans = []
        for k, v in d.items():
            ans.append(v)
            
        return (ans)

"""
Runtime: 100 ms, faster than 73.66% of Python3 online submissions for Group Anagrams.
Memory Usage: 17.7 MB, less than 59.67% of Python3 online submissions for Group Anagrams.
"""

import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Sort every words of the list
        s = [''.join(sorted(i)) for i in strs]
        
        # Map the index of the common words
        d = collections.defaultdict(lambda: list())
        for i, word in enumerate(s):
            d[word].append(i)
        
        ans = []
        # Group common indices
        for v in d.values():
            common = []
            for i in v:
                common.append(strs[i])
            ans.append(common)
            
        return (ans)

"""
Runtime: 96 ms, faster than 81.15% of Python3 online submissions for Group Anagrams.
Memory Usage: 18.7 MB, less than 27.12% of Python3 online submissions for Group Anagrams.
"""