# https://leetcode.com/problems/binary-tree-preorder-traversal/


"""
1. Preorder Traversal: Traversing through the child node first
2. Similar with DFS
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Recursive solution
"""
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            
        if not root:
            return []
        
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
            
"""
Runtime: 28 ms, faster than 86.22% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 14.1 MB, less than 73.76% of Python3 online submissions for Binary Tree Preorder Traversal.
"""