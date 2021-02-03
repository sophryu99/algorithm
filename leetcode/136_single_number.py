"""
Key objective:
- Linear runtime
- No extra memory usage

Approach:
1. Create hash table with key/value in nums
2. Return the element which appeared only once
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for i in nums:                          # iterate through nums list
            hash_table[i] +=1                   # create key-value in hash_table
            
        for i in hash_table:                    # if only appeared once,
            if hash_table[i] == 1:
                return i                        # return i

"""
Runtime: 144 ms, faster than 36.09% of Python3 online submissions for Single Number.
Memory Usage: 16.7 MB, less than 63.67% of Python3 online submissions for Single Number.

"""
