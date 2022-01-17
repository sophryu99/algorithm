# https://leetcode.com/problems/merge-two-sorted-lists/

"""
Time Complexity: O(n)
Space Complexity: O(n)
- Creating a new Linked List
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:   
        base = ListNode(0)
        tail = base
        
        while True:
            if not l1:
                tail.next = l2
                break
            if not l2:
                tail.next = l1
                break
            
            # Compare the current values of the current nodes of both ListNode
            if l1.val <= l2.val:
                tail.next = l1
                # Rotate tail and l1
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = l2
                # Rotate tail and l2
                tail = tail.next
                l2 = l2.next
            
        return base.next

"""
Runtime: 37 ms, faster than 63.55% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14.3 MB, less than 62.15% of Python3 online submissions for Merge Two Sorted Lists.
"""
            
            
        
        