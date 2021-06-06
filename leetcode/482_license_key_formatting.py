# https://leetcode.com/problems/license-key-formatting/

# google OA

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        L = len(s)
        
        if L == 1:
            return s
        
        ans = ""
        ans += (s[0: L % k])
        
        for i in range(L % k, L, k):
            if len(ans) > 0:
                ans += '-'
            ans += s[i: i + k]
            
        return (ans)

"""
Runtime: 36 ms, faster than 87.34% of Python3 online submissions for License Key Formatting.
Memory Usage: 14.8 MB, less than 75.83% of Python3 online submissions for License Key Formatting."""