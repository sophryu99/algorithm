"""
Approach: 
Traverse through node by checking the conditions below:
1. If Node p and q exists, continue traversal by recursion
2. If Node p or q does not exist, return False as the length does not match
3. If Node p.val does not equal q.val, return False as the value does not equate
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if not p and not q:                   # if p and q are both None 
            return True                       # end of traversal -> True
        
        if not q or not p:                    # if one of p and q is None
            return False                      # end of traversal -> False
        
        if p.val != q.val:                    # if either p or q are not the same
            return False                      # end of traversal -> False

        return self.isSameTree(p.right, q.right) and \
    self.isSameTree(p.left, q.left)
    
    
    """
    Runtime: 48 ms, faster than 7.18% of Python3 online submissions for Same Tree.
    Memory Usage: 14.4 MB, less than 35.73% of Python3 online submissions for Same Tree.

    """


    
    
