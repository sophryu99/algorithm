# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        # Build a hashmap: character and how it often appears
        # O(n) time
        count = Counter(nums)
        
        # From heapq, use nlargest function to get the top k element from count
        # O(Nlogk) time
        return heapq.nlargest(k, count.keys(), key = count.get)

"""Runtime: 103 ms, faster than 60.01% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.7 MB, less than 59.10% of Python3 online submissions for Top K Frequent Elements.
"""