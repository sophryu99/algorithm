# https://leetcode.com/problems/merge-two-binary-trees/

# Recursive approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        
        if not root2:
            return root1
        
        t = TreeNode(root1.val + root2.val)
        t.left = self.mergeTrees(root1.left, root2.left)
        t.right = self.mergeTrees(root1.right, root2.right)
        return t

"""
Runtime: 110 ms, faster than 20.62% of Python3 online submissions for Merge Two Binary Trees.
Memory Usage: 15.5 MB, less than 55.64% of Python3 online submissions for Merge Two Binary Trees.
"""


