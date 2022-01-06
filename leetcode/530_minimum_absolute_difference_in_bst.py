# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

"""
Traverse through the tree and keep track of the values of each nodes
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Traverse through the tree and store the values
        q = deque([root])
        vals = []
        while q:
            node = q.popleft()
            if node:
                vals.append(node.val)
                if node.left:
                    q.append((node.left))
                if node.right:
                    q.append((node.right))
        
        # Get the minimum absolute difference amongst the values   
        s = sorted(vals)
        start = 0
        end = 1
        mindiff = 100000
        while end < len(s):
            absdiff = abs(s[start] - s[end])
            mindiff = min(absdiff, mindiff)
            start += 1
            end += 1
        
        return mindiff
"""
Runtime: 103 ms, faster than 5.57% of Python3 online submissions for Minimum Absolute Difference in BST.
Memory Usage: 16.3 MB, less than 33.02% of Python3 online submissions for Minimum Absolute Difference in BST.
"""
