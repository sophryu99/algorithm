# https://leetcode.com/problems/merge-two-sorted-lists/
"""
1. Create a dummy list node and assign it to the tail
2. If L1 is empty, assing L2 to tail.next. Vice versa
3. If l1.val <= l2.val, assign L1 to tail.next. L1 is reassigned to the next node.
4. If L2.val > L1.val, assign L2 to tail.next. L2 is reassigned to the next node. 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:    
        dummy = ListNode(0)
        tail = dummy
        
        while True:
            if l1 is None:
                tail.next = l2
                break
            if l2 is None:
                tail.next = l1
                break
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        return dummy.next
        
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:   
        merged = ListNode(0)
        tail = merged
        
        while True:
            # Continue appending to the ListNode until l1, l2 reaches the end element
            if not l1:
                tail.next = l2
                break
            if not l2:
                tail.next = l1
                break
            # If l1.val is less than or equal to l2.val, add to the ListNode and rotate l1
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            # Rotate tail Node
            tail = tail.next
        
        return (merged.next)
        
        