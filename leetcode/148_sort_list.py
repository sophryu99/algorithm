# https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Traverse through the Listnode and store the values
        vals = []
        tail = head
        while tail:
            vals.append(tail.val)
            tail = tail.next
        
        # Sort values
        sorted_val = sorted(vals)
        
        # Initiate a new ListNode and append the vals
        ans = ListNode(0)
        tail_ans = ans
        for num in sorted_val:
            tail_ans.next = ListNode(num)
            tail_ans = tail_ans.next
        
        return ans.next
            
        
"""
Runtime: 267 ms, faster than 79.93% of Python3 online submissions for Sort List.
Memory Usage: 38.2 MB, less than 10.71% of Python3 online submissions for Sort List.
"""
