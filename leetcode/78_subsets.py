# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        base = []
        
        def backtrack(first = 0, curr = []):
            # If the subset reaches k length
            if len(curr) == k:
                output.append(curr[:])
                return
            for i in range(first, n):
                # Add nums[i] to the current combination
                curr.append(nums[i])
                # Use next integers to complete the combination
                backtrack(i + 1, curr)
                curr.pop()
                
        output = []
        n = len(nums)
        # Every possible k length of subsets in a given array
        for k in range(n + 1):
            backtrack()
            
        return output
                
                
"""
Runtime: 43 ms, faster than 20.81% of Python3 online submissions for Subsets.
Memory Usage: 14.5 MB, less than 18.87% of Python3 online submissions for Subsets.
"""