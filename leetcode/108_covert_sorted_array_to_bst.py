# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# [-11,-10,-3,0,5,9, 11]
# [0,-10,9,-11,-3,5,11]
"""
        0
    -10 9
-11 -3 5 11
"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        # Get the median value of nums
        median = len(nums) // 2
        root = TreeNode(nums[median])
        
        root.left = self.sortedArrayToBST(nums[:median])
        root.right = self.sortedArrayToBST(nums[median + 1:])
        return root
    
        
                
            
"""
Runtime: 160 ms, faster than 5.22% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 15.5 MB, less than 87.08% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
"""