# https://leetcode.com/problems/maximum-subarray

"""
Approach:
Loop fibonacci
1. Loop through the list and try adding currsum and the next element in the list
2. If the sum is larger than currsum, reset currsum as the sum
3. Compare currsum with maxsum, and reset maxsum with higher value

"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        currsum, maxsum = 0, float('-inf')      # Set maxsum as the smallest float possible
        
        for i in nums:
            currsum += i                        # Sum currsum and the next element in the list
            
            if currsum < i:                     # if currsum is smaller than the next element
                currsum = i                     # reset currsum as the next element
                                                # else, keep currsum
            maxsum = max(currsum, maxsum)       # compare currsum and maxsum, and take the larger sum
            
        return maxsum
        
        
"""
Runtime: 64 ms, faster than 78.58% of Python3 online submissions for Maximum Subarray.
Memory Usage: 15 MB, less than 60.75% of Python3 online submissions for Maximum Subarray.
"""
        
        
    
        
    

    
