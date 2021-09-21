# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution():
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return
        curr = head
        
        while curr != None:
            if curr.next:
                base = curr
                while curr.next and curr.next.val == base.val:
                    curr = curr.next
                base.next = curr.next
            curr = curr.next 
        return head

                    
        
        
"""
Runtime: 44 ms, faster than 64.06% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 14.4 MB, less than 23.39% of Python3 online submissions for Remove Duplicates from Sorted List.
"""