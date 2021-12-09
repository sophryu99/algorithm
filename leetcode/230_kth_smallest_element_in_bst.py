# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root, k):
        stack = []
        while True:
            # While root exists
            while root:
                # Append the root to the stack
                stack.append(root)
                # Reassign root to root left for the in order traversal
                root = root.left
            # Get the uppermost leaf from the stack and re assign as root
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right