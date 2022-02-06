# https://leetcode.com/problems/longest-increasing-subsequence/

"""
DP Approach

Iterate through the nums array and check if the current num > preceding nums. 
This indicates that an increasing subsequence exists, store the length of the array to dp[i]

nums = [10,9,2,5,3,7,101,18]
dp = [1,1,1,1,1,1,1,1]

i = 1, j = 0, nums[i] = 9, nums[j] = 10

i = 2, j = 0, nums[i] = 2, nums[j] = 10
i = 2, j = 1, nums[i] = 2, nums[j] = 9

i = 3, j = 0, nums[i] = 5, nums[j] = 10
i = 3, j = 1, nums[i] = 5, nums[j] = 9
i = 3, j = 2, nums[i] = 5, nums[j] = 2
Since nums[i] > nums[j] => dp[3] = max(1 + 1, 1)
dp = [1,1,1,2,1,1,1,1]

i = 4, j = 0, nums[i] = 3, nums[j] = 10
i = 4, j = 1, nums[i] = 3, nums[j] = 9
i = 4, j = 2, nums[i] = 3, nums[j] = 2
Since nums[i] > nums[j] => dp[4] = max(1 + 1, 1)
dp = [1,1,1,2,2,1,1,1]
i = 4, j = 3, nums[i] = 3, nums[j] = 5

i = 5, j = 0, nums[i] = 7, nums[j] = 10
i = 5, j = 1, nums[i] = 7, nums[j] = 9
i = 5, j = 2, nums[i] = 7, nums[j] = 2
Since nums[i] > nums[j] => dp[5] = max(1 + 1, 1)
dp = [1,1,1,2,2,2,1,1]
...
i = 5, j = 2, nums[i] = 7, nums[j] = 5
i = 5, j = 2, nums[i] = 7, nums[j] = 3

dp = [1,1,1,2,2,3,4,4]
...


Efficiency ------------
n: input size
Runtime Complexity: O(n**2)
- Nested for loop
- Can be improved by implementing binary search

Space Complexity: O(n)
- List for dp
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp = [1 for _ in range(len(nums))]
        
        # For every element in nums, 
        for i in range(1, len(nums)):
            # check the elements in the rest of the list
            for j in range(i):
                # If curr element in larger than the next element, that would be the maxmimum increasing subsequence 
                # Reassign the local maximum to dp[i]
                if nums[i] > nums[j]:
                    dp[i] = max(1 + dp[j], dp[i])
        
        return max(dp)

"""
Runtime: 3860 ms, faster than 52.78% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 14.4 MB, less than 85.50% of Python3 online submissions for Longest Increasing Subsequence.
"""