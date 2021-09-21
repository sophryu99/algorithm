# https://leetcode.com/problems/find-mode-in-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = defaultdict(int)
        
        def iterate(root):
            if not root:
                return []
            
            return [root.val] + iterate(root.left) + iterate(root.right)
        
        parsed = iterate(root)
        
        for i in parsed:
            d[i] += 1

        maxval = max(d.values())
        duplicate = [k for k, v in d.items() if v == maxval]
        
        return duplicate
        
            
"""
Runtime: 56 ms, faster than 71.50% of Python3 online submissions for Find Mode in Binary Search Tree.
Memory Usage: 18.6 MB, less than 14.67% of Python3 online submissions for Find Mode in Binary Search Tree.
"""