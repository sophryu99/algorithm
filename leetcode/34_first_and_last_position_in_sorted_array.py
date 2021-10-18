# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

"""
Level: medium
"""

"""
Binary Search
- Conduct binary search searching for the first index, and the second index.
- If either of them does not exist, return -1, -1
"""
class Solution:
    def searchRange(self, nums, target):
        
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        
        left = 0
        right = len(nums) - 1        
        mid_ans = 0
        searched = False
        
        # Search for an arbitrary point where target initially occurs
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                mid_ans = mid
                searched = True
                break
            
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # Binary Search until first occurence of number less than target
        def search_left(idx):
            left = 0
            right = idx
            ans = idx
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    if mid < ans:
                        ans = mid
                    right = mid -1 
                else:
                    left = mid + 1
            return ans
        
       
        # Binary Search until first occurence of number larger than target
        def search_right(idx):
            left = idx
            right = len(nums) - 1
            ans = idx
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    if mid > ans:
                        ans = mid
                    left = mid + 1 
                else:
                    right = mid - 1
            
            return ans
        
        if searched:
            return [search_left(mid_ans), search_right(mid_ans)]
        
        return [-1, -1]

"""
Runtime: 157 ms, faster than 7.00% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 15.4 MB, less than 52.93% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
"""