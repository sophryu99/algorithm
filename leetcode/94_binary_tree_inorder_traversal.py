# https://leetcode.com/problems/binary-tree-inorder-traversal/

"""
1. Inorder Traversal
2. Iterate through left -> root -> right node
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        
"""
Runtime: 16 ms, faster than 99.89% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 14.1 MB, less than 91.37% of Python3 online submissions for Binary Tree Inorder Traversal.
"""