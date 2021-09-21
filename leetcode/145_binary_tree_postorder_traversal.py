# https://leetcode.com/problems/binary-tree-postorder-traversal/

"""
1. Post-order traversal
2. Iterate through left -> right -> root
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        

"""
Runtime: 32 ms, faster than 66.45% of Python3 online submissions for Binary Tree Postorder Traversal.
Memory Usage: 14.1 MB, less than 74.58% of Python3 online submissions for Binary Tree Postorder Traversal.
"""