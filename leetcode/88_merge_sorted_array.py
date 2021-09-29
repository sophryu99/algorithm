#https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        
        nums1[m: m + n] = nums2
        nums1.sort()
                    
            
        
        
"""
Runtime: 28 ms, faster than 98.18% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 14.3 MB, less than 30.34% of Python3 online submissions for Merge Sorted Array.
"""
