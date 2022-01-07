# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        t1 = deque([root1])
        t2 = deque([root2])
        ele = []
        
        while t1:
            t1_root = t1.popleft()
            if t1_root:
                ele.append(t1_root.val)
                if t1_root.left:
                    t1.append(t1_root.left)
                if t1_root.right:
                    t1.append(t1_root.right)
        while t2:
            t2_root = t2.popleft()
            if t2_root:
                ele.append(t2_root.val)
                if t2_root.left:
                    t2.append(t2_root.left)
                if t2_root.right:
                    t2.append(t2_root.right)
                    
        return sorted(ele)
        
"""
Runtime: 424 ms, faster than 34.50% of Python3 online submissions for All Elements in Two Binary Search Trees.
Memory Usage: 17.8 MB, less than 98.10% of Python3 online submissions for All Elements in Two Binary Search Trees.
"""