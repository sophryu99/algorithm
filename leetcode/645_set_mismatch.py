# https://leetcode.com/problems/set-mismatch/
"""
3 * 4 // 2 = 6
1. Calculate the possible true sum of an array of length n
2. Calculate the acutal sum of the array 
3. Calculate the missing number
4. Return the duplicate num and the missing num
"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        true_sum = n * (n + 1) // 2                         # 1 
        actual_sum = sum(nums)                              # 2
        set_sum = sum(set(nums))                            # 3
        return [actual_sum - set_sum, true_sum - set_sum]   # 4

"""
Runtime: 176 ms, faster than 98.77% of Python3 online submissions for Set Mismatch.
Memory Usage: 16 MB, less than 39.90% of Python3 online submissions for Set Mismatch.
"""