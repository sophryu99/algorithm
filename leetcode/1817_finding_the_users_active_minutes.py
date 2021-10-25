# https://leetcode.com/problems/finding-the-users-active-minutes/

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        uam = [0] * k
        cnt = {}
        for log in logs:
            cnt.setdefault(log[0], set()).add(log[1])
        uu = [len(val) for (key, val) in cnt.items()]
        
        for num in uu:
            uam[num - 1] += 1
        return (uam)
         
            
"""
Runtime: 972 ms, faster than 96.46% of Python3 online submissions for Finding the Users Active Minutes.
Memory Usage: 24.9 MB, less than 42.91% of Python3 online submissions for Finding the Users Active Minutes.
"""