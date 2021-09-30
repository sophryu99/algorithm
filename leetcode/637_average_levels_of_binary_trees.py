# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        q = [root]
        avg = []
        while q:
            level_avg = 0
            cnt = 0
            for i in range(len(q)):
                node = q.pop(0)
                if node:
                    level_avg += node.val
                    cnt += 1
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            average = level_avg/cnt
            avg.append(average)
            
        return (avg)
            
        