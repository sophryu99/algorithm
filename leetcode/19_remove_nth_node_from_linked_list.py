# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
1. Traverse the ListNode to count the nodes
2. Traverse once again until u, and remove the node.
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        node_count = 1
        
        while left:
            if left.next:
                node_count += 1
                left = left.next
            else:
                break
        
        base = head
        nth = node_count - n - 1
        cnt = 0
        if nth + 1 <= 0:
            base = base.next
            return base
            
        while base:
            if cnt == nth:
                base.next = base.next.next
                break
            base = base.next
            cnt += 1
            
        return (head)
            
            
            
"""
Runtime: 32 ms, faster than 81.32% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 14.3 MB, less than 14.00% of Python3 online submissions for Remove Nth Node From End of List."""
