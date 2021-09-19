# https://leetcode.com/problems/contains-duplicate-ii/

"""
1. Create a dictionary d
2. Iterate through the nums list and keep track of the most recent index of the key
3. If a key already exists in the dictionary, check if the difference of the current i and the value of the key is less than or equal to k
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
            else:
                if i - d[nums[i]] <= k:
                    return True
                else:
                    d[nums[i]] = i
        return False
                
            
"""
Runtime: 631 ms, faster than 48.10% of Python3 online submissions for Contains Duplicate II.
Memory Usage: 28.4 MB, less than 43.01% of Python3 online submissions for Contains Duplicate II.
"""