# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        # heapq.nlargest(num_of_elements, elements_to_be_returned, nums_to_be_used_to_determine_largest)
        eles = heapq.nlargest(k, c.keys(), key = c.get)
        return eles

"""
Runtime: 140 ms, faster than 36.14% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.5 MB, less than 95.57% of Python3 online submissions for Top K Frequent Elements."""
