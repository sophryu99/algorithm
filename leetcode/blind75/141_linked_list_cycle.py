# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
slow = [3,2,0,-4]
head = [3,2,0,-4]

slow = [2,0,-4]
fast = [0, -4]

1) If cycle exists:
slow = [0, -4]
fast = [2,0,-4]

slow = [-4]
fast = [-4]
>> True

2) If cycle does not exist:
slow = [0, -4]
fast = None

>> False

"""
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        # While the fast node and the fast.next exists
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False
            
"""
Runtime: 90 ms, faster than 20.98% of Python3 online submissions for Linked List Cycle.
Memory Usage: 17.6 MB, less than 81.28% of Python3 online submissions for Linked List Cycle.
"""