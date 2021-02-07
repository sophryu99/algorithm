# https://leetcode.com/problems/happy-number/

"""
Approach:
1. Create a set to keep track of created numbers from n
2. While n is not equal to 1, if n is not in set, calculate new num
3. Repeat until n = 1
4. If the number never reaches 1, returns false
"""
class Solution:
    def isHappy(self, n):
        s = set()
        while n != 1:
            if n in s: 
                return False
            s.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        else:
            return True
        
"""
Runtime: 32 ms, faster than 85.38% of Python3 online submissions for Happy Number.
Memory Usage: 14.3 MB, less than 19.06% of Python3 online submissions for Happy Number.
"""
