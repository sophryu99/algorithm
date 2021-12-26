# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry %2)
            carry //= 2

        return result[::-1]

"""
Runtime: 28 ms, faster than 91.93% of Python3 online submissions for Add Binary.
Memory Usage: 14.3 MB, less than 22.95% of Python3 online submissions for Add Binary."""
