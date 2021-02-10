# https://leetcode.com/problems/maximum-depth-of-binary-tree
"""
Approach:
1. If root does not exist, return 0 as depth
2. Store root in var que and track depth count
3. If que has left or right leaf, store it in var que
4. Repeat until none gets appended to que and increment count
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def maxDepth(self, root: TreeNode) -> int:
        if not root:                        # if root does not exist
            return 0                        # return 0 as count 
        que, count = [root], 0              # var for node and count
        while que:                          # while que exists
            count +=1                       # increment count 
            for i in range(len(que)):
                node = que.pop(0)           # store que's root to node
                if node.left:               # if left leaf exists
                    que.append(node.left)   # append the leaf to que
                if node.right:              # if right leaf existss
                    que.append(node.right)  # append the leaf to que
                        
        return count
        
"""
Runtime: 40 ms, faster than 76.96% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 15.3 MB, less than 92.68% of Python3 online submissions for Maximum Depth of Binary Tree.
"""
