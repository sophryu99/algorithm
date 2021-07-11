# https://leetcode.com/problems/majority-element/

"""
1. Iterate through the list and increment count on dictionary
2. If the count of a key is larger than len(nums) / 2, return the key 
"""

from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        for n in nums:
            cnt[n] += 1
            
        for key, val in cnt.items():
            if val > len(nums) / 2:
                return key
            
"""
Runtime: 192 ms, faster than 19.55% of Python3 online submissions for Majority Element.
Memory Usage: 15.5 MB, less than 50.58% of Python3 online submissions for Majority Element.
"""