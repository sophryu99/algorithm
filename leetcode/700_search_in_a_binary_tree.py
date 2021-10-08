# https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
1. Append the root to an array
2. If the value of the root is larger than the value searching, traverse to right
3. If the value of the root is less than the value searching, traverse to left

Time: O(log(N))
"""

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Traverse through nodes
        node = [root]
        
        while node:
            n = node.pop(0)
            if n.val == val:
                return n
            if n.val < val and n.right:
                node.append(n.right)
            elif n.val > val and n.left:
                node.append(n.left)
        
        return None
        

"""
Runtime: 60 ms, faster than 99.67% of Python3 online submissions for Search in a Binary Search Tree.
Memory Usage: 16.2 MB, less than 70.80% of Python3 online submissions for Search in a Binary Search Tree.
"""