# https://leetcode.com/problems/product-of-array-except-self/

"""
[1,2,3,4]

base 1 => default
ans [1]
base 1 => 1 * 1
ans [1, 1]
base 2 => 1 * 2
ans [1, 1, 2]
base 6 => 2 * 3
ans [1, 1, 2, 6]
base 24 => 6 * 4

Iterate reverse way
base2 1 => default
base2 1 => 1 * 1
ans2 [1, 1, 2, 6]
base2 4 => 2 * 4
ans2 [1, 1, 8, 6]
base2 12
ans2 [1, 12, 8, 6]
base2 24
ans2 [24, 12, 8, 6]
base2 24

"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        base = 1
        
        for i in range(n):
            ans.append(base)
            base = base * nums[i]
        
        base = 1
        for i in range(n-1,-1,-1):
            ans[i] = ans[i] * base
            base = base * nums[i]
        return ans
        
"""
Runtime: 419 ms, faster than 11.49% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 21.1 MB, less than 59.28% of Python3 online submissions for Product of Array Except Self.
"""