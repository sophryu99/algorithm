# https://leetcode.com/problems/counting-bits/

"""
[1]
[0, 1]
[1, 2]
[0, 1, 1, 2]
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Base res array
        res = [0]
        # While the length of the res array is less than n
        while len(res) <= n:
            # Extend the res array with ele + 1 in res array
            res += [i+1 for i in res]
            
        return res[: n + 1]

"""
Runtime: 99 ms, faster than 50.15% of Python3 online submissions for Counting Bits.
Memory Usage: 20.9 MB, less than 35.31% of Python3 online submissions for Counting Bits.
"""