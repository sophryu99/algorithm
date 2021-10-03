# https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        l = [1]
        i2, i3, i5 = 0, 0, 0
        l2 = 2 * l[i2]
        l3 = 3 * l[i3]
        l5 = 5 * l[i5]
                    
        while len(l) < n:
            minn = min(l2, l3, l5)
            l.append(minn)
            if minn == l2:
                i2 += 1
                l2 = l[i2] * 2
            if minn == l3:
                i3 += 1
                l3 = l[i3] * 3
            if minn == l5:
                i5 += 1
                l5 = l[i5] * 5
        return l[n - 1]
                
"""
Runtime: 132 ms, faster than 90.38% of Python3 online submissions for Ugly Number II.
Memory Usage: 14.2 MB, less than 90.38% of Python3 online submissions for Ugly Number II.
"""