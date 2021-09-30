# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        nums1 = [1,2,2,1], nums2 = [2,2]
        """
        longer = nums1
        shorter = nums2
        
        if nums1 < nums2:
            longer = nums2
            shorter = nums1
        ans = []
        
        for i, ele in enumerate(longer):
            if ele in shorter:
                ans.append(ele)
                idx = shorter.index(ele)
                shorter.pop(idx)
                
        return (ans)
                
        
"""Runtime: 64 ms, faster than 39.64% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 14.4 MB, less than 69.87% of Python3 online submissions for Intersection of Two Arrays II.
"""