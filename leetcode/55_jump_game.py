# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if (i + nums[i]) >= last:
                last = i 
                
        return last == 0
        
        
"""
Runtime: 750 ms, faster than 22.53% of Python3 online submissions for Jump Game.
Memory Usage: 15.5 MB, less than 12.08% of Python3 online submissions for Jump Game.

"""