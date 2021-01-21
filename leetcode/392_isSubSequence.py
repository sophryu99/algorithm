class Solution:
    def isSubsequence(self, s: str, t: str):
        len_s = len(s) 
        if len_s == 0: 
            return True 
        cnt = 0 
        for val in t: 
            if val == s[cnt]: 
                cnt = cnt + 1 
                if cnt == len_s: 
                    return True 
                    break

"""
Runtime: 24 ms, faster than 96.52% of Python3 online submissions for Is Subsequence.
Memory Usage: 14.3 MB, less than 53.53% of Python3 online submissions for Is Subsequence.
"""
