# https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        # Travere through linked list nodes, and if the value equals node, pop the head
        next_ = node.next
        node.val = next_.val
        node.next = next_.next
        
"""
Runtime: 36 ms, faster than 87.91% of Python3 online submissions for Delete Node in a Linked List.
Memory Usage: 14.8 MB, less than 60.12% of Python3 online submissions for Delete Node in a Linked List.
"""