# https://leetcode.com/problems/path-sum

"""
Approach:
DFS (or BFS)
1. Traverse through binary tree and keep track of sum
2. While traversing, if the sum equals targetSum, end traversing and return True
3. Else False
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:                                # if no root
            return False                            # return false
        stack = [(root, 0)]                         # stack to store root and sum
        while stack:                            
            root, rsum = stack.pop()                # pop value from stack
            rsum += root.val                        # add root.val to rsum
            if not root.left and not root.right:    # if the tree reaches an end
                if rsum == targetSum:               # if total sum equals target
                    return True                     # return true
            
            if root.right:                          # if right node exists
                stack.append((root.right, rsum))    # redefine root node and rsum
            if root.left:                           # if left node exissts
                stack.append((root.left, rsum))     # redefine root node and rsum
        return False
    
"""
Runtime: 44 ms, faster than 63.59% of Python3 online submissions for Path Sum.
Memory Usage: 15.8 MB, less than 95.78% of Python3 online submissions for Path Sum.
"""
