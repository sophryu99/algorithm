# https://leetcode.com/problems/factorial-trailing-zeroes/

"""
1. Create a factorial function to solve for the factorial of n
2. Convert the factorial to string and iterate reversely to count for consequent zeros
"""
class Solution:
    def factorial(self, n: int) -> int:
        s = 1
        for i in range(1, n+1):
            s *= i
        return s
    
    def trailingZeroes(self, n: int) -> int:
        fact = self.factorial(n)
        fact = str(fact)
        numzeros = 0
        for i in range(len(fact) - 1, -1, -1):
            if fact[i] == '0':
                numzeros += 1
            else:
                break
        return numzeros
        
"""
Runtime: 3856 ms, faster than 21.46% of Python3 online submissions for Factorial Trailing Zeroes.
Memory Usage: 14.4 MB, less than 22.18% of Python3 online submissions for Factorial Trailing Zeroes.
"""