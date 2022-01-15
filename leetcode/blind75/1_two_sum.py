
class Solution:
    def twoSum(self, nums, target):
        # Num: index
        d = {}
        
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i
            