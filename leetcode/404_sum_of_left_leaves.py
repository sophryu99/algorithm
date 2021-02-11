# https://leetcode.com/problems/sum-of-left-leaves/
"""
Approach:
BFS
1. Traverse through nodes
2. If node.left and node.right does not exist, add node.left.valto res

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        que = [root]
        res = 0
        while que:
            for _ in range(len(que)):
                node = que.pop(0)
                if node.left:  
                    que.append(node.left)
                    if not node.left.left and not node.left.right:
                        res += node.left.val
                if node.right:
                    que.append(node.right)
        return res
        
        
        
"""
Runtime: 32 ms, faster than 72.64% of Python3 online submissions for Sum of Left Leaves.
Memory Usage: 14.6 MB, less than 81.74% of Python3 online submissions for Sum of Left Leaves.
"""
