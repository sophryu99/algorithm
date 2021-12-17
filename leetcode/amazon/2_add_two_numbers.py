# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Traverse through the linked list and store the results, reverse the num values
        def store(node):
            lst = []
            while node:
                lst.append(node.val)
                node = node.next
            return lst[::-1]
        
        l1num = int("".join([str(integer) for integer in store(l1)]))
        l2num = int("".join([str(integer) for integer in store(l2)]))
        newsum = list(str(l1num + l2num))
        
        # Store it back as linked list
        def result(num):
            node = ListNode(newsum[-1])
            tail = node
            for num in range(len(newsum) - 2, -1, -1):
                tail.next = ListNode(newsum[num])
                tail = tail.next
            return node
        
        return (result(newsum))
            
"""
Runtime: 72 ms, faster than 57.01% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.4 MB, less than 45.56% of Python3 online submissions for Add Two Numbers.
"""