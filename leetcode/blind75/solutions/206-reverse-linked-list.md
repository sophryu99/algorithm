## https://leetcode.com/problems/reverse-linked-list/description/

# Intuition
- My intuition was to traverse through the LinkedList once, store the values in an array, and create a new LL and store the values from reversed array
- Works with short LLs, but lack efficiency in terms of both time complexity and memory usage 

# Approach
Main idea is to store a copy of the current LL (curr), rotate the current LL (head), and store the rest of the val of the copy (curr) in prev, and append the prev LLs to curr LL.

```
First iteration
Initial head: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: None}}}

# Create a copy of the original ListNode head 
curr:         ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: None}}}

# Rotate the original head
head reset:   ListNode{val: 2, next: ListNode{val: 3, next: None}}

# Set the curr.next as prev which contains the curr state before this iteration
curr:         ListNode{val: 1, next: None}

# Set prev as the current rotated array
prev:         ListNode{val: 1, next: None}

# Second Iteration------
Initial head: ListNode{val: 2, next: ListNode{val: 3, next: None}}
curr: ListNode{val: 2, next: ListNode{val: 3, next: None}}
head reset: ListNode{val: 3, next: None}
curr: ListNode{val: 2, next: ListNode{val: 1, next: None}}
prev: ListNode{val: 2, next: ListNode{val: 1, next: None}}

# Third Iteration-----
Initial head: ListNode{val: 3, next: None}
curr: ListNode{val: 3, next: None}
head reset: None
curr: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}
prev: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}

```
# Complexity
- Time complexity: O(n)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(1)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            # Create a copy of the whole ListNode
            curr = head
            # Rotate the head LL
            head = head.next
            # Set the curr.next as prev which contains the curr state before this iteration
            curr.next = prev
            # Set prev as the current rotated array
            prev = curr
        return prev
            
```
