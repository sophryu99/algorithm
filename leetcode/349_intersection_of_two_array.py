# https://leetcode.com/problems/intersection-of-two-arrays/

"""
Approach:
1. Create a set to keep track of numbers in nums1
2. Loop through nums2 to check for numbers in nums1, and add to another set
3. Return answer set

"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        newSet = set()              # set for nums1
        ans = set()                 # set for nums2
        for i in nums1:             # loop through nums1 and add to newSet
            newSet.add(i)
        for j in nums2:             # loop through nums2
            if j in newSet:         # check if it's in j
                ans.add(j)          # add to ansset
        return ans

"""
Runtime: 44 ms, faster than 80.26% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 14.5 MB, less than 48.23% of Python3 online submissions for Intersection of Two Arrays.
"""
