# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# https://sophuu.tistory.com/69

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import defaultdict
class Solution:
    
    def maxLevelSum(self, root: TreeNode) -> int:
        q = [(root, 1)]
        cnt = 0
        vals = defaultdict(int)
        vals[1] = root.val

        while q:
            rt, level = q.pop(0)
            if rt.left:
                q.append((rt.left, level + 1))
                vals[level + 1] += rt.left.val
            if rt.right:
                q.append((rt.right, level + 1))
                vals[level + 1] += rt.right.val
        
        sort_orders = sorted(vals.items(), key=lambda x: x[1], reverse=True)
        return sort_orders[0][0]

"""
Runtime: 344 ms, faster than 17.22% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
Memory Usage: 18.8 MB, less than 11.38% of Python3 online submissions for Maximum Level Sum of a Binary Tree."""