# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        allnum = []
        stck = [(root, '')]
        while stck:
            root, localsum = stck.pop()
            localsum += str(root.val)
            # If the end of the tree is reached, append to allnum
            if not root.left and not root.right:
                allnum.append(localsum)
            
            if root.left:
                stck.append((root.left, localsum))
                
            if root.right:
                stck.append((root.right, localsum))
                
        totalsum = sum([int(i) for i in allnum])
        return totalsum
                
"""
Runtime: 42 ms, faster than 21.93% of Python3 online submissions for Sum Root to Leaf Numbers.
Memory Usage: 14.2 MB, less than 79.10% of Python3 online submissions for Sum Root to Leaf Numbers.
"""