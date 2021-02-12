# https://leetcode.com/problems/binary-search/
"""
Approach:
1. Keep track of start and end index
2. Create mid var
3. While start <= end, compare mid and target
4. Redefine start, end var 
5. Repeat until mid == target

Exceptions:
- If target not in nums, return -1

"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        
        while start <= end:
            mid = start + (end - start) // 2
        
            if nums[mid] == target:
                return nums.index(target)
            
            if target < nums[mid]:
                end = mid - 1
            
            else:
                start = mid + 1
        
        return -1
            
"""
Runtime: 236 ms, faster than 69.45% of Python3 online submissions for Binary Search.
Memory Usage: 15.5 MB, less than 91.81% of Python3 online submissions for Binary Search.
"""
            
            
        
