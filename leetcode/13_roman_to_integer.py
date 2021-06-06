# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        diction = {'I': 1, 'V': 5 ,'X': 10, 'L': 50, 'C': 100, 'D':500, 'M' : 1000}
        N = len(s)
        
        start = 0 
        summ = 0
        while start < N :
            if start == N - 1:
                summ += diction[s[start]]
                start += 1 
                
            else:
                if diction[s[start]] > diction[s[start + 1]]:
                    summ += diction[s[start]]
                    start += 1

                elif diction[s[start]] < diction[s[start + 1]]:
                    summ += diction[s[start + 1]] - diction[s[start]]
                    start += 2

                else:
                    summ += diction[s[start]]
                    start += 1
        
        return (summ)

"""
Runtime: 40 ms, faster than 91.61% of Python3 online submissions for Roman to Integer.
Memory Usage: 14.4 MB, less than 27.26% of Python3 online submissions for Roman to Integer."""