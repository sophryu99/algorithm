# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        
        negative = False
        if x < 0:
            negative = True
            
        x = list(str(abs(x)))
        
        for i in range(len(x) // 2):
            left, right = x[i], x[len(x) - i - 1]
            x[i] = right
            x[len(x) - i - 1] = left
        
        res = 0
        if negative:
            res = int('-' + str(int(''.join(x))))
        else:
            res = int(''.join(x))
    
        if res < -2**31 or res > 2 ** 31 - 1:
            return 0
        
        return res
                
            

        
"""
Runtime: 32 ms, faster than 74.94% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.2 MB, less than 72.33% of Python3 online submissions for Reverse Integer.
"""

## Re-attempted (10/20)

class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        if x >= 0:
            ans = int(''.join(list(str(x))[::-1]))
        else:
            x = ''.join(list(str(abs(x)))[::-1])
            ans = int('-' + x)
            
        if ans > 2**31 -1 or ans < -2**31:
            return 0
        return ans
    
"""
Solving Time: 2:43 ~ 2:48 (5min)

Runtime: 32 ms, faster than 78.68% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.3 MB, less than 44.16% of Python3 online submissions for Reverse Integer.
"""