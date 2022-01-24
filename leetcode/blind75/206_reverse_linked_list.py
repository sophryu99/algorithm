# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = head
        vals = []
        while tail:
            vals.append(tail.val)
            tail = tail.next
        base = ListNode(0)
        tail_ = base
        for i in range(len(vals) - 1, -1, -1):
            node = ListNode(vals[i])
            tail_.next = node
            tail_ = tail_.next
            
        return base.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
prev = None
curr = [1,2,3,4,5]
head = [2,3,4,5]
curr = [1]

prev = [1]
curr = [2,3,4,5]
head = [3,4,5]
curr = [2,1]

prev = [2,1]
curr = [3,4,5]
head = [4,5]
curr = [3,2,1]

prev = [3,2,1]
...

prev = [5,4,3,2,1]
"""
# Switch node in-place without assigning extra space    
class Solution:
    def reverseList(self, head):
        # keep track of prev node
        prev = None
        while head:
            # Store head to curr
            curr = head
            # Rotate head
            head = head.next
            # Assign curr.next as prev
            curr.next = prev
            # Assign prev to curr
            prev = curr
        return prev

"""
Runtime: 36 ms, faster than 77.99% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.6 MB, less than 77.52% of Python3 online submissions for Reverse Linked List.
"""