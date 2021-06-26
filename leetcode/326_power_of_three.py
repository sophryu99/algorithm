# https://leetcode.com/problems/power-of-three/

"""
1. 재귀가 종료되는 조건을 명시해준다.
2. 3으로 나눠지는 숫자의 경우, 다시 한 번 재귀를 수행해준다.
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        
        if n == 3:
            return True
        
        elif n == 1:
            return True
        
        elif n % 3 == 0:
            return self.isPowerOfThree(n / 3)
        
        else:
            return False

"""
Runtime: 68 ms, faster than 85.89% of Python3 online submissions for Power of Three.
Memory Usage: 14.2 MB, less than 47.98% of Python3 online submissions for Power of Three.
"""