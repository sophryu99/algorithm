# https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        # Get perfect squares that is less than n
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        cnt = 0
        tocheck = {n}
        while tocheck:
            cnt += 1
            temp = set()
            for x in tocheck:
                for y in squares:
                    # If x is a perfect square return the current count
                    if x == y:
                        return cnt
                    # If x is less than y, break loop
                    if x < y:
                        break
                    # Add newly calcuated base to temp
                    temp.add(x - y)
            
            # Reset tocheck as temp
            tocheck = temp
        
        return cnt
                    
                
"""
Runtime: 283 ms, faster than 79.79% of Python3 online submissions for Perfect Squares.
Memory Usage: 14.9 MB, less than 37.39% of Python3 online submissions for Perfect Squares.
"""