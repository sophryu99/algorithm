# https://leetcode.com/problems/valid-perfect-square/

"""
Approach:
1. Square root the num
2. If squared value is an integer, return true
3. else False
"""
class Solution: 
    def isPerfectSquare(self, num: int) -> bool:
        sqrt_num = num ** 0.5 
        answer = False 
        
        if sqrt_num == int(sqrt_num): 
            answer = True 
        
        return answer

    
"""
Runtime: 32 ms, faster than 62.84% of Python3 online submissions for Valid Perfect Square.
Memory Usage: 14.3 MB, less than 43.34% of Python3 online submissions for Valid Perfect Square.
"""
