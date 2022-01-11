#https://leetcode.com/problems/two-sum/submissions/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force approach
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[j] == target - nums[i]:
                        return i, j
                        break

"""
TLE
Runtime: 48 ms, faster than 63.01% of Python3 online submissions for Two Sum.
Memory Usage: 14.3 MB, less than 75.07% of Python3 online submissions for Two Sum.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)): 
            if target - nums[i] in nums[i + 1:]:
                n = nums[i + 1:]
                return [i, n.index(target - nums[i]) + len(nums) - len(n)]
    
    
            
"""
Runtime: 652 ms, faster than 36.11% of Python3 online submissions for Two Sum.
Memory Usage: 14.9 MB, less than 65.96% of Python3 online submissions for Two Sum.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in nums[i + 1:]:
                return [i, nums[i + 1:].index(remainder) + len(nums) - len(nums[i+1:])]
                        
# https://leetcode.com/problems/two-sum/

                
"""
Runtime: 682 ms, faster than 36.76% of Python3 online submissions for Two Sum.
Memory Usage: 14.6 MB, less than 98.24% of Python3 online submissions for Two Sum.
"""


class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i,num in enumerate(nums):
            if target - num in d:
                return d[target-num], i
            d[num] = i
            
"""
Runtime: 52 ms, faster than 97.00% of Python3 online submissions for Two Sum.
Memory Usage: 15.4 MB, less than 19.10% of Python3 online submissions for Two Sum.
"""


