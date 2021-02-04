# https://leetcode.com/problems/contains-duplicate/

"""
Approach:
1. Iterate through the list and create hash table to track count of each key
2. If value of a key is larger than 2, return True
3. Else, continue iterating
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_table = defaultdict(int)           # create empty hash table
        for i in nums:
            hash_table[i] += 1                  # iterate through the list to create a hash table
        
        for j in hash_table:                    # if a key's value exceeds 2, return True
            if hash_table[j] >= 2:
                return True
            else:                               # else, continue iterating
                continue
            return False

        
"""
Runtime: 136 ms, faster than 18.76% of Python3 online submissions for Contains Duplicate.
Memory Usage: 21.5 MB, less than 6.79% of Python3 online submissions for Contains Duplicate.
"""       
