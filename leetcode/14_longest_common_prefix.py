# https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs, temp = sorted(strs),""
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]: temp += strs[0][i]
            else: break
        return temp
"""
Runtime: 49 ms, faster than 31.68% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14.5 MB, less than 24.69% of Python3 online submissions for Longest Common Prefix.
"""

# Second attempt

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlength = min([len(i) for i in strs])
        temp = strs[0]
        ans = ""
        for s in range(minlength):
            common = ""
            for j in strs:
                if j[s] == temp[s]:
                    common += j[s]
                else:
                    break
            
            if len(common) == len(strs):
                ans += common[0]
            else:
                break
                
        return ans
                
                    
"""
Runtime: 56 ms, faster than 20.66% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14.5 MB, less than 24.69% of Python3 online submissions for Longest Common Prefix.
"""
            
                
        