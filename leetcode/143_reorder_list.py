# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        """
        1. Reverse the listnode and save it
        2. Weave the two listnodes until the nodcount reaches the number of nodes
        """
        reverse = head 
        previous = None
        cnt = 0
        
        while reverse:
            cnt += 1
            temp = ListNode(reverse.val, next=previous)
            previous = temp
            reverse = reverse.next

        node = head
        reverse = temp
    
        nodecnt = 0
        for i in range(1, cnt + 1):
            if nodecnt == cnt - 1:
                node.next = None
            else:
                if i % 2 == 0:
                    node.next = t
                    node = node.next
                    nodecnt += 1
                else:
                    t = node.next
                    node.next = reverse
                    node = node.next
                    reverse = reverse.next
                    nodecnt += 1
            
                        
"""
Runtime: 219 ms, faster than 5.01% of Python3 online submissions for Reorder List.
Memory Usage: 24 MB, less than 6.30% of Python3 online submissions for Reorder List.
"""
            
        
        
        