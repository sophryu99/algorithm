# https://leetcode.com/problems/shortest-palindrome/

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        for i in range(len(s) + 1,-1,-1):
            if s.startswith(s[:i][::-1]):
                return s[i:][::-1] + s
        return ""
                

s = "palindrome"
print(s[:2][::-1])
print(s[2:][::-1])
print(s.startswith(s[:2][::-1]))
