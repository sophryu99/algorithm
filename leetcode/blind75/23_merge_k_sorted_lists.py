# https://leetcode.com/problems/merge-k-sorted-lists/

"""
1. Add the ListNodes to the pq in the order of the first element of each ListNodes
q:
(1, 0, ListNode{val: 1, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}),
(1, 1, ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}),
(2, 2, ListNode{val: 2, next: ListNode{val: 6, next: None}}),

2. While q exists, pop the ListNode with the minimum value
3. Append the popped ListNode to the current ListNode
4. Rotate the current ListNode
5. Rotate the popped ListNode, and check if next node exists. If exists, add to the pq

Time Complexity: ?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = PriorityQueue()
        result = current = ListNode(0)
        i = 0
        for item in lists:
            # 1
            if item:
                q.put((item.val, i, item))
                i += 1   
        
        while not q.empty():
            # 2
            val, _, item = q.get()
            # 3
            current.next = item
            # 4
            current = current.next
            # 5
            item = item.next
            if item:
                # Adds to the pq by the num 
                q.put((item.val, i, item))
                i += 1
            
        return result.next


"""
Another solution
"""

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(h)
        head = cur = ListNode(None)
        while h:
            val, idx = heapq.heappop(h)
            cur.next = ListNode(val)
            cur = cur.next
            node = lists[idx] = lists[idx].next
            if node:
                heapq.heappush(h, (node.val, idx))
        return head.next

"""
Runtime: 164 ms, faster than 34.43% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 18 MB, less than 47.56% of Python3 online submissions for Merge k Sorted Lists.
"""