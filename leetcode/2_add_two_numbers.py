# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        numone = []
        numtwo = []
        
        def iterate(lst, result):
            result.append(str(lst.val))
            if not lst.next:
                newnum = result[::-1]
                return newnum
            
            return iterate(lst.next, result)
        
        numone, numtwo = iterate(l1, []), iterate(l2, [])
        newsum = (int(''.join(numone)) + int(''.join(numtwo)))
        res = (list(int(i) for i in list(str(newsum))[::-1]))   
                
        def lst2link(lst):
            cur = dummy = ListNode(0)
            for e in lst:
                cur.next = ListNode(e)
                cur = cur.next
            return dummy.next
        
        return (lst2link(res))

"""
Runtime: 84 ms, faster than 8.00% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.5 MB, less than 12.23% of Python3 online submissions for Add Two Numbers."""

"""Needs to be improved"""
