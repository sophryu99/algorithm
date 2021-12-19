# https://leetcode.com/problems/top-k-frequent-words/

from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Record the frequency of each words
        c = Counter(words)
        
        # Sort by counts descending order, key ascending order
        res = sorted(c, key=lambda word: (-c[word], word))
        return res[:k]
        
"""
Runtime: 56 ms, faster than 72.45% of Python3 online submissions for Top K Frequent Words.
Memory Usage: 14.5 MB, less than 38.84% of Python3 online submissions for Top K Frequent Words.
"""