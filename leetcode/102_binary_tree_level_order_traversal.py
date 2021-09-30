# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = [root]
        
        lst = []
        
        while que:
            level_lst = []
            for i in range(len(que)):
                node = que.pop(0)
                if node:
                    level_lst.append(node.val)
                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)
            if level_lst:
                lst.append(level_lst)
            
        return (lst)
       

"""
Runtime: 40 ms, faster than 32.10% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 14.6 MB, less than 66.70% of Python3 online submissions for Binary Tree Level Order Traversal.
"""