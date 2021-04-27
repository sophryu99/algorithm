# https://leetcode.com/problems/binary-tree-paths/
# https://sophuu.tistory.com/68

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        def dfs(node, path):
            path += '->'
            path += str(node.val)

            if not node.left and not node.right:
                return ans.append(path[2:])

            if node.left:
                dfs(node.left, path)

            if node.right:
                dfs(node.right, path)
            
        ans = []
        dfs(root, "")
        return ans
        
"""
Runtime: 32 ms, faster than 68.68% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 14.2 MB, less than 60.15% of Python3 online submissions for Binary Tree Paths.
"""