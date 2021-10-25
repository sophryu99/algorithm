# https://leetcode.com/problems/the-kth-factor-of-n/

"""
1. Find the factor of n
2. Return the k - 1th element of the factor
"""

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        lst = []
        for i in range(n + 1,0,-1):
            if n % i == 0:
                lst.append(n // i)
                
        if k <= len(lst): 
            return lst[k - 1]
        else:
            return -1

"""
Runtime: 36 ms, faster than 53.20% of Python3 online submissions for The kth Factor of n.
Memory Usage: 14.2 MB, less than 49.15% of Python3 online submissions for The kth Factor of n.
"""