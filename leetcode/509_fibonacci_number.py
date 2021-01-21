class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
    
        return self.fib(n-1) + self.fib(n-2)
        
        
"""
Runtime: 912 ms, faster than 14.00% of Python3 online submissions for Fibonacci Number.
Memory Usage: 14.2 MB, less than 44.10% of Python3 online submissions for Fibonacci Number.
"""
