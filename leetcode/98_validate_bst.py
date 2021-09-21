# https://leetcode.com/problems/validate-binary-search-tree/

"""
1. In-order Traversal
2. Compare if the traversed list is the same with the sorted list
3. Compare if the traversed list's length is the same with the set of the list (checking for duplicates)
4. If 2, 3 are True, return True
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def iterate(root):
            if not root:
                return []
            
            return iterate(root.left) + [root.val] + iterate(root.right)
        
        lst = iterate(root)
        dup = set(lst)
        return lst == sorted(lst) and len(dup) == len(lst)
        
        
"""
Runtime: 52 ms, faster than 33.05% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 17.7 MB, less than 6.76% of Python3 online submissions for Validate Binary Search Tree.
"""