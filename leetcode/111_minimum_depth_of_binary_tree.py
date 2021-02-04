# https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""
Approach:
BFS Method
1. Check for root, if left, right leaf exists, recur through existing leaf
2. Iterate until left, right leaf does not exist for a root.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:                                    # if there is no root, return 0 for height
            return 0
        
        if root.left is None and root.right is None:        # if there is no right, left leaf
            return 1                                        # return 1 for height
        
        if root.left is None:                               # if there is no left leaf, 
            return self.minDepth(root.right) + 1            # recur through right leaf and increment 1 height
        
        if root.right is None:                              # if there is no right leaf, 
            return self.minDepth(root.left) + 1             # recur through left leaf and increment 1 height      
        
        return min(self.minDepth(root.right), self.minDepth(root.left)) + 1
    

    """
Runtime: 896 ms, faster than 5.09% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 53 MB, less than 36.62% of Python3 online submissions for Minimum Depth of Binary Tree.
"""
