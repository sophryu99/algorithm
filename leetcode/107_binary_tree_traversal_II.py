# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
        1
    2       3
4               5

Output: [[4,5],[2,3],[1]]

"""
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # BFS level order traversal with a reversed array
        
        queue = [root]
        next_q = []
        level = []
        result = []
        
        if not root:
            return []
        
		# Start with root in queue
        while queue:
            for node in queue: # for every node at each level check if it has children then add to next_q
                level.append(node.val)
                
                if node.left:
                    next_q.append(node.left)

                if node.right:
                    next_q.append(node.right)
                
            result.append(level) # Add every node at current level to result
            level = []
            queue = next_q # set queue to children of nodes on current level
            next_q = [] 
          
        result.reverse() # we traverse top to bottom then simply reverse result to get bottom to top
        return result
                
"""
Runtime: 32 ms, faster than 79.79% of Python3 online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 14.6 MB, less than 43.91% of Python3 online submissions for Binary Tree Level Order Traversal II.
"""