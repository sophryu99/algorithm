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

"""
Second Attempt (10/20)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Traverse until the end of the ListNode and store the values, return the reversed values
        def store(lnode):
            vals = []
            while lnode:
                vals.append(lnode.val)
                lnode = lnode.next
            return vals[::-1]
        
        def to_int(lst):
            strings = [str(integer) for integer in lst]
            a_string = "". join(strings)
            an_integer = int(a_string)
            return an_integer
        
        # 2. Get the sum of the two values and reverse it
        l1_val = store(l1)
        l2_val = store(l2)
        summed = list(str(to_int(l1_val) + to_int(l2_val)))
        summed = [int(i) for i in summed][::-1]
        
        # 3. Initialize a new ListNode and store reversed sum sccordingly
        l3 = ListNode(summed[0])
        tail = l3
        for i in range(1, len(summed)):
            tail.next = ListNode(summed[i])
            tail = tail.next
        
        return l3
      
    
        
"""
Start Time: 1:40 ~ 2:08 (28 min)

Runtime: 120 ms, faster than 11.52% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.5 MB, less than 11.79% of Python3 online submissions for Add Two Numbers.
"""