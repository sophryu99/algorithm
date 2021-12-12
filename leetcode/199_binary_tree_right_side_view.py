# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def rightSideView(self, root):
        # Call deque data structure
        deque = collections.deque()
        if root:
            deque.append(root)
        res = []
        # While deque exists
        while deque:
            size, val = len(deque), 0
            # Pop the first element from the deque
            for _ in range(size):
                node = deque.popleft()
                 # store last value in each level
                val = node.val
                # If left node exists, append to the deque
                if node.left:
                    deque.append(node.left)
                # If right node exists, append to the deque
                if node.right:
                    deque.append(node.right)
            # Append the node to the res
            res.append(val)
        return res