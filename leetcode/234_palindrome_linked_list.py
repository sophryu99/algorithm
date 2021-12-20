# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Traverse through linked list and check if it's a palindrome
        nums = []
        tail = head
        while tail:
            nums.append(str(tail.val))
            tail = tail.next
        
        return nums[::-1] == nums


"""
Runtime: 872 ms, faster than 37.17% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 46.9 MB, less than 57.95% of Python3 online submissions for Palindrome Linked List."""
