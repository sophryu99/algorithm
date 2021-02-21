# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
                return True
    
        return self.countHeight(root) < 1000000000
    
    def countHeight(self,node):
        if not node:
            return -1
        
        lHeight = self.countHeight(node.left)
        rHeight = self.countHeight(node.right)
        if abs(lHeight - rHeight) > 1:
            return 1000000000
        return max(lHeight,rHeight) + 1 
        
"""
Runtime: 52 ms, faster than 61.07% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 18 MB, less than 80.13% of Python3 online submissions for Balanced Binary Tree.
"""
