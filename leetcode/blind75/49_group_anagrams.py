# https://leetcode.com/problems/group-anagrams/

"""
1. Sort the words in str in alphabetical order
2. Iterate through the list and add the index of each words to a dict if they are the same
3. Iterate through the dict and group words according to the indices
"""

import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        sorted_strs = [''.join(sorted(i)) for i in strs]
        d = {}
        ans = []
        
        # Iterate through the sorted list and add the index to d
        for idx, word in enumerate(sorted_strs):
            if word not in d:
                d[word] = [idx]
            else:
                d[word].append(idx)
        for k, v in d.items():
            anagrams = []
            for idx in v:
                anagrams.append(strs[idx])
            ans.append(anagrams)
        return (ans)

"""
Runtime: 181 ms, faster than 16.95% of Python3 online submissions for Group Anagrams.
Memory Usage: 18.4 MB, less than 28.80% of Python3 online submissions for Group Anagrams.
"""


class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()

"""
Runtime: 113 ms, faster than 54.72% of Python3 online submissions for Group Anagrams.
Memory Usage: 18.3 MB, less than 34.97% of Python3 online submissions for Group Anagrams.
"""