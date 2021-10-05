# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
When traversing the list with a pointer slow, make another pointer fast that traverses twice as fast. When fast reaches the end of the list, slow must be in the middle.
"""
class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
"""
Runtime: 28 ms, faster than 87.49% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 14.3 MB, less than 42.97% of Python3 online submissions for Middle of the Linked List.
"""