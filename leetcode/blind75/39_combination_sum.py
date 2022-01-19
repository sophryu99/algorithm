# https://leetcode.com/problems/combination-sum/

"""
Backtracking appraoch
# try out each possible cases
# this is the case, cur_sum will never equal to target, break recursion
# If adds up to the target, append the current combination to the ar
# For every element from the current index,
# Extend the combination list, update cursum, and index

candidates = [2,3,6,7], target = 7

dfs([], 0, 0)

dfs([2], 2, 0)

dfs([2], 2, 0)
- dfs([2, 2], 4, 0)
...
dfs([3], 3, 0)
- dfs([3, 3], 6, 0)
-   dfs([3, 3, 3], 9, 0) -> return
...
dfs([6], 6, 0)
dfs([7], 7, 0)
...

Time Complexity: O(N ** (M / min(candidates)))
- N: len(candidates)
- M: target

Space Complexity: O(M / min(candidates))
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def dfs(comb_arr, currsum, idx):
            # If currsum == target, append the current combination to the ans array
            if currsum == target:
                ans.append(comb_arr)
                return
            # If currsum > target, it will never add up to the target, break search
            if currsum > target:
                return
            
            for i in range(idx, len(candidates)):
                dfs(comb_arr + [candidates[i]], currsum + candidates[i], i)
                
        dfs([], 0, 0)
        return ans
                
            
"""
Runtime: 99 ms, faster than 52.05% of Python3 online submissions for Combination Sum.
Memory Usage: 14.3 MB, less than 77.73% of Python3 online submissions for Combination Sum.
"""