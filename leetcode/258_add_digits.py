# https://leetcode.com/problems/add-digits/

"""
1. Convert num into string
2. Sum all elements of the list until the length becomes 1
3. Return the final sum
"""
class Solution:
    def addDigits(self, num: int) -> int:
        num = list(str(num))
        
        while len(num) > 1 :
            num = [int(n) for n in num]
            num = sum(num)
            num = list(str(num))
        
        return (int(num[0]))
            
"""
Runtime: 32 ms, faster than 70.96% of Python3 online submissions for Add Digits.
Memory Usage: 14.3 MB, less than 11.49% of Python3 online submissions for Add Digits.
"""